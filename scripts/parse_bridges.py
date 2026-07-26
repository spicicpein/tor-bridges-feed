import json, re, datetime

try:
    with open("bridge_prefs.js", encoding="utf-8", errors="ignore") as f:
        content = f.read()
except FileNotFoundError:
    content = ""

lines = re.findall(r'"((?:obfs4|webtunnel) [^"]+)"', content)
seen = set()
bridges = []
for l in lines:
    if l not in seen:
        seen.add(l)
        bridges.append(l)

feed = {
    "updated": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "source_fetch_ok": len(content) > 0,
    "bridges": bridges,
}
with open("bridges.json", "w") as f:
    json.dump(feed, f, indent=2)
print(f"wrote {len(bridges)} bridge lines, source_fetch_ok={len(content) > 0}")
