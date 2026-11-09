"""Fetch the IoTID20 dataset into ./data (Kaggle: rohulaminlabid/iotid20-dataset).

kagglehub downloads public datasets anonymously (no kaggle.json needed where
Kaggle is reachable). If Kaggle is unreachable from your region, manually place
'IoT Network Intrusion Dataset.csv' - or its .csv.gz / split ZIP parts - inside
./data/ and the notebook will pick them up automatically.
"""
import shutil
import sys
from pathlib import Path

DATA = Path("data")
DATA.mkdir(exist_ok=True)

existing = [p for p in DATA.rglob("*")
            if p.is_file() and p.suffix.lower() in (".csv", ".gz", ".zip")
            and "iot" in p.name.lower()]
if existing:
    print("dataset already present:")
    for p in existing:
        print("  ", p)
    sys.exit(0)

try:
    import kagglehub
except ImportError:
    sys.exit("run:  pip install kagglehub   (it is in requirements.txt)")

print("downloading IoTID20 (~53 MB) ...")
path = kagglehub.dataset_download("rohulaminlabid/iotid20-dataset")
for p in Path(path).rglob("*.csv"):
    if "iot network intrusion" in p.name.lower():
        shutil.copy(p, DATA / p.name)
        print("copied to data/:", p.name)
print("done - open the notebook and run all cells.")
