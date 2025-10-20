# QuLab - AI Career Navigator & Pathway Planner

## 🚀 Project Title and Description

This project, **"QuLab - AI Career Navigator & Pathway Planner,"** is a Streamlit-based web application designed as a lab project to explore and interact with the **AI-Readiness Score (AI-R) framework**. The AI-R framework is a parametric model that quantifies an individual's preparedness for AI-enabled careers by considering both personal capabilities (Idiosyncratic Readiness - $V^R$) and market opportunities (Systematic Opportunity - $H^R$), along with a Synergy component.

The application provides an interactive environment for users to:
*   Understand the theoretical underpinnings and components of the AI-Readiness Score.
*   Calculate their own AI-R score by adjusting various individual and market parameters.
*   Simulate the impact of different learning pathways on their projected AI-Readiness.
*   Visualize how different factors contribute to their overall career readiness in an AI-driven labor market.

This tool aims to empower individuals to make informed decisions about skill development and career transitions in the evolving landscape of AI-enabled professions.

## ✨ Features

*   **AI-Readiness Score Components Overview**: Detailed explanations of Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($H^R$), and Synergy components, including their sub-components and underlying formulas.
*   **Interactive AI-Readiness Score Calculator**:
    *   Adjust individual attributes (AI-Fluency, Domain-Expertise, Adaptive-Capacity) through sliders and input fields.
    *   Select target occupations and adjust market parameters (e.g., job growth, wage premium) to calculate Systematic Opportunity ($H^R$).
    *   Input global parameters like the weighting of individual vs. market factors ($\alpha$) and the Synergy coefficient ($\beta$).
    *   Calculate and display current $V^R$, $H^R$, Synergy %, and the overall AI-R Score.
    *   Visualizations (pie charts, bar charts) to show component contributions to scores.
*   **Learning Pathway Simulation**:
    *   Select from predefined learning pathways.
    *   Adjust pathway completion and mastery scores to simulate their impact.
    *   Project how a pathway might change an individual's $V^R$ sub-components and the overall AI-R Score.
    *   Compare current vs. projected scores through intuitive visualizations.
*   **Synthetic Data Integration**: Utilizes pre-generated synthetic datasets for individual profiles, occupational data, learning pathways, and skill requirements, making the application fully functional for demonstration and exploration without external data sources.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd QuLab-AI-Career-Navigator
    ```
    *(Replace `<repository-url>` with the actual URL of your repository)*

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
    Create a `requirements.txt` file in your project root with the following content:
    ```
    streamlit==1.x.x # Use a compatible version, e.g., 1.30.0
    pandas==2.x.x
    numpy==1.x.x
    plotly==5.x.x
    plotly-express==0.4.x
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Usage

1.  **Run the Streamlit application**:
    Ensure your virtual environment is activated and you are in the project's root directory.
    ```bash
    streamlit run app.py
    ```
    This command will open the application in your default web browser (usually at `http://localhost:8501`).

2.  **Navigate the Application**:
    Use the sidebar to switch between the main sections:
    *   **AI-Readiness Score Components**: Provides a foundational understanding of the AI-R framework. Includes expandable sections to view the synthetic datasets used in the application.
    *   **AI-Readiness Score Calculator**: Interact with sliders and input fields to define an individual's profile and a target occupation. Click "Calculate AI-Readiness Score" to see the results and visualizations.
    *   **Pathway Simulation**: (Recommended to use after calculating a base score in the "Calculator" page). Select a learning pathway, adjust completion and mastery, and simulate its projected impact on your scores.

3.  **Explore "What-If" Scenarios**:
    *   On the "AI-Readiness Score Calculator" page, experiment with different inputs for individual skills, experience, education, and target occupations to see how your AI-R score changes.
    *   On the "Pathway Simulation" page, observe how investing in different learning pathways at varying levels of completion and mastery can boost your readiness.

## 📁 Project Structure

```
.
├── README.md
├── app.py
├── requirements.txt
└── application_pages/
    ├── __init__.py
    ├── ai_readiness_functions.py
    ├── page1.py
    ├── page2.py
    └── page3.py
```

*   `README.md`: This file, providing an overview of the project.
*   `app.py`: The main Streamlit application entry point. It sets up the page configuration, displays the introduction, initializes synthetic dataframes in Streamlit's session state, and handles navigation between different pages.
*   `requirements.txt`: Lists all Python dependencies required to run the application.
*   `application_pages/`: A directory containing the logic for different sections (pages) of the Streamlit application.
    *   `ai_readiness_functions.py`: Contains all the core Python functions for calculating the various components of the AI-Readiness Score (AI-Fluency, Domain-Expertise, Adaptive-Capacity, Idiosyncratic Readiness, Systematic Opportunity, Synergy) and the pathway simulation logic. *(Note: This file also implicitly defines or loads the synthetic data structures (e.g., `individual_profiles_data`, `occupational_data`) that are imported by `app.py`, although the definitions were not included in the provided snippet.)*
    *   `page1.py`: Implements the "AI-Readiness Score Components" page, explaining the framework's theory and displaying the synthetic datasets.
    *   `page2.py`: Implements the "AI-Readiness Score Calculator" page, allowing interactive input and calculation of the AI-R score with visualizations.
    *   `page3.py`: Implements the "Pathway Simulation" page, enabling users to simulate the impact of learning pathways on their projected AI-R scores.

## 🛠️ Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: For building the interactive web application interface.
*   **Pandas**: For data manipulation and handling synthetic datasets.
*   **NumPy**: Used for numerical operations within the calculation functions.
*   **Plotly Express / Plotly Graph Objects**: For creating interactive data visualizations (pie charts, bar charts) within the application.

## 🤝 Contributing

This project is primarily a lab exercise. However, contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE.md file for details (if applicable, otherwise state 'For academic/lab use only').

## 📧 Contact

For any questions or feedback, please contact:

*   **Your Name/Organization**: [Quant University](https://www.quantuniversity.com/)
*   **Project Link**: [https://github.com/your-username/your-repository-name](https://github.com/your-username/your-repository-name)
    *(Replace with actual GitHub link)*
