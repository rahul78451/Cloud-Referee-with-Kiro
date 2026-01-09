import streamlit as st
import pandas as pd
from logic import evaluate_clouds, recommend

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Cloud Referee",
    page_icon="⚖️",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(26,115,232,0.15), transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(66,133,244,0.18), transparent 45%),
        linear-gradient(180deg, #f7f9fc 0%, #eef2fb 100%);
    font-family: 'Inter', sans-serif;
}

/* Container */
.block-container {
    max-width: 920px;
    padding-top: 3rem;
}

/* Title */
.main-title {
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    color: #1f2937;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 1.05rem;
    color: #4b5563;
    margin-bottom: 2.5rem;
}

/* Card */
.card {
    background: #ffffff;
    border-radius: 18px;
    padding: 1.8rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    margin-bottom: 2rem;
}

/* Section Title */
.section-title-line {
    font-size: 1.35rem;
    font-weight: 700;
    padding-left: 12px;
    border-left: 5px solid #1a73e8;
    margin-bottom: 1rem;
    color: #1f2937;
}

/* Requirement Title */
.requirement-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #000000;
    margin-bottom: 1.4rem;
}

/* Labels */
label {
    color: #1f2937 !important;
    font-weight: 600 !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #1f2937 !important;
    border-radius: 10px !important;
    border: 1px solid #d1d5db !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #1a73e8, #4285f4);
    color: white;
    border-radius: 12px;
    padding: 0.7rem 1.6rem;
    font-size: 1.05rem;
    border: none;
    box-shadow: 0 10px 20px rgba(26,115,232,0.35);
}

/* Expander */
div[data-testid="stExpander"] {
    background: #ffffff;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
}

div[data-testid="stExpander"] summary {
    font-size: 1.05rem;
    font-weight: 600;
    color: #1f2937 !important;
}

div[data-testid="stExpander"] summary svg {
    color: #1a73e8 !important;
    fill: #1a73e8 !important;
}

div[data-testid="stExpander"] p {
    color: #1f2937 !important;
    font-weight: 500;
}

/* Verdict */
.verdict {
    background: #e8f0fe;
    border-left: 6px solid #1a73e8;
    padding: 1.6rem;
    border-radius: 14px;
    font-size: 1.25rem;
    font-weight: 700;
    color: #1f2937;
}

/* Final explanation text */
.final-explanation {
    margin-top: 0.8rem;
    font-size: 1rem;
    color: #1f2937;
    line-height: 1.6;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 0.85rem;
    color: #6b7280;
    margin-top: 3rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<div class='main-title'>⚖️ Cloud Referee</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>A creative decision-support system for choosing the right cloud platform</div>",
    unsafe_allow_html=True
)

# ---------------- Requirements ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<div class='requirement-title'>🔍 Define Your Requirements</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    budget = st.selectbox("💰 Budget", ["Low", "Medium", "High"])
    use_case = st.selectbox("🎯 Primary Use Case", ["AI", "Web App", "Storage"])

with col2:
    workload = st.selectbox("🏗️ Workload Type", ["Startup", "Enterprise"])
    learning_curve = st.selectbox("📘 Learning Curve Preference", ["Beginner", "Moderate", "Advanced"])

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Action ----------------
if st.button("⚖️ Evaluate Cloud Options"):

    scores = evaluate_clouds(budget, workload, use_case, learning_curve)
    winner = recommend(scores)

    # ---------------- Cloud Comparison ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title-line'>📊 Cloud Comparison</div>", unsafe_allow_html=True)

    df = pd.DataFrame.from_dict(scores, orient="index", columns=["Decision Score"])
    st.dataframe(df, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- Trade-Off Analysis ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title-line'>⚖️ Trade-Off Analysis</div>", unsafe_allow_html=True)

    with st.expander("AWS"):
        st.write("• Broadest cloud ecosystem")
        st.write("• Extremely scalable infrastructure")
        st.write("• Steeper learning curve")

    with st.expander("GCP"):
        st.write("• Industry-leading AI and ML services")
        st.write("• Cost-efficient for startups")
        st.write("• Smaller enterprise footprint")

    with st.expander("Azure"):
        st.write("• Deep Microsoft ecosystem integration")
        st.write("• Strong hybrid cloud offerings")
        st.write("• Higher cost for smaller teams")

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- Final Decision ----------------
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title-line'>🏆 Final Decision</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='verdict'>Recommended Platform: {winner}</div>", unsafe_allow_html=True)

    reasoning = {
        "AWS": "Best suited for complex, large-scale, and highly scalable cloud solutions.",
        "GCP": "Ideal for AI-driven and innovation-focused workloads with cost efficiency.",
        "Azure": "Optimal choice for enterprises leveraging Microsoft technologies."
    }

    st.markdown(
        f"""
        <div class="final-explanation">
            <p>{reasoning[winner]}</p>
            <p><b>Why this decision?</b><br>
            Recommendation derived by evaluating multiple trade-offs rather than a single metric.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown(
    "<div class='footer'>Cloud Referee • Designed as a professional decision-support experience using Kiro</div>",
    unsafe_allow_html=True
)
