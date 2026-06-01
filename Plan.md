# Resume-to-Job Matching Knowledge Base

## Architecture and Implementation Plan

### Objective

Build a self-hosted platform that ingests job postings, extracts structured information, generates embeddings, and stores both semantic and structured representations for future resume evaluation.

The long-term goal is to iteratively improve resumes by measuring how well they match desired job openings and identifying gaps in skills, experience, and qualifications.

The system will remain self-hosted and source-code driven, with no requirement to host a public application.

---

# Phase 1 Scope

Phase 1 focuses only on job posting ingestion.

Input:

* Company Name
* Job Title
* Job Description

Output:

* Structured metadata
* Job-level embeddings
* Chunk-level embeddings
* Searchable knowledge base

No resume processing is implemented yet.

---

# Technology Decisions

## Workflow Orchestration

### LangGraph

Reasons:

* Future-proof for multi-step workflows
* Easy expansion for resume parsing and evaluation
* Supports branching, retries, checkpointing, and human review
* Clear separation between orchestration and business logic

---

## LLM

### Gemma via Ollama

Usage:

* Metadata extraction
* Skill extraction
* Experience extraction
* Seniority extraction
* Job categorization

All inference runs locally.

---

## Embedding Model

### Preferred: BGE-M3

Alternative:

* mxbai-embed-large

Reasons for BGE-M3:

* Strong retrieval quality
* Supports dense retrieval
* Suitable for semantic matching workloads
* Future-proof for advanced retrieval strategies

Served locally via Ollama.

---

## Vector Database

### Qdrant

Reasons:

* Easy self-hosting
* Excellent metadata filtering
* Simple operational model
* Sufficient for projected scale
* Easier than Milvus for a single-user project

---

## REST API Framework

### FastAPI

Reasons:

* Mature ecosystem
* Strong typing support
* Easy OpenAPI generation
* Works well with LangGraph

---

# High-Level Architecture

```
                ┌─────────────┐
                │  FastAPI    │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │ LangGraph   │
                └──────┬──────┘
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
```

Metadata         Embedding         Storage
Extraction       Generation        Layer

```
      │                │                │
      ▼                ▼                ▼

   Gemma           BGE-M3          Qdrant
```

---

# REST API Design

## Create Job

POST /api/v1/jobs

Request

```json
{
  "company": "Amazon",
  "job_title": "Software Development Engineer II",
  "job_description": "...",
  "source": "manual"
}
```

Response

```json
{
  "job_id": "uuid",
  "status": "accepted"
}
```

---

## Retrieve Job

GET /api/v1/jobs/{job_id}

Response

```json
{
  "job_id": "...",
  "company": "...",
  "job_title": "...",
  "metadata": {
    "skills": [
      "Java",
      "AWS"
    ]
  }
}
```

---

## Semantic Search

POST /api/v1/jobs/search

Request

```json
{
  "query": "Java backend engineer with AWS experience",
  "top_k": 10
}
```

Response

```json
{
  "results": [...]
}
```

---

# LangGraph Workflow

## Phase 1 Graph

START

↓

Validate Input

↓

Normalize Input

↓

Extract Metadata

↓

Chunk Document

↓

Generate Embeddings

↓

Store Data

↓

END

---

# Node Responsibilities

## Validation Node

Responsibilities:

* Validate required fields
* Validate payload size
* Generate job identifier

Output:

Normalized request object

---

## Normalization Node

Responsibilities:

* Clean whitespace
* Standardize formatting
* Prepare canonical JobPosting object

Output:

Canonical job document

---

## Metadata Extraction Node

Uses:

Gemma via Ollama

Extract:

* Skills
* Technologies
* Experience requirements
* Seniority
* Employment type
* Domain/category
* Certifications (if present)
* Location (if present)

Store:

* Normalized metadata
* Raw extraction output

---

## Chunking Node

Responsibilities:

Generate:

* Full job representation
* Chunk representations

Output:

