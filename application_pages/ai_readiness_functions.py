import pandas as pd
import numpy as np
import plotly.express as px

# AI-Fluency Sub-Components
def calculate_technical_ai_skills(prompting, tools, understanding, data_lit):
    return (prompting + tools + understanding + data_lit) / 4

def calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai):
    if output_quality_without_ai == 0 or time_with_ai == 0:
        return 0.0 # Handle division by zero
    return (output_quality_with_ai / output_quality_without_ai) * (time_without_ai / time_with_ai)

def calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions):
    # Ensure no division by zero and handle edge cases
    term1 = (errors_caught / total_ai_errors) if total_ai_errors > 0 else 0
    term2 = (appropriate_trust_decisions / total_decisions) if total_decisions > 0 else 0
    
    if total_ai_errors == 0 and total_decisions == 0:
        return 1.0 # If no errors or decisions, perfect judgment
    
    if total_ai_errors == 0 and errors_caught > 0: 
        term1 = 0
    if total_decisions == 0 and appropriate_trust_decisions > 0: 
        term2 = 0
        
    return 1 - (term1 + term2) / 2

def calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested):
    if delta_t_hours_invested == 0:
        return 0.0 # If no hours invested, no velocity
    return delta_proficiency / delta_t_hours_invested

def calculate_ai_fluency(s1, s2, s3, s4):
    return 0.1 * s1 + 0.2 * s2 + 0.3 * s3 + 0.4 * s4

# Domain-Expertise Sub-Components
def calculate_education_foundation(education_level):
    education_map = {
        "PhD": 1.0,
        "Master's": 0.8,
        "Bachelor's": 0.6,
        "Associate's/Certificate": 0.4,
        "HS + significant coursework": 0.2,
        "Some College": 0.3,
        "Other": 0.0
    }
    return education_map.get(education_level, 0.0)

def calculate_practical_experience(years_experience, gamma=0.15):
    if years_experience < 0: return 0.0 # Invalid input
    return years_experience / (years_experience + (1 / gamma))

def calculate_specialization_depth(portfolio_score, recognition_score, credentials_score):
    return (portfolio_score + recognition_score + credentials_score) / 3

def calculate_domain_expertise(education_foundation, practical_experience, specialization_depth):
    return 0.125 * education_foundation + 0.25 * practical_experience + 0.625 * specialization_depth

# Adaptive-Capacity
def calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management):
    return (cognitive_flexibility + social_emotional_intelligence + strategic_career_management) / 3

# Idiosyncratic Readiness (V^R)
def calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1=0.45, w2=0.35, w3=0.20):
    return (w1 * ai_fluency) + (w2 * domain_expertise) + (w3 * adaptive_capacity)

# Systematic Opportunity (H^R) Sub-Components
def calculate_ai_enhancement_potential(ai_enhancement_score):
    return ai_enhancement_score

def calculate_job_growth_projection(growth_rate_g):
    score = 50 + (growth_rate_g * 100)
    score = max(0, min(score, 100))
    return int(score)

def calculate_wage_premium(ai_skilled_wage, median_wage):
    if median_wage == 0:
        return 0.0 # Handle division by zero
    return (ai_skilled_wage - median_wage) / median_wage

def calculate_entry_accessibility(education_years_required, experience_years_required):
    return 1 / (1 + 0.1 * (education_years_required + experience_years_required))

def calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1=0.30, w2=0.30, w3=0.25, w4=0.15):
    return (w1 * ai_enhancement +
            w2 * job_growth_normalized +
            w3 * wage_premium +
            w4 * entry_accessibility)

def calculate_growth_multiplier(current_job_postings, previous_job_postings, lambda_val=0.3):
    if previous_job_postings == 0: # Handle division by zero gracefully
        return 1.0
    return (current_job_postings / previous_job_postings)**lambda_val

def calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma=0.2):
    if national_avg_demand == 0: # Handle division by zero
        return 1.0
    return 1 + gamma * (local_demand/national_avg_demand + remote_work_factor - 1)

def calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier):
    return h_base * growth_multiplier * regional_multiplier

# Synergy Components
def calculate_skills_match_score(user_skills_df, required_skills_df):
    if user_skills_df.empty or required_skills_df.empty:
        return 0.0

    merged_df = pd.merge(user_skills_df, required_skills_df, on='skill_name', how='inner')

    if merged_df.empty:
        return 0.0

    weighted_sum = 0
    total_importance = required_skills_df['skill_importance'].sum()

    if total_importance == 0:
        return 0.0

    for _, row in merged_df.iterrows():
        weighted_sum += (min(row['individual_skill_score'], row['required_skill_score']) / 100) * row['skill_importance']

    return (weighted_sum / total_importance) * 100

def calculate_timing_factor(years_experience):
    if years_experience <= 0:
        return 1.0
    else:
        return 1 + (years_experience / 5)

def calculate_alignment_factor(skills_match_score, max_possible_match, timing_factor):
    if max_possible_match == 0:
        return 0.0 # Handle division by zero
    return (skills_match_score / max_possible_match) * timing_factor

def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    return (vr_score * hr_score * alignment_factor) / 100.0

# Final AI-Readiness Score
def calculate_ai_readiness_score(vr_score, hr_score, synergy_percentage, alpha, beta):
    return alpha * vr_score + (1-alpha) * hr_score + beta * synergy_percentage

# Pathway Simulation
def simulate_pathway_impact(current_ai_fluency, current_domain_expertise, current_adaptive_capacity, impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity, completion_score=1.0, mastery_score=1.0):
    ai_fluency = current_ai_fluency + impact_ai_fluency * completion_score * mastery_score
    domain_expertise = current_domain_expertise + impact_domain_expertise * completion_score * mastery_score
    adaptive_capacity = current_adaptive_capacity + impact_adaptive_capacity * completion_score * mastery_score

    ai_fluency = min(ai_fluency, 1.0)
    domain_expertise = min(domain_expertise, 1.0)
    adaptive_capacity = min(adaptive_capacity, 1.0)

    return ai_fluency, domain_expertise, adaptive_capacity