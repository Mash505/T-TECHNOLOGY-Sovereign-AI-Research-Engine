import streamlit as st
import ollama
import fitz
import re
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="T TECHNOLOGY Sovereign AI Research Engine",
    page_icon="🚀",
    layout="wide"
)

# =========================================================
# ADVANCED STYLING
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(
        135deg,
        #0E1117 0%,
        #111827 100%
    );
    color: white;
}

h1, h2, h3 {
    font-weight: 700 !important;
}

code {
    white-space: pre-wrap !important;
    color: #00FFAA !important;
    font-size: 15px !important;
}

.katex {
    font-size: 1.25em !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "generated_notes" not in st.session_state:
    st.session_state.generated_notes = ""

if "generated_quiz" not in st.session_state:
    st.session_state.generated_quiz = ""

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("⚡ T TECHNOLOGY AI")

    st.markdown("---")

    model_choice = st.selectbox(
        "Model",
        [
            "gemma3:12b",
            "gemma3:4b"
        ]
    )

    research_mode = st.selectbox(
        "Research Mode",
        [
            "Quantitative Finance",
            "Mathematics",
            "Physics",
            "Machine Learning",
            "General Research"
        ]
    )

    temperature = st.slider(
        "Creativity",
        0.0,
        1.0,
        0.2
    )

    max_context = st.slider(
        "Max Context Size",
        2000,
        30000,
        12000
    )

    st.markdown("---")

    st.info(
        f"""
        🚀 Sovereign AI Engine
        
        • Model: {model_choice}
        • Mode: {research_mode}
        • Local Inference Enabled
        """
    )

# =========================================================
# HEADER
# =========================================================

st.title("🚀 T TECHNOLOGY Sovereign AI Research Engine")

st.markdown("""
### Architected by MOSIN LIYAKAT SHAIKH

Advanced AI infrastructure for:

- Mathematical reasoning
- Quantitative finance
- Scientific research
- PDF intelligence
- LaTeX-preserving workflows
- Sovereign local inference
""")

# =========================================================
# PDF PROCESSING
# =========================================================

def extract_pdf_text(uploaded_file):

    text = ""

    pdf_document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    for page in pdf_document:
        text += page.get_text()

    return text

# =========================================================
# LATEX CLEANER
# =========================================================

def clean_latex(text):

    text = re.sub(
        r'\\\[',
        '$$',
        text
    )

    text = re.sub(
        r'\\\]',
        '$$',
        text
    )

    return text

# =========================================================
# SYSTEM PROMPT
# =========================================================

def build_system_prompt(mode):

    base_prompt = f"""
You are an elite AI research scientist working for T TECHNOLOGY RESEARCH LAB.

SPECIALIZATION:
{mode}

STRICT RULES:

1. NEVER destroy equations.
2. Preserve ALL formulas exactly.
3. Use LaTeX formatting.
4. Show step-by-step derivations.
5. Use professional markdown.
6. Explain concepts deeply.
7. Maintain academic rigor.
8. Use structured sections.
9. Provide examples.
10. Generate copyable raw LaTeX blocks.
11. Always cross-verify mathematical steps before presenting results.

LATEX RULES:

Inline:
$E = mc^2$

Block:
$$
a^2 + b^2 = c^2
$$

After every important equation provide:

```latex
a^2 + b^2 = c^2
