import streamlit as st
import pandas as pd
import plotly.express as px


def run_page2():
    st.subheader("AI-Readiness Scores & Insights")

    cs = st.session_state.get('current_scores', None)
    if cs is None:
        st.info("No scores computed yet. Please go to 'Overview & Inputs' and click 'Calculate AI-Readiness'.")
        return

    # Top-level metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("V^R (0-100)", f"{cs['vr_score']:.1f}")
    c2.metric("H^R (0-100)", f"{cs['hr_score']:.1f}")
    c3.metric("Synergy %", f"{cs['synergy_pct']:.1f}")
    c4.metric("AI-R (0-100+)", f"{cs['ai_r']:.1f}")

    st.markdown("Explanation and formulae")
    st.markdown(
        "The AI-Readiness Score combines individual readiness, market opportunity, and alignment-driven synergy."
    )
    st.latex(r" AI\text{-}R_{i,t} = \alpha\, V^R_i(t) + (1-\alpha)\, H^R_i(t) + \beta\, \text{Synergy}\% ")
    st.latex(r" V^R = 0.45\cdot \text{AI-Fluency} + 0.35\cdot \text{Domain-Expertise} + 0.20\cdot \text{Adaptive-Capacity} ")
    st.latex(r" H^R = H_{\text{base}} \cdot M_{\text{growth}} \cdot M_{\text{regional}} ")

    st.divider()

    # V^R composition as a pie or bar
    vr_bd = cs['vr_breakdown']
    vr_comp = {
        'AI-Fluency': vr_bd['AI-Fluency (01)'] * 0.45,
        'Domain-Expertise': vr_bd['Domain-Expertise (01)'] * 0.35,
        'Adaptive-Capacity': vr_bd['Adaptive-Capacity (01)'] * 0.20,
    }
    vr_df = pd.DataFrame({'Component': list(vr_comp.keys()), 'Weighted Share (0-1)': list(vr_comp.values())})
    fig_vr = px.pie(vr_df, names='Component', values='Weighted Share (0-1)', title='V^R Composition (weighted)')

    # H_base breakdown
    hb = cs['h_breakdown']
    hb_df = pd.DataFrame({
        'Component': ['AI-Enhancement', 'Job Growth (01)', 'Wage Premium', 'Entry Accessibility'],
        'Value (0-1)': [hb['AI-Enhancement'], hb['Job Growth (01)'], hb['Wage Premium'], hb['Entry Accessibility']]
    })
    fig_h = px.bar(hb_df, x='Component', y='Value (0-1)', title='H_base Components (pre-multipliers)', text='Value (0-1)')

    colA, colB = st.columns(2)
    with colA:
        st.plotly_chart(fig_vr, use_container_width=True)
    with colB:
        st.plotly_chart(fig_h, use_container_width=True)

    # Multipliers visualization
    mult_df = pd.DataFrame({
        'Multiplier': ['Growth Multiplier', 'Regional Multiplier'],
        'Value': [hb['Growth Multiplier'], hb['Regional Multiplier']]
    })
    fig_m = px.bar(mult_df, x='Multiplier', y='Value', title='Opportunity Multipliers', text='Value')
    st.plotly_chart(fig_m, use_container_width=True)

    with st.expander("Detailed Numbers"):
        st.write("V^R breakdown (normalized components and sub-metrics):")
        st.json(cs['vr_breakdown'])
        st.write("H^R breakdown and multipliers:")
        st.json(cs['h_breakdown'])
        st.write("Synergy inputs:")
        st.json({'skills_match': cs['skills_match'], 'timing_factor': cs['timing_factor'], 'alignment': cs['alignment']})

    with st.expander("Underlying DataFrames"):
        st.write("individual_profiles_df")
        st.dataframe(st.session_state.individual_profiles_df, use_container_width=True)
        st.write("occupational_data_df")
        st.dataframe(st.session_state.occupational_data_df, use_container_width=True)
        st.write("occupation_required_skills_df")
        st.dataframe(st.session_state.occupation_required_skills_df, use_container_width=True)
        st.write("learning_pathways_df")
        st.dataframe(st.session_state.learning_pathways_df, use_container_width=True)
        st.write("individual_skills_df")
        st.dataframe(st.session_state.individual_skills_df, use_container_width=True)
