
# 🧠 NeuralNexus: Document Intelligence Platform

**NeuralNexus** is a high-performance, multi-modal engine designed to transform static documents into interactive, searchable intelligence assets. Unlike traditional keyword search (Ctrl+F), NeuralNexus understands the **semantic meaning** and **architectural intent** behind document content.

---

## 🚀 Key Technical Features

* **Vector Search Engine:** Leverages Bi-Encoder architectures (`all-miniLM-L6-v2`) to map document chunks into a multi-dimensional vector space for high-accuracy semantic retrieval.
* **Automated Intelligence Briefing:** Automatically extracts document metadata, including authors, submitters, and technical domains upon ingestion (e.g., identifying Computer Vision vs. General Tech).
* **Static Code Audit:** Scans embedded code snippets to provide heuristic complexity analysis—such as detecting $O(N^2)$ nested loops in texture analysis algorithms (LBP/LTP)—and suggests performance optimizations.
* **Edge-Optimized Design:** Built with a "Headless-First" logic to run efficiently on CPU-only hardware (like the AMD Ryzen 5) with restricted RAM.

---

## 🛠️ Project Intelligence Examples

Based on initial testing with specialized engineering documentation:
* **Spatial Intelligence:** The engine successfully parsed "Titan Vision" documentation, detailing the transition from standard object detection to **Centroid-based Geofencing** using `cv2.pointPolygonTest()`.
* **Concurrency Management:** Documented the use of the `.after()` method in Event-Driven UI design to prevent graphical freezing during heavy AI inference.
* **Algorithm Robustness:** Analyzed the ternary "dead zone" logic in **Local Ternary Patterns (LTP)** as a noise-reduction upgrade over binary systems.

---

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mutahirgillani1717/NeuralNexus.git](https://github.com/mutahirgillani1717/NeuralNexus.git)
   cd NeuralNexus

```

2. **Install dependencies:**
```bash
pip install sentence-transformers pymupdf streamlit rich

```


3. **Run the Dashboard:**
```bash
streamlit run app.py

```



---

**Author:** Syed Mutahir Hussain

**Academic Context:** Final Year Computer Science | UET Taxila

**Focus:** AI, Data Science, and Machine Learning

```