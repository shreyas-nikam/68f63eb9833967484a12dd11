id: 68f63eb9833967484a12dd11_user_guide
summary: AI-Readiness score - GPT-5 User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# AI Career Navigator & Pathway Planner: Understanding Your AI-Readiness

## 1. Welcome to the AI-Readiness Lab: Your Personal Career Compass
Duration: 0:05

Welcome to the AI Career Navigator & Pathway Planner, an interactive application designed to help you understand and simulate your "AI-Readiness" using a unique framework. In today's rapidly evolving job market, understanding your preparedness for AI-enabled roles is crucial for career planning and skill development. This application provides a quantitative approach to assess your current standing and explore potential future pathways.

This codelab will guide you through the application's core functionalities, explaining the concepts behind the AI-Readiness Score and how you can leverage this tool to make informed career decisions.

The application revolves around the AI-Readiness score ($AI\text{-}R$), which quantifies your preparedness for AI-enabled careers by combining three main factors:
1.  **Idiosyncratic Readiness ($V^R$):** Your individual capabilities, skills, and adaptive traits.
2.  **Systematic Opportunity ($H^R$):** The attractiveness and accessibility of a specific AI-enabled role in the labor market.
3.  **Synergy (%):** The alignment and fit between your individual capabilities and the requirements of the target occupation.

The core formula for calculating your AI-Readiness ($AI\text{-}R$) is:
$$AI\text{-}R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R)$$

Here, $\alpha$ and $\beta$ are weighting coefficients that allow you to adjust the relative importance of individual readiness, market opportunity, and synergy.

The application is structured into three main pages, each serving a distinct purpose:
*   **Page 1 - Overview:** Introduces the framework, concepts, and underlying data.
*   **Page 2 - AI-R Calculator:** Allows you to input your profile details, select an occupation, and calculate your AI-Readiness score.
*   **Page 3 - Pathways & Scenarios:** Enables you to simulate the impact of various learning pathways on your AI-Readiness.

Let's begin by exploring the Overview page to get a foundational understanding of the AI-Readiness framework.

## 2. Exploring the Overview Page
Duration: 0:05

Navigate to **"Page 1 - Overview"** using the sidebar navigation on the left.

This page serves as an introduction to the AI-Readiness framework, providing context and outlining the core principles. It reiterates the fundamental formula and intuitively explains what each component represents:

*   $V^R$: Combines your **AI-Fluency**, **Domain-Expertise**, and **Adaptive-Capacity**. Think of it as your personal toolkit for an AI-driven world.
*   $H^R$: Considers factors like the **AI-Enhancement** of a role, **job growth**, **wage premium**, and **entry accessibility**. This represents the external pull from the job market.
*   Synergy%: This factor acts as a multiplier, boosting your score when your unique skills strongly align with the requirements of your chosen occupation, especially when coupled with relevant experience (timing).

The "Business Value" section highlights how this tool can help you diagnose your current readiness, test "what-if" scenarios for learning, and compare different occupations.

<aside class="positive">
<b>Tip:</b> Take a moment to read through the initial markdown on this page to grasp the foundational concepts before proceeding.
</aside>

Below the initial explanations, you'll find an expandable section titled "Show Synthetic Datasets". Expand this section to view the sample data that populates the application:

*   **Individual Profile:** Contains a hypothetical user's current scores for various attributes, which will be editable later.
*   **Individual Skills:** A list of skills held by the hypothetical user, also editable.
*   **Occupational Data:** A list of various AI-enabled occupations along with their market characteristics.
*   **Occupation Required Skills:** Specific skills needed for certain occupations.
*   **Learning Pathways:** A set of predefined learning programs and their potential impact on your capabilities.

These datasets provide the initial values for all calculations within the application. Don't worry about memorizing them, but understand that they represent the data the application uses to quantify readiness and opportunity.

Finally, the page concludes with a "Job Growth Rate by Occupation" bar chart. This visualization offers a quick insight into one of the key components of market opportunity ($H^R$) across different occupations, illustrating which roles are projected to grow faster.

