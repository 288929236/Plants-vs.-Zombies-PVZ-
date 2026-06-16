import json, os, time
_FILE = os.path.join(os.path.dirname(__file__), "progress.json")

def load():
    if not os.path.exists(_FILE):
        return {"chapter": 1, "stage": 1, "records": {}}
    with open(_FILE, encoding="utf-8") as f:
        return json.load(f)

def save(chapter, stage):
    p = load()
    p["chapter"] = chapter
    p["stage"] = stage
    _write(p)

def current_level():
    p = load()
    return f"level_{p['chapter']}-{p['stage']}"

def record_pass(level_name, elapsed):
    """记录某关通关时间"""
    p = load()
    if "records" not in p:
        p["records"] = {}
    p["records"][level_name] = round(elapsed, 1)
    _write(p)

def get_record(level_name):
    """获取某关通关时间，未通关返回 None"""
    p = load()
    return p.get("records", {}).get(level_name)

def _write(data):
    json.dump(data, open(_FILE, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
