id: 68f63eb9833967484a12dd11_user_guide
summary: AI-Readiness score - GPT-5 User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Exploring Your AI Career Readiness with QuLab

## Introduction to the AI-Readiness Framework
Duration: 05:00

Welcome to the QuLab! In today's rapidly evolving job market, understanding your readiness for an AI-driven career is more critical than ever. This application provides a structured, data-driven framework to help you explore and simulate your **AI-Readiness Score (AI-R)**.

The core idea is that true readiness isn't just about one skill; it's a blend of your individual capabilities, the opportunities available in the market, and the synergy between the two. The application quantifies this through a central formula:

$$ AI\text{-}R_{i,t} = \alpha\, V^R_i(t) + (1-\alpha)\, H^R_i(t) + \beta\, \text{Synergy}\% $$

Let's break down what these components mean:

*   **$V^R$ (Idiosyncratic Readiness):** This is all about **you**. It measures your personal capabilities across three key areas:
    *   **AI-Fluency:** Your practical skills in using AI tools, your ability to judge AI outputs critically, and how quickly you can learn new AI concepts.
    *   **Domain-Expertise:** Your foundational knowledge, practical experience, and specialized credentials in your chosen field.
    *   **Adaptive-Capacity:** Your ability to adapt to change, manage your career strategically, and collaborate effectively in a dynamic environment.

*   **$H^R$ (Systematic Opportunity):** This is about the **job market**. It evaluates the attractiveness of a specific career path by considering factors like:
    *   How much the role is enhanced by AI.
    *   Projected job growth and wage premiums for AI-skilled professionals.
    *   How accessible the career is in terms of required education and experience.

*   **Synergy%:** This is a bonus that rewards **alignment**. Your score gets a boost when your unique skills ($V^R$) are a great match for the requirements of a high-opportunity job ($H^R$) at the right time in your career.

In this codelab, you will learn how to use the QuLab to input your personal profile, analyze your scores, and simulate how different learning pathways could improve your AI-Readiness.

## Navigating the Application & Global Parameters
Duration: 03:00

The application is organized into three main pages, which you can select from the **Navigation** dropdown in the sidebar on the left.

1.  **Overview & Inputs:** This is where you'll start. You'll enter all the data about yourself and your target career.
2.  **Scores & Insights:** After calculating, you'll come here to see detailed visualizations and breakdowns of your scores.
3.  **Pathway Simulation:** This page allows you to perform "what-if" analysis to see how completing a learning program could impact your AI-R score.

### Global Parameters

Below the navigation menu, you will find the **Global Parameters**. These two sliders allow you to adjust the core weights in the AI-Readiness formula, tailoring the model to your personal career philosophy.

*   **Weight on Individual Factors ($\alpha$):** This slider determines the balance between your personal readiness ($V^R$) and market opportunity ($H^R$).
    *   A **higher $\alpha$** (e.g., 0.8) means your final score is mostly determined by your personal skills and capabilities.
    *   A **lower $\alpha$** (e.g., 0.3) places more emphasis on the attractiveness of the job market you are targeting.

*   **Synergy Coefficient ($\beta$):** This slider controls the magnitude of the bonus you receive for strong alignment between your skills and job requirements. A higher $\beta$ means that having a perfect skill match for a role will have a more significant positive impact on your overall AI-R score.

<aside class="positive">
<b>Tip:</b> For this codelab, you can leave the global parameters at their default values. As you get more familiar with the concepts, feel free to experiment with them to see how they influence your score.
</aside>

## Calculating Your Baseline Score
Duration: 15:00

Let's begin by calculating your initial AI-Readiness Score. Navigate to the **Overview & Inputs** page. This page is organized into sections that correspond to the main components of the AI-R formula.

### Idiosyncratic Readiness ($V^R$) Inputs

This is the most detailed section, where you define your personal profile. The inputs are grouped into three expandable sections: AI-Fluency, Domain-Expertise, and Adaptive-Capacity.

1.  **AI-Fluency:** This measures your practical ability to work with and alongside AI.
    *   **Technical Skills ($S_{i,1}$):** Use the first four sliders (`Prompting Score`, `Tools Score`, etc.) to rate your technical competency.
    *   **AI-Augmented Productivity ($S_{i,2}$):** Use the next set of inputs to estimate how much more effective AI makes you. For a given task, how does the quality and time-to-complete change when you use AI versus when you don't?
    *   **Critical AI Judgment ($S_{i,3}$):** These inputs quantify your ability to critically evaluate AI outputs—catching errors and knowing when to trust the AI.
    *   **AI Learning Velocity ($S_{i,4}$):** This measures how quickly you learn. How much has your proficiency changed (`Delta Proficiency`) given a certain number of hours invested in learning (`Delta T Hours Invested`)?

