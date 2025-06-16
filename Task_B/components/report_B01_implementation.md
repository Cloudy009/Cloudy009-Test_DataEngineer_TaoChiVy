## IV. Implementation Guidance
---

### Practical Walkthrough
<details open>
<summary>End-to-end implementation of Qdrant with Python SDK and Docker</summary>

---

#### Step 1 – Install Qdrant using Docker

- Use the following command to run Qdrant locally:

  ```bash
  docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
  ```

- Port `6333` is used for REST API, and `6334` is for gRPC communication.
- Docker allows easy setup without installing Qdrant manually.

---

#### Step 2 – Connect to Qdrant via Python SDK

- Install the Qdrant Python client:

  ```bash
  pip install qdrant-client
  ```

- Establish a connection to the running Qdrant instance:

  ```python
  from qdrant_client import QdrantClient

  client = QdrantClient(host="localhost", port=6333)
  ```

---

#### Step 3 – Create a Collection

- Create a new collection to store 4-dimensional vectors using cosine similarity:

  ```python
  from qdrant_client.models import VectorParams, Distance

  client.recreate_collection(
      collection_name="demo_collection",
      vectors_config=VectorParams(size=4, distance=Distance.COSINE)
  )
  ```

---

#### Step 4 – Upsert Vector with Payload

- Insert a vector and associate metadata (payload) such as category or user ID:

  ```python
  from qdrant_client.models import PointStruct

  client.upsert(
      collection_name="demo_collection",
      points=[
          PointStruct(
              id=1,
              vector=[0.1, 0.2, 0.3, 0.4],
              payload={"category": "news", "user_id": 123}
          )
      ]
  )
  ```

---

#### Step 5 – Search Nearest Vectors

- Retrieve the most similar vectors to a given query vector:

  ```python
  results = client.search(
      collection_name="demo_collection",
      query_vector=[0.1, 0.2, 0.3, 0.4],
      limit=3
  )

  for hit in results:
      print(hit.id, hit.score)
  ```

---

#### Step 6 – Filter by Metadata (Payload)

- Search by both vector similarity and metadata filters:

  ```python
  from qdrant_client.models import Filter, FieldCondition, MatchValue

  results = client.search(
      collection_name="demo_collection",
      query_vector=[0.1, 0.2, 0.3, 0.4],
      limit=3,
      query_filter=Filter(
          must=[
              FieldCondition(key="category", match=MatchValue(value="news")),
              FieldCondition(key="user_id", match=MatchValue(value=123))
          ]
      )
  )
  ```

- This enables multi-tenant or domain-specific search where filtering is essential.

---
</details>
