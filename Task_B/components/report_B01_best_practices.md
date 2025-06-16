## V. Best Practices
---

### Optimization Guidelines
<details open>
<summary>Recommended practices to improve accuracy, performance, and maintainability</summary>

---

- **Understand Distance Metrics Properly**
  - The choice of distance metric significantly affects retrieval relevance and performance.
  - **Cosine Similarity**
    - Measures the angle between two vectors (focuses on direction, not magnitude).
    - Suitable for NLP tasks like document or sentence embedding (e.g., BERT).
    - Commonly used when vectors are normalized.
  - **Euclidean Distance (L2 Norm)**
    - Measures actual geometric distance between vectors.
    - Suitable for visual similarity or sensor data where magnitude matters.
  - **Dot Product**
    - Measures the projection of one vector onto another.
    - Often used in recommendation systems and ANN libraries like FAISS.
    - Sensitive to magnitude; should be used carefully when vectors aren’t normalized.

- **Optimize HNSW Parameters for Balanced Search**
  - **HNSW** (Hierarchical Navigable Small World) is a graph-based ANN algorithm.
  - Important tuning parameters:
    - `M` (connectivity): Controls the number of edges per node. Higher `M` → better recall, slower build.
    - `ef_construction`: Controls index build quality. Recommended range: 100–400.
    - `ef_search`: Affects recall at query time. Higher values → better accuracy, slower search.
  - Trade-offs:
    - High accuracy needs high `ef_search` but may increase query latency.
    - Low `M` or `ef` improves speed but reduces recall.

- **Combine Vector Search with Metadata Filtering**
  - Use **payload (metadata)** fields to enable hybrid querying.
  - Example fields: `category`, `language`, `user_id`, `region`, `timestamp_range`, etc.
  - Benefits:
    - Improves precision by pre-filtering candidates before vector scoring.
    - Supports contextual or user-personalized recommendations.
  - Supported natively by tools like Qdrant, Weaviate.

- **Remove Stale or Unused Vectors Regularly**
  - Accumulated vector data can degrade system performance over time.
  - Implement cleanup strategies:
    - Tag vectors with expiration timestamps or last-accessed time.
    - Use TTL policies or scheduled jobs to delete unused entries.
  - Benefits:
    - Keeps index size manageable.
    - Improves performance and reduces storage costs.

- **Design Collection Structure Strategically**
  - Organize your collections by logical groupings:
    - By **data domain**: `articles`, `products`, `audio_clips`
    - By **access control**: multi-tenant systems → per client collection
    - By **model type or embedding dimensions**
  - Advantages:
    - Faster indexing and search within smaller, specialized collections.
    - Simplifies access control, lifecycle management, and scaling.

- **Benchmark and Monitor Continuously**
  - Use real workloads to test indexing and search performance.
  - Tools like Qdrant’s `/collections/{name}/points/search` API include response time stats.
  - Log query latency, recall, and index size over time.

- **Choose Vector Size Appropriately**
  - Match vector dimensionality to your embedding model.
  - Do not overuse large vectors (e.g., 1536-dim) unless needed.
  - Normalize vectors when using cosine similarity to ensure consistency.

- **Apply Hybrid Ranking if Supported**
  - Combine lexical relevance (e.g., BM25) with vector similarity.
  - Especially useful for re-ranking results in text-based search.

- **Document Your Schema and Query Logic**
  - Clearly define embedding model used, vector dimensions, and distance metric.
  - Keep track of changes across deployments or collection versions.

---
</details>
