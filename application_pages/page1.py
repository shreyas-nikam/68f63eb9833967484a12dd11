import streamlit as st
import pandas as pd
import plotly.express as px

def run_page1():
    st.header("AI-Readiness Score Components: Core Concepts")
    st.markdown("""
    This section introduces the foundational components of the AI-Readiness Score (AI-R): **Idiosyncratic Readiness** ($V^R$), **Systematic Opportunity** ($H^R$), and **Synergy**. Understanding these elements is crucial for evaluating and enhancing an individual's career preparedness in an AI-driven landscape.

    ### Core AI-Readiness Functions
    This section implements the various functions required to calculate the $V^R$, $H^R$, and Synergy components, leading to the final AI-Readiness Score. Each function directly corresponds to a mathematical definition or calculation method outlined in the provided technical paper, with adjustments made to reflect the actual Python implementation in the Jupyter Notebook. The correct implementation of these functions is essential for the accuracy of the AI-R score.
    """)

    st.subheader("1. Idiosyncratic Readiness ($V^R$)")
    st.markdown("""
    $V^R$ quantifies an individual's personal capabilities and readiness for AI-enabled roles. It is a composite score based on three main sub-components:

    -   **AI-Fluency**: Measures an individual's proficiency in interacting with AI systems, understanding AI outputs, and adapting to AI-driven workflows.
        $$ \text{AI-Fluency} = 0.1 \cdot S_{i,1} + 0.2 \cdot S_{i,2} + 0.3 \cdot S_{i,3} + 0.4 \cdot S_{i,4} $$
        Where:
        -   $S_{i,1}$: Technical AI Skills
        -   $S_{i,2}$: AI-Augmented Productivity
        -   $S_{i,3}$: Critical AI Judgment
        -   $S_{i,4}$: AI Learning Velocity

    -   **Domain-Expertise**: Assesses the depth of knowledge and experience within a specific field, including educational background, professional experience, and specialized skills.
        $$ \text{Domain-Expertise} = 0.125 \cdot E_{\text{education}} + 0.25 \cdot E_{\text{experience}} + 0.625 \cdot E_{\text{specialization}} $$
        Where:
        -   $E_{\text{education}}$: Education Foundation
        -   $E_{\text{experience}}$: Practical Experience
        -   $E_{\text{specialization}}$: Specialization Depth

    -   **Adaptive-Capacity**: Evaluates an individual's ability to adapt to new technologies, learn new skills, and navigate changing career landscapes.
        $$ \text{Adaptive-Capacity} = \frac{\text{cognitive\_flexibility} + \text{social\_emotional\_intelligence} + \text{strategic\_career\_management}}{3} $$
    The overall $V^R$ is a weighted sum of these components:
    $$ V^R = w_1 \cdot \text{AI-Fluency} + w_2 \cdot \text{Domain-Expertise} + w_3 \cdot \text{Adaptive-Capacity} $$
    *Typically, $w_1=0.45, w_2=0.35, w_3=0.20$*.
    """)

    st.subheader("2. Systematic Opportunity ($H^R$)")
    st.markdown("""
    $H^R$ reflects the external market demand and opportunities available for a given AI-enabled career path. It considers various market factors:

    -   **AI-Enhancement Potential**: The degree to which AI can augment or transform a particular occupation.
    -   **Job Growth Projection**: Future growth prospects for the occupation.
    -   **Wage Premium**: The additional earnings potential for AI-skilled professionals in that role.
    -   **Entry Accessibility**: The ease of entering the occupation based on educational and experience requirements.

    These factors combine to form a base opportunity score, which is then adjusted by growth and regional multipliers:
    $$ H^R = H_{\text{base}} \cdot M_{\text{growth}} \cdot M_{\text{regional}} $$
    Where:
    -   $H_{\text{base}}$: Base Opportunity Score
    -   $M_{\text{growth}}$: Growth Multiplier
    -   $M_{\text{regional}}$: Regional Multiplier
    """)

    st.subheader("3. Synergy Percentage ($	ext{Synergy}\%$)")
    st.markdown("""
    The Synergy component captures the alignment between an individual's capabilities ($V^R$) and the market's opportunities ($H^R$), particularly focusing on skills matching and timing factors. A high synergy indicates a strong fit between individual readiness and market demand.
    $$ \text{Synergy}\% = \frac{V^R \cdot H^R \cdot \text{Alignment}}{100.0} $$
    Where:
    -   **Skills Match Score**: Measures how well an individual's skills align with the required skills for a target occupation.
    -   **Timing Factor**: Accounts for the relevance of experience in the current market.
    -   **Alignment Factor**: Combines skills match and timing to represent overall strategic alignment.
    """)

    st.subheader("Synthetic Dataframes for Reference")

    with st.expander("Individual Profiles Data"): 
        st.dataframe(st.session_state.individual_profiles_df)

    with st.expander("Occupational Data"): 
        st.dataframe(st.session_state.occupational_data_df)

    with st.expander("Learning Pathways Data"): 
        st.dataframe(st.session_state.learning_pathways_df)

    with st.expander("Occupation Required Skills Data"): 
        st.dataframe(st.session_state.occupation_required_skills_df)

    with st.expander("Individual Skills Data"): 
        st.dataframe(st.session_state.individual_skills_df)