## 3. Understanding Idiosyncratic Readiness ($V^R$)
Duration: 0:15

Now, switch to **"Page 2 - AI-R Calculator"** using the sidebar navigation.

This page is where you'll actively engage with the AI-Readiness model. The first major section focuses on **Idiosyncratic Readiness ($V^R$)**, representing *your* unique capabilities and attributes. It is composed of three main pillars: AI-Fluency, Domain-Expertise, and Adaptive-Capacity.

<aside class="positive">
<b>Tip:</b> As you adjust the sliders and selections on this page, observe how your individual profile inputs might conceptually affect your overall readiness. The actual score will be calculated after you press the "Calculate AI-Readiness" button.
</aside>

Let's explore each tab under "Idiosyncratic Readiness ($V^R$) Inputs":

### AI-Fluency
This tab assesses your practical competence in working with AI. It's broken down into four key sub-components, which you can adjust using the sliders:

*   **Prompting Score, Tools Score, Understanding Score, Datalit Score:** These collectively form your **Technical AI Skills ($S_{i,1}$)**, reflecting your proficiency in using AI, interacting with it effectively, and understanding its implications.
*   **Output Quality with/without AI, Time with/without AI:** These inputs contribute to your **AI-Augmented Productivity ($S_{i,2}$)**, measuring how much AI enhances your efficiency and the quality of your work.
*   **Errors Caught, Total AI Errors, Appropriate Trust Decisions, Total Decisions:** These define your **Critical AI Judgment ($S_{i,3}$)**, evaluating your ability to discern and correct AI mistakes, and to appropriately trust or distrust AI outputs.
*   **Delta Proficiency, Delta T Hours Invested:** These measure your **AI Learning Velocity ($S_{i,4}$)**, indicating how quickly you acquire new AI-related skills relative to the effort invested.

Adjust these sliders to reflect your current or desired levels for each aspect of AI-Fluency.

### Domain-Expertise
This tab focuses on your knowledge and experience within a specific field.

*   **Education Level:** Your formal academic background forms the **Education Foundation ($E_{education}$)**. A higher education level generally contributes more.
*   **Years Experience:** Your professional tenure contributes to **Practical Experience ($E_{experience}$)**. More years of experience generally mean deeper expertise.
*   **Portfolio Score, Recognition Score, Credentials Score:** These represent your **Specialization Depth ($E_{specialization}$)**, reflecting tangible achievements, professional recognition, and certifications in your field.

Modify these inputs to accurately represent your domain knowledge.

### Adaptive-Capacity
This tab evaluates your ability to navigate change and learn new things, essential qualities in a dynamic AI-driven landscape.

*   **Cognitive Flexibility:** Your ability to adjust thinking and problem-solving approaches.
*   **Social-Emotional Intelligence:** Your capacity to understand and manage emotions, both your own and others', crucial for human-AI collaboration.
*   **Strategic Career Management:** Your foresight and planning in steering your career path amidst technological shifts.

Adjust these sliders (values are out of 100) to reflect your adaptability. These scores are averaged to contribute to your overall Adaptive-Capacity.

By adjusting these inputs, you are defining your unique individual profile, which is the foundation of your $V^R$ score.

## 4. Analyzing Systematic Opportunity ($H^R$)
Duration: 0:10

Still on **"Page 2 - AI-R Calculator"**, let's move to the "Systematic Opportunity ($H^R$) Inputs" section.

**Systematic Opportunity ($H^R$)** represents the attractiveness and accessibility of an AI-enabled role in the labor market, independent of your individual skills. It's about the "market fit" of a particular occupation.

*   **Target Occupation:** This is the most crucial input for $H^R$. Use the dropdown to select an occupation you are interested in. The application will then pull all relevant market data for this specific role from the "Occupational Data" dataset. This selection dictates the values used for the $H^R$ calculation.

