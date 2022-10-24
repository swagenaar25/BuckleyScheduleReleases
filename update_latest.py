import sys
import json

ver = sys.argv[1]
with open("versions/latest.json") as f:
    dat = json.load(f)

dat["latest"] = ver
with open("versions/latest.json", "w") as f:
    json.dump(dat, f)