## III. Deep Dive into One Tool
---

### Qdrant Architecture
<details open>
<summary>Internal architecture and indexing design of Qdrant</summary>

---

- **Indexing Algorithm**: Uses **HNSW (Hierarchical Navigable Small World)** for efficient approximate nearest neighbor search with high accuracy.
- **Storage Backend**: Built with persistence in mind — supports storing vectors and payloads directly on disk with WAL (write-ahead log) mechanism.
- **Multi-threaded Engine**: Designed in Rust for high concurrency and safety.
- **API Interfaces**: Offers both **REST** and **gRPC** APIs for querying and data ingestion.
- **Filtering Mechanism**: Enables advanced filtering using vector metadata (payload).

---
</details>

### Installation and Deployment
<details open>
<summary>Installation methods and deployment options for Qdrant</summary>

---

- **Docker Deployment**
  - Easiest method for local setup or production.
  - Example:
    ```bash
    docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
    ```

- **Local Binary**
  - Download and run standalone executable from [https://qdrant.tech/download](https://qdrant.tech/download)
  - No external dependencies needed.

- **Cloud Deployment**
  - Qdrant Cloud offers fully managed hosting.
  - Includes monitoring, auto-backup, and scaling capabilities.

---
</details>

### Python SDK Usage
<details open>
<summary>Working with Qdrant in Python using official SDK</summary>

---

- **Install SDK**
  ```bash
  pip install qdrant-client
  ```

- **Create Collection**
```bash
  from qdrant_client import QdrantClient
  from qdrant_client.models import Distance, VectorParams

  client = QdrantClient(host="localhost", port=6333)
  client.recreate_collection(
      collection_name="my_vectors",
      vectors_config=VectorParams(size=768, distance=Distance.COSINE),
  )
```
- **Upsert Vector**
```bash
  from qdrant_client.models import PointStruct

  client.upsert(
      collection_name="my_vectors",
      points=[
          PointStruct(id=1, vector=[0.1, 0.2, ...], payload={"category": "news"}),
      ]
  )
```

- **Search Vector**
```bash
results = client.search(
    collection_name="my_vectors",
    query_vector=[0.1, 0.2, ...],
    limit=5,
)
```

- **Filter with Payload**
```bash
from qdrant_client.models import Filter, FieldCondition, MatchValue

results = client.search(
    collection_name="my_vectors",
    query_vector=[...],
    limit=3,
    query_filter=Filter(
        must=[
            FieldCondition(key="category", match=MatchValue(value="news"))
        ]
    )
)
```
---

</details>


### Real-World Integration
<details open> 
<summary>How Qdrant integrates with modern AI and backend stacks</summary>

---

- LangChain:
  + Qdrant serves as a vector store for document embeddings in RAG pipelines.
  + Supported via langchain.vectorstores.Qdrant.

- FastAPI / Flask:
  + Can be integrated into APIs for semantic search, personalized recommendations, or similarity-based routing.
  + Store embeddings in Qdrant and expose similarity queries via REST endpoints.

- Retrieval-Augmented Generation (RAG):
  + Qdrant stores document chunks; LLM queries retrieve semantically relevant content from Qdrant before generating responses.

---
</details>