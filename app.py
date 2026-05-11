import streamlit as st
from engine import NeuralNexusEngine
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="NeuralNexus | Doc Intelligence", page_icon="🧠", layout="wide")

# --- CUSTOM CSS (FIXED ARGUMENT) ---
st.markdown("""
    <style>
    .stApp { background-color: #09090b; color: #10b981; }
    .stTextInput>div>div>input { background-color: #000000; color: #10b981; border: 1px solid #10b981; }
    .stButton>button { background-color: #10b981; color: black; font-weight: bold; width: 100%; }
    .stExpander { background-color: #111827; border: 1px solid #374151; }
    /* Target sidebar explicitly */
    section[data-testid="stSidebar"] { background-color: #111827; color: #10b981; }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE INITIALIZATION ---
@st.cache_resource
def load_engine():
    return NeuralNexusEngine()

nexus = load_engine()

# --- SIDEBAR: INGESTION & AUDIT ---
with st.sidebar:
    st.title("📁 DATA INGESTION")
    uploaded_file = st.file_uploader("Drop Intelligence Source (PDF)", type="pdf")
    
    if uploaded_file:
        file_path = f"temp_{uploaded_file.name}"
        if not os.path.exists(file_path):
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            with st.spinner("Mapping Vector Space..."):
                nexus.load_pdf(file_path)
        
        st.success("Target Source Mapped.")
        
        # --- AUTOMATIC METADATA SUMMARY ---
        st.write("---")
        st.header("📊 METADATA SUMMARY")
        meta = nexus.get_metadata_summary()
        for key, val in meta.items():
            st.write(f"**{key}:** {val}")

        # --- AUTOMATIC COMPLEXITY AUDIT ---
        st.write("---")
        st.header("🛠️ ARCHITECTURE AUDIT")
        audit_notes = nexus.analyze_complexity()
        for note in audit_notes:
            st.info(note)

# --- MAIN INTERFACE: NEURAL QUERY ---
st.title("🧠 NEURALNEXUS")
st.subheader("Semantic Document Intelligence Platform")
st.write("---")

query = st.text_input("Enter Neural Query (e.g., 'What is the LTP threshold logic?')")

if query:
    with st.spinner("Retrieving Relevant Nodes..."):
        results = nexus.query(query)
        st.write("### 📂 Recovered Intelligence Nodes")
        for i, res in enumerate(results):
            with st.expander(f"Node #{i+1} Context", expanded=True):
                st.write(res)

# --- FOOTER ---
st.write("---")
st.caption("NeuralNexus Engine v1.2 | Multi-Modal Vector Search Enabled")