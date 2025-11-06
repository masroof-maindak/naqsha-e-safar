import os
import zipfile

import requests


def download_worldpop_zip(url: str, download_dir: str) -> str:
    zip_fname = url.split("/")[-1]
    zip_fpath = os.path.join(download_dir, zip_fname)

    if not os.path.exists(zip_fpath):
        print(f"Downloading {zip_fname}...")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(zip_fpath, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded {zip_fname} to {zip_fpath}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
            return ""
    else:
        print(f"{zip_fname} already exists. Skipping download.")
    return zip_fpath


def unzip_worldpop_data(zip_fpath: str, extract_dir: str):
    if not zip_fpath or not os.path.exists(zip_fpath):
        print(f"Error: Zip file not found at {zip_fpath}. Skipping unzip.")
        return

    zip_fname = os.path.basename(zip_fpath)
    unzipped_fname = zip_fname.replace(".zip", ".csv")
    unzipped_fpath = os.path.join(extract_dir, unzipped_fname)

    if not os.path.exists(unzipped_fpath):
        print(f"Unzipping {zip_fname}...")
        try:
            with zipfile.ZipFile(zip_fpath, "r") as archive:
                archive.extract(unzipped_fname, extract_dir)
                print(f"Unzipped {unzipped_fname} to {unzipped_fpath}")
        except Exception as e:
            print(f"Error unzipping file: {e}")
    else:
        print(f"{unzipped_fname} already exists. Skipping unzip.")


if __name__ == "__main__":
    worldpop_url = "https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/PAK/pak_pd_2020_1km_UNadj_ASCII_XYZ.zip"
    base_data_dir = os.path.join(os.path.dirname(__file__), "..", "data")

    worldpop_data_dir = os.path.join(base_data_dir, "worldpop")
    os.makedirs(worldpop_data_dir, exist_ok=True)

    downloaded_zip_path = download_worldpop_zip(worldpop_url, worldpop_data_dir)
    unzip_worldpop_data(downloaded_zip_path, worldpop_data_dir)
