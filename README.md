# QuLab: AI Career Navigator & Pathway Planner

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title: AI-Readiness Score - GPT-5 Lab (QuLab)

## Description

Welcome to QuLab, the AI Career Navigator & Pathway Planner. This interactive Streamlit application provides a comprehensive framework to understand and simulate your **AI-Readiness** using the **AI-R** model. It helps individuals and organizations quantify their preparedness for AI-enabled careers by integrating personal capabilities, market opportunities, and skill alignment.

The application allows users to explore how their unique profile, encompassing idiosyncratic readiness ($V^R$), systematic market opportunities ($H^R$), and their alignment (Synergy%), combine to produce an overall AI-Readiness score. You can test "what-if" scenarios, analyze the impact of learning pathways, and compare your readiness across various AI-enabled occupations.

### Business Logic Overview

The AI-R framework is built upon the following core components:

*   **Idiosyncratic Readiness ($V^R$)**: A composite score reflecting an individual's personal capabilities, calculated from:
    *   **AI-Fluency**: Encompasses Technical AI Skills, AI-Augmented Productivity, Critical AI Judgment, and AI Learning Velocity.
    *   **Domain-Expertise**: Derived from Education Foundation, Practical Experience, and Specialization Depth.
    *   **Adaptive-Capacity**: Based on Cognitive Flexibility, Social-Emotional Intelligence, and Strategic Career Management.

*   **Systematic Opportunity ($H^R$)**: A measure of market attractiveness for a given occupation, considering:
    *   **AI-Enhancement Potential**: How much AI can augment the role.
    *   **Job Growth Projection**: Expected growth rate for the occupation.
    *   **Wage Premium**: The additional earning potential for AI-skilled professionals in that role.
    *   **Entry Accessibility**: Ease of entry based on educational and experience requirements.
    *   Adjusted by **Growth Multiplier** (based on job postings) and **Regional Multiplier** (based on local vs. national demand and remote work).

*   **Synergy%**: Captures the alignment between an individual's skills and the skills required for a chosen occupation, scaled by a timing factor (years of experience). It quantifies how well an individual's unique skill set matches the demands of a target role.

*   **Final AI-Readiness ($AI\text{-}R$)**: The ultimate score, a weighted sum of $V^R$ and $H^R$ with an additional boost from Synergy%, controlled by adjustable parameters $\alpha$ and $\beta$.

The core formula is:
$$AI\text{-}R_{i,t} = \alpha \cdot V^R_i(t) + (1-\alpha) \cdot H^R_i(t) + \beta \cdot \text{Synergy}\%(V^R, H^R)$$

## Features

QuLab provides a multi-page interface to explore different aspects of AI-Readiness:

1.  **Page 1 - Overview**:
    *   Introduction to the AI-Readiness ($AI\text{-}R$) framework, its formula, and business value.
    *   Display of all synthetic datasets used by the application (Individual Profiles, Occupational Data, Learning Pathways, Skills Data).
    *   Visualizations, such as job growth rates by occupation, to provide initial insights.

2.  **Page 2 - AI-R Calculator**:
    *   **Interactive Inputs**: Sliders and select boxes to customize individual capabilities ($V^R$ components like AI-Fluency, Domain-Expertise, Adaptive-Capacity) and select a target occupation for market opportunity ($H^R$).
    *   **Global Parameter Tuning**: Adjust weights for $V^R$ vs. $H^R$ ($\alpha$) and the Synergy Coefficient ($\beta$), as well as growth ($\lambda$) and regional ($\gamma$) multipliers.
    *   **Skill Management**: Edit your individual skills and view required skills for the selected occupation to fine-tune Synergy calculations.
    *   **Dynamic Calculation**: Calculate and instantly visualize your $V^R$, $H^R$, Synergy%, and overall $AI\text{-}R$ scores using interactive gauges.
    *   **Component Breakdowns**: Detailed charts showing the contribution of sub-components to $V^R$ and $H^R$.

