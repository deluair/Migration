# AI Migration Simulation

This project models AI-induced labour displacement, internal migration, and policy responses across U.S. metropolitan regions from 2024-2030.  It is built with [Mesa](https://github.com/projectmesa/mesa), a Python agent-based modelling framework.

## Features

* **500 K synthetic workers, 50 K firms, 384 MSAs** (scalable – small counts used by default).
* Dynamic **job market** with a central `job_board`.  Firms lay off workers as they adopt AI and post new vacancies; displaced individuals search and apply.
* **Migration decision** based on unemployment, housing cost and personal preferences.
* **Regional feedback loop** – MSAs update unemployment and wage growth each step.
* Hooks for **government policy** (training subsidies, relocation incentives).
* Modular structure for easy extension and analysis.

## Directory Map

```
ai_migration_simulation/
├── data/               # raw & processed data placeholders
├── notebooks/          # exploratory analysis
├── src/
│   ├── agents/         # Individual, Firm, Regional, Government definitions
│   ├── simulation/
│   │   ├── model.py    # MigrationModel orchestrator
│   │   └── job_market.py
│   └── utils/          # synthetic data generation
├── tests/              # unit & integration tests (stubs)
├── run.py              # quick-start script
└── requirements.txt
```

## Quick Start

```bash
# 1. Install deps (Python ≥3.9)
python -m pip install -r requirements.txt

# 2. Run a small demo (50 indivs, 10 firms, 5 regions)
python run.py
```
The script prints step progress, model-level employment, sample agent data and a final unemployment rate.

## Parameter Tweaks
Edit `run.py` or instantiate `MigrationModel` directly:

```python
model = MigrationModel(n_individuals=1000,
                       n_firms=200,
                       n_regions=50,
                       steps=52)
```

## Extending the Model
* Add richer behaviour in each agent’s `step()`.
* Replace synthetic data with real labour statistics.
* Implement government policies in `GovernmentAgent.step()` and observe macro outcomes.
* Write tests in `tests/` and visualise results in `notebooks/`.

## License
MIT
