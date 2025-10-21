import streamlit as st
import pandas as pd
import plotly.express as px
from .utils import (
    normalize_to_100,
    simulate_pathway_impact,
    calculate_idiosyncratic_readiness,
    calculate_ai_readiness_score,
    calculate_synergy_percentage,
)

def run_page3():
    st.header("Pathway Simulator & What-If Analysis")

    if not st.session_state.get("calculated", False):
        st.warning("Please calculate your current AI-Readiness on the previous page first.")
        return

    lp_df = st.session_state["learning_pathways_df"].copy()

    # Current baselines
    vr_score = float(st.session_state.get("vr_score", 0.0))
    hr_score = float(st.session_state.get("hr_score", 0.0))
    synergy_pct = float(st.session_state.get("synergy_pct", 0.0))
    ai_r = float(st.session_state.get("ai_r", 0.0))

    ai_fluency = float(st.session_state.get("ai_fluency_val", 0.0))
    domain_expertise = float(st.session_state.get("domain_expertise_val", 0.0))
    adaptive_capacity = float(st.session_state.get("adaptive_capacity_val", 0.0))

    alpha = float(st.session_state.get("alpha", 0.6))
    beta = float(st.session_state.get("beta", 0.15))

    st.subheader("Current Scores")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("V^R", f"{vr_score:.1f}")
    c2.metric("H^R", f"{hr_score:.1f}")
    c3.metric("Synergy%", f"{synergy_pct:.1f}")
    c4.metric("AI-R", f"{ai_r:.1f}")

    st.markdown("---")
    st.subheader("Select Learning Pathway")
    pathway_name = st.selectbox("Select Learning Pathway", options=list(lp_df["pathway_name"].values), index=0)
    path_row = lp_df[lp_df["pathway_name"] == pathway_name].iloc[0]

    completion_score = st.slider("Pathway Completion Score", 0.0, 1.0, 1.0, 0.05)
    mastery_score = st.slider("Pathway Mastery Score", 0.0, 1.0, 1.0, 0.05, help="Simulate the impact of completing a learning pathway with a certain completion and mastery level.")

    if st.button("Simulate Pathway Impact"):
        new_ai_fluency, new_domain_expertise, new_adaptive_capacity = simulate_pathway_impact(
            ai_fluency, domain_expertise, adaptive_capacity,
            float(path_row["impact_ai_fluency"]), float(path_row["impact_domain_expertise"]), float(path_row["impact_adaptive_capacity"]),
            completion_score=completion_score, mastery_score=mastery_score
        )

        # Recompute V^R
        new_vr_raw = calculate_idiosyncratic_readiness(new_ai_fluency, new_domain_expertise, new_adaptive_capacity)
        new_vr_score = normalize_to_100(new_vr_raw)

        # Assume H^R unchanged by learning pathway in short-run
        new_hr_score = hr_score

        # Recompute Synergy (alignment presumed unchanged; synergy scales with V^R change)
        # For stability, scale synergy by ratio of new V^R to old V^R
        if vr_score <= 0:
            new_synergy_pct = synergy_pct
        else:
            ratio = new_vr_score / vr_score
            new_synergy_pct = min(100.0, synergy_pct * ratio)

        new_ai_r = calculate_ai_readiness_score(new_vr_score, new_hr_score, new_synergy_pct, alpha, beta)
        new_ai_r = min(100.0, max(0.0, new_ai_r))

        st.session_state.update({
            "new_ai_fluency": new_ai_fluency,
            "new_domain_expertise": new_domain_expertise,
            "new_adaptive_capacity": new_adaptive_capacity,
            "new_vr_score": new_vr_score,
            "new_hr_score": new_hr_score,
            "new_synergy_pct": new_synergy_pct,
            "new_ai_r": new_ai_r,
            "simulation_done": True,
        })

    if st.session_state.get("simulation_done", False):
        st.subheader("Projected Scores")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("V^R (new)", f"{st.session_state['new_vr_score']:.1f}", delta=f"{st.session_state['new_vr_score'] - vr_score:.1f}")
        c2.metric("H^R (new)", f"{st.session_state['new_hr_score']:.1f}", delta=f"{st.session_state['new_hr_score'] - hr_score:.1f}")
        c3.metric("Synergy% (new)", f"{st.session_state['new_synergy_pct']:.1f}", delta=f"{st.session_state['new_synergy_pct'] - synergy_pct:.1f}")
        c4.metric("AI-R (new)", f"{st.session_state['new_ai_r']:.1f}", delta=f"{st.session_state['new_ai_r'] - ai_r:.1f}")

        # Comparison chart
        comp_df = pd.DataFrame({
            "Metric": ["V^R", "H^R", "AI-R"],
            "Current": [vr_score, hr_score, ai_r],
            "Projected": [st.session_state['new_vr_score'], st.session_state['new_hr_score'], st.session_state['new_ai_r']]
        })
        comp_df = comp_df.melt(id_vars=["Metric"], var_name="State", value_name="Score")
        fig = px.bar(comp_df, x="Metric", y="Score", color="State", barmode="group", title="Current vs. Projected Scores")
        st.plotly_chart(fig, use_container_width=True)

        st.info("Interpretation: Increases in AI-Fluency, Domain-Expertise, or Adaptive-Capacity lift $V^R$ and may raise overall $AI\text{-}R$ even if market opportunity ($H^R$) remains unchanged in the short run.")
    else:
        st.info("Configure pathway inputs and click 'Simulate Pathway Impact' to see projected changes.")
