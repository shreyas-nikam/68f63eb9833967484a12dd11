import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import application_pages.utils as utils

# Page 1: Overview & Calculator

def _get_occupation_row(occupation_name):
    df = st.session_state.occupational_data_df
    row = df[df['occupation_name'] == occupation_name].iloc[0]
    return row


def run_page1():
    st.header('Overview & Calculator')

    st.markdown('''
This page lets you configure inputs for Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($H^R$), and Synergy, then compute your overall AI-Readiness score.

Key formulas in use:
- $V^R = 0.45\,\text{AI-Fluency} + 0.35\,\text{Domain-Expertise} + 0.20\,\text{Adaptive-Capacity}$
- $H^R = H_{\text{base}} \cdot M_{\text{growth}} \cdot M_{\text{regional}}$
- $AI\text{-}R = \alpha V^R + (1-\alpha) H^R + \beta\, \text{Synergy}\%$
''')

    with st.sidebar:
        st.markdown('---')
        st.markdown('Global Parameters')
        alpha = st.slider('Weight on Individual Factors (alpha)', 0.0, 1.0, st.session_state.alpha, help='Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$).')
        beta = st.slider('Synergy Coefficient (beta)', 0.0, 1.0, st.session_state.beta, help='Coefficient for the Synergy component, amplifying the score when readiness aligns with opportunity.')
        st.session_state.alpha = alpha
        st.session_state.beta = beta

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Idiosyncratic Readiness (V^R) Inputs')
        st.caption('AI-Fluency sub-components ($S_{i,1}, S_{i,2}, S_{i,3}, S_{i,4}$) and related inputs.')
        prompting = st.slider('Prompting Score', 0.0, 1.0, float(st.session_state.individual_profiles_df.loc[0, 'prompting_score']))
        tools = st.slider('Tools Score', 0.0, 1.0, float(st.session_state.individual_profiles_df.loc[0, 'tools_score']))
        understanding = st.slider('Understanding Score', 0.0, 1.0, float(st.session_state.individual_profiles_df.loc[0, 'understanding_score']))
        datalit = st.slider('Datalit Score', 0.0, 1.0, float(st.session_state.individual_profiles_df.loc[0, 'datalit_score']))

        oq_ai = st.slider('Output Quality with AI', 0.0, 100.0, float(st.session_state.individual_profiles_df.loc[0, 'output_quality_with_ai']))
        oq_noai = st.slider('Output Quality without AI', 0.0, 100.0, float(st.session_state.individual_profiles_df.loc[0, 'output_quality_without_ai']))
        t_noai = st.slider('Time without AI (hours)', 0.0, 24.0, float(st.session_state.individual_profiles_df.loc[0, 'time_without_ai']))
        t_ai = st.slider('Time with AI (hours)', 0.0, 24.0, float(st.session_state.individual_profiles_df.loc[0, 'time_with_ai']))

        errors_caught = st.number_input('Errors Caught', min_value=0, value=int(st.session_state.individual_profiles_df.loc[0, 'errors_caught']))
        total_ai_errors = st.number_input('Total AI Errors', min_value=0, value=int(st.session_state.individual_profiles_df.loc[0, 'total_ai_errors']))
        trust_decisions = st.number_input('Appropriate Trust Decisions', min_value=0, value=int(st.session_state.individual_profiles_df.loc[0, 'appropriate_trust_decisions']))
        total_decisions = st.number_input('Total Decisions', min_value=0, value=int(st.session_state.individual_profiles_df.loc[0, 'total_decisions']))

        delta_prof = st.slider('Delta Proficiency', 0.0, 1.0, float(st.session_state.individual_profiles_df.loc[0, 'delta_proficiency']))
        delta_hours = st.number_input('Delta T Hours Invested', min_value=0, value=int(st.session_state.individual_profiles_df.loc[0, 'delta_t_hours_invested']))

        st.subheader('Domain-Expertise')
        education_level = st.selectbox('Education Level', options=[
            'PhD', "Master's", "Bachelor's", "Associate's/Certificate", 'HS + significant coursework', 'Some College', 'Other'
        ], index=[
            'PhD', "Master's", "Bachelor's", "Associate's/Certificate", 'HS + significant coursework', 'Some College', 'Other'
        ].index(st.session_state.individual_profiles_df.loc[0, 'education_level']))
        years_exp = st.slider('Years Experience', 0, 50, int(st.session_state.individual_profiles_df.loc[0, 'years_experience']))
        portfolio = st.slider('Portfolio Score', 0.0, 1.0, float(st.session_state.individual_profiles_df.loc[0, 'portfolio_score']))
        recognition = st.slider('Recognition Score', 0.0, 1.0, float(st.session_state.individual_profiles_df.loc[0, 'recognition_score']))
        credentials = st.slider('Credentials Score', 0.0, 1.0, float(st.session_state.individual_profiles_df.loc[0, 'credentials_score']))

        st.subheader('Adaptive-Capacity (0-100)')
        cogflex = st.slider('Cognitive Flexibility', 0, 100, int(st.session_state.individual_profiles_df.loc[0, 'cognitive_flexibility']))
        sei = st.slider('Social-Emotional Intelligence', 0, 100, int(st.session_state.individual_profiles_df.loc[0, 'social_emotional_intelligence']))
        scm = st.slider('Strategic Career Management', 0, 100, int(st.session_state.individual_profiles_df.loc[0, 'strategic_career_management']))

    with col2:
        st.subheader('Systematic Opportunity (H^R) Inputs')
        occ_name = st.selectbox('Target Occupation', options=st.session_state.occupational_data_df['occupation_name'].tolist(), index=st.session_state.occupational_data_df['occupation_name'].tolist().index(st.session_state.selected_occupation), help='Select a target occupation to calculate market opportunity ($H^R$).')
        st.session_state.selected_occupation = occ_name
        lambda_val = st.slider('Lambda value for Growth Multiplier (lambda)', 0.0, 1.0, float(st.session_state.lambda_val), help='Adjust $\\lambda$ to dampen volatility in job posting growth.')
        gamma_val = st.slider('Gamma value for Regional Multiplier (gamma)', 0.0, 1.0, float(st.session_state.gamma_val), help='Adjust $\\gamma$ for regional market influence.')
        st.session_state.lambda_val = lambda_val
        st.session_state.gamma_val = gamma_val

        st.subheader('Synergy Inputs')
        with st.expander('Manage Individual Skills Data'):
            st.write('Add or update your skill scores to compute the skills match vs. occupation requirements.')
            with st.form('add_skill_form', clear_on_submit=True):
                skill_name = st.text_input('Skill name')
                skill_score = st.number_input('Individual skill score (0-100)', min_value=0, max_value=100, value=70)
                submitted = st.form_submit_button('Add/Update Skill')
                if submitted:
                    if skill_name:
                        df = st.session_state.user_skills_df.copy()
                        if (df['skill_name'] == skill_name).any():
                            df.loc[df['skill_name'] == skill_name, 'individual_skill_score'] = skill_score
                        else:
                            df = pd.concat([df, pd.DataFrame({'user_id': [1], 'skill_name': [skill_name], 'individual_skill_score': [skill_score]})], ignore_index=True)
                        st.session_state.user_skills_df = df
                        st.success(f'Updated skill: {skill_name} -> {skill_score}')
                    else:
                        st.warning('Please enter a skill name.')
            st.dataframe(st.session_state.user_skills_df, use_container_width=True)

        req_df = st.session_state.occupation_required_skills_df[st.session_state.occupation_required_skills_df['occupation_name'] == occ_name]
        st.markdown('Required Skills for selected occupation:')
        st.dataframe(req_df, use_container_width=True)
        max_possible_match = st.number_input('Max Possible Skills Match', min_value=1.0, value=float(st.session_state.max_possible_match))
        st.session_state.max_possible_match = max_possible_match

    st.divider()
    calc_btn = st.button('Calculate Scores', type='primary')
    if calc_btn:
        try:
            inputs = {
                'prompting': prompting,
                'tools': tools,
                'understanding': understanding,
                'datalit': datalit,
                'oq_ai': oq_ai,
                'oq_noai': oq_noai,
                't_noai': t_noai,
                't_ai': t_ai,
                'errors_caught': errors_caught,
                'total_ai_errors': total_ai_errors,
                'trust_decisions': trust_decisions,
                'total_decisions': total_decisions,
                'delta_prof': delta_prof,
                'delta_hours': delta_hours,
                'education': education_level,
                'years_exp': years_exp,
                'portfolio': portfolio,
                'recognition': recognition,
                'credentials': credentials,
                'cogflex': cogflex,
                'sei': sei,
                'scm': scm,
                'required_skills_df': req_df,
            }
            occ_row = _get_occupation_row(occ_name)
            results = utils.compute_scores_from_inputs(
                inputs=inputs,
                occupation_row=occ_row,
                lambda_val=lambda_val,
                gamma_val=gamma_val,
                user_skills_df=st.session_state.user_skills_df,
                max_possible_match=max_possible_match,
                alpha=alpha,
                beta=beta,
            )
            st.session_state.results = results
        except ZeroDivisionError as e:
            st.error(str(e))

    # Display results if available
    if st.session_state.results:
        r = st.session_state.results
        m1, m2, m3, m4 = st.columns(4)
        m1.metric('V^R (0-100)', f"{r['vr_score']:.2f}")
        m2.metric('H^R (0-100)', f"{r['hr_score']:.2f}")
        m3.metric('Synergy %', f"{r['synergy_pct']:.2f}")
        m4.metric('AI-Readiness (AI-R)', f"{r['ai_r']:.2f}")

        st.markdown('---')
        c1, c2 = st.columns(2)
        with c1:
            # Contribution pie for V^R components (use normalized contributions)
            vf = max(r['ai_fluency'], 0)
            de = max(r['domain_expertise'], 0)
            ac = max(r['adaptive_capacity'], 0)
            comp_df = pd.DataFrame({
                'Component': ['AI-Fluency', 'Domain-Expertise', 'Adaptive-Capacity'],
                'Value': [vf, de, ac]
            })
            fig = px.pie(comp_df, names='Component', values='Value', title='V^R Component Contributions (raw scale)')
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            # H_base breakdown bar chart
            hb = r['h_base_components']
            hb_df = pd.DataFrame({
                'Component': list(hb.keys()),
                'Value (0-1)': list(hb.values())
            })
            fig2 = px.bar(hb_df, x='Component', y='Value (0-1)', title='H_base Component Breakdown (scaled to 0-1)')
            st.plotly_chart(fig2, use_container_width=True)

        st.markdown('---')
        # Comparison current values
        cmp_df = pd.DataFrame({
            'Metric': ['V^R', 'H^R', 'AI-R'],
            'Score': [r['vr_score'], r['hr_score'], r['ai_r']]
        })
        fig3 = px.bar(cmp_df, x='Metric', y='Score', title='Current Scores', text='Score')
        fig3.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig3, use_container_width=True)

        with st.expander('Computation details and formulas'):
            st.latex(r"AI\text{-}R_{i,t} = \alpha V^R + (1-\alpha) H^R + \beta\, \text{Synergy}\%")
            st.latex(r"V^R = 0.45\,\text{AI-Fluency} + 0.35\,\text{Domain-Expertise} + 0.20\,\text{Adaptive-Capacity}")
            st.latex(r"H^R = H_{\text{base}} \cdot M_{\text{growth}} \cdot M_{\text{regional}}")
            st.write('H_base components (0-1 scale):', r['h_base_components'])