* Job-level document
* Chunk-level documents

---

## Embedding Node

Uses:

BGE-M3

Generate:

* Job-level embedding
* Chunk-level embeddings

Output:

Vectors ready for storage

---

## Storage Node

Uses:

Qdrant

Store:

* Raw text
* Metadata
* Embeddings

---

# Storage Strategy

Single collection:

career_documents

---

## Record Types

### Job Summary Record

Represents:

Entire job posting

Metadata:

```json
{
  "record_type": "job_summary"
}
```

Contains:

* Full text
* Job-level embedding

---

### Job Chunk Record

Represents:

Individual chunks

Metadata:

```json
{
  "record_type": "job_chunk",
  "chunk_index": 0
}
```

Contains:

* Chunk text
* Chunk embedding

---

# Document Model

All records should contain:

```json
{
  "document_type": "job",

  "job_id": "...",

  "company": "...",

  "job_title": "...",

  "job_description": "...",

  "skills": [],

  "experience_years": null,

  "seniority": null,

  "employment_type": null,

  "location": null,

  "keywords": [],

  "source": "manual",

  "embedding_model": "bge-m3",

  "embedding_version": "v1",

  "ingested_at": "...",

  "record_type": "job_summary"
}
```

---

# Metadata Preservation Strategy

Store three forms of information.

## Raw Input

```json
{
  "company": "...",
  "job_title": "...",
  "job_description": "..."
}
```

---

## Structured Metadata

```json
{
  "skills": [],
  "experience_years": 5,
  "seniority": "Senior"
}
```

---

## Raw LLM Extraction

```json
{
  ...
}
```

Reason:

Allows reprocessing without losing extracted context.

---

# Abstraction Layers

To keep the system extensible:

## Embedding Service

Interface:

```python
EmbeddingService
```

Implementations:

```python
OllamaEmbeddingService
```

Future:

```python
OpenAIEmbeddingService
```

---

## Vector Store

Interface:

```python
VectorStore
```

Implementations:

```python
QdrantStore
```

Future:

```python
MilvusStore
```

```python
PgVectorStore
```

No LangGraph node should directly depend on Qdrant APIs.

---

# Graph State Design

State must remain serializable.

Example:

```python
class GraphState(TypedDict):
    raw_input: dict

    normalized_document: dict

    extracted_metadata: dict

    chunks: list[str]

    embeddings: list[list[float]]

    storage_result: dict

    errors: list[str]
```

Never store:

* Qdrant client
* Ollama client
* SDK objects

inside graph state.

---

# Future Phase 2

Resume Processing

Workflow:

Resume PDF

↓

PDF Parsing

↓

Metadata Extraction

↓

Chunking

↓

Embedding

↓

Storage

---

Document Type

```json
{
  "document_type": "resume"
}
```

Same collection.

Same retrieval pipeline.

---

# Future Phase 3

Resume Evaluation

Workflow:

Resume

↓

Generate Resume Embedding

↓

Retrieve Matching Jobs

↓

Similarity Scoring

↓

Skill Gap Analysis

↓

Improvement Suggestions

↓

Evaluation Report

---

# Future Scoring Dimensions

Not implemented initially but preserved for future use.

Potential dimensions:

* Overall semantic similarity
* Required skills coverage
* Preferred skills coverage
* Experience match
* Seniority match
* Domain match
* Tooling match
* Technology stack overlap
* Certification overlap
* Keyword coverage
* Education match

Because rich metadata is stored from the beginning, these scoring dimensions can be added later without re-ingesting historical job postings.

---

# Final Design Principles

1. Self-hosted only
2. LangGraph orchestrates workflows
3. Gemma performs metadata extraction
4. BGE-M3 generates embeddings
5. Qdrant stores vectors
6. Store both job-level and chunk-level embeddings
7. Preserve raw, structured, and vector representations
8. Use interfaces around storage and embeddings
9. Keep graph state serializable
10. Design for future resume evaluation without requiring architectural changes
