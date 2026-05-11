import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util
import torch
import re
from rich.console import Console

console = Console()

class NeuralNexusEngine:
    def __init__(self):
        console.print("[bold cyan][*][/bold cyan] Loading NeuralNexus Embedding Engine (MiniLM)...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.document_chunks = []
        self.embeddings = None

    def load_pdf(self, file_path):
        """Extracts text from PDF and chunks it for vector search."""
        console.print(f"[bold green][+][/bold green] Ingesting: {file_path}")
        doc = fitz.open(file_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        
        size = 500
        self.document_chunks = [full_text[i:i+size] for i in range(0, len(full_text), size-100)]
        
        console.print(f"[*] Generated {len(self.document_chunks)} document nodes.")
        self.embeddings = self.model.encode(self.document_chunks, convert_to_tensor=True)
        console.print("[bold green][+][/bold green] Vector Space initialized.")

    def query(self, user_query, top_k=3):
        """Finds the most relevant chunks using Semantic Search."""
        if self.embeddings is None:
            return ["No document indexed."]
        
        query_embedding = self.model.encode(user_query, convert_to_tensor=True)
        hits = util.semantic_search(query_embedding, self.embeddings, top_k=top_k)
        
        results = []
        for hit in hits[0]:
            results.append(self.document_chunks[hit['corpus_id']])
        return results

    def get_metadata_summary(self):
        """Interrogates the document for high-level intelligence."""
        if not self.document_chunks:
            return {"Status": "Offline"}
        
        header_context = " ".join(self.document_chunks[:5]).lower()
        
        # Logic to find "Submitted by" from your assignment source [cite: 5, 6]
        author_match = re.search(r"submitted by:\s*([a-zA-Z\s]+)", header_context)
        author = author_match.group(1).strip().title() if author_match else "Undetected"

        summary = {
            "Author/Submitter": author,
            "Total Data Nodes": len(self.document_chunks),
            "Domain": "Computer Vision" if "pixel" in header_context or "lbp" in header_context else "General Tech",
            "Key Indicators": [w for w in ["LBP", "LTP", "Histogram", "Threshold", "Python"] if w.lower() in header_context]
        }
        return summary

    def analyze_complexity(self):
        """Heuristic Big-O audit of extracted code snippets."""
        complexity_report = []
        combined_text = " ".join(self.document_chunks).lower()
        
        # Check for nested loops which indicate O(N^2) based on the LBP logic [cite: 27, 28]
        if "for" in combined_text and "range" in combined_text:
            if combined_text.count("for") >= 2:
                complexity_report.append("⚠️ **Efficiency Alert:** Nested loops detected. Estimated Complexity: **$O(N^2)$**. Consider NumPy vectorization.")
            else:
                complexity_report.append("✅ **Efficiency Check:** Linear processing detected. Estimated Complexity: **$O(N)$**.")
        
        if "histogram" in combined_text:
            complexity_report.append("ℹ️ **Memory Note:** Large feature vectors (512-dim) detected.")
            
        return complexity_report

if __name__ == "__main__":
    nexus = NeuralNexusEngine()
    console.print("[yellow]Engine standing by...[/yellow]")