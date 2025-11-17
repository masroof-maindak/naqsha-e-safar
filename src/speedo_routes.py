"""
Speedo Bus Routes → GeoJSON + CSV for naqsha-e-safar

- Creates a 'data' folder at the project root if it doesn't exist
- Writes:
    data/speedo_sections.geojson
    data/speedo_routes_with_coords.csv
"""

import json
import time
import csv
from pathlib import Path

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# ---------------------------------------------------------------------
# Paths: assume this file lives in src/, project root is parent folder
# ---------------------------------------------------------------------
THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parent.parent           
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)                    # create "data" if needed

GEOJSON_PATH = DATA_DIR / "speedo_sections.geojson"
CSV_PATH = DATA_DIR / "speedo_routes_with_coords.csv"

print(f"Project root: {PROJECT_ROOT}")
print(f"Data dir:     {DATA_DIR}")

# ---------------------------------------------------------------------
# Geocoder setup
# ---------------------------------------------------------------------
geolocator = Nominatim(user_agent="naqsha-e-safar-speedo-converter")

# ---------------------------------------------------------------------
# Speedo routes data (same as before)
# ---------------------------------------------------------------------
SPEEDO_ROUTES = {
    "Route 1": {
        "from": "Railway Station",
        "to": "Bhatti Chowk",
        "stops": [
            "Railway Station",
            "Ek Moriya",
            "Nawaz Sharif Hospital",
            "Kashmiri Gate",
            "Lari Adda",
            "Azadi Chowk",
            "Texali Chowk",
            "Bhatti Chowk"
        ]
    },
    "Route 2": {
        "from": "Samanabad Mor",
        "to": "Bhatti Chowk",
        "stops": [
            "Samanabad Morr",
            "Corporation Chowk",
            "Taj Company",
            "Sanda",
            "Double Sarkan",
            "Moon Market",
            "Ganda Nala",
            "Bhatti Chowk"
        ]
    },
    "Route 3": {
        "from": "Railway Station",
        "to": "Shahdara Lari Adda",
        "stops": [
            "Railway Station",
            "Ek Moriya",
            "Nawaz Sharif Hospital",
            "Kashmiri Gate",
            "Lari Adda",
            "Azadi Chowk",
            "Timber Market",
            "METRO",
            "Niazi Chowk",
            "Shahdara Metro Station",
            "Shahdara Lari Adda"
        ]
    },
    "Route 4": {
        "from": "R.A Bazar",
        "to": "Chungi Amar Sidhu",
        "stops": ["R.A Bazar", "Nadeem Chowk", "Defence Morr", "Shareef Market",
                  "Walton", "Qainchi", "Ghazi Chowk", "Chungi Amar Sidhu"]
    },
    "Route 5": {
        "from": "Shad Bagh Underpass",
        "to": "Bhatti Chowk",
        "stops": ["Shad Bagh Underpass", "Rajput Park", "Madina Chowk", "Lohay Wali Pulley",
                  "Badami Bagh", "Lari Adda Gol Chakar", "Azadi Chowk", "Taxali Chowk", "Bhatti Chowk"]
    },
    "Route 6": {
        "from": "Babu Sabu",
        "to": "Raj Garh Chowk",
        "stops": ["Babu Sabu", "Niazi Adda", "City Bus Stand", "Chowk Yateem Khana", "Bhala Stop",
                  "Samanabad Morr", "Chauburji", "Riwaz Garden", "M.A.O College", "Firdous Cinema", "Raj Garh Chowk"]
    },
    "Route 7": {
        "from": "Bagrian",
        "to": "Chungi Amar Sidhu",
        "stops": ["Bagrian", "Depot Chowk", "Minhaj University", "Hamdard Chowk", "Rehmat Eye Hospital",
                  "Pindi Stop", "Peco Morr", "Kot Lakhpat Railway Station", "Phatak Mandi", "Qainchi",
                  "Ghazi Chowk", "Chungi Amar Sidhu"]
    },
    "Route 8": {
        "from": "Doctor Hospital",
        "to": "Canal",
        "stops": ["Doctor Hospital", "Wafaqi Colony", "IBA Stop", "Hailey College", "Campus Pull",
                  "Barkat Market", "Kalma Chowk", "Qaddafi Stadium", "Canal"]
    },
    "Route 9": {
        "from": "Railway Station",
        "to": "Sham Nagar",
        "stops": ["Railway Station", "Haji Camp", "Shimla Pahari", "Lahore Zoo", "Chairing Cross",
                  "Ganga Ram Hospital", "Qartaba Chowk", "Chauburji", "Sham Nagar"]
    },
    "Route 10": {
        "from": "Multan Chungi",
        "to": "Qartaba Chowk",
        "stops": ["Multan Chungi", "Mustafa Town", "Karim Block Market", "PU Examination Center",
                  "Bhekewal Morr", "Wahdat Colony", "Naqsha Stop", "Canal", "Ichra", "Shama", "Qartaba Chowk"]
    },
    "Route 11": {
        "from": "Babu Sabu",
        "to": "Main Market Gulberg",
        "stops": ["Babu Sabu", "Niazi Adda", "City Bus Stand", "Chowk Yateem Khana", "Scheme Morr",
                  "Flat Stop", "Dubai Chowk", "Bhekewal Morr", "Sheikh Zaid Hospital", "Campus Pull",
                  "Barkat Market", "Kalma Chowk", "Liberty Chowk", "Hafeez Center", "Mini Market", "Main Market Gulberg"]
    },
    "Route 12": {
        "from": "R.A Bazar",
        "to": "Civil Secretariat",
        "stops": ["R.A Bazar", "PAF Market", "Girja Chowk", "Afshan Chowk", "Fortress Stadium",
                  "Gymkhana", "Aitchison College", "PC Hotel", "Lahore Zoo", "Chairing Cross",
                  "GPO", "Anarkali", "Civil Secretariat"]
    },
    "Route 13": {
        "from": "Bagrian",
        "to": "Kalma Chowk",
        "stops": ["Bagrian", "Ghazi Chowk", "UMT Stop", "Khokhar Chowk", "Akbar Chowk", "Pindi Stop",
                  "Peco Morr", "Phatak Mandi", "Ittefaq Hospital", "Model Town", "Kalma Chowk"]
    },
    "Route 14": {
        "from": "R.A Bazar",
        "to": "Chungi Amar Sidhu",
        "stops": ["R.A Bazar", "Fauji Foundation", "Ali View Garden", "Bhatta Chowk", "DHA Nursery",
                  "LESCO", "Chota Ishara Stop", "Naka Stop", "Ghazi Chowk", "Chungi Amar Sidhu"]
    },
    "Route 15": {
        "from": "Qartba Chowk",
        "to": "Babu Sabu",
        "stops": ["Qartba Chowk", "Hakeem M. Ajmal Khan Road", "Gulshan Ravi Road",
                  "Kacha Ferozepur Road", "Babu Sabu"]
    },
    "Route 16": {
        "from": "Railway Station",
        "to": "Bhatti Chowk",
        "stops": ["Railway Station", "Circular Road", "Ek Moriya", "Bhatti Chowk"]
    },
    "Route 17": {
        "from": "Canal",
        "to": "Railway Station",
        "stops": ["Canal", "Main Boulevard Shadman", "Davis Road", "Shimla Pahari", "Haji Camp", "Railway Station"]
    },
    "Route 18": {
        "from": "Bhatti Chowk",
        "to": "Shimla Pahari",
        "stops": ["Bhatti Chowk", "Circular Road", "Nisbat Road", "Abbot Road", "Shimla Pahari"]
    },
    "Route 19": {
        "from": "Main Market",
        "to": "Bhatti Chowk",
        "stops": ["Main Market", "Jail Road", "Lytton Road", "Crust Road", "Lower Mall Road", "Bhatti Chowk"]
    },
    "Route 20": {
        "from": "Jain Mandar",
        "to": "Chowk Yateem Khana",
        "stops": ["Jain Mandar", "Al-Mumtaz Road", "Poonch Road", "Lake Road", "Chowk Yateem Khana"]
    },
    "Route 21": {
        "from": "Depot Chowk",
        "to": "Thokar Niaz Baig",
        "stops": ["Depot Chowk", "Madar-e-Millat Road", "Ali Road", "Baig Road",
                  "Canal Bank Road", "Thokar Niaz Baig"]
    },
    "Route 22": {
        "from": "Depot Chowk",
        "to": "Thokar Niaz Baig",
        "stops": ["Depot Chowk", "Madar-e-Millat Road", "Sutlej Avenue",
                  "Shahrah Nazria-e-Pakistan Avenue", "Thokar Niaz Baig"]
    },
    "Route 23": {
        "from": "Valencia",
        "to": "Thokar Niaz Baig",
        "stops": ["Valencia", "Valencia Main Boulevard", "Khayaban-e-Jinnah",
                  "Raiwind Road", "Thokar Niaz Baig"]
    },
    "Route 24": {
        "from": "Multan Chungi",
        "to": "Ghazi Chowk",
        "stops": ["Multan Chungi", "College Road", "Maulana Shaukat Ali Road", "Wahdat Road", "Ghazi Chowk"]
    },
    "Route 25": {
        "from": "R.A Bazar",
        "to": "Railway Station",
        "stops": ["R.A Bazar", "Lahore-Bedian Road", "Allama Iqbal Road", "Railway Station"]
    },
    "Route 26": {
        "from": "R.A Bazar",
        "to": "Daroghawala",
        "stops": ["R.A Bazar", "G.T Road", "Shalimar Link Road", "Tufail Road",
                  "Sarfraz Rafique Road", "Daroghawala"]
    },
    "Route 27": {
        "from": "BataPur",
        "to": "Daroghawala",
        "stops": ["BataPur", "GT Road", "Daroghawala"]
    },
    "Route 28": {
        "from": "Quaid e Azam Interchange",
        "to": "Airport",
        "stops": ["Quaid e Azam Interchange", "Harbanspura Road", "Zarar Shaheed Road", "Airport"]
    },
    "Route 29": {
        "from": "Niazi Interchange",
        "to": "Salamat Pura",
        "stops": ["Niazi Interchange", "Lahore Ring Road", "Band Road", "Sue Wala Road", "Salamat Pura"]
    },
    "Route 30": {
        "from": "Daroghawala",
        "to": "Airport",
        "stops": ["Daroghawala", "G.T. Road", "Shalimar Link Road", "Airport"]
    },
    "Route 31": {
        "from": "Daroghawala",
        "to": "Lari Adda",
        "stops": ["Daroghawala", "Chamra Mandi", "Cooper Store", "UET", "Shalimar Chowk", "Lari Adda"]
    },
    "Route 32": {
        "from": "Shimla Pahari",
        "to": "Ek Moriya",
        "stops": ["Shimla Pahari", "Durand Road", "Queen Mary Road", "Garhi Shahu Bridge",
                  "Cooper Store", "Chamra Mandi", "Ek Moriya"]
    },
    "Route 33": {
        "from": "Cooper Store",
        "to": "Mughalpura",
        "stops": ["Cooper Store", "Workshop Road", "Mughalpura Road", "Mughalpura"]
    },
    "Route 34": {
        "from": "Singhpura",
        "to": "Mughalpura",
        "stops": ["Singhpura", "Wheatman Road", "Griffin Road", "Mughalpura"]
    }
}

# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------
def geocode_location(location_name: str, retry_count: int = 3):
    """Return [lon, lat] for a stop, or [None, None] if it fails."""
    query = f"{location_name}, Lahore, Pakistan"
    for attempt in range(retry_count):
        try:
            time.sleep(1)  # be nice to the API
            loc = geolocator.geocode(query, timeout=10)
            if loc:
                return [loc.longitude, loc.latitude]
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"  ⚠️  Geocoding error for '{location_name}' attempt {attempt+1}: {e}")
        time.sleep(1)
    print(f"  ⚠️  Could not geocode '{location_name}'")
    return [None, None]


def create_route_feature(route_name, route_data, route_id):
    """Build a single GeoJSON Feature for a route."""
    print(f"\n Processing {route_name}...")
    coordinates = []

    for stop in route_data["stops"]:
        print(f"   {stop}")
        lon, lat = geocode_location(stop)
        if lon is not None and lat is not None:
            coordinates.append([lon, lat])

    if len(coordinates) < 2:
        print(f"   Not enough coordinates for {route_name}, skipping")
        return None

    length = len(coordinates) * 500  # rough estimate

    return {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": coordinates,
        },
        "properties": {
            "id": route_id,
            "klass": "Section",
            "length": length,
            "opening": 2013,
            "lines": [{
                "line": route_name,
                "line_url_name": f"speedo-{route_name.lower().replace(' ', '-')}",
                "system": "Lahore Speedo Bus",
            }],
        },
    }


