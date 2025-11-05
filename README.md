# Naqsha-e-Safar

This project aims to identify and classify public transit deserts in Lahore
using Graph Neural Networks.

## Setup

```bash
# Install dependencies and synchronize environment
uv sync

# 2.  Download and prepare WorldPop population density data
uv run scripts/01-download_worldpop.py

# 3. Run the './scripts/02-osmnx-preprocessing.ipynb` Jupyter Notebook
# Select the `.venv` interpreter and click 'Run All' inside the Notebook
uv run --with jupyter jupyter lab
# Or (w/ VS Code)
code .
```

## TODOs

- [ ] Data Downloading/Aggregation
  - [x] Population density - Worldpop
    - [ ] Isolate Lahore's data
  - [x] Lahore's PoIs
  - [ ] Lahore's public transport routes via CityLines
- [ ] Graph representation
  - [ ] ???
- [ ] ???

## Acknowledgements

- [WorldPop (Population Density Data)](https://hub.worldpop.org/geodata/summary?id=48110)
- [OpenStreetMap](https://www.openstreetmap.org/)
