# Naqsha-e-Safar

**Identifying and Classifying Public Transit Deserts in Lahore Using Graph
Neural Networks**

## Problem Statement

This project identifies areas in Lahore with high population density but poor
access to public transport i.e “transit deserts.” Using population data
(WorldPop), transit routes (CityLines), and the city’s road network
(OpenStreetMap), we model Lahore as a spatial graph and apply a Graph Neural
Network to classify underserved regions. The outcome is a data-driven map of
transit accessibility gaps to guide future transport planning.

## Setup

```bash
# Install dependencies and synchronize environment
uv sync

# 2. Download and prepare WorldPop population density data
uv run scripts/01-download-worldpop.py

# 3. Set up kernel
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=naqsha-e-safar

# 4. Run the './scripts/02-osmnx-preprocessing.ipynb` Jupyter Notebook
# Select the `.venv` interpreter and click 'Run All' inside the Notebook
uv run --with jupyter jupyter lab
# Or (w/ VS Code)
code .
```

## TODOs

- [ ] ~~Data Downloading/Aggregation~~
  - [x] Population density - Worldpop
    - [ ] ~~Isolate Lahore's data~~
  - [x] Lahore's PoIs
  - [x] Lahore `osmnx` graph analysis
  - [ ] ~~Lahore's public transport routes via CityLines~~

---

- [x] Identify all the latitude-longitude sets that lie within Lahore's
      boundaries
- [ ] Get the coordinates for the orange line & metro's stops from the CityLines
      API
- [ ] Get as many Speedo stops as possible from miscellaneous data on the
      internet
- [ ] Get as many randomly distributed bus stops as possible by manually
      checking Google Maps

## Acknowledgements

- [WorldPop (Population Density Data)](https://hub.worldpop.org/geodata/summary?id=48110)
- [OpenStreetMap](https://www.openstreetmap.org/)
