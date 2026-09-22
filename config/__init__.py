# ============================================
#  config 统一入口
# ============================================

from config.settings import *
from config.maps     import ALL as MAPS
from config.plants   import ALL as PLANT_ALL
from config.zombies  import ALL as ZOMBIE_ALL

# ---- 构建精灵注册表 (从植物/僵尸配置中提取动画) ----
SPRITES = {}

for key, p in PLANT_ALL.items():
    if p["idle"] and p["idle_cfg"]:
        SPRITES[key + "_idle"] = {
            "file": p["idle"], "cols": p["idle_cfg"]["cols"],
            "rows": p["idle_cfg"]["rows"], "fps": p["idle_cfg"]["fps"],
            "scale": p["idle_cfg"]["scale"], "note": p["name"] + " - 待机",
        }
    if p["attack"] and p["attack_cfg"]:
        SPRITES[key + "_attack"] = {
            "file": p["attack"], "cols": p["attack_cfg"]["cols"],
            "rows": p["attack_cfg"]["rows"], "fps": p["attack_cfg"]["fps"],
            "scale": p["attack_cfg"]["scale"], "note": p["name"] + " - 攻击",
        }

for key, z in ZOMBIE_ALL.items():
    if z["walk"] and z["walk_cfg"]:
        SPRITES[key + "_walk"] = {
            "file": z["walk"], "cols": z["walk_cfg"]["cols"],
            "rows": z["walk_cfg"]["rows"], "fps": z["walk_cfg"]["fps"],
            "scale": z["walk_cfg"]["scale"], "note": z["name"] + " - 行走",
        }
    if z["attack"] and z["attack_cfg"]:
        SPRITES[key + "_attack"] = {
            "file": z["attack"], "cols": z["attack_cfg"]["cols"],
            "rows": z["attack_cfg"]["rows"], "fps": z["attack_cfg"]["fps"],
            "scale": z["attack_cfg"]["scale"], "note": z["name"] + " - 攻击",
        }


# ---- 辅助函数 ----
def get_sprite(key):
    """获取精灵完整配置"""
    s = SPRITES[key]
    return {
        "path":  s["file"],
        "cols":  s["cols"],
        "rows":  s["rows"],
        "fps":   s.get("fps", DEFAULT_FPS),
        "scale": s.get("scale", DEFAULT_SCALE),
        "note":  s["note"],
    }


# ---- 关卡加载 ----
import json, os

def load_level(level_name="level_1-1"):
    """加载关卡数据（JSON 格式）"""
    base = os.path.join(os.path.dirname(__file__), "..", "data", level_name)
    with open(os.path.join(base, "summary.json"), encoding="utf-8") as f:
        summary = json.load(f)
    with open(os.path.join(base, "waves.json"), encoding="utf-8") as f:
        waves = json.load(f)
    return {
        "chapter":        summary["chapter"],
        "stage":          summary["stage"],
        "name":           summary["name"],
        "map":            summary["map"],
        "total_zombies":  summary["total_zombies"],
        "total_waves":    summary["total_waves"],
        "count":          summary["count"],
        "total_time":     summary.get("total_time", 0),
        "waves":          waves["waves"],
    }

