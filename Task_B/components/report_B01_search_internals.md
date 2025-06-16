## VIII. Vector Search Internals
---

### HNSW Index Search Flow (Mermaid)
<details open>
<summary>Understanding how HNSW retrieves top-k vectors efficiently</summary>

---

```mermaid
flowchart TD
  A[Start Search<br>with Query Vector] --> B[Enter Top Layer<br>of HNSW Graph]
  B --> C[Greedy Search to Closest Node]
  C --> D[Go Down One Layer]
  D --> E[Repeat Greedy Search<br>on Lower Layer]
  E --> F{At Base Layer?}
  F -- No --> D
  F -- Yes --> G[Explore Local Neighborhood]
  G --> H[Collect Candidates into Priority Queue]
  H --> I[Return Top-k Nearest Neighbors]
```

---

### Explanation

| Step | Description |
|------|-------------|
| **A → B** | Start by querying the topmost layer of the hierarchical graph. |
| **B → C** | Move greedily from one node to another based on closest vector similarity (e.g., cosine). |
| **C → D → E** | Once local optimum is found in one layer, descend to the next lower layer. |
| **F** | Continue descending until base layer is reached. |
| **G → H** | At base layer, use `ef_search` to explore a local neighborhood. |
| **H → I** | Return top-k vectors from the maintained candidate queue. |

---

### Key Tuning Parameters

- **`M`**: Maximum connections per node (affects accuracy vs. memory).
- **`ef_search`**: Larger values improve recall at cost of speed.
- **`ef_construction`**: Controls indexing quality (higher → better accuracy).

---

### Real-world Note from Senior Architect

> HNSW is an optimal choice when you need a high-recall, low-latency ANN solution that scales. It maintains logarithmic complexity and allows online insertions, making it ideal for applications like semantic search, RAG, and product recommendations.

---
</details>
