import json
import re

json_open = open("./sample.json", 'r')
json_load = json.load(json_open)
# print(json_load)/.
# print(json_load.get("attributes").keys())
keys = json_load.get("attributes").keys()
for k in keys:
    print(f'{k} = "{k}"')

print("\n------------------------------------\n")

for k in keys:
    print(f'{k}: attrs.get({k}),')

print("\n------------------------------------\n")

tmp = """| #KEY#     | {{data.#KEY#     | default("None")}} |"""

for k in keys:
    md = re.sub("#KEY#", k, tmp)
    print(md)
