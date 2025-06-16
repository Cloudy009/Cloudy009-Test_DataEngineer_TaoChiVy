## I. Concept Introduction
---

### Vector Fundamentals
<details open>
<summary>Definition and use of vectors in machine learning</summary>

---

- A **vector** in machine learning is a numerical representation of data in a high-dimensional continuous space.
- Vectors are essential for processing unstructured data such as text, images, and audio.
- The process of converting raw data into vectors is known as **embedding** or **vectorization**.

- **Embeddings** capture semantics or visual/audio features that allow machines to perform similarity comparison.

---
</details>

### Vector Similarity
<details open>
<summary>Understanding similarity metrics and their use cases</summary>

---

- Vector similarity determines how close or similar two vectors are within a vector space.
- It is used to perform **nearest neighbor search** in applications like search, recommendation, and classification.

- Common similarity metrics:

  - **Cosine Similarity**: Measures angle between vectors; ideal for text/NLP use cases.
  - **Euclidean Distance (L2 norm)**: Measures straight-line distance; commonly used in vision or geometric models.
  - **Dot Product**: Measures vector projection; used in ANN libraries and performance-optimized search.

- **When to use which:**
  - Use **cosine similarity** when magnitude doesn't matter (e.g., BERT or Word2Vec embeddings).
  - Use **L2 distance** when location and scale are important (e.g., visual feature comparison).
  - Use **dot product** for optimized mathematical operations in dense vector scenarios.

---
</details>

### Vector Databases
<details open>
<summary>What is a vector database and how it differs from traditional DBs</summary>

---

- A **vector database** is a specialized system built to store, index, and query high-dimensional vectors efficiently.
- Unlike traditional databases that rely on exact matches or relational joins, vector DBs support **approximate nearest neighbor (ANN)** search.
- ANN enables fast **top-k retrieval** based on vector similarity rather than key or value match.

- Key features of vector databases:
  - **High-dimensional indexing** using algorithms like HNSW, IVF, PQ.
  - **Payload storage** for attaching metadata to each vector.
  - **Filtering and hybrid search** using both metadata and vector similarity.

- **Comparison with traditional databases:**

  | Traditional DB                  | Vector DB                           |
  |----------------------------------|--------------------------------------|
  | Key-value or relational access   | Similarity-based nearest search      |
  | Exact match                      | Approximate (ANN) match              |
  | Optimized for structured data    | Optimized for embeddings             |
  | Uses SQL or query languages      | Uses API-based vector search         |

---
</details>

### Applications
<details open>
<summary>Real-world use cases of vector databases</summary>

---

- **Semantic Search**: Retrieve semantically similar documents, questions, or FAQs.
- **Image Similarity**: Find visually similar images using feature vectors from CNNs.
- **Audio Matching**: Identify similar sounds or music patterns.
- **Product Recommendations**: Suggest similar or co-purchased products using user/item embeddings.
- **Retrieval-Augmented Generation (RAG)**: Feed relevant chunks of documents to LLMs to enhance contextual responses.
- **Chatbot Memory**: Persist contextual information and retrieve relevant past interactions using vector matching.

---
</details>