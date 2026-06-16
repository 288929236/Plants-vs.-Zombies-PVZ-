# ============================================
#  植物配置 —— 封面 / 待机 / 攻击 / 属性
# ============================================
#
#  字段:
#    cover:   封面图路径  (images/plants_cover/)
#    idle:    待机动画路径 (images/plants_idle/)
#    attack:  攻击动画路径 (images/plants_attack/)
#    name:       中文名
#    attribute:  {hp:生命, atk:攻击, cd:冷却秒, cost:阳光}
#    idle_cfg:  {cols, rows, fps, scale}  待机动画
#    attack_cfg:{cols, rows, fps, scale}  攻击动画（无攻击则 None）
# ============================================================

ALL = {

    # ========== 基础植物 ==========

    "peashooter": {
        "cover":      "images/plants_cover/peashooter.jpg",
        "idle":       "images/plants_idle/peashooter_idle.png",
        "attack":     "images/plants_attack/peashooter_shoot.png",
        "name":       "豌豆射手",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 100},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 8, "rows": 2, "fps": 15, "scale": 2},
    },

    "sunflower": {
        "cover":      "images/plants_cover/sunflower.jpg",
        "idle":       "images/plants_idle/sunflower_idle.png",
        "attack":     None,
        "name":       "向日葵",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 50},
        "idle_cfg":   {"cols": 6, "rows": 3, "fps": 10, "scale": 2},
        "attack_cfg": None,
    },

    "cherry_bomb": {
        "cover":      "images/plants_cover/cherry_bomb.jpg",
        "idle":       "images/plants_idle/cherry_bomb_idle.png",
        "attack":     "images/plants_attack/cherry_bomb_explode.png",
        "name":       "樱桃炸弹",
        "attribute":  {"hp": 300, "atk": 1800, "cd": 50, "cost": 150},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 10, "scale": 2},
        "attack_cfg": {"cols": 7, "rows": 3, "fps": 14, "scale": 3},
    },

    "wall_nut": {
        "cover":      "images/plants_cover/wall_nut.jpg",
        "idle":       "images/plants_idle/wall_nut_idle.png",
        "attack":     None,
        "name":       "坚果墙",
        "attribute":  {"hp": 4000, "atk": 0, "cd": 30, "cost": 50},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8,  "scale": 2},
        "attack_cfg": None,
    },

    "potato_mine": {
        "cover":      "images/plants_cover/potato_mine.jpg",
        "idle":       "images/plants_idle/potato_mine_idle.png",
        "attack":     "images/plants_attack/potato_mine_explode.png",
        "name":       "土豆雷",
        "attribute":  {"hp": 300, "atk": 1800, "cd": 30, "cost": 25},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8,  "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 3, "fps": 12, "scale": 2},
    },

    "snow_pea": {
        "cover":      "images/plants_cover/snow_pea.jpg",
        "idle":       "images/plants_idle/snow_pea_idle.png",
        "attack":     "images/plants_attack/snow_pea_shoot.png",
        "name":       "寒冰射手",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 175},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 8, "rows": 2, "fps": 15, "scale": 2},
    },

    # ========== 新增植物 ==========

    "chomper": {
        "cover":      "images/plants_cover/chomper.jpg",
        "idle":       "images/plants_idle/chomper_idle.png",
        "attack":     "images/plants_attack/chomper_attack.png",
        "name":       "大嘴花",
        "attribute":  {"hp": 300, "atk": 1800, "cd": 7.5, "cost": 150},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 3, "fps": 14, "scale": 2},
    },

    "repeater": {
        "cover":      "images/plants_cover/repeater.jpg",
        "idle":       "images/plants_idle/repeater_idle.png",
        "attack":     "images/plants_attack/repeater_shoot.png",
        "name":       "双发射手",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 200},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 8, "rows": 2, "fps": 15, "scale": 2},
    },

    "puff_shroom": {
        "cover":      "images/plants_cover/puff_shroom.jpg",
        "idle":       "images/plants_idle/puff_shroom_idle.png",
        "attack":     "images/plants_attack/puff_shroom_shoot.png",
        "name":       "小喷菇",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 0},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 4, "rows": 2, "fps": 10, "scale": 2},
    },

    "sun_shroom": {
        "cover":      "images/plants_cover/sun_shroom.jpg",
        "idle":       "images/plants_idle/sun_shroom_idle.png",
        "attack":     None,
        "name":       "阳光菇",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 25},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "fume_shroom": {
        "cover":      "images/plants_cover/fume_shroom.jpg",
        "idle":       "images/plants_idle/fume_shroom_idle.png",
        "attack":     "images/plants_attack/fume_shroom_attack.png",
        "name":       "大喷菇",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 75},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 2},
    },

    "chomper2": {
        "cover":      "images/plants_cover/chomper2.jpg",
        "idle":       "images/plants_idle/chomper2_idle.png",
        "attack":     None,
        "name":       "吞噬者",
        "attribute":  {"hp": 300, "atk": 1800, "cd": 7.5, "cost": 75},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "hypno_shroom": {
        "cover":      "images/plants_cover/hypno_shroom.jpg",
        "idle":       "images/plants_idle/hypno_shroom_idle.png",
        "attack":     None,
        "name":       "魅惑菇",
        "attribute":  {"hp": 300, "atk": 0, "cd": 30, "cost": 75},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "scaredy_shroom": {
        "cover":      "images/plants_cover/scaredy_shroom.jpg",
        "idle":       "images/plants_idle/scaredy_shroom_idle.png",
        "attack":     "images/plants_attack/scaredy_shroom_shoot.png",
        "name":       "胆小菇",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 25},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 4, "rows": 2, "fps": 12, "scale": 2},
    },

    "ice_shroom": {
        "cover":      "images/plants_cover/ice_shroom.jpg",
        "idle":       "images/plants_idle/ice_shroom_idle.png",
        "attack":     "images/plants_attack/ice_shroom_attack.png",
        "name":       "寒冰菇",
        "attribute":  {"hp": 300, "atk": 20, "cd": 50, "cost": 75},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 3, "fps": 14, "scale": 3},
    },

    "doom_shroom": {
        "cover":      "images/plants_cover/doom_shroom.jpg",
        "idle":       "images/plants_idle/doom_shroom_idle.png",
        "attack":     "images/plants_attack/doom_shroom_explode.png",
        "name":       "毁灭菇",
        "attribute":  {"hp": 300, "atk": 1800, "cd": 50, "cost": 125},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 8, "rows": 4, "fps": 14, "scale": 4},
    },

    "lily_pad": {
        "cover":      "images/plants_cover/lily_pad.jpg",
        "idle":       "images/plants_idle/lily_pad_idle.png",
        "attack":     None,
        "name":       "荷叶",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 25},
        "idle_cfg":   {"cols": 2, "rows": 1, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "squash": {
        "cover":      "images/plants_cover/squash.jpg",
        "idle":       "images/plants_idle/squash_idle.png",
        "attack":     "images/plants_attack/squash_smash.png",
        "name":       "窝瓜",
        "attribute":  {"hp": 300, "atk": 1800, "cd": 30, "cost": 50},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 3},
    },

    "threepeater": {
        "cover":      "images/plants_cover/threepeater.jpg",
        "idle":       "images/plants_idle/threepeater_idle.png",
        "attack":     "images/plants_attack/threepeater_shoot.png",
        "name":       "三线豌豆",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 325},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 8, "rows": 2, "fps": 15, "scale": 2},
    },

    "sea_shroom": {
        "cover":      "images/plants_cover/sea_shroom.jpg",
        "idle":       "images/plants_idle/sea_shroom_idle.png",
        "attack":     None,
        "name":       "海草",
        "attribute":  {"hp": 300, "atk": 0, "cd": 30, "cost": 25},
        "idle_cfg":   {"cols": 2, "rows": 1, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "jalapeno": {
        "cover":      "images/plants_cover/jalapeno.jpg",
        "idle":       "images/plants_idle/jalapeno_idle.png",
        "attack":     "images/plants_attack/jalapeno_fire.png",
        "name":       "火爆辣椒",
        "attribute":  {"hp": 300, "atk": 1800, "cd": 50, "cost": 125},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 3, "fps": 14, "scale": 3},
    },

    "spikeweed": {
        "cover":      "images/plants_cover/spikeweed.jpg",
        "idle":       "images/plants_idle/spikeweed_idle.png",
        "attack":     "images/plants_attack/spikeweed_attack.png",
        "name":       "地刺",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 100},
        "idle_cfg":   {"cols": 4, "rows": 1, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 12, "scale": 2},
    },

    "torchwood": {
        "cover":      "images/plants_cover/torchwood.jpg",
        "idle":       "images/plants_idle/torchwood_idle.png",
        "attack":     None,
        "name":       "火炬树桩",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 175},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "tall_nut": {
        "cover":      "images/plants_cover/tall_nut.jpg",
        "idle":       "images/plants_idle/tall_nut_idle.png",
        "attack":     None,
        "name":       "高坚果",
        "attribute":  {"hp": 8000, "atk": 0, "cd": 30, "cost": 125},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    # ========== 第二波（23种） ==========

    "sea_soldier": {
        "cover":      "images/plants_cover/sea_soldier.jpg",
        "idle":       "images/plants_idle/sea_soldier_idle.png",
        "attack":     None,
        "name":       "水兵菇",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 0},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "plantern": {
        "cover":      "images/plants_cover/plantern.jpg",
        "idle":       "images/plants_idle/plantern_idle.png",
        "attack":     None,
        "name":       "灯笼",
        "attribute":  {"hp": 300, "atk": 0, "cd": 30, "cost": 25},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "cactus": {
        "cover":      "images/plants_cover/cactus.jpg",
        "idle":       "images/plants_idle/cactus_idle.png",
        "attack":     "images/plants_attack/cactus_shoot.png",
        "name":       "仙人掌",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 125},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 2},
    },

    "blover": {
        "cover":      "images/plants_cover/blover.jpg",
        "idle":       "images/plants_idle/blover_idle.png",
        "attack":     None,
        "name":       "三叶草",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 100},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "split_pea": {
        "cover":      "images/plants_cover/split_pea.jpg",
        "idle":       "images/plants_idle/split_pea_idle.png",
        "attack":     "images/plants_attack/split_pea_shoot.png",
        "name":       "双向射手",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 125},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 8, "rows": 2, "fps": 15, "scale": 2},
    },

    "starfruit": {
        "cover":      "images/plants_cover/starfruit.jpg",
        "idle":       "images/plants_idle/starfruit_idle.png",
        "attack":     "images/plants_attack/starfruit_shoot.png",
        "name":       "五角星",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 125},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 2},
    },

    "pumpkin": {
        "cover":      "images/plants_cover/pumpkin.jpg",
        "idle":       "images/plants_idle/pumpkin_idle.png",
        "attack":     None,
        "name":       "南瓜罩",
        "attribute":  {"hp": 4000, "atk": 0, "cd": 30, "cost": 125},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "magnet_shroom": {
        "cover":      "images/plants_cover/magnet_shroom.jpg",
        "idle":       "images/plants_idle/magnet_shroom_idle.png",
        "attack":     None,
        "name":       "磁力菇",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 100},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "cabbage_pult": {
        "cover":      "images/plants_cover/cabbage_pult.jpg",
        "idle":       "images/plants_idle/cabbage_pult_idle.png",
        "attack":     "images/plants_attack/cabbage_pult_throw.png",
        "name":       "卷心菜投手",
        "attribute":  {"hp": 300, "atk": 40, "cd": 7.5, "cost": 100},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 10, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 2},
    },

    "flower_pot": {
        "cover":      "images/plants_cover/flower_pot.jpg",
        "idle":       "images/plants_idle/flower_pot_idle.png",
        "attack":     None,
        "name":       "花盆",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 25},
        "idle_cfg":   {"cols": 2, "rows": 1, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "kernel_pult": {
        "cover":      "images/plants_cover/kernel_pult.jpg",
        "idle":       "images/plants_idle/kernel_pult_idle.png",
        "attack":     "images/plants_attack/kernel_pult_throw.png",
        "name":       "玉米投手",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 100},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 10, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 2},
    },

    "coffee_bean": {
        "cover":      "images/plants_cover/coffee_bean.jpg",
        "idle":       "images/plants_idle/coffee_bean_idle.png",
        "attack":     None,
        "name":       "咖啡豆",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 75},
        "idle_cfg":   {"cols": 2, "rows": 1, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "garlic": {
        "cover":      "images/plants_cover/garlic.jpg",
        "idle":       "images/plants_idle/garlic_idle.png",
        "attack":     None,
        "name":       "大蒜",
        "attribute":  {"hp": 400, "atk": 0, "cd": 7.5, "cost": 50},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "umbrella_leaf": {
        "cover":      "images/plants_cover/umbrella_leaf.jpg",
        "idle":       "images/plants_idle/umbrella_leaf_idle.png",
        "attack":     None,
        "name":       "萝卜伞",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 100},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "gold_magnet": {
        "cover":      "images/plants_cover/gold_magnet.jpg",
        "idle":       "images/plants_idle/gold_magnet_idle.png",
        "attack":     None,
        "name":       "金银花",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 50},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "melon_pult": {
        "cover":      "images/plants_cover/melon_pult.jpg",
        "idle":       "images/plants_idle/melon_pult_idle.png",
        "attack":     "images/plants_attack/melon_pult_throw.png",
        "name":       "西瓜投手",
        "attribute":  {"hp": 300, "atk": 80, "cd": 7.5, "cost": 300},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 10, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 2},
    },

    "gatling_pea": {
        "cover":      "images/plants_cover/gatling_pea.jpg",
        "idle":       "images/plants_idle/gatling_pea_idle.png",
        "attack":     "images/plants_attack/gatling_pea_shoot.png",
        "name":       "机枪豌豆",
        "attribute":  {"hp": 300, "atk": 20, "cd": 50, "cost": 250},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 12, "scale": 2},
        "attack_cfg": {"cols": 8, "rows": 2, "fps": 15, "scale": 2},
    },

    "twin_sunflower": {
        "cover":      "images/plants_cover/twin_sunflower.jpg",
        "idle":       "images/plants_idle/twin_sunflower_idle.png",
        "attack":     None,
        "name":       "双胞胎向日葵",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 150},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 10, "scale": 2},
        "attack_cfg": None,
    },

    "gloom_shroom": {
        "cover":      "images/plants_cover/gloom_shroom.jpg",
        "idle":       "images/plants_idle/gloom_shroom_idle.png",
        "attack":     "images/plants_attack/gloom_shroom_attack.png",
        "name":       "忧郁菇",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 150},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 2},
    },

    "cattail": {
        "cover":      "images/plants_cover/cattail.jpg",
        "idle":       "images/plants_idle/cattail_idle.png",
        "attack":     "images/plants_attack/cattail_shoot.png",
        "name":       "香蒲",
        "attribute":  {"hp": 300, "atk": 20, "cd": 7.5, "cost": 225},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 2},
    },

    "winter_melon": {
        "cover":      "images/plants_cover/winter_melon.jpg",
        "idle":       "images/plants_idle/winter_melon_idle.png",
        "attack":     "images/plants_attack/winter_melon_throw.png",
        "name":       "冰西瓜投手",
        "attribute":  {"hp": 300, "atk": 80, "cd": 7.5, "cost": 200},
        "idle_cfg":   {"cols": 4, "rows": 3, "fps": 10, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 14, "scale": 2},
    },

    "coin_magnet": {
        "cover":      "images/plants_cover/coin_magnet.jpg",
        "idle":       "images/plants_idle/coin_magnet_idle.png",
        "attack":     None,
        "name":       "吸金磁",
        "attribute":  {"hp": 300, "atk": 0, "cd": 7.5, "cost": 50},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": None,
    },

    "spikerock": {
        "cover":      "images/plants_cover/spikerock.jpg",
        "idle":       "images/plants_idle/spikerock_idle.png",
        "attack":     "images/plants_attack/spikerock_attack.png",
        "name":       "地刺王",
        "attribute":  {"hp": 300, "atk": 40, "cd": 7.5, "cost": 125},
        "idle_cfg":   {"cols": 4, "rows": 1, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 6, "rows": 2, "fps": 12, "scale": 2},
    },

    "cob_cannon": {
        "cover":      "images/plants_cover/cob_cannon.jpg",
        "idle":       "images/plants_idle/cob_cannon_idle.png",
        "attack":     "images/plants_attack/cob_cannon_shoot.png",
        "name":       "玉米加农炮",
        "attribute":  {"hp": 300, "atk": 1800, "cd": 50, "cost": 500},
        "idle_cfg":   {"cols": 4, "rows": 2, "fps": 8, "scale": 2},
        "attack_cfg": {"cols": 8, "rows": 4, "fps": 14, "scale": 4},
    },

}