def write_geojson():
    """Write data/speedo_sections.geojson"""
    features = []
    route_id = 30000

    for route_name, route_data in SPEEDO_ROUTES.items():
        feature = create_route_feature(route_name, route_data, route_id)
        if feature:
            features.append(feature)
            route_id += 1

    collection = {"type": "FeatureCollection", "features": features}
    with GEOJSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(collection, f, indent=2, ensure_ascii=False)

    print(f"\n GeoJSON written to {GEOJSON_PATH}")
    print(f" Total routes: {len(features)}")


def write_csv():
    """Write data/speedo_routes_with_coords.csv"""
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "route_id", "route_name", "from", "to",
            "stop_index", "stop_name", "longitude", "latitude",
        ])

        route_id = 30000
        for route_name, route_data in SPEEDO_ROUTES.items():
            print(f"\n CSV: {route_name}")
            for i, stop in enumerate(route_data["stops"], start=1):
                lon, lat = geocode_location(stop)
                writer.writerow([
                    route_id,
                    route_name,
                    route_data["from"],
                    route_data["to"],
                    i,
                    stop,
                    lon,
                    lat,
                ])
            route_id += 1

    print(f"\n CSV written to {CSV_PATH}")


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("🚍 Generating Speedo GeoJSON + CSV for naqsha-e-safar")
    print("=" * 60)

    write_geojson()
    write_csv()

    print("\nAll done ✅")
