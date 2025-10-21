import streamlit as st
import pandas as pd
import plotly.express as px
from application_pages.core import compute_all_scores


def _ensure_defaults():
    if not hasattr(st.session_state, 'individual_profiles_df'):
        st.session_state.individual_profiles_df = pd.DataFrame()
    df = st.session_state.individual_profiles_df
    row = df.iloc[0].to_dict() if not df.empty else {}

    def set_if_missing(key, value):
        if key not in st.session_state:
            st.session_state[key] = value

    set_if_missing('prompting_score', float(row.get('prompting_score', 0.75)))
    set_if_missing('tools_score', float(row.get('tools_score', 0.6)))
    set_if_missing('understanding_score', float(row.get('understanding_score', 0.8)))
    set_if_missing('datalit_score', float(row.get('datalit_score', 0.9)))

    set_if_missing('output_quality_with_ai', float(row.get('output_quality_with_ai', 90)))
    set_if_missing('output_quality_without_ai', float(row.get('output_quality_without_ai', 60)))
    set_if_missing('time_without_ai', float(row.get('time_without_ai', 4)))
    set_if_missing('time_with_ai', float(row.get('time_with_ai', 1)))

    set_if_missing('errors_caught', int(row.get('errors_caught', 15)))
    set_if_missing('total_ai_errors', int(row.get('total_ai_errors', 20)))
    set_if_missing('appropriate_trust_decisions', int(row.get('appropriate_trust_decisions', 25)))
    set_if_missing('total_decisions', int(row.get('total_decisions', 30)))

    set_if_missing('delta_proficiency', float(row.get('delta_proficiency', 0.3)))
    set_if_missing('delta_t_hours_invested', float(row.get('delta_t_hours_invested', 10)))

    set_if_missing('education_level', row.get('education_level', "Master's"))
    set_if_missing('years_experience', float(row.get('years_experience', 5)))
    set_if_missing('portfolio_score', float(row.get('portfolio_score', 0.85)))
    set_if_missing('recognition_score', float(row.get('recognition_score', 0.7)))
    set_if_missing('credentials_score', float(row.get('credentials_score', 0.9)))

    set_if_missing('cognitive_flexibility', float(row.get('cognitive_flexibility', 85)))
    set_if_missing('social_emotional_intelligence', float(row.get('social_emotional_intelligence', 90)))
    set_if_missing('strategic_career_management', float(row.get('strategic_career_management', 75)))

    # Systematic opportunity params
    set_if_missing('selected_occupation_name', st.session_state.get('selected_occupation_name', 'Data Analyst with AI Skills'))
    set_if_missing('lambda_val', float(st.session_state.get('lambda_val', 0.3)))
    set_if_missing('gamma_val', float(st.session_state.get('gamma_val', 0.2)))

    # Synergy params
    set_if_missing('max_possible_match', float(st.session_state.get('max_possible_match', 100.0)))

    # Skills df
    if 'individual_skills_df' not in st.session_state:
        st.session_state.individual_skills_df = pd.DataFrame({'user_id': [], 'skill_name': [], 'individual_skill_score': []})



def _get_selected_occupation_row(occupation_name):
    df = st.session_state.occupational_data_df
    row = df[df['occupation_name'] == occupation_name]
    if row.empty:
        return df.iloc[0]
    return row.iloc[0]


