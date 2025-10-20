import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
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
    calculate_synergy_percentage, calculate_ai_readiness_score,
    simulate_pathway_impact
)

def run_page3():
    st.header("Pathway Simulation")
    st.markdown("""
    This page allows you to simulate the impact of different learning pathways on your AI-Readiness Score. Select a pathway and adjust completion/mastery scores to see how your $V^R$, $H^R$, Synergy, and overall AI-R scores are projected to change.

    **Note**: It is recommended to first calculate your base AI-Readiness Score on the "AI-Readiness Score Calculator" page to establish current values before simulating pathways.
    """)

    # Initialize session state for Page 3 inputs and simulation results
    if "page3_initialized" not in st.session_state:
        st.session_state.selected_pathway_name = st.session_state.learning_pathways_df['pathway_name'].iloc[0]
        st.session_state.pathway_completion_score = 1.0
        st.session_state.pathway_mastery_score = 1.0
        st.session_state.simulation_run = False
        st.session_state.page3_initialized = True

    with st.expander("Learning Pathway Inputs", expanded=True):
        st.session_state.selected_pathway_name = st.selectbox(
            label="Select Learning Pathway",
            options=st.session_state.learning_pathways_df['pathway_name'].tolist(),
            index=st.session_state.learning_pathways_df['pathway_name'].tolist().index(st.session_state.selected_pathway_name),
            help="Simulate the impact of completing a learning pathway on your AI-Readiness Score."
        )

        st.session_state.pathway_completion_score = st.slider(
            label="Pathway Completion Score",
            min_value=0.0, max_value=1.0, value=st.session_state.pathway_completion_score, step=0.05,
            help="Score representing the percentage of the pathway completed."
        )

        st.session_state.pathway_mastery_score = st.slider(
            label="Pathway Mastery Score",
            min_value=0.0, max_value=1.0, value=st.session_state.pathway_mastery_score, step=0.05,
            help="Score representing the level of mastery achieved in the pathway."
        )

    if st.button("Simulate Pathway Impact"):
        if "ai_r_score" not in st.session_state:
            st.warning("Please calculate your base AI-Readiness Score on the 'AI-Readiness Score Calculator' page first.")
        else:
            # Retrieve current scores from session state (from Page 2 calculation)
            current_vr_score = st.session_state.vr_score
            current_hr_score = st.session_state.hr_score # HR is generally not directly impacted by individual learning pathways
            current_synergy_percentage = st.session_state.synergy_percentage
            current_ai_r_score = st.session_state.ai_r_score

            # Retrieve current 0-1 scaled VR sub-components for simulation
            current_ai_fluency_0_1 = st.session_state.current_ai_fluency
            current_domain_expertise_0_1 = st.session_state.current_domain_expertise
            current_adaptive_capacity_0_1 = st.session_state.current_adaptive_capacity

            selected_pathway = st.session_state.learning_pathways_df[
                st.session_state.learning_pathways_df['pathway_name'] == st.session_state.selected_pathway_name
            ].iloc[0]

            impact_ai_fluency = selected_pathway['impact_ai_fluency']
            impact_domain_expertise = selected_pathway['impact_domain_expertise']
            impact_adaptive_capacity = selected_pathway['impact_adaptive_capacity']

            # Simulate new VR sub-components
            new_ai_fluency_0_1, new_domain_expertise_0_1, new_adaptive_capacity_0_1 = simulate_pathway_impact(
                current_ai_fluency_0_1, current_domain_expertise_0_1, current_adaptive_capacity_0_1,
                impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity,
                st.session_state.pathway_completion_score, st.session_state.pathway_mastery_score
            )
            
            # Recalculate new VR score based on simulated components
            new_vr_score = calculate_idiosyncratic_readiness(
                new_ai_fluency_0_1, new_domain_expertise_0_1, new_adaptive_capacity_0_1
            ) * 100 # Normalize to 100 for display and further calculations

            # For Synergy calculation, we need required skills for the target occupation
            target_occupation = st.session_state.target_occupation
            required_skills_for_occupation = st.session_state.occupation_required_skills_df[
                st.session_state.occupation_required_skills_df['occupation_name'] == target_occupation
            ]

            # If user_skills_data is modified in page2, use that, otherwise default
            user_skills_data_for_synergy = st.session_state.get('user_skills_data', st.session_state.individual_skills_df)

            skills_match_score = calculate_skills_match_score(
                user_skills_data_for_synergy, required_skills_for_occupation
            )
            timing_factor = calculate_timing_factor(st.session_state.years_experience) # years_experience from Page 2
            max_possible_skills_match = st.session_state.max_possible_skills_match # from Page 2
            alignment_factor = calculate_alignment_factor(
                skills_match_score, max_possible_skills_match, timing_factor
            )
            
            new_synergy_percentage = calculate_synergy_percentage(new_vr_score, current_hr_score, alignment_factor)

            # Recalculate new AI-R score
            new_ai_r_score = calculate_ai_readiness_score(
                new_vr_score, current_hr_score, new_synergy_percentage,
                st.session_state.alpha, st.session_state.beta
            )

            # Store new scores in session state
            st.session_state.new_vr_score = new_vr_score
            st.session_state.new_hr_score = current_hr_score # HR typically unchanged by pathway
            st.session_state.new_synergy_percentage = new_synergy_percentage
            st.session_state.new_ai_r_score = new_ai_r_score
            st.session_state.simulation_run = True
            
            st.session_state.new_ai_fluency_0_1 = new_ai_fluency_0_1
            st.session_state.new_domain_expertise_0_1 = new_domain_expertise_0_1
            st.session_state.new_adaptive_capacity_0_1 = new_adaptive_capacity_0_1

            st.success("Pathway Impact Simulated!")

    if st.session_state.simulation_run:
        st.subheader("Current vs. Projected AI-Readiness Scores")

        metrics_data = {
            "Metric": ["AI-R Score", "V^R Score", "H^R Score", "Synergy %"],
            "Current": [
                st.session_state.ai_r_score,
                st.session_state.vr_score,
                st.session_state.hr_score,
                st.session_state.synergy_percentage,
            ],
            "Projected": [
                st.session_state.new_ai_r_score,
                st.session_state.new_vr_score,
                st.session_state.new_hr_score,
                st.session_state.new_synergy_percentage,
            ],
        }
        metrics_df = pd.DataFrame(metrics_data)

        fig_comparison = go.Figure()
        fig_comparison.add_trace(go.Bar(name='Current', x=metrics_df['Metric'], y=metrics_df['Current']))
        fig_comparison.add_trace(go.Bar(name='Projected', x=metrics_df['Metric'], y=metrics_df['Projected']))

        fig_comparison.update_layout(barmode='group', title='Comparison: Current vs. Projected Scores')
        st.plotly_chart(fig_comparison, use_container_width=True)

        st.subheader("Current vs. Projected V^R Sub-Components")
        vr_sub_components_data = {
            "Component": ["AI-Fluency", "Domain-Expertise", "Adaptive-Capacity"],
            "Current": [
                st.session_state.current_ai_fluency * 100, # Display normalized to 100
                st.session_state.current_domain_expertise * 100,
                st.session_state.current_adaptive_capacity * 100,
            ],
            "Projected": [
                st.session_state.new_ai_fluency_0_1 * 100,
                st.session_state.new_domain_expertise_0_1 * 100,
                st.session_state.new_adaptive_capacity_0_1 * 100,
            ],
        }
        vr_sub_components_df = pd.DataFrame(vr_sub_components_data)

        fig_vr_sub_comparison = go.Figure()
        fig_vr_sub_comparison.add_trace(go.Bar(name='Current', x=vr_sub_components_df['Component'], y=vr_sub_components_df['Current']))
        fig_vr_sub_comparison.add_trace(go.Bar(name='Projected', x=vr_sub_components_df['Component'], y=vr_sub_components_df['Projected']))
        fig_vr_sub_comparison.update_layout(barmode='group', title='Comparison: Current vs. Projected V^R Sub-Components')
        st.plotly_chart(fig_vr_sub_comparison, use_container_width=True)
