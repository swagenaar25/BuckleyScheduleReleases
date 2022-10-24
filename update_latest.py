import sys
import json

ver = sys.argv[1]
with open("versions/latest.json") as f:
    dat = json.load(f)

print(f"Update latest from {dat['latest']} to {ver}")
dat["latest"] = ver
with open("versions/latest.json", "w") as f:
    json.dump(dat, f, indent=2)