<aside class="positive">
<b>Tip:</b> Experiment with different occupations to see how the market opportunity component of your AI-Readiness might change.
</aside>

The market opportunity for an occupation is calculated based on several factors:
*   **AI-Enhancement Potential:** How much AI can augment and improve productivity within this role.
*   **Job Growth Projection:** The anticipated growth rate of this occupation.
*   **Wage Premium:** The additional salary typically earned by AI-skilled professionals in this role compared to their non-AI counterparts.
*   **Entry Accessibility:** How easy or difficult it is to enter this profession based on educational and experience requirements.

These factors combine to form a *base opportunity score*. This base score is then adjusted by two multipliers:

*   **Lambda value for Growth Multiplier ($\lambda$):** This parameter (adjustable via slider) helps to smooth out or dampen the impact of fluctuations in job posting growth. A higher $\lambda$ means recent growth patterns have a stronger influence on the opportunity score.
*   **Gamma value for Regional Multiplier ($\gamma$):** This parameter (adjustable via slider) allows you to weigh the influence of local vs. national demand, along with remote work opportunities. A higher $\gamma$ means local market conditions and remote work flexibility have a stronger impact on the opportunity.

Adjust $\lambda$ and $\gamma$ to understand how these dynamics influence the overall market opportunity for your chosen occupation.

## 5. Grasping Synergy and Skill Alignment
Duration: 0:10

Continuing on **"Page 2 - AI-R Calculator"**, scroll down to the "Synergy Inputs" section.

**Synergy (%)** captures the alignment between your individual skills and the specific skills required for your chosen occupation. It's not just about having skills, but having the *right* skills for the *right* job. A strong synergy boosts your overall AI-Readiness.

This section provides two important views and an adjustable parameter:

1.  **Required Skills (selected occupation):** This table displays the key skills, their required proficiency scores, and their importance weight for the **target occupation** you selected in the $H^R$ section. This helps you understand what the market specifically demands.

2.  **Your Skills (editable):** This is a dynamic table where you can view, add, edit, or delete your individual skills and their corresponding proficiency scores.
    *   Click on a cell to edit a skill name or score.
    *   Use the "Add row" button to introduce new skills you possess.
    *   This direct interaction allows you to see how improving or acquiring specific skills for an occupation impacts your alignment.

    <aside class="positive">
    <b>Tip:</b> Try adding skills that are listed in the "Required Skills" table for your chosen occupation, or increasing your score for existing matching skills. Observe how this might conceptually improve your synergy.
    </aside>

3.  **Max Possible Skills Match:** This numerical input acts as a scaling factor for the skill alignment calculation. It represents the ideal or maximum possible score one could achieve in skills matching. It helps normalize the `skills_match_score` for the alignment factor.

The synergy calculation also considers a **Timing Factor** which is based on your "Years Experience" (from the Domain-Expertise tab). Generally, more experience can lead to a higher timing factor, implying a more opportune moment for transition or leveraging skills.

## 6. Calculating and Interpreting Your AI-Readiness Score
Duration: 0:10

You're still on **"Page 2 - AI-R Calculator"**. Before calculating, let's briefly look at the "Global Parameters" at the very top of the page.

*   **Weight on Individual Factors ($\alpha$):** This slider allows you to determine how much importance is given to your individual capabilities ($V^R$) versus market opportunity ($H^R$) in the final AI-Readiness score. A higher $\alpha$ means your personal skills matter more, while a lower $\alpha$ emphasizes market trends.
*   **Synergy Coefficient ($\beta$):** This slider controls how much the Synergy component boosts your overall AI-Readiness. A higher $\beta$ means that strong alignment between your skills and market needs will have a more significant positive impact.

Adjust these parameters to reflect your personal career philosophy or strategic focus (e.g., are you prioritizing personal growth or market demand?).

Now that you've reviewed all the inputs, click the **"Calculate AI-Readiness"** button (primary button).

The application will process all your inputs and display your results:

