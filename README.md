# QuLab - AI-Readiness: AI Career Navigator & Pathway Planner

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## 🌟 Project Title and Description

**QuLab: AI-Readiness - GPT-5: AI Career Navigator & Pathway Planner** is an interactive Streamlit web application designed as a lab project to help individuals quantify and simulate their career readiness for the AI era. It utilizes a comprehensive AI-Readiness framework that integrates:

1.  **Individual Capability (Idiosyncratic Readiness, $V^R$)**: Your unique skills, expertise, and adaptive traits.
2.  **Market Opportunity (Systematic Opportunity, $H^R$)**: The demand, growth, and accessibility of target AI-enabled roles.
3.  **Synergy**: How well your current skills align with target role requirements and market timing, amplifying your overall score.

The core of the application is the **AI-Readiness Score**, calculated using the formula:

$AI\text{-}R_{i,t} = \alpha\, V^R_i(t) + (1-\alpha)\, H^R_i(t) + \beta\, \text{Synergy}\%(V^R, H^R)$

Where:
*   $\alpha \in [0,1]$: Weight for individual readiness ($V^R$) vs. market opportunity ($H^R$).
*   $\beta > 0$: Coefficient for the Synergy component.

The application allows users to interactively adjust various parameters, explore synthetic data, and simulate learning pathways to understand their current AI-Readiness and potential future states.

## ✨ Features

*   **Interactive AI-Readiness Calculator**:
    *   Adjust a wide range of personal inputs for AI-Fluency, Domain-Expertise, and Adaptive-Capacity.
    *   Select target occupations to evaluate Systematic Opportunity ($H^R$).
    *   Manage and update individual skill profiles for Synergy calculation.
    *   Customize global parameters ($\alpha$, $\beta$, $\lambda$, $\gamma$).
    *   View real-time calculated $V^R$, $H^R$, Synergy, and overall AI-Readiness scores.
    *   Visualizations using Plotly to break down component contributions.
*   **Pathway Simulator**:
    *   Select predefined learning pathways (e.g., Prompt Engineering, AI for Financial Analysis).
    *   Simulate the impact of pathway completion and mastery on your $V^R$ components and overall AI-Readiness.
    *   Compare current vs. projected scores through intuitive bar charts.
*   **Data Explorer**:
    *   Browse and understand the synthetic datasets used in the application (individual profiles, occupational data, learning pathways, skills data).
    *   Download raw data in CSV format.
    *   Visualize base opportunity scores ($H_{base}$) across different occupations.
    *   Explore skill matches between your profile and selected occupations.
*   **Comprehensive Formula Display**: LaTeX-formatted explanations of all key formulas for transparency.
*   **Responsive UI**: Built with Streamlit for a clean, interactive, and user-friendly experience.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/qu Lab-ai-readiness.git
    cd qu Lab-ai-readiness
    ```
    (Replace `your-username/qu Lab-ai-readiness.git` with the actual repository URL)

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    (The `requirements.txt` should contain: `streamlit`, `pandas`, `numpy`, `plotly`)

    If `requirements.txt` is not provided, you can create it based on the imports:
    ```
    streamlit
    pandas
    numpy
    plotly
    ```
    Then run `pip install -r requirements.txt`.

## 🏃 Usage

1.  **Run the Streamlit application**:
    Ensure your virtual environment is active, then execute:
    ```bash
    streamlit run app.py
    ```

2.  **Access the application**:
    Your web browser should automatically open to `http://localhost:8501` (or a similar address). If not, open your browser and navigate to that URL.

3.  **Navigate and Interact**:
    *   Use the sidebar to navigate between **Overview & Calculator**, **Pathway Simulator**, and **Data Explorer**.
    *   **Overview & Calculator**: Adjust sliders, select occupations, and manage your skills data. Click "Calculate Scores" to see your AI-Readiness.
    *   **Pathway Simulator**: Choose a learning pathway and specify completion/mastery to see its projected impact on your scores.
    *   **Data Explorer**: View and download the underlying synthetic data.

## 📂 Project Structure

```
qu Lab-ai-readiness/
├── app.py                      # Main Streamlit application entry point
├── requirements.txt            # Python dependencies
└── application_pages/          # Directory for individual Streamlit pages and utilities
    ├── __init__.py             # Makes application_pages a Python package
    ├── utils.py                # Core functions for data generation, calculations, and simulations
    ├── page1.py                # Logic for the 'Overview & Calculator' page
    ├── page2.py                # Logic for the 'Pathway Simulator' page
    └── page3.py                # Logic for the 'Data Explorer' page
```

## 🛠️ Technology Stack

*   **Framework**: [Streamlit](https://streamlit.io/)
*   **Language**: [Python](https://www.python.org/)
*   **Data Manipulation**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
*   **Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/)

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes and ensure the code adheres to existing style guidelines.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
*(Note: Create a `LICENSE` file in the root directory if not already present.)*

## 📧 Contact

*   **Project Maintainer**: [Your Name/Quant University]
*   **Email**: [your.email@example.com / info@quantuniversity.com]
*   **GitHub**: [Your GitHub Profile / QuantUniversity GitHub]
*   **Website**: [https://www.quantuniversity.com/](https://www.quantuniversity.com/) (if applicable)



## License

## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@quantuniversity.com](mailto:info@quantuniversity.com)
