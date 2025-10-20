import streamlit as st
from application_pages.data_models import get_initial_data

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""\
Welcome to the AI-Readiness score - GPT-5 lab. This interactive application (AI Career Navigator & Pathway Planner) helps you understand and simulate your AI-Readiness using the AI-R framework. You can explore how your individual capabilities ($V^R$), market opportunities ($H^R$), and their alignment (Synergy%) combine to produce your overall AI-Readiness score.

Business Logic Overview
- Idiosyncratic Readiness ($V^R$): A composite of AI-Fluency, Domain-Expertise, and Adaptive-Capacity, each built from measurable sub-components.
- Systematic Opportunity ($H^R$): A function of occupation-level opportunity using AI-Enhancement, job growth, wage premium, and entry accessibility, adjusted by growth and regional multipliers.
- Synergy%: Captures alignment between your skills and the skills required for a chosen occupation, scaled by a timing factor.
- Final AI-Readiness ($AI\text{-}R$): A weighted sum of $V^R$ and $H^R$ with an additional boost from Synergy%, controlled by $\alpha$ and $\beta$.
""")
st.latex(r"AI\text{-}R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R)")

# Initialize shared data and state once
if "data_initialized" not in st.session_state:
    data = get_initial_data()
    st.session_state["individual_profiles_df"] = data["individual_profiles_df"]
    st.session_state["occupational_data_df"] = data["occupational_data_df"]
    st.session_state["learning_pathways_df"] = data["learning_pathways_df"]
    st.session_state["occupation_required_skills_df"] = data["occupation_required_skills_df"]
    st.session_state["individual_skills_df"] = data["individual_skills_df"]
    # Defaults and derived state
    st.session_state.setdefault("alpha", 0.6)
    st.session_state.setdefault("beta", 0.15)
    st.session_state.setdefault("selected_occupation", "Data Analyst with AI Skills")
    st.session_state.setdefault("lambda_val", 0.3)
    st.session_state.setdefault("gamma_val", 0.2)
    st.session_state.setdefault("max_possible_match", 100)
    st.session_state.setdefault("last_results", {})
    st.session_state["data_initialized"] = True

# Navigation
page = st.sidebar.selectbox(label="Navigation", options=[
    "Page 1 - Overview",
    "Page 2 - AI-R Calculator",
    "Page 3 - Pathways & Scenarios"
])

if page == "Page 1 - Overview":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2 - AI-R Calculator":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3 - Pathways & Scenarios":
    from application_pages.page3 import run_page3
    run_page3()
