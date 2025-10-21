import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

st.markdown(
    "In this lab, you will explore and simulate your AI-Readiness Score (AI-R) using a structured, data-driven framework that blends individual capability with market opportunity and alignment.\n\n"
    "AI-Readiness decomposes into three core parts: Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($H^R$), and a Synergy component that rewards alignment between your skills and market needs."
)
st.latex(r" AI\text{-}R_{i,t} = \alpha\, V^R_i(t) + (1-\alpha)\, H^R_i(t) + \beta\, \text{Synergy}\% ")
st.markdown(
    "- $V^R$: Your individual readiness based on AI-Fluency, Domain-Expertise, and Adaptive-Capacity.\n"
    "- $H^R$: The market opportunity for your selected occupation, combining AI enhancement, job growth, wage premium, and entry accessibility adjusted by growth and regional multipliers.\n"
    "- $\\alpha \\in [0,1]$: Weight on individual vs. market factors.\n"
    "- $\\beta \\in [0,1]$: Weight on the synergy term, which increases when your skills align with role requirements at the right time.\n"
)


def _init_state():
    if "initialized" in st.session_state:
        return

    individual_profiles_data = {
        'user_id': [1], 'prompting_score': [0.75], 'tools_score': [0.6],
        'understanding_score': [0.8], 'datalit_score': [0.9],
        'output_quality_with_ai': [90], 'output_quality_without_ai': [60],
        'time_without_ai': [4], 'time_with_ai': [1], 'errors_caught': [15],
        'total_ai_errors': [20], 'appropriate_trust_decisions': [25],
        'total_decisions': [30], 'delta_proficiency': [0.3],
        'delta_t_hours_invested': [10], 'education_level': ["Master's"],
        'years_experience': [5], 'portfolio_score': [0.85], 'recognition_score': [0.7],
        'credentials_score': [0.9], 'cognitive_flexibility': [85],
        'social_emotional_intelligence': [90], 'strategic_career_management': [75]
    }
    st.session_state.individual_profiles_df = pd.DataFrame(individual_profiles_data)

    occupational_data = {
        'occupation_name': ['Data Analyst with AI Skills', 'AI UX Researcher', 'AI Prompt Engineer', 'Data Scientist', 'Nursing Informatics', 'Medical Coding'],
        'ai_enhancement_score': [0.8, 0.9, 0.7, 0.95, 0.75, 0.6],
        'job_growth_rate_g': [0.25, 0.35, 0.4, 0.3, 0.2, 0.15],
        'ai_skilled_wage': [120000, 130000, 140000, 150000, 110000, 90000],
        'median_wage': [90000, 95000, 100000, 110000, 85000, 70000],
        'education_years_required': [4, 4, 4, 4, 4, 2],
        'experience_years_required': [2, 3, 1, 3, 2, 0],
        'current_job_postings': [500, 400, 600, 700, 300, 200],
        'previous_job_postings': [400, 300, 450, 500, 250, 180],
        'remote_work_factor': [0.6, 0.7, 0.8, 0.5, 0.4, 0.3],
        'local_demand': [1.2, 1.1, 1.3, 1.4, 1.0, 0.9],
        'national_avg_demand': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    }
    st.session_state.occupational_data_df = pd.DataFrame(occupational_data)

    learning_pathways_data = {
        'pathway_id': [1, 2, 3],
        'pathway_name': ['Prompt Engineering Fundamentals', 'AI for Financial Analysis', 'Human-AI Collaboration'],
        'pathway_type': ['AI-Fluency', 'Domain+AI Integration', 'Adaptive Capacity'],
        'impact_ai_fluency': [0.2, 0.1, 0.05],
        'impact_domain_expertise': [0.05, 0.2, 0.1],
        'impact_adaptive_capacity': [0.1, 0.05, 0.2]
    }
    st.session_state.learning_pathways_df = pd.DataFrame(learning_pathways_data)

    occupation_required_skills_data = {
        'occupation_name': ['Data Analyst with AI Skills'] * 3 + ['AI UX Researcher'] * 3,
        'skill_name': ['Python', 'Data Visualization', 'Machine Learning'] + ['User Research', 'UI Design', 'AI Ethics'],
        'required_skill_score': [80, 70, 60, 90, 80, 75],
        'skill_importance': [0.7, 0.8, 0.5, 0.9, 0.7, 0.6]
    }
    st.session_state.occupation_required_skills_df = pd.DataFrame(occupation_required_skills_data)

    individual_skills_data = {
        'user_id': [1] * 3,
        'skill_name': ['Python', 'Data Visualization', 'Machine Learning'],
        'individual_skill_score': [70, 60, 40]
    }
    st.session_state.individual_skills_df = pd.DataFrame(individual_skills_data)

    st.session_state.selected_occupation_name = 'Data Analyst with AI Skills'
    st.session_state.max_possible_match = 100.0
    st.session_state.current_scores = None
    st.session_state.initialized = True


_init_state()

page = st.sidebar.selectbox(label="Navigation", options=["Overview & Inputs", "Scores & Insights", "Pathway Simulation"])
st.sidebar.subheader("Global Parameters")
st.sidebar.slider(
    "Weight on Individual Factors (\\u03B1)", min_value=0.0, max_value=1.0, value=0.6, step=0.01,
    help="Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$) in the overall AI-Readiness Score.",
    key="alpha_weight",
)
st.sidebar.slider(
    "Synergy Coefficient (\\u03B2)", min_value=0.0, max_value=1.0, value=0.15, step=0.01,
    help="Coefficient for the Synergy component, amplifying the AI-Readiness Score when individual readiness aligns with market opportunity.",
    key="beta_weight",
)

if page == "Overview & Inputs":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Scores & Insights":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Pathway Simulation":
    from application_pages.page3 import run_page3
    run_page3()