3.  **Page 3 - Pathways & Scenarios**:
    *   **Learning Pathway Simulation**: Select from predefined learning pathways and simulate their impact on your skills and scores.
    *   **Completion & Mastery Adjustment**: Control the level of completion and mastery for a pathway to understand incremental benefits.
    *   **What-If Analysis**: Compare your current AI-Readiness scores ($V^R$, $H^R$, Synergy%, $AI\text{-}R$) against projected scores after completing a pathway, displayed via comparative bar charts.
    *   **Baseline Management**: Automatically loads the last calculated scores from the Calculator page or computes a default baseline if none exists.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   `git` (for cloning the repository)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/qu-lab-ai-readiness.git
    cd qu-lab-ai-readiness
    ```
    *(Note: Replace `your-username` with the actual GitHub username/organization if this project is hosted.)*

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install dependencies**:
    Create a `requirements.txt` file in the root directory with the following content:
    ```
    streamlit>=1.0.0
    pandas>=1.0.0
    plotly>=5.0.0
    numpy>=1.0.0
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit application**:
    Ensure your virtual environment is active and you are in the project's root directory (`qu-lab-ai-readiness`).
    ```bash
    streamlit run app.py
    ```

2.  **Access the application**:
    The command above will open the application in your default web browser (usually at `http://localhost:8501`).

3.  **Navigation**:
    Use the sidebar on the left to navigate between the three main pages: "Page 1 - Overview", "Page 2 - AI-R Calculator", and "Page 3 - Pathways & Scenarios".

4.  **Explore and Interact**:
    *   Start with **Page 1 - Overview** to understand the framework and data.
    *   Move to **Page 2 - AI-R Calculator** to input your profile, select an occupation, adjust parameters, and calculate your current AI-Readiness. Make sure to click "Calculate AI-Readiness" to store your results in the session state.
    *   Proceed to **Page 3 - Pathways & Scenarios** to simulate the impact of learning paths on your calculated readiness scores.

## Project Structure

The project is organized into a modular structure for clarity and maintainability:

```
qu-lab-ai-readiness/
├── app.py                      # Main Streamlit application entry point and navigation.
├── requirements.txt            # List of Python dependencies.
└── application_pages/          # Directory containing individual page modules and core logic.
    ├── __init__.py             # Makes application_pages a Python package.
    ├── data_models.py          # Functions to generate initial synthetic dataframes.
    ├── ai_readiness_core.py    # Contains all core calculation functions for AI-R, V^R, H^R, Synergy, and simulation.
    ├── page1.py                # Logic and UI for the "Overview" page.
    ├── page2.py                # Logic and UI for the "AI-R Calculator" page.
    └── page3.py                # Logic and UI for the "Pathways & Scenarios" page.
```

## Technology Stack

*   **Streamlit**: For rapidly building the interactive web application user interface.
*   **Python**: The core programming language used for all business logic and application development.
*   **Pandas**: Essential for data manipulation and handling structured datasets (DataFrames).
*   **Plotly**: Used for creating rich, interactive data visualizations and charts within the Streamlit app.
*   **NumPy**: Provides numerical computing capabilities, often used implicitly by Pandas and other libraries.

## Contributing

Contributions are welcome! If you have suggestions for improvements, find bugs, or want to add new features, please feel free to:

1.  **Fork** the repository.
2.  **Create a new branch** (`git checkout -b feature/AmazingFeature`).
3.  **Commit your changes** (`git commit -m 'Add some AmazingFeature'`).
4.  **Push to the branch** (`git push origin feature/AmazingFeature`).
5.  **Open a Pull Request**.

Please ensure your code adheres to good practices and includes appropriate documentation and tests where applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
*(Note: You will need to create a `LICENSE` file in the root directory if you choose the MIT License or another.)*

## Contact

For any questions or inquiries, please contact:

*   **QuantUniversity**
*   **Project Link**: `https://github.com/your-username/qu-lab-ai-readiness` *(Replace with actual link)*

---
