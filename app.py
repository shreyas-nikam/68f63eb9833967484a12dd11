import streamlit as st
from application_pages.ai_readiness_functions import (
    individual_profiles_data, occupational_data, learning_pathways_data,
    occupation_required_skills_data, individual_skills_data
)
import pandas as pd

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab - AI Career Navigator & Pathway Planner")
st.divider()

st.markdown("""
In this lab, we explore the **AI-Readiness Score (AI-R) framework**, a parametric model designed to quantify an individual's preparedness for AI-enabled careers. This application provides an interactive environment to understand, calculate, and simulate career readiness in AI-driven labor markets, considering both individual capabilities and market opportunities.

### Learning Goals
- Understand the key insights contained in the uploaded document and supporting data.
- Decompose the AI-Readiness Score into its systematic opportunity ($H^R$), idiosyncratic readiness ($V^R$), and synergy components.
- Evaluate the potential impact of various learning pathways on individual skill development and career readiness.
- Analyze different career paths based on market demand and personal capabilities through "what-if" scenarios.

### Introduction to the AI-Readiness Score
This application explores the AI-Readiness Score (AI-R) framework, a parametric model designed to quantify an individual's preparedness for AI-enabled careers. The AI-R score helps in navigating career transitions by considering both individual capabilities and market opportunities.

The core formula for the AI-Readiness Score for an individual $i$ at time $t$ is defined as:
$$ AI-R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R) $$

Where:
- $V^R(t)$ is the Idiosyncratic Readiness (individual capability).
- $H^R(t)$ is the Systematic Opportunity (market demand).
- $\alpha \in [0,1]$ is the weight on individual vs. market factors.
- $\beta > 0$ is the Synergy coefficient.
- Both $V^R$ and $H^R$ are normalized to $[0, 100]$.
- $\text{Synergy}\%$ is also normalized to $[0, 100]$ percentage units.

This framework allows for dynamic "what-if" scenario planning, enabling users to understand how different learning pathways and career transitions impact their future career prospects.

### Synthetic Data Generation
This section prepares the environment by generating synthetic datasets that will be used throughout the application. The datasets are designed to be lightweight and representative of the data structures described in the AI-Readiness Score paper.

""")

# Initialize session state for all dataframes if not already present
if "individual_profiles_df" not in st.session_state:
    st.session_state.individual_profiles_df = pd.DataFrame(individual_profiles_data)
if "occupational_data_df" not in st.session_state:
    st.session_state.occupational_data_df = pd.DataFrame(occupational_data)
if "learning_pathways_df" not in st.session_state:
    st.session_state.learning_pathways_df = pd.DataFrame(learning_pathways_data)
if "occupation_required_skills_df" not in st.session_state:
    st.session_state.occupation_required_skills_df = pd.DataFrame(occupation_required_skills_data)
if "individual_skills_df" not in st.session_state:
    st.session_state.individual_skills_df = pd.DataFrame(individual_skills_data)


page = st.sidebar.selectbox(label="Navigation", options=["AI-Readiness Score Components", "AI-Readiness Score Calculator", "Pathway Simulation"])

if page == "AI-Readiness Score Components":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "AI-Readiness Score Calculator":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Pathway Simulation":
    from application_pages.page3 import run_page3
    run_page3()