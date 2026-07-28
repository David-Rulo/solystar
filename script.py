import json
with open("customer_profiles.json") as f:
    data = json.load(f)
print(f"✅ JSON válido — {len(data['perfiles'])} perfiles, {len(data['meta'])} metadatos")
print(f"   Esquema: {list(data['perfiles'][0].keys())}")