id: 68f63eb9833967484a12dd11_documentation
summary: AI-Readiness score - GPT-5 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab - AI Career Navigator & Pathway Planner: A Developer's Guide to the AI-Readiness Framework

## 1. Introduction to the AI-Readiness Framework and Application Overview
Duration: 0:10

<aside class="positive">
This first step provides essential context for the application. Understanding the core problem it solves and the theoretical framework it implements will greatly aid in comprehending the code and its functionalities.
</aside>

In today's rapidly evolving labor market, the advent of Artificial Intelligence (AI) is transforming jobs and creating new career opportunities. Navigating this landscape requires a robust framework to assess an individual's preparedness for AI-enabled roles and to strategically plan for future career development. The **QuLab - AI Career Navigator & Pathway Planner** is a Streamlit application designed to implement and interactively explore the **AI-Readiness Score (AI-R) framework**.

The **AI-Readiness Score (AI-R)** is a parametric model that quantifies an individual's preparedness for AI-enabled careers by considering both their intrinsic capabilities and the external market opportunities. It serves as a powerful tool for self-assessment, career guidance, and "what-if" scenario planning.

The core formula for the AI-Readiness Score for an individual $i$ at time $t$ is defined as:

$$ AI-R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R) $$

Where:
*   $V^R(t)$ is the **Idiosyncratic Readiness**, representing an individual's personal capabilities.
*   $H^R(t)$ is the **Systematic Opportunity**, reflecting external market demand and opportunities.
*   $\alpha \in [0,1]$ is the weight on individual vs. market factors.
*   $\beta > 0$ is the **Synergy coefficient**, capturing the alignment between $V^R$ and $H^R$.
*   Both $V^R$ and $H^R$ are normalized to $[0, 100]$.
*   $\text{Synergy}\%$ is also normalized to $[0, 100]$ percentage units.

This application is built with Streamlit, a popular Python library for creating interactive web applications with minimal code. It comprises three main pages, accessible via the sidebar navigation:

1.  **AI-Readiness Score Components**: Provides a theoretical deep dive into the $V^R$, $H^R$, and Synergy components, their sub-components, and the mathematical formulas underpinning their calculation. It also displays the synthetic datasets used throughout the application.
2.  **AI-Readiness Score Calculator**: An interactive tool where users can input various personal and market parameters to calculate their real-time AI-Readiness Score. It visualizes the contributions of different factors.
3.  **Pathway Simulation**: Allows users to simulate the impact of completing different learning pathways on their AI-Readiness Score, enabling them to evaluate potential career development strategies.

### Application Architecture

The application follows a modular architecture, separating the core calculation logic from the Streamlit UI components and data handling.

```mermaid
graph TD
    A[User Interaction] --> B{Streamlit Application <br> (app.py)}
    B --> C[Page 1: Components Explanation <br> (page1.py)]
    B --> D[Page 2: Score Calculator <br> (page2.py)]
    B --> E[Page 3: Pathway Simulation <br> (page3.py)]
    C --> F[DataFrames (Session State)]
    D --> F
    E --> F
    D --> G[AI-Readiness Functions <br> (ai_readiness_functions.py)]
    E --> G
    F --> G
```

*   **`app.py`**: The central orchestrator, managing navigation and initial data loading.
*   **`application_pages/page1.py`, `page2.py`, `page3.py`**: Handle the specific UI and logic for each page.
*   **`application_pages/ai_readiness_functions.py`**: Contains all the pure Python functions for calculations, ensuring business logic is separated from presentation.
*   **Session State**: Streamlit's `st.session_state` is extensively used to persist data (like calculated scores or selected options) across page navigations and reruns, creating a cohesive user experience.
*   **DataFrames**: Synthetic data is loaded into Pandas DataFrames and stored in session state, serving as the basis for calculations and simulations.

This codelab will guide you through understanding each part of this application, from the underlying mathematical models to their Streamlit implementation.

## 2. Setting Up the Development Environment
Duration: 0:05

To run and explore the QuLab application, you'll need a Python development environment.

### Prerequisites

*   Python 3.8 or higher
*   `pip` (Python package installer)

### Installation Steps

1.  **Create a Project Directory**:
    If you don't have the files yet, create a directory for your project and save the provided Python files into it.
    ```bash
    mkdir qulab_ai_readiness
    cd qulab_ai_readiness
    mkdir application_pages
    # Save app.py here
    # Save ai_readiness_functions.py into application_pages/
    # Save page1.py into application_pages/
    # Save page2.py into application_pages/
    # Save page3.py into application_pages/
    ```

