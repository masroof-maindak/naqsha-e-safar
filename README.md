# Naqsha-e-Safar

This project aims to identify and classify public transit deserts in Lahore
using Graph Neural Networks.

## Setup

```bash
# Install dependencies and synchronize environment
uv sync

# 2.  Download and prepare WorldPop population density data
uv run scripts/01-download_worldpop.py
```

## TODOs

- [ ] Data Downloading/Aggregation
  - [x] Population density - Worldpop
    - [ ] Isolate Lahore's data
  - [ ] Lahore's PoIs and boundaries via osmnx
  - [ ] Lahore's public transport routes via CityLines
- [ ] Graph representation
  - [ ] ???
- [ ] ???

## Acknowledgements

- [WorldPop (Population Density Data)](https://hub.worldpop.org/geodata/summary?id=48110)
- [OpenStreetMap](https://www.openstreetmap.org/)
