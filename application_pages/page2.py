import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def run_page2():
    st.subheader("AI-Readiness Scores & Insights")
    st.markdown(
        "This page presents the computed components of your AI-Readiness Score: $V^R$, $H^R$, Synergy%, and the overall $AI\\text{-}R$."
    )

    cs = st.session_state.get("current_scores", None)
    if cs is None:
        st.info("No scores computed yet. Go to 'Overview & Inputs' and click 'Calculate AI-Readiness'.")
        return

    # Top metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("V^R (0-100)", f"{cs['vr_score']:.1f}")
    c2.metric("H^R (0-100)", f"{cs['hr_score']:.1f}")
    c3.metric("Synergy %", f"{cs['synergy_pct']:.1f}")
    c4.metric("AI-R (0-100+)", f"{cs['ai_r']:.1f}")

    st.divider()

    # VR composition chart
    st.markdown("Breakdown of $V^R$ by components (weighted)")
    vr_comp_weights = {
        'AI-Fluency': 0.45 * float(cs['vr_breakdown']['AI-Fluency (01)']),
        'Domain-Expertise': 0.35 * float(cs['vr_breakdown']['Domain-Expertise (01)']),
        'Adaptive-Capacity': 0.20 * float(cs['vr_breakdown']['Adaptive-Capacity (01)']),
    }
    vr_df = pd.DataFrame({
        'Component': list(vr_comp_weights.keys()),
        'Weighted Share (0-1)': list(vr_comp_weights.values()),
    })
    fig_vr = px.bar(vr_df, x='Component', y='Weighted Share (0-1)', title='V^R Composition (Weighted, Normalized)')
    fig_vr.update_layout(yaxis_tickformat='.0%', yaxis_range=[0, 1])
    st.plotly_chart(fig_vr, use_container_width=True)

    # H_base components chart
    st.markdown("Breakdown of $H_{\\text{base}}$ components (pre-multipliers)")
    hb = cs['h_breakdown']
    hb_df = pd.DataFrame({
        'Component': ['AI-Enhancement', 'Job Growth (0-1)', 'Wage Premium', 'Entry Accessibility'],
        'Value': [
            float(hb['AI-Enhancement']),
            float(hb['Job Growth (01)']),
            float(hb['Wage Premium']),
            float(hb['Entry Accessibility'])
        ]
    })
    fig_h = px.bar(hb_df, x='Component', y='Value', title='H_base Components')
    st.plotly_chart(fig_h, use_container_width=True)

    # Current AI-R composition vs raw components
    st.markdown("Current $AI\\text{-}R$ vs. its components")
    comp_df = pd.DataFrame({
        'Metric': ['V^R', 'H^R', 'Synergy%'],
        'Score': [cs['vr_score'], cs['hr_score'], cs['synergy_pct']],
    })
    fig_comp = px.bar(comp_df, x='Metric', y='Score', title='Components of Current Readiness')
    st.plotly_chart(fig_comp, use_container_width=True)

    with st.expander("Detailed Numbers and Definitions"):
        st.markdown("Key definitions and the final score formula:")
        st.latex(r" AI\\text{-}R_{i,t} = \\alpha \\, V^R_i(t) + (1-\\alpha) \\, H^R_i(t) + \\beta \\, \\text{Synergy}\\% ")
        st.json({'V^R breakdown': cs['vr_breakdown']})
        st.json({'H^R breakdown and multipliers': cs['h_breakdown']})
        st.json({'Synergy inputs': {
            'skills_match': cs['skills_match'],
            'timing_factor': cs['timing_factor'],
            'alignment': cs['alignment'],
        }})

    with st.expander("Underlying DataFrames"):
        st.write("individual_profiles_df")
        st.dataframe(st.session_state.individual_profiles_df, use_container_width=True)
        st.write("occupational_data_df")
        st.dataframe(st.session_state.occupational_data_df, use_container_width=True)
        st.write("occupation_required_skills_df")
        st.dataframe(st.session_state.occupation_required_skills_df, use_container_width=True)
        st.write("individual_skills_df")
        st.dataframe(st.session_state.individual_skills_df, use_container_width=True)
