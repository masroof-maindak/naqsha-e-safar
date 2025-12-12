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
# 1. Install dependencies and synchronize environment
uv sync

# 2. Run the './src/preprocessing.ipynb' Jupyter Notebook
uv run --with jupyter jupyter lab # Or; w/ VS Code
code .

# 3. Run './src/community-detection.ipynb'
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

#### Week 4

- [x] Build graph by aggregating numerous datasets
  - [x] Convert route b/w two consecutive stops to edges (perhaps w/ a higher
        weight?)
  - [x] Quantize nodes to the population density of their nearest lat-long from
        amongst the population density dataset
- [ ] [WIP] **Community density problem?**
  - [x] Louvain

#### Week 5

_Goal: find a neighbourhood w/ a high population density but poor public
transport i.e a subgraph that is densely connected within some boundary (small
diameter), has lots of people, and has very little public transport stops_

- [x] Rather than quantizing every node to its nearest population reading,
      distribute every population reading's population value equally amongst all
      nodes in its vicinity
- [x] Create a new node feature for 'distance_to_nearest_stop'

</details>

#### Week 6

_At this point, we have two potential future approaches. Although I'm personally
leaning towards #1, we'll be proceeding w/ #2 as per the instructor's advice,
and more importantly: time constraints._

<details>

<summary><b><i>1. Graph Classification</i></b></summary>

1. [ ] Convert all existing communities (generated via Louvain) to their own
       separate graphs
2. [ ] Take a few really obvious picks (for served & underserved communities
       (now graphs)) and mark them as such.
3. [ ] Train a GNN
4. [ ] Run it on the remaining communities

</details>

**_2. Node Classification_**

1. [x] Create a new 'distance_to_nearest_stop' feature for every Point of
       Interest
2. [x] Add community label (using Louvain) via one-hot encoding as a node
       feature
3. [x] Generate binary labels based on `distance_to_nearest_stop < 600` &
       `distance_to_nearest_stop > 3500`; these denote cases where we are
       definitely not-inside and inside a transit desert, respectively; every
       other node is used for testing
4. [ ] Train a GNN on the graph + labels
5. [ ] Run it on all other nodes & predict their label
6. [ ] Sort communities based on the ratio of their nodes whose label set is
       high (i.e 'this node is not in a transit desert')

## Assumptions/Caveats/Limitations

- Few stops; we only have the Red Metro, Orange Line, and 20 unique Speedo stops
- The 'communities' returned by Louvain are not representative of actual
  residential 'societies' in Lahore
- We don't account for 'self-sufficient' methods of transport e.g communities w/
  a teeming qingqi culture
- Some missing data e.g stops along Speedo routes (we ignore these)

## Datasets

1. [WorldPop (Population Density Data)](https://hub.worldpop.org/geodata/summary?id=48110)
2. [OpenStreetMap](https://www.openstreetmap.org/)
3. [CityLines](https://www.citylines.co/lahore)
4. [Punjab Mass Transit Authority](https://pma.punjab.gov.pk/system/files/LFRMap11.pdf)
5. [Zameen - Speedo Bus Routes in Lahore](https://www.zameen.com/blog/speedo-bus-routes-lahore.html)
