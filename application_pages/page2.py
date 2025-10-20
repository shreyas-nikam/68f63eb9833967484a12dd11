import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from application_pages.ai_readiness_functions import (
    calculate_technical_ai_skills, calculate_ai_augmented_productivity,
    calculate_critical_ai_judgment, calculate_ai_learning_velocity,
    calculate_ai_fluency, calculate_education_foundation,
    calculate_practical_experience, calculate_specialization_depth,
    calculate_domain_expertise, calculate_adaptive_capacity,
    calculate_idiosyncratic_readiness, calculate_ai_enhancement_potential,
    calculate_job_growth_projection, calculate_wage_premium,
    calculate_entry_accessibility, calculate_base_opportunity_score,
    calculate_growth_multiplier, calculate_regional_multiplier,
    calculate_systematic_opportunity, calculate_skills_match_score,
    calculate_timing_factor, calculate_alignment_factor,
    calculate_synergy_percentage, calculate_ai_readiness_score
)

def run_page2():
    st.header("AI-Readiness Score Calculator")
    st.markdown("""
    This page allows you to input various parameters to calculate your **AI-Readiness Score (AI-R)**. Adjust the sliders and dropdowns to see how different factors influence your individual readiness, market opportunity, and overall AI-R score.
    """)

    # Initialize session state for inputs if not already present
    if "page2_initialized" not in st.session_state:
        st.session_state.alpha = 0.6
        st.session_state.beta = 0.15

        # VR inputs (using values from individual_profiles_df as defaults)
        st.session_state.prompting_score = 0.75
        st.session_state.tools_score = 0.6
        st.session_state.understanding_score = 0.8
        st.session_state.datalit_score = 0.9
        st.session_state.output_quality_with_ai = 90
        st.session_state.output_quality_without_ai = 60
        st.session_state.time_without_ai = 4
        st.session_state.time_with_ai = 1
        st.session_state.errors_caught = 15
        st.session_state.total_ai_errors = 20
        st.session_state.appropriate_trust_decisions = 25
        st.session_state.total_decisions = 30
        st.session_state.delta_proficiency = 0.3
        st.session_state.delta_t_hours_invested = 10

        st.session_state.education_level = "Master's"
        st.session_state.years_experience = 5
        st.session_state.portfolio_score = 0.85
        st.session_state.recognition_score = 0.7
        st.session_state.credentials_score = 0.9

        st.session_state.cognitive_flexibility = 85
        st.session_state.social_emotional_intelligence = 90
        st.session_state.strategic_career_management = 75
        
        # HR inputs
        st.session_state.target_occupation = "Data Analyst with AI Skills"
        st.session_state.lambda_val = 0.3
        st.session_state.gamma_val = 0.2
        
        # Synergy inputs
        st.session_state.user_skills_data = st.session_state.individual_skills_df.copy()
        st.session_state.max_possible_skills_match = 100
        
        st.session_state.page2_initialized = True

    # Global Parameters
    st.sidebar.subheader("Global Parameters")
    st.session_state.alpha = st.sidebar.slider(
        label="Weight on Individual Factors (\\alpha)",
        min_value=0.0, max_value=1.0, value=st.session_state.alpha, step=0.05,
        help="Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$) in the overall AI-Readiness Score."
    )
    st.session_state.beta = st.sidebar.slider(
        label="Synergy Coefficient (\\beta)",
        min_value=0.0, max_value=1.0, value=st.session_state.beta, step=0.05,
        help="Coefficient for the Synergy component, amplifying the AI-Readiness Score when individual readiness aligns with market opportunity."
    )

    with st.expander("Idiosyncratic Readiness (V^R) Inputs", expanded=True):
        st.markdown("Adjust your personal attributes and skills that contribute to your $V^R$ score.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("AI-Fluency Sub-Components")
            st.session_state.prompting_score = st.slider("Prompting Score", 0.0, 1.0, st.session_state.prompting_score, 0.05, help="Skill in crafting effective prompts for AI systems ($S_{i,1}$ component).")
            st.session_state.tools_score = st.slider("Tools Score", 0.0, 1.0, st.session_state.tools_score, 0.05, help="Proficiency in using AI-powered tools and platforms ($S_{i,1}$ component).")
            st.session_state.understanding_score = st.slider("Understanding Score", 0.0, 1.0, st.session_state.understanding_score, 0.05, help="Ability to interpret and comprehend AI outputs and models ($S_{i,1}$ component).")
            st.session_state.datalit_score = st.slider("Datalit Score", 0.0, 1.0, st.session_state.datalit_score, 0.05, help="Data Literacy: ability to understand, analyze, and use data effectively ($S_{i,1}$ component).")
            st.session_state.output_quality_with_ai = st.number_input("Output Quality with AI", 0, 100, st.session_state.output_quality_with_ai, help="Quality of output when using AI tools (for $S_{i,2}$).")
            st.session_state.output_quality_without_ai = st.number_input("Output Quality without AI", 0, 100, st.session_state.output_quality_without_ai, help="Quality of output without using AI tools (for $S_{i,2}$).")
            st.session_state.time_without_ai = st.number_input("Time without AI (hours)", 1, 100, st.session_state.time_without_ai, help="Time taken for a task without AI (for $S_{i,2}$).")
            st.session_state.time_with_ai = st.number_input("Time with AI (hours)", 1, 100, st.session_state.time_with_ai, help="Time taken for a task with AI (for $S_{i,2}$).")
            st.session_state.errors_caught = st.number_input("Errors Caught", 0, 100, st.session_state.errors_caught, help="Number of AI-generated errors an individual successfully identified (for $S_{i,3}$).")
            st.session_state.total_ai_errors = st.number_input("Total AI Errors", 0, 100, st.session_state.total_ai_errors, help="Total number of AI-generated errors present (for $S_{i,3}$).")
            st.session_state.appropriate_trust_decisions = st.number_input("Appropriate Trust Decisions", 0, 100, st.session_state.appropriate_trust_decisions, help="Number of times an individual made appropriate decisions regarding trusting AI (for $S_{i,3}$).")
            st.session_state.total_decisions = st.number_input("Total Decisions", 0, 100, st.session_state.total_decisions, help="Total number of AI-related trust decisions made (for $S_{i,3}$).")
            st.session_state.delta_proficiency = st.slider("Delta Proficiency", 0.0, 1.0, st.session_state.delta_proficiency, 0.05, help="Change in proficiency over a learning period (for $S_{i,4}$).")
            st.session_state.delta_t_hours_invested = st.number_input("Delta T Hours Invested", 0, 100, st.session_state.delta_t_hours_invested, help="Hours invested in learning or training (for $S_{i,4}$).")

        with col2:
            st.subheader("Domain-Expertise Sub-Components")
            education_options = ["PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other"]
            st.session_state.education_level = st.selectbox("Education Level", education_options, education_options.index(st.session_state.education_level), help="Highest level of education attained ($E_{\text{education}}$ component).")
            st.session_state.years_experience = st.number_input("Years Experience", 0, 50, st.session_state.years_experience, help="Total years of professional experience ($E_{\text{experience}}$ component).")
            st.session_state.portfolio_score = st.slider("Portfolio Score", 0.0, 1.0, st.session_state.portfolio_score, 0.05, help="Quality and relevance of personal project portfolio ($E_{\text{specialization}}$ component).")
            st.session_state.recognition_score = st.slider("Recognition Score", 0.0, 1.0, st.session_state.recognition_score, 0.05, help="Industry recognition, awards, or publications ($E_{\text{specialization}}$ component).")
            st.session_state.credentials_score = st.slider("Credentials Score", 0.0, 1.0, st.session_state.credentials_score, 0.05, help="Relevant certifications or specialized training ($E_{\text{specialization}}$ component).")

        with col3:
            st.subheader("Adaptive-Capacity Sub-Components")
            st.session_state.cognitive_flexibility = st.slider("Cognitive Flexibility", 0, 100, st.session_state.cognitive_flexibility, help="Ability to adapt thinking to new situations and information.")
            st.session_state.social_emotional_intelligence = st.slider("Social-Emotional Intelligence", 0, 100, st.session_state.social_emotional_intelligence, help="Ability to understand and manage one's own emotions, and to understand and influence the emotions of others.")
            st.session_state.strategic_career_management = st.slider("Strategic Career Management", 0, 100, st.session_state.strategic_career_management, help="Proactive approach to planning and developing one's career path.")

    with st.expander("Systematic Opportunity (H^R) Inputs", expanded=True):
        st.markdown("Select a target occupation and adjust market parameters that contribute to your $H^R$ score.")
        st.session_state.target_occupation = st.selectbox(
            label="Target Occupation",
            options=st.session_state.occupational_data_df['occupation_name'].tolist(),
            index=st.session_state.occupational_data_df['occupation_name'].tolist().index(st.session_state.target_occupation),
            help="Select a target occupation to calculate your market opportunity ($H^R$) based on its attributes."
        )

        current_occupation_data = st.session_state.occupational_data_df[
            st.session_state.occupational_data_df['occupation_name'] == st.session_state.target_occupation
        ].iloc[0]

        st.session_state.lambda_val = st.slider(
            label="Lambda value for Growth Multiplier (\\lambda)",
            min_value=0.0, max_value=1.0, value=st.session_state.lambda_val, step=0.05,
            help="Adjust $\lambda$ to dampen volatility in job posting growth."
        )
        st.session_state.gamma_val = st.slider(
            label="Gamma value for Regional Multiplier (\\gamma)",
            min_value=0.0, max_value=1.0, value=st.session_state.gamma_val, step=0.05,
            help="Adjust $\gamma$ for regional market influence."
        )

    with st.expander("Synergy Inputs", expanded=True):
        st.markdown("Manage your individual skills and define the maximum possible skills match for the synergy calculation.")
        
        st.session_state.max_possible_skills_match = st.number_input(
            "Max Possible Skills Match", 1, 200, st.session_state.max_possible_skills_match,
            help="The theoretical maximum possible skills match score (e.g., 100 if scores are out of 100)." 
        )

        st.subheader("Your Individual Skills")
        st.dataframe(st.session_state.user_skills_data, key="individual_skills_editor") # Display existing skills
        
        st.subheader("Required Skills for Selected Occupation")
        required_skills_for_occupation = st.session_state.occupation_required_skills_df[
            st.session_state.occupation_required_skills_df['occupation_name'] == st.session_state.target_occupation
        ]
        if required_skills_for_occupation.empty:
            st.info(f"No specific required skills listed for {st.session_state.target_occupation}.")
        else:
            st.dataframe(required_skills_for_occupation)

    if st.button("Calculate AI-Readiness Score"):
        # Calculate VR Components
        s1 = calculate_technical_ai_skills(
            st.session_state.prompting_score, st.session_state.tools_score, 
            st.session_state.understanding_score, st.session_state.datalit_score
        )
        s2 = calculate_ai_augmented_productivity(
            st.session_state.output_quality_with_ai, st.session_state.output_quality_without_ai,
            st.session_state.time_without_ai, st.session_state.time_with_ai
        )
        s3 = calculate_critical_ai_judgment(
            st.session_state.errors_caught, st.session_state.total_ai_errors,
            st.session_state.appropriate_trust_decisions, st.session_state.total_decisions
        )
        s4 = calculate_ai_learning_velocity(
            st.session_state.delta_proficiency, st.session_state.delta_t_hours_invested
        )
        ai_fluency = calculate_ai_fluency(s1, s2, s3, s4)

        e_education = calculate_education_foundation(st.session_state.education_level)
        e_experience = calculate_practical_experience(st.session_state.years_experience)
        e_specialization = calculate_specialization_depth(
            st.session_state.portfolio_score, st.session_state.recognition_score,
            st.session_state.credentials_score
        )
        domain_expertise = calculate_domain_expertise(e_education, e_experience, e_specialization)

        adaptive_capacity = calculate_adaptive_capacity(
            st.session_state.cognitive_flexibility, st.session_state.social_emotional_intelligence,
            st.session_state.strategic_career_management
        )
        
        # Normalize VR sub-components to 100 for display, but calculations use 0-1 scale 
        st.session_state.ai_fluency_normalized = ai_fluency * 100
        st.session_state.domain_expertise_normalized = domain_expertise * 100
        st.session_state.adaptive_capacity_normalized = adaptive_capacity # This is already 0-100

        vr_score = calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity/100) * 100 # Normalize adaptive capacity for VR calc, then VR itself to 100
        st.session_state.vr_score = vr_score

        # Calculate HR Components
        ai_enhancement_potential = current_occupation_data['ai_enhancement_score']
        job_growth_projection = calculate_job_growth_projection(current_occupation_data['job_growth_rate_g'])
        wage_premium = calculate_wage_premium(current_occupation_data['ai_skilled_wage'], current_occupation_data['median_wage'])
        entry_accessibility = calculate_entry_accessibility(current_occupation_data['education_years_required'], current_occupation_data['experience_years_required'])

        h_base = calculate_base_opportunity_score(
            ai_enhancement_potential,
            job_growth_projection / 100, # Normalize job growth for calculation
            wage_premium,
            entry_accessibility
        )

        growth_multiplier = calculate_growth_multiplier(
            current_occupation_data['current_job_postings'], current_occupation_data['previous_job_postings'],
            st.session_state.lambda_val
        )
        regional_multiplier = calculate_regional_multiplier(
            current_occupation_data['local_demand'], current_occupation_data['national_avg_demand'],
            current_occupation_data['remote_work_factor'], st.session_state.gamma_val
        )

        hr_score = calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier) * 100 # Normalize to 100
        st.session_state.hr_score = hr_score
        
        # Calculate Synergy
        skills_match_score = calculate_skills_match_score(
            st.session_state.user_skills_data, required_skills_for_occupation
        )
        timing_factor = calculate_timing_factor(st.session_state.years_experience)
        alignment_factor = calculate_alignment_factor(
            skills_match_score, st.session_state.max_possible_skills_match, timing_factor
        )
        synergy_percentage = calculate_synergy_percentage(vr_score, hr_score, alignment_factor)
        st.session_state.synergy_percentage = synergy_percentage

        # Calculate Final AI-R Score
        st.session_state.ai_r_score = calculate_ai_readiness_score(
            vr_score, hr_score, synergy_percentage,
            st.session_state.alpha, st.session_state.beta
        )
        st.success("AI-Readiness Score Calculated!")
    
    # Display Results
    if "ai_r_score" in st.session_state:
        st.subheader("Calculated AI-Readiness Score")
        col_res1, col_res2, col_res3, col_res4 = st.columns(4)
        col_res1.metric("Idiosyncratic Readiness (V^R)", f"{st.session_state.vr_score:.2f}")
        col_res2.metric("Systematic Opportunity (H^R)", f"{st.session_state.hr_score:.2f}")
        col_res3.metric("Synergy %", f"{st.session_state.synergy_percentage:.2f}")
        col_res4.metric("Overall AI-Readiness Score (AI-R)", f"{st.session_state.ai_r_score:.2f}")

        st.subheader("Visualizations")
        # Pie chart for VR components
        vr_components_data = {'Component': ['AI-Fluency', 'Domain-Expertise', 'Adaptive-Capacity'], 
                              'Score': [st.session_state.ai_fluency_normalized, 
                                          st.session_state.domain_expertise_normalized, 
                                          st.session_state.adaptive_capacity_normalized]}
        vr_components_df = pd.DataFrame(vr_components_data)

        fig_vr_pie = px.pie(vr_components_df, values='Score', names='Component',
                            title='Contribution to Idiosyncratic Readiness (V^R)')
        st.plotly_chart(fig_vr_pie, use_container_width=True)

        # Bar chart for HR base components
        # Need to recalculate the base components to display them individually
        ai_enhancement_potential = current_occupation_data['ai_enhancement_score'] * 100 # Scale for display
        job_growth_projection = calculate_job_growth_projection(current_occupation_data['job_growth_rate_g'])
        wage_premium = calculate_wage_premium(current_occupation_data['ai_skilled_wage'], current_occupation_data['median_wage']) * 100 # Scale for display
        entry_accessibility = calculate_entry_accessibility(current_occupation_data['education_years_required'], current_occupation_data['experience_years_required']) * 100 # Scale for display

        hr_components_data = {'Component': ['AI-Enhancement Potential', 'Job Growth Projection', 'Wage Premium', 'Entry Accessibility'],
                              'Score': [ai_enhancement_potential, job_growth_projection, wage_premium, entry_accessibility]}
        hr_components_df = pd.DataFrame(hr_components_data)

        fig_hr_bar = px.bar(hr_components_df, x='Component', y='Score',
                            title='Systematic Opportunity (H^R) Base Components', 
                            labels={'Score': 'Score (0-100)'})
        st.plotly_chart(fig_hr_bar, use_container_width=True)

