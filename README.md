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

# 2. Set up kernel
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=naqsha-e-safar

# 3. Run the './src/preprocessing.ipynb' Jupyter Notebook
# Select the `.venv` interpreter and click 'Run All' inside the Notebook
uv run --with jupyter jupyter lab
# Or (w/ VS Code)
code .
```

## TODOs

<details>

<summary>Prior Weeks</summary>

#### Week 1

- [ ] ~~Data Downloading/Aggregation~~
  - [x] Population density - Worldpop
    - [ ] ~~Isolate Lahore's data~~
  - [x] Lahore's PoIs
  - [x] Lahore `osmnx` graph analysis
  - [ ] ~~Lahore's public transport routes via CityLines~~

#### Week 2

- [x] Identify all the latitude-longitude sets that lie within Lahore's
      boundaries
- [x] Get the coordinates for the orange line & metro's stops from the CityLines
      API
- [ ] ~~Get as many Speedo stops as possible from miscellaneous data on the
      internet~~
- [ ] ~~Get as many randomly distributed bus stops as possible by manually
      checking Google Maps~~
  - ~~Search for 'bus station' 'bus stop', 'bus terminal', 'metro station'~~

#### Week 3

- [x] See if Rehman's script (`speedodata` branch) can be developed further
- [x] Copy over Speedo routes manually, in the same 'style' as how CityLines'
      `lahore_sections.geojson` is arrayed (dataset \#4)
- [ ] ~~Build a list of points by cross-referencing PMA's PDF (dataset \#5)~~

</details>

#### Week 4

- [x] Build graph by aggregating numerous datasets
  - [x] Convert route b/w two consecutive stops to edges (perhaps w/ a higher
        weight?)
  - [x] Quantize nodes to the population density of their nearest lat-long from
        amongst the population density dataset
- [ ] Community density problem?

## Datasets

1. [WorldPop (Population Density Data)](https://hub.worldpop.org/geodata/summary?id=48110)
2. [OpenStreetMap](https://www.openstreetmap.org/)
3. [CityLines](https://www.citylines.co/lahore)
4. [Punjab Mass Transit Authority](https://pma.punjab.gov.pk/system/files/LFRMap11.pdf)
5. [Zameen - Speedo Bus Routes in Lahore](https://www.zameen.com/blog/speedo-bus-routes-lahore.html)
