import streamlit as st
import re
from datetime import datetime

# =========================================================
# OPTIONAL IMPORTS (Cross Platform Safe)
# =========================================================

OLLAMA_AVAILABLE = True
PDF_AVAILABLE = True

try:
    import ollama
except:
    OLLAMA_AVAILABLE = False

try:
    import fitz
except:
    PDF_AVAILABLE = False

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="T TECHNOLOGY Sovereign AI Research Engine",
    page_icon="🚀",
    layout="wide"
)

# =========================================================
# ADVANCED CSS
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

[data-testid="stSidebar"] {
    background-color: #111827;
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
        "Gemma Model",
        [
            "gemma3:4b",
            "gemma3:12b"
        ]
    )

    research_mode = st.selectbox(
        "Research Mode",
        [
            "Mathematics",
            "Quantitative Finance",
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
        "Context Size",
        2000,
        30000,
        12000
    )

    st.markdown("---")

    if OLLAMA_AVAILABLE:
        st.success("✅ Ollama Available")
    else:
        st.warning("⚠ Ollama Not Installed")

    if PDF_AVAILABLE:
        st.success("✅ PDF Engine Available")
    else:
        st.warning("⚠ PDF Support Disabled")

# =========================================================
# HEADER
# =========================================================

st.title("🚀 T TECHNOLOGY Sovereign AI Research Engine")

st.markdown("""
### Architected by MOSIN LIYAKAT SHAIKH

Advanced sovereign AI infrastructure for:

- Mathematical reasoning
- Quantitative finance
- Scientific research
- LaTeX-preserving workflows
- Local AI inference
- Cross-platform compatibility
""")

st.markdown("---")

# =========================================================
# PDF EXTRACTION
# =========================================================

def extract_pdf_text(uploaded_file):

    if not PDF_AVAILABLE:
        return "PDF support unavailable on this device."

    try:

        text = ""

        pdf_document = fitz.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        for page in pdf_document:
            text += page.get_text()

        return text

    except Exception as e:

        return f"PDF extraction error: {str(e)}"

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

    prompt = f"""
You are an elite AI research scientist working for T TECHNOLOGY RESEARCH LAB.

SPECIALIZATION:
{mode}

STRICT RULES:

1. Preserve equations exactly.
2. Use LaTeX formatting.
3. Show step-by-step derivations.
4. Maintain academic rigor.
5. Use professional markdown.
6. Include examples.
7. Keep outputs readable.
8. Never simplify mathematical expressions incorrectly.

LATEX EXAMPLES:

Inline:
$E = mc^2$

Block:
$$
a^2 + b^2 = c^2
$$

After important equations provide copyable LaTeX blocks.

Use:
- headings
- bullet points
- structured formatting
"""

    return prompt

# =========================================================
# GEMMA ENGINE
# =========================================================

def ask_gemma(user_prompt, context):

    if not OLLAMA_AVAILABLE:

        return f"""
# Demo Response

Ollama is not installed on this device.

## User Prompt

{user_prompt}

## Example Equation

$$
E = mc^2
$$

```latex
E = mc^2