2.  **Domain-Expertise:** This captures your knowledge and experience in your professional field. Adjust the sliders for your `Education Level`, `Years Experience`, `Portfolio Score`, and other credentials.

3.  **Adaptive-Capacity:** This reflects your "soft skills" that are crucial in a changing world. Rate your `Cognitive Flexibility`, `Social-Emotional Intelligence`, and `Strategic Career Management`.

### Systematic Opportunity ($H^R$) Inputs

Here, you define the market conditions you want to be measured against.

1.  Use the **Target Occupation** dropdown to select a career path that interests you, for example, 'Data Analyst with AI Skills'. The application's data for this role will be used to calculate your opportunity score.
2.  The `lambda` and `gamma` sliders are advanced parameters that control how market volatility and regional demand are weighted. You can leave them at their defaults for now.

### Synergy Inputs

This section measures the alignment between your skills and the requirements of your target occupation.

1.  The app displays a table of **Required skills** for the occupation you selected.
2.  Below that, you'll find an editable table of **Your skills**. You can add new skills, update your scores (on a 0-100 scale), or remove skills to accurately reflect your current abilities.
3.  The application will compare these two tables to calculate your **Skills Match Score**.

### Calculate Your Score

Once you have adjusted the inputs across all sections to best represent your profile, scroll to the bottom of the page and click the large blue **Calculate AI-Readiness** button.

A success message will appear, and you will see your four primary scores displayed as metrics.

## Understanding Your Scores
Duration: 10:00

Now that you have a baseline score, navigate to the **Scores & Insights** page using the sidebar. This page is dedicated to helping you visualize and interpret your results.

At the top of the page, you'll see the four key metrics:
*   **V^R (Idiosyncratic Readiness):** Your personal capability score (0-100).
*   **H^R (Systematic Opportunity):** The market opportunity score for your chosen role (0-100).
*   **Synergy %:** The alignment bonus you received.
*   **AI-R Score:** Your final, combined AI-Readiness Score.

Below these metrics, you will find several charts designed to give you deeper insights.

1.  **V^R Composition Chart:** This chart is incredibly valuable. It breaks down your $V^R$ score into its three core pillars: AI-Fluency, Domain-Expertise, and Adaptive-Capacity. This immediately shows you where your strengths lie and which areas offer the most room for improvement. For example, you might have strong Domain-Expertise but a lower AI-Fluency, indicating a clear area for upskilling.

2.  **H_base Components Chart:** This chart breaks down the market opportunity score ($H^R$) *before* market multipliers are applied. It shows you the relative strength of the selected occupation in terms of AI Enhancement, Job Growth, Wage Premium, and Entry Accessibility. This helps you understand *why* a certain career path is considered a high or low opportunity.

<aside class="positive">
<b>For a Deeper Dive:</b> If you are curious about the specific numbers behind the charts, expand the "Detailed Numbers" section at the bottom of the page. This will show you the precise values for all the calculated sub-components.
</aside>

## Simulating Your Future
Duration: 07:00

Knowledge of your current score is useful, but the real power comes from planning for the future. The **Pathway Simulation** page is a "what-if" tool that allows you to see how specific learning activities could impact your AI-Readiness.

1.  Navigate to the **Pathway Simulation** page from the sidebar.
2.  Use the **Select Learning Pathway** dropdown to choose a program you are considering, such as 'Prompt Engineering Fundamentals'. Each pathway is designed to impact different components of your $V^R$.
3.  Use the **Pathway Completion Score** and **Pathway Mastery Score** sliders to simulate your expected performance in the program. A score of 1.0 on both means you complete the entire pathway and master its content fully.

As you adjust the sliders, the charts and metrics on the page will update in real-time.

*   **Comparison Chart:** The main bar chart shows your **Current** scores versus your **Projected** scores after completing the pathway. You can immediately see the potential uplift in your $V^R$, Synergy%, and overall AI-R score.
*   **Projected Metrics:** The metric boxes provide a clear numerical summary of the projected changes.

This tool is designed to help you make informed decisions about your upskilling journey. By simulating different pathways, you can identify which learning opportunities will provide the most significant boost to your AI career readiness.

## Conclusion
Duration: 02:00

Congratulations! You have successfully used the QuLab to calculate, analyze, and simulate your AI-Readiness Score.

You have learned how to:
*   Understand the core components of AI-Readiness: $V^R$, $H^R$, and Synergy.
*   Input your personal and professional profile to calculate a baseline score.
*   Interpret the results using insightful visualizations to identify strengths and areas for improvement.
*   Simulate the impact of future learning to make data-driven career development decisions.

The true power of this tool lies in experimentation. We encourage you to go back to the **Overview & Inputs** page and continue exploring. How does your score change if you target a different occupation? What if you improve your portfolio? Which learning pathway gives you the biggest return on investment?

Use the QuLab as your personal navigator to strategically plan your career in the exciting age of AI.
