import pandas as pd

# --------- Core Calculation Functions ---------

def calculate_technical_ai_skills(prompting, tools, understanding, data_lit):
    return (float(prompting) + float(tools) + float(understanding) + float(data_lit)) / 4.0


def calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai):
    if output_quality_without_ai == 0 or time_with_ai == 0:
        return 0.0
    return (float(output_quality_with_ai) / float(output_quality_without_ai)) * (float(time_without_ai) / float(time_with_ai))


def calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions):
    # Defensive checks against division by zero per notebook comment
    if (total_ai_errors is None or total_ai_errors == 0) and (total_decisions is None or total_decisions == 0):
        return 0.0
    part1 = 0.0
    part2 = 0.0
    if total_ai_errors and total_ai_errors > 0:
        part1 = float(errors_caught) / float(total_ai_errors)
    if total_decisions and total_decisions > 0:
        part2 = float(appropriate_trust_decisions) / float(total_decisions)
    return 1.0 - (part1 + part2) / 2.0


def calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested):
    if delta_t_hours_invested == 0:
        if delta_proficiency == 0:
            return 0.0
        # Graceful cap if hours is zero but proficiency changed
        return 1.0
    return float(delta_proficiency) / float(delta_t_hours_invested)


def calculate_ai_fluency(s1, s2, s3, s4):
    return 0.1 * float(s1) + 0.2 * float(s2) + 0.3 * float(s3) + 0.4 * float(s4)


def calculate_education_foundation(education_level):
    if education_level == "PhD":
        return 1.0
    elif education_level == "Master's":
        return 0.8
    elif education_level == "Bachelor's":
        return 0.6
    elif education_level == "Associate's/Certificate":
        return 0.4
    elif education_level == "HS + significant coursework":
        return 0.2
    elif education_level == "Some College":
        return 0.3
    else:
        return 0.0


def calculate_practical_experience(years_experience, gamma=0.15):
    years = max(0.0, float(years_experience))
    denom = years + (1.0 / float(gamma))
    if denom == 0:
        return 0.0
    return years / denom


def calculate_specialization_depth(portfolio_score, recognition_score, credentials_score):
    return (float(portfolio_score) + float(recognition_score) + float(credentials_score)) / 3.0


def calculate_domain_expertise(education_foundation, practical_experience, specialization_depth):
    return 0.125 * float(education_foundation) + 0.25 * float(practical_experience) + 0.625 * float(specialization_depth)


def calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management):
    # Inputs are 0..100 sliders; normalize to 0..1
    return ((float(cognitive_flexibility) + float(social_emotional_intelligence) + float(strategic_career_management)) / 3.0) / 100.0


def calculate_ai_enhancement_potential(ai_enhancement_score):
    return float(ai_enhancement_score)


def calculate_job_growth_projection(growth_rate_g):
    score = 50 + (float(growth_rate_g) * 100.0)
    score = max(0.0, min(score, 100.0))
    return int(score)


def calculate_wage_premium(ai_skilled_wage, median_wage):
    if median_wage == 0:
        return 0.0
    return (float(ai_skilled_wage) - float(median_wage)) / float(median_wage)


def calculate_entry_accessibility(education_years_required, experience_years_required):
    return 1.0 / (1.0 + 0.1 * (float(education_years_required) + float(experience_years_required)))


def calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1=0.30, w2=0.30, w3=0.25, w4=0.15):
    return (float(w1) * float(ai_enhancement) +
            float(w2) * float(job_growth_normalized) +
            float(w3) * float(wage_premium) +
            float(w4) * float(entry_accessibility))


def calculate_growth_multiplier(current_job_postings, previous_job_postings, lambda_val=0.3):
    if previous_job_postings == 0:
        return 1.0
    return (float(current_job_postings) / float(previous_job_postings)) ** float(lambda_val)


def calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma=0.2):
    if national_avg_demand == 0:
        return 1.0
    return 1.0 + float(gamma) * ((float(local_demand) / float(national_avg_demand)) + float(remote_work_factor) - 1.0)


def calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier):
    return float(h_base) * float(growth_multiplier) * float(regional_multiplier)


def calculate_skills_match_score(user_skills_df, required_skills_df):
    if user_skills_df is None or required_skills_df is None:
        return 0.0
    if user_skills_df.empty or required_skills_df.empty:
        return 0.0
    merged_df = pd.merge(user_skills_df, required_skills_df, on='skill_name', how='inner')
    if merged_df.empty:
        return 0.0
    weighted_sum = 0.0
    total_importance = required_skills_df['skill_importance'].sum()
    if total_importance == 0:
        return 0.0
    for _, row in merged_df.iterrows():
        weighted_sum += (min(float(row['individual_skill_score']), float(row['required_skill_score'])) / 100.0) * float(row['skill_importance'])
    return (weighted_sum / float(total_importance)) * 100.0


def calculate_timing_factor(years_experience):
    years = float(years_experience)
    if years <= 0:
        return 1.0
    return 1.0 + (years / 5.0)


def calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor):
    if max_possible_match is None or max_possible_match == 0:
        return 0.0
    return (float(skills_match_score) / float(max_possible_match)) * float(timing_factor)


def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    return (float(vr_score) * float(hr_score) * float(alignment_factor)) / 100.0


def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
    return float(alpha) * float(vr_score) + (1.0 - float(alpha)) * float(hr_score) + float(beta) * float(synergy_percentage)


# --------- Helper to compute everything end-to-end ---------

def _clip01(x):
    return max(0.0, min(float(x), 1.0))


