import streamlit as st
import pandas as pd
import plotly.express as px
from application_pages.core import compute_all_scores, simulate_pathway_impact


def _get_selected_occupation_row(occupation_name):
    df = st.session_state.occupational_data_df
    row = df[df['occupation_name'] == occupation_name]
    if row.empty:
        return df.iloc[0]
    return row.iloc[0]


def run_page3():
    st.subheader("Pathway Simulation")
    st.markdown("Explore how completing a learning pathway could change your $V^R$, Synergy, and overall AI-Readiness.")

    if st.session_state.get('current_scores', None) is None:
        st.info("Tip: Compute your baseline first on 'Overview & Inputs'. You can still simulate now; the baseline will be derived from current inputs.")

    # Select pathway and parameters
    lp_df = st.session_state.learning_pathways_df
    pathway_name = st.selectbox("Select Learning Pathway", options=list(lp_df['pathway_name'].values), index=0)
    pathway_row = lp_df[lp_df['pathway_name'] == pathway_name].iloc[0]

    completion_score = st.slider("Pathway Completion Score", 0.0, 1.0, 1.0, 0.05, help="Simulate completion extent.")
    mastery_score = st.slider("Pathway Mastery Score", 0.0, 1.0, 1.0, 0.05, help="Simulate mastery depth.")

    # Build baseline inputs from session
    occ_row = _get_selected_occupation_row(st.session_state.selected_occupation_name)
    required_skills_df = st.session_state.occupation_required_skills_df[
        st.session_state.occupation_required_skills_df['occupation_name'] == st.session_state.selected_occupation_name
    ][['skill_name', 'required_skill_score', 'skill_importance']]

    base_inputs = {
        'prompting_score': st.session_state.prompting_score,
        'tools_score': st.session_state.tools_score,
        'understanding_score': st.session_state.understanding_score,
        'datalit_score': st.session_state.datalit_score,
        'output_quality_with_ai': st.session_state.output_quality_with_ai,
        'output_quality_without_ai': st.session_state.output_quality_without_ai,
        'time_without_ai': st.session_state.time_without_ai,
        'time_with_ai': st.session_state.time_with_ai,
        'errors_caught': st.session_state.errors_caught,
        'total_ai_errors': st.session_state.total_ai_errors,
        'appropriate_trust_decisions': st.session_state.appropriate_trust_decisions,
        'total_decisions': st.session_state.total_decisions,
        'delta_proficiency': st.session_state.delta_proficiency,
        'delta_t_hours_invested': st.session_state.delta_t_hours_invested,
        'education_level': st.session_state.education_level,
        'years_experience': st.session_state.years_experience,
        'portfolio_score': st.session_state.portfolio_score,
        'recognition_score': st.session_state.recognition_score,
        'credentials_score': st.session_state.credentials_score,
        'cognitive_flexibility': st.session_state.cognitive_flexibility,
        'social_emotional_intelligence': st.session_state.social_emotional_intelligence,
        'strategic_career_management': st.session_state.strategic_career_management,
        'occupation_row': occ_row,
        'lambda_val': st.session_state.lambda_val,
        'gamma_val': st.session_state.gamma_val,
        'individual_skills_df': st.session_state.individual_skills_df.copy(),
        'required_skills_df': required_skills_df.copy(),
        'max_possible_match': st.session_state.max_possible_match,
        'alpha': st.session_state.alpha_weight,
        'beta': st.session_state.beta_weight,
    }

    # Baseline scores (reuse if available)
    baseline = st.session_state.get('current_scores', None)
    if baseline is None:
        baseline = compute_all_scores(base_inputs)

    # Current VR component levels (0..1)
    current_ai_fluency = baseline['vr_breakdown']['AI-Fluency (01)']
    current_domain_expertise = baseline['vr_breakdown']['Domain-Expertise (01)']
    current_adaptive_capacity = baseline['vr_breakdown']['Adaptive-Capacity (01)']

    # Apply pathway impacts
    sim_ai_fluency, sim_domain_expertise, sim_adaptive_capacity = simulate_pathway_impact(
        current_ai_fluency,
        current_domain_expertise,
        current_adaptive_capacity,
        pathway_row['impact_ai_fluency'],
        pathway_row['impact_domain_expertise'],
        pathway_row['impact_adaptive_capacity'],
        completion_score=completion_score,
        mastery_score=mastery_score,
    )

    # Compute HR and alignment from baseline inputs
    base_results = compute_all_scores(base_inputs)

    # Rebuild simulated V^R
    vr_new_01 = max(0.0, min(1.0, 0.45 * float(sim_ai_fluency) + 0.35 * float(sim_domain_expertise) + 0.20 * float(sim_adaptive_capacity)))
    vr_new_100 = vr_new_01 * 100.0

    # Keep HR and alignment from base
    hr_100 = base_results['hr_score']
    alignment = base_results['alignment']

    # New synergy and AI-R
    synergy_new = (vr_new_100 * hr_100 * alignment) / 100.0
    synergy_new = max(0.0, min(100.0, synergy_new))
    ai_r_new = st.session_state.alpha_weight * vr_new_100 + (1.0 - st.session_state.alpha_weight) * hr_100 + st.session_state.beta_weight * synergy_new

    # Comparison chart
    st.markdown("Current vs. Projected after pathway simulation")
    comp_df = pd.DataFrame({
        'Metric': ['V^R', 'H^R', 'Synergy%', 'AI-R'],
        'Current': [baseline['vr_score'], baseline['hr_score'], baseline['synergy_pct'], baseline['ai_r']],
        'Projected': [vr_new_100, hr_100, synergy_new, ai_r_new],
    })
    fig_comp = px.bar(
        comp_df.melt(id_vars='Metric', value_vars=['Current', 'Projected'], var_name='State', value_name='Score'),
        x='Metric', y='Score', color='State', barmode='group', title='Comparison: Current vs. Projected Scores'
    )
    st.plotly_chart(fig_comp, use_container_width=True)

    # KPI tiles
    st.markdown("Projected component values")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("V^R (new)", f"{vr_new_100:.1f}")
    c2.metric("H^R (unchanged)", f"{hr_100:.1f}")
    c3.metric("Synergy % (new)", f"{synergy_new:.1f}")
    c4.metric("AI-R (new)", f"{ai_r_new:.1f}")

    with st.expander("Pathway parameters and impacts"):
        st.write({
            'pathway_name': pathway_name,
            'completion_score': float(completion_score),
            'mastery_score': float(mastery_score),
            'impact_ai_fluency': float(pathway_row['impact_ai_fluency']),
            'impact_domain_expertise': float(pathway_row['impact_domain_expertise']),
            'impact_adaptive_capacity': float(pathway_row['impact_adaptive_capacity']),
            'sim_ai_fluency (01)': float(sim_ai_fluency),
            'sim_domain_expertise (01)': float(sim_domain_expertise),
            'sim_adaptive_capacity (01)': float(sim_adaptive_capacity),
        })
