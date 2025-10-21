import streamlit as st
import pandas as pd
import numpy as np
from application_pages.utils import init_data

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown(
    "In this lab, we build an interactive AI Career Navigator & Pathway Planner to compute an AI-Readiness score (AI-R) for individuals and explore career transitions. "
    "The AI-R framework blends Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($H^R$), and a Synergy component to reflect the alignment between a person’s skills and market demand. "
    "You can: (1) adjust inputs for your skills and experience, (2) select occupations to see market opportunity, and (3) simulate learning pathways to project future AI-R.\n\n" 
    "Business logic summary:\n"
    "- $AI\text{-}R_{i,t} = \alpha\,V^R + (1-\alpha)\,H^R + \beta\,\text{Synergy}\%$\n"
    "- $V^R$ aggregates AI-Fluency, Domain-Expertise, and Adaptive-Capacity.\n"
    "- $H^R$ accounts for AI-enhancement, job growth, wage premium, and entry accessibility, adjusted by growth and regional multipliers.\n"
    "- Synergy% scales with how well your skills match occupation requirements and timing (experience).\n"
    "All quantities are normalized to the $[0, 100]$ scale where applicable; error handling avoids division-by-zero and provides guidance in the UI."
)

# Initialize data and defaults once
if "data_initialized" not in st.session_state:
    data_dict = init_data()
    st.session_state.update(data_dict)
    # Global tuning defaults
    st.session_state.setdefault("alpha", 0.6)
    st.session_state.setdefault("beta", 0.15)
    st.session_state.setdefault("lambda_val", 0.3)
    st.session_state.setdefault("gamma_val", 0.2)
    # Selections
    default_occ = "Data Analyst with AI Skills"
    if default_occ in st.session_state["occupational_data_df"]["occupation_name"].values:
        st.session_state.setdefault("selected_occupation", default_occ)
    else:
        st.session_state.setdefault(
            "selected_occupation",
            st.session_state["occupational_data_df"]["occupation_name"].iloc[0]
        )
    st.session_state.setdefault("calculated", False)
    st.session_state.setdefault("simulation_done", False)
    st.session_state["data_initialized"] = True

# Navigation
page = st.sidebar.selectbox(
    label="Navigation",
    options=["Overview & Data", "AI-Readiness Calculator", "Pathway Simulator"],
)

if page == "Overview & Data":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "AI-Readiness Calculator":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Pathway Simulator":
    from application_pages.page3 import run_page3
    run_page3()