2.  **Create a Virtual Environment** (Recommended):
    Virtual environments help manage project dependencies and avoid conflicts with other Python projects.
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**:
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows (Command Prompt):
        ```cmd
        venv\Scripts\activate.bat
        ```
    *   On Windows (PowerShell):
        ```powershell
        venv\Scripts\Activate.ps1
        ```

4.  **Install Dependencies**:
    The application requires `streamlit`, `pandas`, `numpy`, and `plotly`. You can install them using `pip`:
    ```bash
    pip install streamlit pandas numpy plotly
    ```

5.  **Run the Streamlit Application**:
    Navigate to the directory containing `app.py` and run the Streamlit command:
    ```bash
    streamlit run app.py
    ```
    This will open the application in your default web browser (usually `http://localhost:8501`).

<aside class="positive">
Always use a virtual environment for your Python projects. It keeps your dependencies isolated and prevents "dependency hell" where different projects might require conflicting versions of the same library.
</aside>

## 3. Understanding the AI-Readiness Score Components ($V^R$, $H^R$, Synergy)
Duration: 0:25

This step delves into the foundational mathematical and conceptual components of the AI-Readiness Score. The `application_pages/page1.py` file serves as a user-friendly introduction to these concepts within the Streamlit app, while `application_pages/ai_readiness_functions.py` contains their concrete implementations.

### 3.1 Idiosyncratic Readiness ($V^R$)

$V^R$ quantifies an individual's personal capabilities and readiness for AI-enabled roles. It's a weighted average of three main sub-components, each normalized to a $[0, 1]$ scale for internal calculations and then scaled to $[0, 100]$ for display.

The overall $V^R$ is a weighted sum:
$$ V^R = w_1 \cdot \text{AI-Fluency} + w_2 \cdot \text{Domain-Expertise} + w_3 \cdot \text{Adaptive-Capacity} $$
*(Typically, $w_1=0.45, w_2=0.35, w_3=0.20$)*.

#### AI-Fluency ($S_1, S_2, S_3, S_4$)

Measures an individual's proficiency in interacting with AI systems, understanding AI outputs, and adapting to AI-driven workflows. It's composed of four sub-elements:

*   **Technical AI Skills (S1)**: Calculated as the average of prompting, tools, understanding, and data literacy scores.
*   **AI-Augmented Productivity (S2)**: Measures the improvement in output quality and reduction in time when using AI.
*   **Critical AI Judgment (S3)**: Assesses the ability to identify AI errors and make appropriate trust decisions.
*   **AI Learning Velocity (S4)**: Quantifies how quickly an individual can improve their AI proficiency over time.

The `calculate_ai_fluency` function then combines these:
$$ \text{AI-Fluency} = 0.1 \cdot S_1 + 0.2 \cdot S_2 + 0.3 \cdot S_3 + 0.4 \cdot S_4 $$

**Code Snippet (`ai_readiness_functions.py`):**
```python
# AI-Fluency Sub-Components
def calculate_technical_ai_skills(prompting, tools, understanding, data_lit):
    return (prompting + tools + understanding + data_lit) / 4

def calculate_ai_augmented_productivity(output_quality_with_ai, output_quality_without_ai, time_without_ai, time_with_ai):
    if output_quality_without_ai == 0 or time_with_ai == 0:
        return 0.0 # Handle division by zero
    return (output_quality_with_ai / output_quality_without_ai) * (time_without_ai / time_with_ai)

def calculate_critical_ai_judgment(errors_caught, total_ai_errors, appropriate_trust_decisions, total_decisions):
    # ... (logic for handling division by zero and edge cases)
    term1 = (errors_caught / total_ai_errors) if total_ai_errors > 0 else 0
    term2 = (appropriate_trust_decisions / total_decisions) if total_decisions > 0 else 0
    return 1 - (term1 + term2) / 2

def calculate_ai_learning_velocity(delta_proficiency, delta_t_hours_invested):
    if delta_t_hours_invested == 0:
        return 0.0
    return delta_proficiency / delta_t_hours_invested

def calculate_ai_fluency(s1, s2, s3, s4):
    return 0.1 * s1 + 0.2 * s2 + 0.3 * s3 + 0.4 * s4
```