def run_page1():
    _ensure_defaults()

    st.header('Overview and Inputs')
    st.markdown(
        'This page lets you configure the inputs to compute your AI-Readiness Score. The score blends individual capability $V^R$, market opportunity $H^R$, and alignment-driven Synergy. Use the controls to reflect your current profile and target occupation.'
    )
    st.latex(r" AI\text{-}R_{i,t} = \alpha\, V^R_i(t) + (1-\alpha)\, H^R_i(t) + \beta\, \text{Synergy}\% ")

    tabs = st.tabs(['Idiosyncratic Readiness (V^R)', 'Systematic Opportunity (H^R)', 'Synergy Inputs', 'Data'])

    # --------------------------- V^R Tab ---------------------------
    with tabs[0]:
        st.subheader('Idiosyncratic Readiness Inputs $V^R$')
        st.markdown('Adjust AI-Fluency, Domain-Expertise, and Adaptive-Capacity. All components are normalized internally.')
        st.markdown('- AI-Fluency sub-scores: $S_{i,1}$ (Technical), $S_{i,2}$ (Productivity), $S_{i,3}$ (Judgment), $S_{i,4}$ (Learning Velocity).')

        c1, c2 = st.columns(2)
        with c1:
            st.markdown('AI-Fluency Sub-Components')
            st.slider('Prompting Score', 0.0, 1.0, float(st.session_state.prompting_score), 0.01,
                      help='Part of $S_{i,1}$', key='prompting_score')
            st.slider('Tools Score', 0.0, 1.0, float(st.session_state.tools_score), 0.01,
                      help='Part of $S_{i,1}$', key='tools_score')
            st.slider('Understanding Score', 0.0, 1.0, float(st.session_state.understanding_score), 0.01,
                      help='Part of $S_{i,1}$', key='understanding_score')
            st.slider('Datalit Score', 0.0, 1.0, float(st.session_state.datalit_score), 0.01,
                      help='Part of $S_{i,1}$', key='datalit_score')

            st.number_input('Output Quality with AI', min_value=0.0, value=float(st.session_state.output_quality_with_ai), step=1.0,
                            help='Used in $S_{i,2}$', key='output_quality_with_ai')
            st.number_input('Output Quality without AI', min_value=0.01, value=float(st.session_state.output_quality_without_ai), step=1.0,
                            help='Used in $S_{i,2}$; must be > 0', key='output_quality_without_ai')
            st.number_input('Time without AI (hours)', min_value=0.01, value=float(st.session_state.time_without_ai), step=0.1,
                            help='Used in $S_{i,2}$', key='time_without_ai')
            st.number_input('Time with AI (hours)', min_value=0.01, value=float(st.session_state.time_with_ai), step=0.1,
                            help='Used in $S_{i,2}$; must be > 0', key='time_with_ai')
        with c2:
            st.number_input('Errors Caught', min_value=0, value=int(st.session_state.errors_caught), step=1,
                            help='Used in $S_{i,3}$', key='errors_caught')
            st.number_input('Total AI Errors', min_value=0, value=int(st.session_state.total_ai_errors), step=1,
                            help='Used in $S_{i,3}$', key='total_ai_errors')
            st.number_input('Appropriate Trust Decisions', min_value=0, value=int(st.session_state.appropriate_trust_decisions), step=1,
                            help='Used in $S_{i,3}$', key='appropriate_trust_decisions')
            st.number_input('Total Decisions', min_value=0, value=int(st.session_state.total_decisions), step=1,
                            help='Used in $S_{i,3}$', key='total_decisions')

            st.number_input('Delta Proficiency', min_value=0.0, value=float(st.session_state.delta_proficiency), step=0.01,
                            help='Used in $S_{i,4}$', key='delta_proficiency')
            st.number_input('Delta T Hours Invested', min_value=0.0, value=float(st.session_state.delta_t_hours_invested), step=0.5,
                            help='Used in $S_{i,4}$', key='delta_t_hours_invested')

        c3, c4 = st.columns(2)
        with c3:
            st.markdown('Domain-Expertise Sub-Components')
            st.selectbox('Education Level', options=["PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other"],
                         index=["PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other"].index(st.session_state.education_level) if st.session_state.education_level in ["PhD", "Master's", "Bachelor's", "Associate's/Certificate", "HS + significant coursework", "Some College", "Other"] else 1,
                         help=r'Education foundation $E_{education}$', key='education_level')
            st.slider('Years Experience', 0.0, 40.0, float(st.session_state.years_experience), 0.5,
                      help=r'Practical experience $E_{experience}$', key='years_experience')
            st.slider('Portfolio Score', 0.0, 1.0, float(st.session_state.portfolio_score), 0.01,
                      help=r'Part of specialization $E_{specialization}$', key='portfolio_score')
            st.slider('Recognition Score', 0.0, 1.0, float(st.session_state.recognition_score), 0.01,
                      help=r'Part of specialization $E_{specialization}$', key='recognition_score')
            st.slider('Credentials Score', 0.0, 1.0, float(st.session_state.credentials_score), 0.01,
                      help=r'Part of specialization $E_{specialization}$', key='credentials_score')
        with c4:
            st.markdown('Adaptive-Capacity Sub-Components')
            st.slider('Cognitive Flexibility', 0.0, 100.0, float(st.session_state.cognitive_flexibility), 1.0,
                      help='Adaptive capacity component', key='cognitive_flexibility')
            st.slider('Social-Emotional Intelligence', 0.0, 100.0, float(st.session_state.social_emotional_intelligence), 1.0,
                      help='Adaptive capacity component', key='social_emotional_intelligence')
            st.slider('Strategic Career Management', 0.0, 100.0, float(st.session_state.strategic_career_management), 1.0,
                      help='Adaptive capacity component', key='strategic_career_management')

    # --------------------------- H^R Tab ---------------------------
    with tabs[1]:
        st.subheader('Systematic Opportunity Inputs $H^R$')
        occ_options = list(st.session_state.occupational_data_df['occupation_name'])
        if st.session_state.selected_occupation_name not in occ_options:
            default_index = 0
        else:
            default_index = occ_options.index(st.session_state.selected_occupation_name)
        selected_occ = st.selectbox('Target Occupation', options=occ_options, index=default_index,
                                    help='Select occupation to compute market opportunity $H^R$', key='selected_occupation_name')
        st.slider('Lambda value for Growth Multiplier (lambda)', 0.0, 1.0, float(st.session_state.lambda_val), 0.01,
                  help='Adjust $\\lambda$ to dampen volatility in job posting growth.', key='lambda_val')
        st.slider('Gamma value for Regional Multiplier (gamma)', 0.0, 1.0, float(st.session_state.gamma_val), 0.01,
                  help='Adjust $\\gamma$ for regional market influence.', key='gamma_val')

        occ_row = _get_selected_occupation_row(selected_occ)
        st.markdown('Selected occupation attributes:')
        st.dataframe(pd.DataFrame(occ_row).T, use_container_width=True)

    # --------------------------- Synergy Tab ---------------------------
    with tabs[2]:
        st.subheader('Synergy Inputs')
        st.markdown('Add/update your skills to compute Skills Match for the selected occupation.')
        skill_cols = st.columns([2, 1, 1])
        with skill_cols[0]:
            new_skill_name = st.text_input('Skill Name', value='')
        with skill_cols[1]:
            new_skill_score = st.number_input('Individual Skill Score (0-100)', min_value=0, max_value=100, value=70, step=1)
        with skill_cols[2]:
            add_btn = st.button('Add/Update Skill')
        if add_btn and new_skill_name.strip() != '':
            df = st.session_state.individual_skills_df.copy()
            mask = df['skill_name'].str.lower() == new_skill_name.strip().lower() if not df.empty else pd.Series([], dtype=bool)
            if not df.empty and mask.any():
                df.loc[mask, 'individual_skill_score'] = int(new_skill_score)
            else:
                df = pd.concat([df, pd.DataFrame({'user_id': [1], 'skill_name': [new_skill_name.strip()], 'individual_skill_score': [int(new_skill_score)]})], ignore_index=True)
            st.session_state.individual_skills_df = df
            st.success(f"Skill '{new_skill_name}' saved.")

        # Optional remove tool
        if not st.session_state.individual_skills_df.empty:
            rm_col1, rm_col2 = st.columns([3, 1])
            with rm_col1:
                to_remove = st.selectbox('Remove a Skill', options=['(none)'] + list(st.session_state.individual_skills_df['skill_name']))
            with rm_col2:
                if st.button('Remove') and to_remove != '(none)':
                    df = st.session_state.individual_skills_df.copy()
                    st.session_state.individual_skills_df = df[df['skill_name'] != to_remove].reset_index(drop=True)
                    st.warning(f"Removed skill '{to_remove}'.")

        st.dataframe(st.session_state.individual_skills_df, use_container_width=True)

        st.number_input('Max Possible Skills Match', min_value=1.0, value=float(st.session_state.max_possible_match), step=1.0,
                        help='Used to normalize skills match to a percentage', key='max_possible_match')

        # Show required skills for selected occupation
        req_df = st.session_state.occupation_required_skills_df
        req_view = req_df[req_df['occupation_name'] == st.session_state.selected_occupation_name]
        st.markdown('Required skills for selected occupation:')
        st.dataframe(req_view, use_container_width=True)

    # --------------------------- Data Tab ---------------------------
    with tabs[3]:
        st.subheader('Underlying Synthetic Data')
        with st.expander('individual_profiles_df'):
            st.dataframe(st.session_state.individual_profiles_df, use_container_width=True)
        with st.expander('occupational_data_df'):
            st.dataframe(st.session_state.occupational_data_df, use_container_width=True)
        with st.expander('occupation_required_skills_df'):
            st.dataframe(st.session_state.occupation_required_skills_df, use_container_width=True)
        with st.expander('learning_pathways_df'):
            st.dataframe(st.session_state.learning_pathways_df, use_container_width=True)

    st.divider()
    calc_col1, calc_col2 = st.columns([1, 1])
    with calc_col1:
        if st.button('Calculate AI-Readiness'):
            try:
                occ_row = _get_selected_occupation_row(st.session_state.selected_occupation_name)
                required_skills_df = st.session_state.occupation_required_skills_df[
                    st.session_state.occupation_required_skills_df['occupation_name'] == st.session_state.selected_occupation_name
                ][['skill_name', 'required_skill_score', 'skill_importance']]

                inputs = {
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
                st.session_state.current_scores = compute_all_scores(inputs)
                st.success('Computed AI-Readiness scores. Navigate to "Scores & Insights" to view details.')
            except Exception as e:
                st.error(f'Error during calculation: {e}')

    with calc_col2:
        if st.button('Reset Inputs to Defaults'):
            for k in list(st.session_state.keys()):
                if k not in ['individual_profiles_df', 'occupational_data_df', 'learning_pathways_df', 'occupation_required_skills_df', 'individual_skills_df', 'alpha_weight', 'beta_weight', 'initialized', 'current_scores', 'selected_occupation_name', 'max_possible_match', 'lambda_val', 'gamma_val']:
                    del st.session_state[k]
            _ensure_defaults()
            st.warning('Inputs reset to defaults.')
