import pandas as pd
import math


def clamp01(x):
    try:
        return max(0.0, min(1.0, float(x)))
    except Exception:
        return 0.0


# ------------------------- AI-Fluency Sub-Components -------------------------

def calculate_technical_ai_skills(prompting, tools, understanding, data_lit):
    return (float(prompting) + float(tools) + float(understanding) + float(data_lit)) / 4.0


def calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai):
    oq_wa = float(output_quality_with_ai)
    oq_woa = float(output_quality_without_ai)
    t_woa = float(time_without_ai)
    t_wa = float(time_with_ai)
    if oq_woa <= 0 or t_wa <= 0:
        # Gracefully handle invalid inputs
        return 0.0
    return (oq_wa / oq_woa) * (t_woa / t_wa)


def calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions):
    e_caught = float(errors_caught)
    t_ai_err = float(total_ai_errors)
    appr_trust = float(appropriate_trust_decisions)
    t_dec = float(total_decisions)
    ratio1 = (e_caught / t_ai_err) if t_ai_err > 0 else 0.0
    ratio2 = (appr_trust / t_dec) if t_dec > 0 else 0.0
    val = 1.0 - (ratio1 + ratio2) / 2.0
    return clamp01(val)


def calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested):
    dp = float(delta_proficiency)
    dt = float(delta_t_hours_invested)
    if dt == 0:
        if dp == 0:
            return 0.0
        raise ZeroDivisionError("Cannot divide by zero for AI Learning Velocity if hours invested is zero with non-zero proficiency change.")
    return dp / dt


def calculate_ai_fluency(s1, s2, s3, s4):
    # Clamp each sub-score to [0,1] to maintain normalization
    s1c = clamp01(s1)
    s2c = clamp01(s2)
    s3c = clamp01(s3)
    s4c = clamp01(s4)
    return 0.1 * s1c + 0.2 * s2c + 0.3 * s3c + 0.4 * s4c


# ------------------------- Domain-Expertise Sub-Components -------------------------

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
    y = float(years_experience)
    g = float(gamma) if float(gamma) > 0 else 0.15
    return y / (y + (1.0 / g))


def calculate_specialization_depth(portfolio_score, recognition_score, credentials_score):
    return (float(portfolio_score) + float(recognition_score) + float(credentials_score)) / 3.0


def calculate_domain_expertise(education_foundation, practical_experience, specialization_depth):
    # Inputs are already in [0,1] ranges by construction
    return 0.125 * clamp01(education_foundation) + 0.25 * clamp01(practical_experience) + 0.625 * clamp01(specialization_depth)


# ------------------------- Adaptive-Capacity -------------------------

def calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management):
    # Inputs expected as 0..100; convert to 0..1
    return (float(cognitive_flexibility) + float(social_emotional_intelligence) + float(strategic_career_management)) / 3.0 / 100.0


# ------------------------- Idiosyncratic Readiness (V^R) -------------------------

def calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1=0.45, w2=0.35, w3=0.20):
    return (float(w1) * clamp01(ai_fluency)) + (float(w2) * clamp01(domain_expertise)) + (float(w3) * clamp01(adaptive_capacity))


# ------------------------- Systematic Opportunity (H^R) -------------------------

def calculate_ai_enhancement_potential(ai_enhancement_score):
    return float(ai_enhancement_score)


def calculate_job_growth_projection(growth_rate_g):
    score = 50.0 + (float(growth_rate_g) * 100.0)
    score = max(0.0, min(score, 100.0))
    return int(score)


def calculate_wage_premium(ai_skilled_wage, median_wage):
    mw = float(median_wage)
    if mw <= 0:
        return 0.0
    return (float(ai_skilled_wage) - mw) / mw


def calculate_entry_accessibility(education_years_required, experience_years_required):
    return 1.0 / (1.0 + 0.1 * (float(education_years_required) + float(experience_years_required)))


def calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1=0.30, w2=0.30, w3=0.25, w4=0.15):
    # Ensure all inputs are in [0,1]
    ai_e = clamp01(ai_enhancement)
    jg = clamp01(job_growth_normalized)
    wp = clamp01(wage_premium)
    ea = clamp01(entry_accessibility)
    return (float(w1) * ai_e + float(w2) * jg + float(w3) * wp + float(w4) * ea)


def calculate_growth_multiplier(current_job_postings, previous_job_postings, lambda_val=0.3):
    prev = float(previous_job_postings)
    curr = float(current_job_postings)
    if prev <= 0:
        return 1.0
    lam = float(lambda_val)
    if lam < 0:
        lam = 0.0
    return (curr / prev) ** lam


def calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma=0.2):
    nad = float(national_avg_demand)
    if nad <= 0:
        nad = 1.0
    return 1.0 + float(gamma) * (float(local_demand) / nad + float(remote_work_factor) - 1.0)


def calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier):
    return float(h_base) * float(growth_multiplier) * float(regional_multiplier)


# ------------------------- Synergy Components -------------------------

def calculate_skills_match_score(user_skills_df, required_skills_df):
    if user_skills_df is None or required_skills_df is None:
        return 0.0
    if user_skills_df.empty or required_skills_df.empty:
        return 0.0
    merged_df = pd.merge(user_skills_df, required_skills_df, on='skill_name', how='inner')
    if merged_df.empty:
        return 0.0
    total_importance = required_skills_df['skill_importance'].sum()
    if total_importance == 0:
        return 0.0
    weighted_sum = 0.0
    for _, row in merged_df.iterrows():
        weighted_sum += (min(float(row['individual_skill_score']), float(row['required_skill_score'])) / 100.0) * float(row['skill_importance'])
    return (weighted_sum / float(total_importance)) * 100.0


def calculate_timing_factor(years_experience):
    y = float(years_experience)
    if y <= 0:
        return 1.0
    return 1.0 + (y / 5.0)


def calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor):
    max_match = float(max_possible_match) if float(max_possible_match) > 0 else 100.0
    return (float(skills_match_score) / max_match) * float(timing_factor)


def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    return (float(vr_score) * float(hr_score) * float(alignment_factor)) / 100.0


# ------------------------- Final AI-Readiness -------------------------

def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
    return float(alpha) * float(vr_score) + (1.0 - float(alpha)) * float(hr_score) + float(beta) * float(synergy_percentage)


# ------------------------- Pathway Simulation -------------------------

def simulate_pathway_impact(current_ai_fluency, current_domain_expertise, current_adaptive_capacity, impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity, completion_score=1.0, mastery_score=1.0):
    ai_fluency = float(current_ai_fluency) + float(impact_ai_fluency) * float(completion_score) * float(mastery_score)
    domain_expertise = float(current_domain_expertise) + float(impact_domain_expertise) * float(completion_score) * float(mastery_score)
    adaptive_capacity = float(current_adaptive_capacity) + float(impact_adaptive_capacity) * float(completion_score) * float(mastery_score)
    return clamp01(ai_fluency), clamp01(domain_expertise), clamp01(adaptive_capacity)


# ------------------------- Orchestration -------------------------