### Score Gauges
Four prominent gauges will appear:
*   **$V^R$ (Idiosyncratic):** Your individual readiness score (0-100).
*   **$H^R$ (Systematic):** The market opportunity score for your selected occupation (0-100).
*   **Synergy %:** The percentage representing the alignment between your skills and the occupation's requirements (0-100).
*   **AI-R Score:** Your final, combined AI-Readiness score (0-100).

Higher scores generally indicate greater preparedness and opportunity.

### Component Breakdowns
Below the gauges, you'll find detailed breakdowns that provide insights into how your $V^R$ and $H^R$ scores were derived:

*   **$V^R$ Component Contribution (0-100) (Pie Chart):** This chart shows the relative contribution of your AI-Fluency, Domain-Expertise, and Adaptive-Capacity to your overall $V^R$ score. This helps you identify your strongest areas and potential areas for improvement.
*   **$H\text{_}base$ Components (scaled to 0-100) (Bar Chart):** This chart visualizes the contribution of AI-Enhancement, Job Growth, Wage Premium, and Entry Accessibility to the *base* market opportunity score before multipliers are applied. This helps you understand which market factors are most influential for your chosen occupation.

<aside class="positive">
<b>Key Takeaway:</b> The AI-R score provides a single number, but the component breakdowns offer actionable insights. If your $V^R$ is low, look at its components. If $H^R$ is low, reconsider the occupation or market dynamics. If Synergy is low, focus on relevant skill development.
</aside>

## 7. Simulating Pathways and Scenarios
Duration: 0:10

Finally, navigate to **"Page 3 - Pathways & Scenarios"** using the sidebar navigation.

This page allows you to perform "what-if" analyses, simulating the impact of investing in learning and development on your AI-Readiness. This is a powerful feature for career planning, as it helps you visualize the potential returns on your educational investments.

### Select Learning Pathway
*   **Select Learning Pathway:** Choose a pathway from the dropdown menu (e.g., "Prompt Engineering Fundamentals", "AI for Financial Analysis"). Each pathway is designed to improve specific aspects of your AI-Fluency, Domain-Expertise, or Adaptive-Capacity.
*   **Pathway Completion Score:** This slider allows you to simulate how much of the pathway you successfully complete (0.0 to 1.0).
*   **Pathway Mastery Score:** This slider represents the level of proficiency you achieve upon completing the pathway (0.0 to 1.0).

<aside class="negative">
<b>Important:</b> For this simulation to be accurate, it is highly recommended to run the "AI-Readiness Calculator" (Page 2) first. If you haven't, the simulation will use default baseline values, which might not reflect your personalized profile.
</aside>

### Simulate
After selecting a pathway and adjusting its completion and mastery, click the **"Simulate"** button (primary button).

The application will then calculate your projected AI-Readiness scores after completing the pathway and display the results in a "Current vs Projected Scores" bar chart:

*   **Current vs Projected Scores (Bar Chart):** This chart visually compares your baseline scores ($V^R$, $H^R$, Synergy%, and $AI\text{-}R$) with the scores projected after completing the chosen learning pathway.
    *   You'll likely see an increase in your projected $V^R$ score, as learning pathways typically enhance your individual capabilities.
    *   This increase in $V^R$ will often lead to a higher Synergy% (assuming your skills alignment improves for the target occupation).
    *   The $H^R$ score generally remains unchanged in these simulations, as the market opportunity for an occupation doesn't typically change with individual learning.
    *   The combined effect will be a change in your overall $AI\text{-}R$ score, indicating the impact of your learning investment.

<aside class="positive">
<b>Explore and Plan:</b> Use this page to test different pathways and their potential impact. This can help you prioritize which skills to develop or which courses to take to maximize your AI-Readiness for your desired career.
</aside>

You have now successfully navigated through all the core functionalities of the AI Career Navigator & Pathway Planner. By understanding your current AI-Readiness, exploring market opportunities, and simulating learning pathways, you are well-equipped to strategically plan your career in the AI era.
