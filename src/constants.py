import os

LHR_NAME_STR = "Lahore District, Pakistan"
LHR_LAT = 31.456845
LHR_LON = 74.407836

CITYLINES_SRCS = [
    (
        "https://www.citylines.co/api/lahore/raw_source/sections",
        "lahore_sections.geojson",
    ),
    (
        "https://www.citylines.co/api/lahore/raw_source/stations",
        "lahore_stations.geojson",
    ),
    (
        "https://www.citylines.co/api/data/lahore/lines_systems_and_modes",
        "lahore_lines_systems_and_modes.json",
    ),
]


WORLDPOP_URL: str = "https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/PAK/pak_pd_2020_1km_UNadj_ASCII_XYZ.zip"
WORLDPOP_DATA_DIR = "../data/worldpop"

OSMNX_DATA_DIR = "../data/osmnx"

SPEEDO_DATA_DIR = "../data/speedo"
SPEEDO_ROUTES_FPATH = os.path.join(SPEEDO_DATA_DIR, "speedo_routes_hand_cleaned.csv")

CITYLINES_DATA_DIR = "../data/citylines"
METRO_ROUTES_FPATH = os.path.join(CITYLINES_DATA_DIR, "lahore_sections.geojson")

AGGR_GRAPH_PATH = "../data/graphs/aggregated.graphml"

POP_READING_RADIUS = 1000

COMMUNITY_PARTITIONS_FPATH = "../data/comm_partitions.pkl"

DISTANCE_POSITIVE_THRESHOLD = 1500
DISTANCE_NEGATIVE_THRESHOLD = 4500

FINAL_GRAPH_PATH = "../data/graphs/final.gpickle"

FINAL_GRAPH_PATH_WITH_INFERENCE = "../data/graphs/final_with_inference.gpickle"

BEST_MODEL_PATH = "../data/ModelParameters/best_transit_gcn.pth"
