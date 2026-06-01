resume-job-matcher/
│
├── app/
│   │
│   ├── api/
│   │   ├── jobs.py
│   │   ├── search.py
│   │   ├── resumes.py              # future
│   │   └── evaluations.py          # future
│   │
│   ├── graph/
│   │   ├── state.py
│   │   ├── workflow.py
│   │   ├── nodes/
│   │   │   ├── validate.py
│   │   │   ├── normalize.py
│   │   │   ├── extract_metadata.py
│   │   │   ├── chunk_document.py
│   │   │   ├── generate_embeddings.py
│   │   │   └── store_vectors.py
│   │   │
│   │   └── edges/
│   │       └── routing.py          # future conditional routing
│   │
│   ├── domain/
│   │   ├── models/
│   │   │   ├── job_posting.py
│   │   │   ├── resume.py           # future
│   │   │   ├── chunk.py
│   │   │   └── evaluation.py       # future
│   │   │
│   │   ├── dto/
│   │   │   ├── job_request.py
│   │   │   ├── job_response.py
│   │   │   └── search_request.py
│   │   │
│   │   └── enums/
│   │       ├── document_type.py
│   │       └── record_type.py
│   │
│   ├── services/
│   │   │
│   │   ├── embeddings/
│   │   │   ├── base.py
│   │   │   └── ollama_embedding_service.py
│   │   │
│   │   ├── llm/
│   │   │   ├── base.py
│   │   │   └── ollama_gemma_service.py
│   │   │
│   │   ├── vectorstore/
│   │   │   ├── base.py
│   │   │   └── qdrant_store.py
│   │   │
│   │   ├── chunking/
│   │   │   └── chunking_service.py
│   │   │
│   │   ├── extraction/
│   │   │   └── metadata_extractor.py
│   │   │
│   │   ├── search/
│   │   │   └── semantic_search_service.py
│   │   │
│   │   └── evaluation/
│   │       └── matcher.py          # future
│   │
│   ├── repositories/
│   │   ├── job_repository.py
│   │   └── resume_repository.py    # future
│   │
│   ├── prompts/
│   │   ├── metadata_extraction.txt
│   │   ├── skill_extraction.txt
│   │   └── resume_analysis.txt     # future
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── constants.py
│   │
│   ├── utils/
│   │   ├── logging.py
│   │   ├── ids.py
│   │   └── timestamps.py
│   │
│   └── main.py
│
├── tests/
│   │
│   ├── api/
│   ├── graph/
│   ├── services/
│   └── integration/
│
├── scripts/
│   │
│   ├── create_qdrant_collection.py
│   ├── reindex_jobs.py
│   ├── backfill_metadata.py
│   └── bulk_import_jobs.py
│
├── data/
│   │
│   ├── sample_jobs/
│   ├── sample_resumes/
│   └── exports/
│
├── docker/
│   │
│   ├── fastapi/
│   ├── qdrant/
│   └── ollama/
│
├── docs/
│   │
│   ├── architecture.md
│   ├── api.md
│   ├── ingestion-flow.md
│   └── matching-strategy.md
│
├── .env
├── .env.example
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── Makefile
