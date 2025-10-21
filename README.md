# QuLab — AI-Readiness Lab (Streamlit)

QuLab is an interactive Streamlit lab application that helps you measure and simulate your AI-Readiness (AI-R) using a structured, data-driven framework. It blends:
- Idiosyncratic Readiness (V^R): your capabilities
- Systematic Opportunity (H^R): the market opportunity for a target role
- Synergy: alignment between your skills and market requirements

Core formula:
AI-R_{i,t} = α · V^R_i(t) + (1 − α) · H^R_i(t) + β · Synergy%

The app ships with lightweight synthetic datasets so you can explore the model end-to-end without external data sources. It’s designed for labs, workshops, and as a starting point for integrating real data.

---

## Features

- Interactive inputs for V^R:
  - AI-Fluency (S1 Technical AI skills, S2 AI-augmented productivity, S3 Critical AI judgment, S4 AI learning velocity)
  - Domain-Expertise (Education foundation, Practical experience, Specialization depth)
  - Adaptive-Capacity (Cognitive flexibility, Social-emotional intelligence, Strategic career management)
- Market opportunity (H^R) calculator for a selected occupation:
  - AI enhancement, job growth projection, wage premium, entry accessibility
  - Growth and regional multipliers (λ, γ)
- Synergy modeling:
  - Skills match between your profile and the role’s requirements
  - Timing factor and alignment
- Global controls:
  - α (weight on individual vs market factors)
  - β (weight on synergy)
- Rich visualizations:
  - KPI tiles, composition charts, and breakdowns
- Pathway simulation:
  - “What-if” scenarios for learning pathways affecting V^R, Synergy, and AI-R
- Session-aware navigation:
  - Compute once, then explore breakdowns and simulations across pages
- Synthetic datasets included:
  - Individual profile, occupations, required skills per occupation, learning pathways

---

## Getting Started

### Prerequisites
- Python 3.9+ (3.10+ recommended)
- pip (or uv/poetry/conda if preferred)
- Internet access (for the logo displayed in the sidebar)

### Installation

1) Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2) Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a requirements.txt yet, use:
```txt
# requirements.txt
streamlit>=1.25
pandas>=1.5
numpy>=1.23
plotly>=5.15
```

### Run the app

```bash
streamlit run app.py
```

This opens the app at http://localhost:8501 (or the next available port).

---

## Usage

Typical workflow:
1) Overview & Inputs
   - Set α and β in the sidebar.
   - Fill in your V^R inputs (AI-Fluency, Domain-Expertise, Adaptive-Capacity).
   - Choose a target occupation and adjust λ (growth multiplier) and γ (regional multiplier).
   - Edit your skills and specify Max Possible Skills Match.
   - Click “Calculate AI-Readiness” to compute all components and the final AI-R.

2) Scores & Insights
   - Review V^R, H^R, Synergy%, and AI-R tiles.
   - Explore composition and breakdown charts.
   - Inspect detailed breakdown data and synthetic datasets if needed.

3) Pathway Simulation
   - Choose a learning pathway and set completion/mastery scores.
   - Simulate the impact on V^R, Synergy, and AI-R.
   - Compare current vs projected metrics and compositions.

Notes:
- The app uses Streamlit session_state to persist inputs and results across pages.
- Some calculations include normalization and clamping to maintain stable scales and avoid division-by-zero.

---

## Project Structure

A typical (final) structure looks like:

```
.
├── app.py                         # Streamlit entrypoint and page router
└── application_pages
    ├── __init__.py                # Package initializer
    ├── core.py                    # Core computations (V^R, H^R, Synergy, AI-R, simulation)
    ├── page1.py                   # Overview & Inputs (compute baseline scores)
    ├── page2.py                   # Scores & Insights (visualizations and breakdowns)
    └── page3.py                   # Pathway Simulation (what-if analysis)
```

Key modules:
- app.py
  - Sets branding, initializes synthetic DataFrames (profiles, occupations, required skills, pathways).
  - Provides global controls (α, β) and routes to pages.
- application_pages/core.py
  - Implements all core calculations:
    - AI-Fluency subcomponents S1–S4
    - Domain-Expertise, Adaptive-Capacity
    - V^R aggregation
    - H^R base components + multipliers (λ, γ)
    - Skills Match, Timing, Alignment, and Synergy
    - Final AI-R
  - Orchestrator compute_all_scores(inputs_dict)
  - simulate_pathway_impact for what-if analysis
- application_pages/page1.py
  - UI for inputs to compute baseline V^R, H^R, Synergy, AI-R
  - Skills editor and occupation attribute previews
- application_pages/page2.py
  - KPI tiles and Plotly charts for V^R composition and H^R breakdowns
  - Data expanders for in-depth numbers and synthetic data tables
- application_pages/page3.py
  - Simulation of learning pathway impacts with comparison charts

Note: The repository may contain earlier iterations (e.g., utils/common/ai_readiness modules). The final structure uses application_pages/core.py for all computations. If duplicates exist in your copy, keep one canonical core module and refactor imports accordingly.

---

## Technology Stack

- Streamlit for UI and stateful multipage app
- Pandas for tabular data manipulation
- NumPy for numeric operations
- Plotly (Express and Graph Objects) for interactive charts

Optional/indirect:
- Python venv for environment management

---

## Extending the Project

- Replace synthetic data with real data sources:
  - Load CSVs or connect to APIs/DBs where individual profiles, occupations, and required skills are maintained.
- Add occupations or pathways:
  - Update the synthetic DataFrames in app.py or load external files.
- Customize weights and formulas:
  - Weights for V^R subcomponents (w1=0.45, w2=0.35, w3=0.20) and H^R base weights can be adjusted in core.py.
- Add pages:
  - Create a new module in application_pages and route to it from app.py.

---

## Contributing

Contributions are welcome! To propose changes:
- Open an issue describing the feature or bug.
- Fork the repo and create a feature branch.
- Follow the existing code style and add inline comments for complex logic.
- Test locally: streamlit run app.py
- Open a pull request with a clear summary of your changes.

---

## License

This project is released under the MIT License. See LICENSE for details.

---

## Contact

- Questions or feedback: please open an issue in the repository.
- For lab/course usage: contact your course or lab facilitator.
- Organization: https://www.quantuniversity.com (logo used in the app sidebar)

---

## Appendix: Model Summary

- AI-Readiness (AI-R):
  AI-R = α · V^R + (1 − α) · H^R + β · Synergy%
- V^R (0–100) is a weighted mix of:
  - AI-Fluency (S1, S2, S3, S4)
  - Domain-Expertise (Education, Experience, Specialization)
  - Adaptive-Capacity (Cognitive, Social/Emotional, Strategic)
- H^R (0–100) is computed from:
  - H_base = w1·AI-Enhancement + w2·Job-Growth + w3·Wage-Premium + w4·Entry-Accessibility
  - Then scaled by Growth and Regional multipliers (λ and γ)
- Synergy%:
  - Based on Skills Match (user vs role requirements), Timing factor (experience), and Alignment
  - Synergy% = (V^R · H^R · Alignment) / 100
- Normalization/guardrails:
  - Defensive checks to avoid division-by-zero
  - Clamping/normalization for stability and interpretability

Enjoy exploring your AI-Readiness with QuLab!