#### Domain-Expertise ($E_{\text{education}}, E_{\text{experience}}, E_{\text{specialization}}$)

Assesses the depth of knowledge and experience within a specific field.

*   **Education Foundation**: Mapped from educational levels (e.g., PhD=1.0, Master's=0.8).
*   **Practical Experience**: A sigmoid-like function of years of experience, capturing diminishing returns.
*   **Specialization Depth**: Average of portfolio, recognition, and credentials scores.

The `calculate_domain_expertise` function combines these:
$$ \text{Domain-Expertise} = 0.125 \cdot E_{\text{education}} + 0.25 \cdot E_{\text{experience}} + 0.625 \cdot E_{\text{specialization}} $$

**Code Snippet (`ai_readiness_functions.py`):**
```python
# Domain-Expertise Sub-Components
def calculate_education_foundation(education_level):
    education_map = {
        "PhD": 1.0, "Master's": 0.8, "Bachelor's": 0.6,
        "Associate's/Certificate": 0.4, "HS + significant coursework": 0.2,
        "Some College": 0.3, "Other": 0.0
    }
    return education_map.get(education_level, 0.0)

def calculate_practical_experience(years_experience, gamma=0.15):
    if years_experience < 0: return 0.0
    return years_experience / (years_experience + (1 / gamma))

def calculate_specialization_depth(portfolio_score, recognition_score, credentials_score):
    return (portfolio_score + recognition_score + credentials_score) / 3

def calculate_domain_expertise(education_foundation, practical_experience, specialization_depth):
    return 0.125 * education_foundation + 0.25 * practical_experience + 0.625 * specialization_depth
```

#### Adaptive-Capacity

Evaluates an individual's ability to adapt to new technologies, learn new skills, and navigate changing career landscapes, averaged from three scores: Cognitive Flexibility, Social-Emotional Intelligence, and Strategic Career Management.
$$ \text{Adaptive-Capacity} = \frac{\text{cognitive\_flexibility} + \text{social\_emotional\_intelligence} + \text{strategic\_career\_management}}{3} $$

**Code Snippet (`ai_readiness_functions.py`):**
```python
# Adaptive-Capacity
def calculate_adaptive_capacity(cognitive_flexibility, social_emotional_intelligence, strategic_career_management):
    # These are expected to be 0-100 scores and will be normalized for the VR calculation if needed.
    return (cognitive_flexibility + social_emotional_intelligence + strategic_career_management) / 3
```

Finally, `calculate_idiosyncratic_readiness` combines these:
```python
def calculate_idiosyncratic_readiness(ai_fluency, domain_expertise, adaptive_capacity, w1=0.45, w2=0.35, w3=0.20):
    return (w1 * ai_fluency) + (w2 * domain_expertise) + (w3 * adaptive_capacity)
```

### 3.2 Systematic Opportunity ($H^R$)

$H^R$ reflects the external market demand and opportunities for a given AI-enabled career path. It's a product of a base opportunity score and two multipliers.

$$ H^R = H_{\text{base}} \cdot M_{\text{growth}} \cdot M_{\text{regional}} $$

#### Base Opportunity Score ($H_{\text{base}}$)

A weighted sum of four key market factors:

*   **AI-Enhancement Potential**: The degree to which AI can augment or transform an occupation.
*   **Job Growth Projection**: Future growth prospects for the occupation, normalized.
*   **Wage Premium**: The additional earnings potential for AI-skilled professionals in that role.
*   **Entry Accessibility**: The inverse of the effort required to enter the occupation (based on education and experience).

**Code Snippet (`ai_readiness_functions.py`):**
```python
# Systematic Opportunity (H^R) Sub-Components
def calculate_ai_enhancement_potential(ai_enhancement_score):
    return ai_enhancement_score # Assumed to be 0-1 already

def calculate_job_growth_projection(growth_rate_g):
    score = 50 + (growth_rate_g * 100) # Transforms a growth rate (e.g., 0.1 for 10%) into a 0-100 score
    score = max(0, min(score, 100))
    return int(score)

def calculate_wage_premium(ai_skilled_wage, median_wage):
    if median_wage == 0:
        return 0.0
    return (ai_skilled_wage - median_wage) / median_wage

def calculate_entry_accessibility(education_years_required, experience_years_required):
    return 1 / (1 + 0.1 * (education_years_required + experience_years_required))

def calculate_base_opportunity_score(ai_enhancement, job_growth_normalized, wage_premium, entry_accessibility, w1=0.30, w2=0.30, w3=0.25, w4=0.15):
    return (w1 * ai_enhancement +
            w2 * job_growth_normalized +
            w3 * wage_premium +
            w4 * entry_accessibility)
```

#### Multipliers ($M_{\text{growth}}, M_{\text{regional}}$)

These factors adjust the base opportunity score.

*   **Growth Multiplier**: Accounts for recent changes in job postings.
*   **Regional Multiplier**: Incorporates local demand, national averages, and remote work factors.

**Code Snippet (`ai_readiness_functions.py`):**
```python
def calculate_growth_multiplier(current_job_postings, previous_job_postings, lambda_val=0.3):
    if previous_job_postings == 0:
        return 1.0
    return (current_job_postings / previous_job_postings)**lambda_val

def calculate_regional_multiplier(local_demand, national_avg_demand, remote_work_factor, gamma=0.2):
    if national_avg_demand == 0:
        return 1.0
    return 1 + gamma * (local_demand/national_avg_demand + remote_work_factor - 1)

def calculate_systematic_opportunity(h_base, growth_multiplier, regional_multiplier):
    return h_base * growth_multiplier * regional_multiplier
```

### 3.3 Synergy Percentage ($\text{Synergy}\%$)

The Synergy component captures the alignment between an individual's capabilities ($V^R$) and the market's opportunities ($H^R$). A high synergy indicates a strong fit.
$$ \text{Synergy}\% = \frac{V^R \cdot H^R \cdot \text{Alignment}}{100.0} $$

#### Alignment Factor

Combines skills match and a timing factor.

*   **Skills Match Score**: Measures how well an individual's skills (from `individual_skills_df`) align with the required skills for a target occupation (from `occupation_required_skills_df`).
*   **Timing Factor**: Accounts for the relevance of years of experience in the current market.

**Code Snippet (`ai_readiness_functions.py`):**
```python
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
        return 0.0
    return (skills_match_score / max_possible_match) * timing_factor

def calculate_synergy_percentage(vr_score, hr_score, alignment_factor):
    return (vr_score * hr_score * alignment_factor) / 100.0
```

### 3.4 Synthetic Dataframes

The application uses several synthetic Pandas DataFrames to provide sample data for individuals, occupations, learning pathways, and skills. These are initialized in `app.py` and stored in `st.session_state` for global access across pages.

*   `individual_profiles_df`: Sample individual data.
*   `occupational_data_df`: Data on various AI-enabled occupations.
*   `learning_pathways_df`: Definitions of different learning pathways and their impact.
*   `occupation_required_skills_df`: Skills required for specific occupations.
*   `individual_skills_df`: A sample set of an individual's skills.

You can view these dataframes in the "AI-Readiness Score Components" page of the application within their respective expanders.

<aside class="negative">
It's crucial to understand that these functions operate on normalized scores (often 0-1) internally and only scale to 0-100 for display purposes. Pay attention to how the `* 100` or `/ 100` operations are applied in `page2.py` and `page3.py` to correctly interpret and manipulate these scores.
</aside>

## 4. Implementing the AI-Readiness Score Calculator
Duration: 0:20

This step focuses on `application_pages/page2.py`, which is the interactive "AI-Readiness Score Calculator." This page allows users to manipulate various parameters and see their impact on the final AI-R score.

### 4.1 UI Design and Input Widgets

The page uses Streamlit widgets like `st.slider`, `st.number_input`, and `st.selectbox` to gather user input for the many variables contributing to $V^R$, $H^R$, and Synergy.

**Global Parameters (`st.sidebar`):**
The `alpha` and `beta` coefficients, which are global to the AI-R formula, are placed in the sidebar for easy access and modification.

```python
# Global Parameters
st.sidebar.subheader("Global Parameters")
st.session_state.alpha = st.sidebar.slider(
    label="Weight on Individual Factors (\\alpha)",
    min_value=0.0, max_value=1.0, value=st.session_state.alpha, step=0.05,
    help="Weight allocated to individual readiness ($V^R$) vs. market opportunity ($H^R$) in the overall AI-Readiness Score."
)
st.session_state.beta = st.sidebar.slider(
    label="Synergy Coefficient (\\beta)",
    min_value=0.0, max_value=1.0, value=st.session_state.beta, step=0.05,
    help="Coefficient for the Synergy component, amplifying the AI-Readiness Score when individual readiness aligns with market opportunity."
)
```

**Section-wise Inputs (`st.expander`):**
To manage the large number of input fields, they are organized within `st.expander` components, grouped logically for $V^R$, $H^R$, and Synergy. These expanders are initially open (`expanded=True`) for a better user experience.

*   **Idiosyncratic Readiness (V^R) Inputs**: Further divided into three columns using `st.columns(3)` for AI-Fluency, Domain-Expertise, and Adaptive-Capacity sub-components. Each slider and number input directly corresponds to an argument of the `calculate_*` functions in `ai_readiness_functions.py`.
*   **Systematic Opportunity (H^R) Inputs**: A `st.selectbox` allows users to choose a `target_occupation`. Once selected, relevant data for that occupation is retrieved from `st.session_state.occupational_data_df`. Sliders are provided for `lambda_val` and `gamma_val` which are specific to the growth and regional multipliers.
*   **Synergy Inputs**: Allows setting `max_possible_skills_match` and displays the `user_skills_data` (editable in a future version, currently just a display of `individual_skills_df`) and the `required_skills_for_occupation` based on the selected target occupation.

### 4.2 Calculation Flow

The core calculation logic is triggered by a `st.button("Calculate AI-Readiness Score")`. This ensures that calculations are performed only when explicitly requested, preventing unnecessary re-runs as users adjust sliders.

Here's a breakdown of the calculation process within the button's `if` block:

1.  **Calculate $V^R$ Components**:
    *   All individual scores (prompting, tools, education level, years of experience, cognitive flexibility, etc.) are retrieved from `st.session_state` (which holds the current widget values).
    *   Functions from `ai_readiness_functions.py` are called sequentially: `calculate_technical_ai_skills`, `calculate_ai_augmented_productivity`, `calculate_critical_ai_judgment`, `calculate_ai_learning_velocity` to get `s1`, `s2`, `s3`, `s4`.
    *   These `s` values are then used by `calculate_ai_fluency`.
    *   Similarly, `calculate_education_foundation`, `calculate_practical_experience`, `calculate_specialization_depth` lead to `domain_expertise`.
    *   `calculate_adaptive_capacity` is called.
    *   Finally, `calculate_idiosyncratic_readiness` combines AI-Fluency, Domain-Expertise, and Adaptive-Capacity (with appropriate normalization for the latter) to yield `vr_score`. This `vr_score` is scaled to 0-100.
    *   The raw 0-1 scaled AI-Fluency, Domain-Expertise, and Adaptive-Capacity are stored in `st.session_state` as `current_ai_fluency`, `current_domain_expertise`, `current_adaptive_capacity` for use in the Pathway Simulation.

2.  **Calculate $H^R$ Components**:
    *   Data specific to the `target_occupation` is extracted from `st.session_state.occupational_data_df`.
    *   `ai_enhancement_potential`, `job_growth_projection`, `wage_premium`, `entry_accessibility` are calculated.
    *   These feed into `calculate_base_opportunity_score`.
    *   `calculate_growth_multiplier` and `calculate_regional_multiplier` are called using the user-defined `lambda_val` and `gamma_val`.
    *   Finally, `calculate_systematic_opportunity` combines these to get `hr_score`, also scaled to 0-100.

3.  **Calculate Synergy**:
    *   `calculate_skills_match_score` compares the user's skills (`st.session_state.user_skills_data`) with the `required_skills_for_occupation`.
    *   `calculate_timing_factor` uses `years_experience`.
    *   `calculate_alignment_factor` combines `skills_match_score`, `max_possible_skills_match`, and `timing_factor`.
    *   `calculate_synergy_percentage` uses `vr_score`, `hr_score`, and `alignment_factor`.

4.  **Calculate Final AI-R Score**:
    *   `calculate_ai_readiness_score` uses `vr_score`, `hr_score`, `synergy_percentage`, `alpha`, and `beta` to produce the `ai_r_score`.

All calculated scores are stored in `st.session_state` so they can be displayed and accessed by other pages (like the Pathway Simulation).

**Flowchart for AI-Readiness Score Calculation:**

```mermaid
graph TD
    A[Start Calculation] --> B{Retrieve User Inputs <br> (VR, HR, Synergy parameters)}
    B --> C1[Calculate AI-Fluency]
    B --> C2[Calculate Domain-Expertise]
    B --> C3[Calculate Adaptive-Capacity]
    C1 --> D1[Combine into Idiosyncratic Readiness (VR)]
    C2 --> D1
    C3 --> D1

    B --> E1[Retrieve Occupation Data]
    E1 --> F1[Calculate AI-Enhancement Potential]
    E1 --> F2[Calculate Job Growth Projection]
    E1 --> F3[Calculate Wage Premium]
    E1 --> F4[Calculate Entry Accessibility]
    F1 --> G1[Calculate Base Opportunity Score]
    F2 --> G1
    F3 --> G1
    F4 --> G1

    B --> G2[Calculate Growth Multiplier]
    B --> G3[Calculate Regional Multiplier]

    G1 --> H1[Combine into Systematic Opportunity (HR)]
    G2 --> H1
    G3 --> H1

    B --> I1[Calculate Skills Match Score]
    B --> I2[Calculate Timing Factor]
    I1 --> J1[Calculate Alignment Factor]
    I2 --> J1
    J1 --> K1[Calculate Synergy Percentage]
    D1 --> K1
    H1 --> K1

    D1 --> L[Calculate Final AI-Readiness Score]
    H1 --> L
    K1 --> L
    L --> M[Display Results & Visualizations]
    M --> N[End]
```

### 4.3 Visualizations

After calculation, the page displays the main `vr_score`, `hr_score`, `synergy_percentage`, and `ai_r_score` using `st.metric`. Plotly Express is used to generate two informative charts:

*   **Pie Chart for $V^R$ Components**: Shows the proportional contribution of AI-Fluency, Domain-Expertise, and Adaptive-Capacity to the overall `vr_score`.
*   **Bar Chart for $H^R$ Base Components**: Illustrates the individual scores of AI-Enhancement Potential, Job Growth Projection, Wage Premium, and Entry Accessibility.

**Code Snippet (`page2.py`):**
```python
# Display Results
if "ai_r_score" in st.session_state:
    st.subheader("Calculated AI-Readiness Score")
    col_res1, col_res2, col_res3, col_res4 = st.columns(4)
    col_res1.metric("Idiosyncratic Readiness (V^R)", f"{st.session_state.vr_score:.2f}")
    col_res2.metric("Systematic Opportunity (H^R)", f"{st.session_state.hr_score:.2f}")
    col_res3.metric("Synergy %", f"{st.session_state.synergy_percentage:.2f}")
    col_res4.metric("Overall AI-Readiness Score (AI-R)", f"{st.session_state.ai_r_score:.2f}")

    st.subheader("Visualizations")
    # Pie chart for VR components
    vr_components_data = {'Component': ['AI-Fluency', 'Domain-Expertise', 'Adaptive-Capacity'],
                          'Score': [st.session_state.ai_fluency_normalized,
                                    st.session_state.domain_expertise_normalized,
                                    st.session_state.adaptive_capacity_normalized]}
    vr_components_df = pd.DataFrame(vr_components_data)

    fig_vr_pie = px.pie(vr_components_df, values='Score', names='Component',
                        title='Contribution to Idiosyncratic Readiness (V^R)')
    st.plotly_chart(fig_vr_pie, use_container_width=True)

    # Bar chart for HR base components
    # ... (recalculation and plot for HR components)
```

## 5. Developing the Pathway Simulation Feature
Duration: 0:15

The "Pathway Simulation" page (`application_pages/page3.py`) is a powerful feature for dynamic "what-if" scenario planning. It allows users to assess how investing in specific learning pathways might alter their individual capabilities ($V^R$) and, consequently, their overall AI-Readiness Score.

### 5.1 Pathway Selection and Completion Parameters

Users can select a learning pathway from a dropdown list, which is populated from `st.session_state.learning_pathways_df`. Additionally, `st.slider` widgets allow specifying a "Pathway Completion Score" and "Pathway Mastery Score," simulating partial completion or varying levels of learning effectiveness.

**Code Snippet (`page3.py`):**
```python
with st.expander("Learning Pathway Inputs", expanded=True):
    st.session_state.selected_pathway_name = st.selectbox(
        label="Select Learning Pathway",
        options=st.session_state.learning_pathways_df['pathway_name'].tolist(),
        index=st.session_state.learning_pathways_df['pathway_name'].tolist().index(st.session_state.selected_pathway_name),
        help="Simulate the impact of completing a learning pathway on your AI-Readiness Score."
    )

    st.session_state.pathway_completion_score = st.slider(
        label="Pathway Completion Score",
        min_value=0.0, max_value=1.0, value=st.session_state.pathway_completion_score, step=0.05,
        help="Score representing the percentage of the pathway completed."
    )

    st.session_state.pathway_mastery_score = st.slider(
        label="Pathway Mastery Score",
        min_value=0.0, max_value=1.0, value=st.session_state.pathway_mastery_score, step=0.05,
        help="Score representing the level of mastery achieved in the pathway."
    )
```

### 5.2 Simulation Logic

When the "Simulate Pathway Impact" button is clicked, the application performs the following steps:

1.  **Retrieve Current Scores**: It fetches the *current* `vr_score`, `hr_score`, `synergy_percentage`, and `ai_r_score` from `st.session_state`. This is why it's recommended to calculate the base score on Page 2 first. It also retrieves the 0-1 scaled `current_ai_fluency`, `current_domain_expertise`, and `current_adaptive_capacity` from session state.

2.  **Apply Pathway Impact**:
    *   The `selected_pathway` data (which contains `impact_ai_fluency`, `impact_domain_expertise`, `impact_adaptive_capacity` values) is retrieved from `learning_pathways_df`.
    *   The `simulate_pathway_impact` function (from `ai_readiness_functions.py`) is called. This function takes the current component scores, the pathway's impact, and the completion/mastery scores to calculate *projected* new scores for AI-Fluency, Domain-Expertise, and Adaptive-Capacity. The impact is capped at a maximum of 1.0 for each component.

    **Code Snippet (`ai_readiness_functions.py`):**
    ```python
    # Pathway Simulation
    def simulate_pathway_impact(current_ai_fluency, current_domain_expertise, current_adaptive_capacity, impact_ai_fluency, impact_domain_expertise, impact_adaptive_capacity, completion_score=1.0, mastery_score=1.0):
        ai_fluency = current_ai_fluency + impact_ai_fluency * completion_score * mastery_score
        domain_expertise = current_domain_expertise + impact_domain_expertise * completion_score * mastery_score
        adaptive_capacity = current_adaptive_capacity + impact_adaptive_capacity * completion_score * mastery_score

        ai_fluency = min(ai_fluency, 1.0) # Cap at 1.0
        domain_expertise = min(domain_expertise, 1.0)
        adaptive_capacity = min(adaptive_capacity, 1.0)

        return ai_fluency, domain_expertise, adaptive_capacity
    ```

3.  **Recalculate Derived Scores**:
    *   Using the `new_ai_fluency_0_1`, `new_domain_expertise_0_1`, `new_adaptive_capacity_0_1` from the simulation, `calculate_idiosyncratic_readiness` is called again to get the `new_vr_score`.
    *   The `hr_score` typically remains unchanged by an individual learning pathway, so `current_hr_score` is used as `new_hr_score`.
    *   `calculate_skills_match_score`, `calculate_timing_factor`, `calculate_alignment_factor`, and `calculate_synergy_percentage` are re-run using the `new_vr_score` and `current_hr_score` to determine `new_synergy_percentage`.
    *   Finally, `calculate_ai_readiness_score` is called with the `new_vr_score`, `new_hr_score`, `new_synergy_percentage`, and the global `alpha` and `beta` values to get the `new_ai_r_score`.

All new, projected scores are stored in `st.session_state` for display.

### 5.3 Comparison Visualizations

The page utilizes Plotly `go.Figure` with `go.Bar` traces to visually compare the "Current" (pre-simulation) and "Projected" (post-simulation) scores:

*   **Overall Scores Comparison**: A bar chart comparing current vs. projected AI-R, $V^R$, $H^R$, and Synergy % scores.
*   **$V^R$ Sub-Components Comparison**: Another bar chart specifically showing the impact of the pathway on AI-Fluency, Domain-Expertise, and Adaptive-Capacity.

**Code Snippet (`page3.py`):**
```python
if st.session_state.simulation_run:
    st.subheader("Current vs. Projected AI-Readiness Scores")

    metrics_data = {
        "Metric": ["AI-R Score", "V^R Score", "H^R Score", "Synergy %"],
        "Current": [
            st.session_state.ai_r_score,
            st.session_state.vr_score,
            st.session_state.hr_score,
            st.session_state.synergy_percentage,
        ],
        "Projected": [
            st.session_state.new_ai_r_score,
            st.session_state.new_vr_score,
            st.session_state.new_hr_score,
            st.session_state.new_synergy_percentage,
        ],
    }
    metrics_df = pd.DataFrame(metrics_data)

    fig_comparison = go.Figure()
    fig_comparison.add_trace(go.Bar(name='Current', x=metrics_df['Metric'], y=metrics_df['Current']))
    fig_comparison.add_trace(go.Bar(name='Projected', x=metrics_df['Metric'], y=metrics_df['Projected']))

    fig_comparison.update_layout(barmode='group', title='Comparison: Current vs. Projected Scores')
    st.plotly_chart(fig_comparison, use_container_width=True)

    # ... (similar code for VR sub-components comparison)
```

<aside class="positive">
The use of `st.session_state` to pass calculated scores between pages is a fundamental pattern for multi-page Streamlit applications. It creates a coherent user experience by allowing state to persist.
</aside>

## 6. Extending and Customizing the Application
Duration: 0:10

This application provides a solid foundation for understanding and interacting with the AI-Readiness framework. Here are some ideas for how developers can extend and customize it further:

### 6.1 Enhancing Data Management

*   **User Profile Management**: Implement a backend (e.g., SQLite, PostgreSQL) to allow users to save and load their individual profiles, including skills and calculated scores. This would eliminate the need to re-enter data after each session.
*   **Dynamic Skill Editing**: Currently, individual skills are displayed from a static DataFrame. Enhance the "Synergy Inputs" section on Page 2 to allow users to add, edit, or remove their skills and assign scores, which would directly impact the `calculate_skills_match_score`.
*   **External Data Integration**: Integrate with real-time job market APIs (e.g., LinkedIn API, government labor statistics) to fetch dynamic `occupational_data` (job postings, wage premiums, growth rates) instead of relying solely on synthetic data.
*   **Learning Pathway Database**: Expand `learning_pathways_df` to include more detailed information about each pathway, such as estimated time investment, prerequisites, and specific skills gained, enabling more granular simulation.

### 6.2 Refining the Calculation Models

*   **Advanced Weighting Schemes**: Introduce more sophisticated methods for determining the weights ($\alpha, \beta, w_1, w_2, w_3$, etc.), perhaps through user preferences, machine learning models, or expert system rules.
*   **Time-Series Analysis**: Extend the `simulate_pathway_impact` to consider impact over multiple time steps or with compounding effects, modeling career growth paths more realistically.
*   **Feedback Loops**: Implement mechanisms where the system suggests optimal learning pathways or career transitions based on the user's current profile and desired target occupations.
*   **Uncertainty Quantification**: Incorporate probabilistic models to reflect the inherent uncertainties in skill development, job growth, or market trends, providing a range of possible AI-R scores rather than single point estimates.

### 6.3 Expanding User Interface and Experience

*   **Interactive Skill Editor**: For the "Your Individual Skills" section on Page 2, consider using `st.experimental_data_editor` to allow direct editing of skills within the DataFrame.
*   **Visualizations**: Add more interactive charts, such as a radar chart for comparing $V^R$ sub-components or a scatter plot to show career pathways in a 2D opportunity/readiness space.
*   **User Onboarding**: Implement a guided onboarding process for new users to explain the framework and how to use the application effectively.
*   **Multilingual Support**: Allow the application to be used in different languages.

### 6.4 Contribution Guidelines

To contribute to a project like this:

1.  **Fork the Repository**: Make a copy of the project to your GitHub account.
2.  **Create a New Branch**: For each new feature or bug fix, create a new branch.
    ```bash
    git checkout -b feature/my-new-feature
    ```
3.  **Implement Changes**: Make your code changes, adhering to the existing coding style.
4.  **Test Thoroughly**: Ensure your changes don't introduce regressions and that new features work as expected.
5.  **Commit Your Changes**: Write clear and concise commit messages.
    ```bash
    git commit -m "feat: Add user profile saving functionality"
    ```
6.  **Push to Your Fork**:
    ```bash
    git push origin feature/my-new-feature
    ```
7.  **Open a Pull Request**: Submit a pull request to the main repository, explaining your changes and their benefits.

<aside class="positive">
When extending, remember the modular design. Keep calculation logic in `ai_readiness_functions.py` and UI elements specific to their respective `pageX.py` files. This separation of concerns makes the application easier to maintain and scale.
</aside>
