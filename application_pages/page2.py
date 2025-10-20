import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from application_pages.ai_readiness_core import (
    calculate_technical_ai_skills,
    calculate_ai_augmented_productivity,
    calculate_critical_ai_judgment,
    calculate_ai_learning_velocity,
    calculate_ai_fluency,
    calculate_education_foundation,
    calculate_practical_experience,
    calculate_specialization_depth,
    calculate_domain_expertise,
    calculate_adaptive_capacity,
    calculate_idiosyncratic_readiness,
    calculate_ai_enhancement_potential,
    calculate_job_growth_projection,
    calculate_wage_premium,
    calculate_entry_accessibility,
    calculate_base_opportunity_score,
    calculate_growth_multiplier,
    calculate_regional_multiplier,
    calculate_systematic_opportunity,
    calculate_skills_match_score,
    calculate_timing_factor,
    calculate_alignment_factor,
    calculate_synergy_percentage,
    calculate_ai_readiness_score,
    clamp_0_1,
    to_0_100_from_0_1,
)


def gauge(title, value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': '#2C7BE5'}}
    ))
    fig.update_layout(height=280, margin=dict(l=10, r=10, t=40, b=10))
    return fig


def run_page2():
    st.header("AI-Readiness Calculator")

    # Global parameters
    with st.expander("Global Parameters", expanded=True):
        c1, c2, c3 = st.columns([1,1,2])
        with c1:
            alpha = st.slider("Weight on Individual Factors (\\u03B1)", 0.0, 1.0, float(st.session_state.get("alpha", 0.6)), step=0.01,
                               help="Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$) in the overall AI-Readiness Score.")
        with c2:
            beta = st.slider("Synergy Coefficient (\\u03B2)", 0.0, 1.0, float(st.session_state.get("beta", 0.15)), step=0.01,
                              help="Coefficient for the Synergy component, amplifying the AI-Readiness Score when individual readiness aligns with market opportunity.")
        with c3:
            st.markdown(r"""\
$AI\text{-}R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R)$
""")
        st.session_state["alpha"] = alpha
        st.session_state["beta"] = beta

    # Idiosyncratic Readiness Inputs
    st.subheader("Idiosyncratic Readiness ($V^R$) Inputs")
    tab1, tab2, tab3 = st.tabs(["AI-Fluency", "Domain-Expertise", "Adaptive-Capacity"])

    with tab1:
        c1, c2, c3, c4 = st.columns(4)
        prompting = c1.slider("Prompting Score", 0.0, 1.0, float(st.session_state["individual_profiles_df"].iloc[0]['prompting_score']), step=0.01,
                              help="Part of Technical AI Skills $S_{i,1}$")
        tools = c2.slider("Tools Score", 0.0, 1.0, float(st.session_state["individual_profiles_df"].iloc[0]['tools_score']), step=0.01,
                          help="Part of Technical AI Skills $S_{i,1}$")
        understanding = c3.slider("Understanding Score", 0.0, 1.0, float(st.session_state["individual_profiles_df"].iloc[0]['understanding_score']), step=0.01,
                                  help="Part of Technical AI Skills $S_{i,1}$")
        datalit = c4.slider("Datalit Score", 0.0, 1.0, float(st.session_state["individual_profiles_df"].iloc[0]['datalit_score']), step=0.01,
                            help="Part of Technical AI Skills $S_{i,1}$")

        c5, c6 = st.columns(2)
        with c5:
            oq_ai = st.slider("Output Quality with AI", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['output_quality_with_ai']), step=1,
                              help="Used in AI-Augmented Productivity $S_{i,2}$")
            oq_noai = st.slider("Output Quality without AI", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['output_quality_without_ai']), step=1,
                                help="Used in AI-Augmented Productivity $S_{i,2}$")
            t_noai = st.slider("Time without AI (hours)", 0, 24, int(st.session_state["individual_profiles_df"].iloc[0]['time_without_ai']), step=1,
                                help="Used in AI-Augmented Productivity $S_{i,2}$")
            t_ai = st.slider("Time with AI (hours)", 0, 24, int(st.session_state["individual_profiles_df"].iloc[0]['time_with_ai']), step=1,
                             help="Used in AI-Augmented Productivity $S_{i,2}$")
        with c6:
            errors_caught = st.slider("Errors Caught", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['errors_caught']), step=1,
                                      help="Used in Critical AI Judgment $S_{i,3}$")
            total_ai_errors = st.slider("Total AI Errors", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['total_ai_errors']), step=1,
                                        help="Used in Critical AI Judgment $S_{i,3}$")
            appropriate_trust = st.slider("Appropriate Trust Decisions", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['appropriate_trust_decisions']), step=1,
                                          help="Used in Critical AI Judgment $S_{i,3}$")
            total_decisions = st.slider("Total Decisions", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['total_decisions']), step=1,
                                        help="Used in Critical AI Judgment $S_{i,3}$")

        c7, c8 = st.columns(2)
        with c7:
            delta_prof = st.slider("Delta Proficiency", 0.0, 1.0, float(st.session_state["individual_profiles_df"].iloc[0]['delta_proficiency']), step=0.01,
                                   help="Used in AI Learning Velocity $S_{i,4}$")
        with c8:
            delta_hours = st.slider("Delta T Hours Invested", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['delta_t_hours_invested']), step=1,
                                    help="Used in AI Learning Velocity $S_{i,4}$")

    with tab2:
        education_level = st.selectbox("Education Level", options=["PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other"],
                                       index=["PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other"].index(st.session_state["individual_profiles_df"].iloc[0]['education_level']),
                                       help="Part of Domain-Expertise: $E_{education}$")
        years_experience = st.slider("Years Experience", 0, 40, int(st.session_state["individual_profiles_df"].iloc[0]['years_experience']), step=1,
                                     help="Part of Domain-Expertise: $E_{experience}$ and used in Timing Factor")
        c1, c2, c3 = st.columns(3)
        portfolio_score = c1.slider("Portfolio Score", 0.0, 1.0, float(st.session_state["individual_profiles_df"].iloc[0]['portfolio_score']), step=0.01,
                                    help="Part of Domain-Expertise: $E_{specialization}$")
        recognition_score = c2.slider("Recognition Score", 0.0, 1.0, float(st.session_state["individual_profiles_df"].iloc[0]['recognition_score']), step=0.01,
                                      help="Part of Domain-Expertise: $E_{specialization}$")
        credentials_score = c3.slider("Credentials Score", 0.0, 1.0, float(st.session_state["individual_profiles_df"].iloc[0]['credentials_score']), step=0.01,
                                      help="Part of Domain-Expertise: $E_{specialization}$")

    with tab3:
        c1, c2, c3 = st.columns(3)
        cognitive_flexibility = c1.slider("Cognitive Flexibility", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['cognitive_flexibility']), step=1,
                                          help="Avg. input in Adaptive-Capacity")
        social_emotional_intelligence = c2.slider("Social-Emotional Intelligence", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['social_emotional_intelligence']), step=1,
                                                  help="Avg. input in Adaptive-Capacity")
        strategic_career_management = c3.slider("Strategic Career Management", 0, 100, int(st.session_state["individual_profiles_df"].iloc[0]['strategic_career_management']), step=1,
                                               help="Avg. input in Adaptive-Capacity")

    # Systematic Opportunity Inputs
    st.subheader("Systematic Opportunity ($H^R$) Inputs")
    occ_df = st.session_state["occupational_data_df"]
    selected_occupation = st.selectbox("Target Occupation", options=list(occ_df['occupation_name'].values),
                                       index=list(occ_df['occupation_name'].values).index(st.session_state.get("selected_occupation", "Data Analyst with AI Skills")),
                                       help="Select a target occupation to calculate your market opportunity ($H^R$) based on its attributes.")
    st.session_state["selected_occupation"] = selected_occupation
    c1, c2 = st.columns(2)
    lambda_val = c1.slider("Lambda value for Growth Multiplier (lambda)", 0.0, 1.0, float(st.session_state.get("lambda_val", 0.3)), step=0.01,
                           help=r"Adjust $\\lambda$ to dampen volatility in job posting growth.")
    gamma_val = c2.slider("Gamma value for Regional Multiplier (gamma)", 0.0, 1.0, float(st.session_state.get("gamma_val", 0.2)), step=0.01,
                          help=r"Adjust $\\gamma$ for regional market influence.")
    st.session_state["lambda_val"] = lambda_val
    st.session_state["gamma_val"] = gamma_val

    # Synergy Inputs
    st.subheader("Synergy Inputs")
    st.markdown("""\
- Edit your individual skills below (you can add rows). Required skills for the selected occupation are shown for reference.
- Max Possible Skills Match scales the alignment calculation.
""")
    required_skills_df = st.session_state["occupation_required_skills_df"][
        st.session_state["occupation_required_skills_df"]["occupation_name"] == selected_occupation
    ][['skill_name', 'required_skill_score', 'skill_importance']]

    st.write("Required Skills (selected occupation)")
    st.dataframe(required_skills_df, use_container_width=True)

    st.write("Your Skills (editable)")
    edited_skills_df = st.data_editor(
        st.session_state["individual_skills_df"],
        num_rows="dynamic",
        use_container_width=True,
        key="skills_editor"
    )
    st.session_state["individual_skills_df"] = edited_skills_df

    max_possible_match = st.number_input("Max Possible Skills Match", min_value=1, max_value=1000, value=int(st.session_state.get("max_possible_match", 100)), step=1)
    st.session_state["max_possible_match"] = max_possible_match

    # Calculate button
    if st.button("Calculate AI-Readiness", type="primary"):
        try:
            # AI-Fluency sub-scores
            s1 = calculate_technical_ai_skills(prompting, tools, understanding, datalit)
            s2 = calculate_ai_augmented_productivity(oq_ai, oq_noai, t_noai, t_ai)
            s3 = calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust, total_decisions)
            s4 = calculate_ai_learning_velocity(delta_prof, delta_hours)

            ai_fluency = calculate_ai_fluency(s1, s2, s3, s4)

            # Domain-Expertise
            e_edu = calculate_education_foundation(education_level)
            e_exp = calculate_practical_experience(years_experience, gamma=0.15)
            e_spec = calculate_specialization_depth(portfolio_score, recognition_score, credentials_score)
            domain_expertise = calculate_domain_expertise(e_edu, e_exp, e_spec)

            # Adaptive-Capacity (convert 0-100 inputs to 0-1 scale)
            adaptive_capacity = calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management) / 100.0

            # V^R (0..1) then to 0..100
            vr_raw_0_1 = calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity)
            vr_score = to_0_100_from_0_1(clamp_0_1(vr_raw_0_1))

            # H^R components
            occ_row = occ_df[occ_df['occupation_name'] == selected_occupation].iloc[0]
            ai_enhancement = calculate_ai_enhancement_potential(occ_row['ai_enhancement_score'])  # 0..1
            job_growth_score_0_100 = calculate_job_growth_projection(occ_row['job_growth_rate_g'])
            job_growth_norm_0_1 = job_growth_score_0_100 / 100.0
            wage_premium = calculate_wage_premium(occ_row['ai_skilled_wage'], occ_row['median_wage'])
            entry_access = calculate_entry_accessibility(occ_row['education_years_required'], occ_row['experience_years_required'])
            h_base = calculate_base_opportunity_score(ai_enhancement, job_growth_norm_0_1, wage_premium, entry_access)
            m_growth = calculate_growth_multiplier(occ_row['current_job_postings'], occ_row['previous_job_postings'], lambda_val=lambda_val)
            m_regional = calculate_regional_multiplier(occ_row['local_demand'], occ_row['national_avg_demand'], occ_row['remote_work_factor'], gamma=gamma_val)
            hr_raw = calculate_systematic_opportunity(h_base, m_growth, m_regional)
            hr_score = max(0.0, min(100.0, hr_raw * 100.0))

            # Synergy
            skills_match_score = calculate_skills_match_score(edited_skills_df[['skill_name', 'individual_skill_score']], required_skills_df[['skill_name', 'required_skill_score', 'skill_importance']])
            if skills_match_score is None:
                skills_match_score = 0.0
            timing_factor = calculate_timing_factor(years_experience)
            alignment_factor = calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor)
            # Optional clamp for alignment to avoid exploding synergy
            alignment_factor = max(0.0, min(alignment_factor, 2.0))
            synergy_percentage = calculate_synergy_percentage(vr_score, hr_score, alignment_factor)
            synergy_percentage = max(0.0, min(100.0, synergy_percentage))

            # Final AI-R
            ai_r_score = calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta)
            ai_r_score = max(0.0, min(100.0, ai_r_score))

            # Persist for use on other pages
            st.session_state["last_results"] = {
                "vr_score": vr_score,
                "hr_score": hr_score,
                "synergy_percentage": synergy_percentage,
                "ai_r_score": ai_r_score,
                "ai_fluency": ai_fluency,
                "domain_expertise": domain_expertise,
                "adaptive_capacity": adaptive_capacity,
                "alignment_factor": alignment_factor,
            }

            # Visualization: Gauges
            g1, g2, g3, g4 = st.columns(4)
            g1.plotly_chart(gauge("V^R (Idiosyncratic)", vr_score), use_container_width=True)
            g2.plotly_chart(gauge("H^R (Systematic)", hr_score), use_container_width=True)
            g3.plotly_chart(gauge("Synergy %", synergy_percentage), use_container_width=True)
            g4.plotly_chart(gauge("AI-R Score", ai_r_score), use_container_width=True)

            st.divider()
            st.subheader("Component Breakdowns")

            # V^R contribution breakdown (in 0..100 scale)
            w1, w2, w3 = 0.45, 0.35, 0.20
            vr_comp_vals = [w1 * ai_fluency * 100.0, w2 * domain_expertise * 100.0, w3 * adaptive_capacity * 100.0]
            vr_comp_labels = ["AI-Fluency", "Domain-Expertise", "Adaptive-Capacity"]
            fig_vr = go.Figure(data=[go.Pie(labels=vr_comp_labels, values=vr_comp_vals, hole=0.35)])
            fig_vr.update_layout(title_text="V^R Component Contribution (0-100)", height=420)
            st.plotly_chart(fig_vr, use_container_width=True)

            # H_base breakdown (pre-multipliers)
            hb_w = {"w1": 0.30, "w2": 0.30, "w3": 0.25, "w4": 0.15}
            hb_components = {
                "AI-Enhancement": hb_w["w1"] * ai_enhancement,
                "Job Growth (norm)": hb_w["w2"] * job_growth_norm_0_1,
                "Wage Premium": hb_w["w3"] * wage_premium,
                "Entry Accessibility": hb_w["w4"] * entry_access,
            }
            fig_hb = go.Figure(data=[go.Bar(x=list(hb_components.keys()), y=[v * 100.0 for v in hb_components.values()], marker_color="#2C7BE5")])
            fig_hb.update_layout(title="H_base Components (scaled to 0-100)", yaxis_title="Score (0-100)", height=420)
            st.plotly_chart(fig_hb, use_container_width=True)

        except ZeroDivisionError as zde:
            st.error(f"Calculation error: {zde}")
        except Exception as e:
            st.error(f"Unexpected error during calculation: {e}")
