from pathlib import Path
import json
# Prunes the file name from pwd
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

# the /'s are used to append to the path
DATA = BASE_DIR / "data" / "vehicles.json"

print(DATA)

with DATA.open("r", encoding="utf-8") as f:
    vehicles = json.load(f)

print(vehicles)