def compute_all_scores(inputs_dict):
    # Extract inputs safely
    prompting_score = inputs_dict.get('prompting_score', 0.0)
    tools_score = inputs_dict.get('tools_score', 0.0)
    understanding_score = inputs_dict.get('understanding_score', 0.0)
    datalit_score = inputs_dict.get('datalit_score', 0.0)
    output_quality_with_ai = inputs_dict.get('output_quality_with_ai', 0.0)
    output_quality_without_ai = inputs_dict.get('output_quality_without_ai', 1.0)
    time_without_ai = inputs_dict.get('time_without_ai', 1.0)
    time_with_ai = inputs_dict.get('time_with_ai', 1.0)
    errors_caught = inputs_dict.get('errors_caught', 0.0)
    total_ai_errors = inputs_dict.get('total_ai_errors', 0.0)
    appropriate_trust_decisions = inputs_dict.get('appropriate_trust_decisions', 0.0)
    total_decisions = inputs_dict.get('total_decisions', 0.0)
    delta_proficiency = inputs_dict.get('delta_proficiency', 0.0)
    delta_t_hours_invested = inputs_dict.get('delta_t_hours_invested', 1.0)

    education_level = inputs_dict.get('education_level', "Master's")
    years_experience = inputs_dict.get('years_experience', 0.0)
    portfolio_score = inputs_dict.get('portfolio_score', 0.0)
    recognition_score = inputs_dict.get('recognition_score', 0.0)
    credentials_score = inputs_dict.get('credentials_score', 0.0)

    cognitive_flexibility = inputs_dict.get('cognitive_flexibility', 0.0)
    social_emotional_intelligence = inputs_dict.get('social_emotional_intelligence', 0.0)
    strategic_career_management = inputs_dict.get('strategic_career_management', 0.0)

    occupation_row = inputs_dict.get('occupation_row')
    lambda_val = inputs_dict.get('lambda_val', 0.3)
    gamma_val = inputs_dict.get('gamma_val', 0.2)

    user_skills_df = inputs_dict.get('individual_skills_df', pd.DataFrame(columns=['skill_name', 'individual_skill_score']))
    required_skills_df = inputs_dict.get('required_skills_df', pd.DataFrame(columns=['skill_name', 'required_skill_score', 'skill_importance']))
    max_possible_match = inputs_dict.get('max_possible_match', 100.0)

    alpha = inputs_dict.get('alpha', 0.6)
    beta = inputs_dict.get('beta', 0.15)

    # Compute AI-Fluency components
    s1 = calculate_technical_ai_skills(prompting_score, tools_score, understanding_score, datalit_score)
    s2_raw = calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai)
    s2 = clamp01(s2_raw)
    try:
        s4_raw = calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested)
    except ZeroDivisionError:
        s4_raw = 0.0
    s4 = clamp01(s4_raw)
    s3 = calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions)
    ai_fluency_01 = clamp01(calculate_ai_fluency(s1, s2, s3, s4))

    # Compute Domain-Expertise
    e_edu = calculate_education_foundation(education_level)
    e_exp = calculate_practical_experience(years_experience, gamma=0.15)
    e_spec = calculate_specialization_depth(portfolio_score, recognition_score, credentials_score)
    domain_expertise_01 = clamp01(calculate_domain_expertise(e_edu, e_exp, e_spec))

    # Adaptive-Capacity (0..1)
    adaptive_capacity_01 = clamp01(calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management))

    # Idiosyncratic Readiness V^R (0..1) and (0..100)
    vr_01 = clamp01(calculate_idiosyncratic_readiness(ai_fluency_01, domain_expertise_01, adaptive_capacity_01))
    vr_100 = vr_01 * 100.0

    # Systematic Opportunity
    if occupation_row is None:
        # Construct a safe default in case not provided
        occupation_row = {
            'ai_enhancement_score': 0.8,
            'job_growth_rate_g': 0.25,
            'ai_skilled_wage': 120000,
            'median_wage': 90000,
            'education_years_required': 4,
            'experience_years_required': 2,
            'current_job_postings': 500,
            'previous_job_postings': 400,
            'remote_work_factor': 0.6,
            'local_demand': 1.2,
            'national_avg_demand': 1.0,
        }
    ai_enh = calculate_ai_enhancement_potential(occupation_row['ai_enhancement_score'])
    job_growth_01 = calculate_job_growth_projection(occupation_row['job_growth_rate_g']) / 100.0
    wage_prem = calculate_wage_premium(occupation_row['ai_skilled_wage'], occupation_row['median_wage'])
    entry_acc = calculate_entry_accessibility(occupation_row['education_years_required'], occupation_row['experience_years_required'])

    h_base_01 = calculate_base_opportunity_score(ai_enh, job_growth_01, wage_prem, entry_acc)
    m_growth = calculate_growth_multiplier(occupation_row['current_job_postings'], occupation_row['previous_job_postings'], lambda_val=lambda_val)
    m_regional = calculate_regional_multiplier(occupation_row['local_demand'], occupation_row['national_avg_demand'], occupation_row['remote_work_factor'], gamma=gamma_val)
    hr_01 = clamp01(calculate_systematic_opportunity(h_base_01, m_growth, m_regional))
    hr_100 = hr_01 * 100.0

    # Synergy
    skills_match = calculate_skills_match_score(user_skills_df, required_skills_df)
    timing_factor = calculate_timing_factor(years_experience)
    alignment = calculate_alignment_factor(skills_match, max_possible_match, timing_factor)
    synergy_pct = calculate_synergy_percentage(vr_100, hr_100, alignment)
    synergy_pct = max(0.0, min(100.0, float(synergy_pct)))

    # Final AI-R
    ai_r = calculate_ai_readiness_score(vr_100, hr_100, synergy_pct, alpha, beta)

    return {
        'vr_score': vr_100,
        'hr_score': hr_100,
        'synergy_pct': synergy_pct,
        'ai_r': ai_r,
        'vr_breakdown': {
            'AI-Fluency (01)': ai_fluency_01,
            'Domain-Expertise (01)': domain_expertise_01,
            'Adaptive-Capacity (01)': adaptive_capacity_01,
            'S1 Technical AI Skills': clamp01(s1),
            'S2 AI-Augmented Productivity (raw)': float(s2_raw),
            'S2 (01)': s2,
            'S3 Critical AI Judgment (01)': s3,
            'S4 Learning Velocity (raw)': float(s4_raw),
            'S4 (01)': s4,
        },
        'h_breakdown': {
            'AI-Enhancement': ai_enh,
            'Job Growth (01)': job_growth_01,
            'Wage Premium': wage_prem,
            'Entry Accessibility': entry_acc,
            'H_base (01)': h_base_01,
            'Growth Multiplier': m_growth,
            'Regional Multiplier': m_regional,
        },
        'skills_match': skills_match,
        'timing_factor': timing_factor,
        'alignment': alignment,
    }
