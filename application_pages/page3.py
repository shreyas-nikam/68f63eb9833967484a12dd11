import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import application_pages.utils as utils

# Page 3: Data Explorer

def run_page3():
    st.header('Data Explorer')
    st.markdown('''
Explore the synthetic datasets that power this lab. Use filters and charts to understand assumptions behind $H^R$ and $V^R$.
''')

    with st.expander('Individual Profiles DataFrame'):
        st.dataframe(st.session_state.individual_profiles_df, use_container_width=True)
        st.download_button('Download CSV', data=st.session_state.individual_profiles_df.to_csv(index=False), file_name='individual_profiles.csv', mime='text/csv')

    with st.expander('Occupational DataFrame'):
        st.dataframe(st.session_state.occupational_data_df, use_container_width=True)
        st.download_button('Download CSV', data=st.session_state.occupational_data_df.to_csv(index=False), file_name='occupational_data.csv', mime='text/csv')

    with st.expander('Learning Pathways DataFrame'):
        st.dataframe(st.session_state.learning_pathways_df, use_container_width=True)
        st.download_button('Download CSV', data=st.session_state.learning_pathways_df.to_csv(index=False), file_name='learning_pathways.csv', mime='text/csv')

    with st.expander('Occupation Required Skills DataFrame'):
        st.dataframe(st.session_state.occupation_required_skills_df, use_container_width=True)
        st.download_button('Download CSV', data=st.session_state.occupation_required_skills_df.to_csv(index=False), file_name='occupation_required_skills.csv', mime='text/csv')

    with st.expander('Individual Skills DataFrame (editable in Page 1)'):
        st.dataframe(st.session_state.user_skills_df, use_container_width=True)
        st.download_button('Download CSV', data=st.session_state.user_skills_df.to_csv(index=False), file_name='individual_skills.csv', mime='text/csv')

    st.markdown('---')
    st.subheader('H_base Opportunity Comparison')
    st.caption('Visualize $H_{base}$ for occupations with default multipliers ($M_{growth}=M_{regional}=1$ for comparability).')

    # Compute H_base (0-1) across occupations
    records = []
    for _, row in st.session_state.occupational_data_df.iterrows():
        ai_enh = utils.calculate_ai_enhancement_potential(row['ai_enhancement_score'])
        job_growth_norm = utils.calculate_job_growth_projection(row['job_growth_rate_g']) / 100.0
        wage_prem = float(np.clip(utils.calculate_wage_premium(row['ai_skilled_wage'], row['median_wage']), 0.0, 1.0))
        entry_acc = utils.calculate_entry_accessibility(row['education_years_required'], row['experience_years_required'])
        h_base = utils.calculate_base_opportunity_score(ai_enh, job_growth_norm, wage_prem, entry_acc)
        records.append({'Occupation': row['occupation_name'], 'H_base (0-1)': h_base})
    hb_df = pd.DataFrame(records)

    fig = px.bar(hb_df, x='Occupation', y='H_base (0-1)', title='Base Opportunity by Occupation (scaled 0-1)')
    fig.update_layout(xaxis_tickangle=-30)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('---')
    st.subheader('Skill Match Explorer')
    occ = st.selectbox('Select Occupation', options=st.session_state.occupational_data_df['occupation_name'].tolist())
    req_df = st.session_state.occupation_required_skills_df[st.session_state.occupation_required_skills_df['occupation_name'] == occ]
    score = utils.calculate_skills_match_score(st.session_state.user_skills_df, req_df)
    st.metric('Skills Match %', f"{(0.0 if score is None else score):.2f}")

    if score is not None and not req_df.empty:
        merged = pd.merge(st.session_state.user_skills_df, req_df, on='skill_name', how='outer')
        merged['individual_skill_score'] = merged['individual_skill_score'].fillna(0)
        merged['required_skill_score'] = merged['required_skill_score'].fillna(0)
        merged['Delta'] = merged['individual_skill_score'] - merged['required_skill_score']
        fig2 = px.bar(merged, x='skill_name', y=['individual_skill_score', 'required_skill_score'], barmode='group', title='Individual vs Required Skill Scores')
        st.plotly_chart(fig2, use_container_width=True)