def compute_all_scores(inputs_dict):
    occ = inputs_dict['occupation_row']

    # AI-Fluency subcomponents
    s1 = calculate_technical_ai_skills(inputs_dict['prompting_score'], inputs_dict['tools_score'], inputs_dict['understanding_score'], inputs_dict['datalit_score'])
    s2_raw = calculate_ai_augmented_productivity(inputs_dict['output_quality_with_ai'], inputs_dict['output_quality_without_ai'], inputs_dict['time_without_ai'], inputs_dict['time_with_ai'])
    s2 = min(s2_raw / 4.0, 1.0)  # normalize assuming 4x productivity ~ full score
    s3 = _clip01(calculate_critical_ai_judgment(inputs_dict['errors_caught'], inputs_dict['total_ai_errors'], inputs_dict['appropriate_trust_decisions'], inputs_dict['total_decisions']))
    s4 = _clip01(calculate_ai_learning_velocity(inputs_dict['delta_proficiency'], inputs_dict['delta_t_hours_invested']))

    ai_fluency = _clip01(calculate_ai_fluency(s1, s2, s3, s4))

    # Domain-Expertise
    e_edu = calculate_education_foundation(inputs_dict['education_level'])
    e_exp = _clip01(calculate_practical_experience(inputs_dict['years_experience'], gamma=0.15))
    e_spec = _clip01(calculate_specialization_depth(inputs_dict['portfolio_score'], inputs_dict['recognition_score'], inputs_dict['credentials_score']))
    domain_expertise = _clip01(calculate_domain_expertise(e_edu, e_exp, e_spec))

    # Adaptive-Capacity (normalize to 0..1 inside function)
    adaptive_capacity = _clip01(calculate_adaptive_capacity(inputs_dict['cognitive_flexibility'], inputs_dict['social_emotional_intelligence'], inputs_dict['strategic_career_management']))

    # Idiosyncratic Readiness (0..1)
    vr_01 = _clip01(0.45 * ai_fluency + 0.35 * domain_expertise + 0.20 * adaptive_capacity)
    vr_100 = vr_01 * 100.0

    # Systematic Opportunity
    ai_enh = calculate_ai_enhancement_potential(occ['ai_enhancement_score'])  # 0..1
    job_growth_proj = calculate_job_growth_projection(occ['job_growth_rate_g'])  # 0..100
    job_growth_norm = job_growth_proj / 100.0
    wage_prem = calculate_wage_premium(occ['ai_skilled_wage'], occ['median_wage'])
    wage_prem = _clip01(wage_prem)  # cap to [0,1]
    entry_acc = calculate_entry_accessibility(occ['education_years_required'], occ['experience_years_required'])  # 0..1

    h_base = calculate_base_opportunity_score(ai_enh, job_growth_norm, wage_prem, entry_acc)
    m_growth = calculate_growth_multiplier(occ['current_job_postings'], occ['previous_job_postings'], lambda_val=inputs_dict['lambda_val'])
    m_reg = calculate_regional_multiplier(occ['local_demand'], occ['national_avg_demand'], occ['remote_work_factor'], gamma=inputs_dict['gamma_val'])

    hr_01 = _clip01(calculate_systematic_opportunity(h_base, m_growth, m_reg))
    hr_100 = hr_01 * 100.0

    # Synergy
    skills_match = calculate_skills_match_score(inputs_dict['individual_skills_df'], inputs_dict['required_skills_df'])  # 0..100
    timing_factor = calculate_timing_factor(inputs_dict['years_experience'])
    alignment = calculate_alignment_factor(skills_match, inputs_dict['max_possible_match'], timing_factor)

    synergy_pct = calculate_synergy_percentage(vr_100, hr_100, alignment)
    synergy_pct = max(0.0, min(synergy_pct, 100.0))  # normalize for display

    # Final AI-R
    ai_r = calculate_ai_readiness_score(vr_100, hr_100, synergy_pct, inputs_dict['alpha'], inputs_dict['beta'])

    return {
        'vr_score': float(vr_100),
        'hr_score': float(hr_100),
        'synergy_pct': float(synergy_pct),
        'ai_r': float(ai_r),
        'vr_breakdown': {
            'AI-Fluency (01)': float(ai_fluency),
            'Domain-Expertise (01)': float(domain_expertise),
            'Adaptive-Capacity (01)': float(adaptive_capacity),
            'S1 (Tech AI Skills)': float(s1),
            'S2 (AI-Aug Productivity, norm)': float(s2),
            'S3 (Critical AI Judgment)': float(s3),
            'S4 (AI Learning Velocity)': float(s4)
        },
        'h_breakdown': {
            'AI-Enhancement': float(ai_enh),
            'Job Growth (01)': float(job_growth_norm),
            'Wage Premium': float(wage_prem),
            'Entry Accessibility': float(entry_acc),
            'H_base (01)': float(h_base),
            'Growth Multiplier': float(m_growth),
            'Regional Multiplier': float(m_reg)
        },
        'skills_match': float(skills_match),
        'timing_factor': float(timing_factor),
        'alignment': float(alignment)
    }


# --------- Pathway Simulation Helper ---------

def simulate_pathway_impact(current_ai_fluency, current_domain_expertise, current_adaptive_capacity, impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity, completion_score=1.0, mastery_score=1.0):
    ai_f = float(current_ai_fluency) + float(impact_ai_fluency) * float(completion_score) * float(mastery_score)
    de = float(current_domain_expertise) + float(impact_domain_expertise) * float(completion_score) * float(mastery_score)
    ac = float(current_adaptive_capacity) + float(impact_adaptive_capacity) * float(completion_score) * float(mastery_score)
    return _clip01(ai_f), _clip01(de), _clip01(ac)
