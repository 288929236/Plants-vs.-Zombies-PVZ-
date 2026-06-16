# Plants vs Zombies - Python Clone

A Plants vs Zombies fan game built with pure Python + Pygame (SDL2).

> Non-commercial fan remake for learning purposes.

[GitHub](https://github.com/288929236/Plants-vs.-Zombies-PVZ-.git)

## Quick Start

```bash
pip install pygame Pillow
python main.py
```

## Scenes

### 1. Loading Screen
Splash screen with rotating sun rays animation and progress bar.
- Preloads ~84 images (home UI, 48 plant covers, 3 zombie covers, map, etc.)
- `precompute`: scales + crops all buttons, frees original large images
- Prints total load time in terminal

### 2. Home Screen
14 interactive buttons with pixel-level hover glow via `pygame.mask`.
- Button 1: enter battle preparation
- Buttons 12-13: open info popups
- Button 14 / ESC: open quit popup (highest priority overlay)
- All button surfaces cached after first creation — instant transitions

### 3. Battle Preparation
48 plant cards (6 rows x 8 cols) in a sliding plant box.
- Click card to select (max 10) — fly animation to top bar
- Click selected card to deselect — fly back animation
- START button: begins battle (exit animation)
- Menu button (top-right): return to home
- Arrow button (bottom-right): toggles plant box open/close with map scroll
- Zombie preview: 6 random zombies displayed on map

### 4. Battle Scene
Map + countdown + falling suns.
- Countdown: "Prepare!" -> "3" -> "2" -> "1" -> "Go!"
- Sun: spawns every 3s, falls 5s, lives 10s, click to collect (+25)
- Sun animation: 29-frame GIF extracted via PIL
- ESC quit popup

## Architecture

```
main.py              Entry point, DPI aware, dt cap
asset_manager.py     Image load/cache, map crop, bg fit
config/
  plants.py          48 plant definitions
  zombies.py         3 zombie definitions
  maps.py            4 maps (day/night/pool/roof)
  settings.py        UI state, window config
comment/
  button.py          make_hover, crop_visible, pixel_hit
  popup.py           build_popup, draw_popup, hit_popup_btn (cached)
pages/
  loading_page.py    Animated splash + asset preload + button precompute
  home_page.py       HomePage (14 buttons, popups, cached)
  prepare_page.py    PreparePage (48 cards, toggle, fly anim)
  battle_page.py     BattlePage (map, countdown, sun)
data/                Level JSON (level_1-1 ~ 1-6)
store/               Save + selected plants
docs/                Developer logs
images/              Sprites, maps, UI
```

## Memory & Performance

| Optimization | Before | After | Reduction |
|-------------|--------|-------|-----------|
| Button crop_visible | 2560x1600 RGBA (~16MB) | ~200x160 avg (~128KB) | 99% |
| Plant card pre-scale | Per-frame smoothscale (48x) | Init once, draw blit | 48x faster |
| 3-level cache | Recompute every page switch | Instant cache hit | ~0ms |
| Image resize | 10240x6400 originals (~250MB) | 2560x1600 (~16MB) | 94% |

### Cache Levels

| Cache | Location | Stores | Freed after |
|-------|----------|--------|-------------|
| Image | asset_manager._cache | Raw images | N/A (shared) |
| Popup | comment.popup._popup_cache | Scaled popup surfaces | Never |
| Page | home/prepare module cache | Full button sets | Never |

### Top 10 Plant Covers

| Peashooter | Sunflower | Cherry Bomb | Wall-nut | Potato Mine |
|------------|-----------|-------------|----------|-------------|
| <img src="images/plants_cover/peashooter.jpg" width="90"> | <img src="images/plants_cover/sunflower.jpg" width="90"> | <img src="images/plants_cover/cherry_bomb.jpg" width="90"> | <img src="images/plants_cover/wall_nut.jpg" width="90"> | <img src="images/plants_cover/potato_mine.jpg" width="90"> |
| **Snow Pea** | **Chomper** | **Repeater** | **Puff-shroom** | **Sun-shroom** |
| <img src="images/plants_cover/snow_pea.jpg" width="90"> | <img src="images/plants_cover/chomper.jpg" width="90"> | <img src="images/plants_cover/repeater.jpg" width="90"> | <img src="images/plants_cover/puff_shroom.jpg" width="90"> | <img src="images/plants_cover/sun_shroom.jpg" width="90"> |

### Zombie Covers

| Normal | Conehead | Buckethead |
|--------|----------|------------|
| <img src="images/zombies_cover/zombie.png" width="100"> | <img src="images/zombies_cover/conehead.png" width="100"> | <img src="images/zombies_cover/buckethead.png" width="100"> |

## Plant System (48 total)

24 base + 23 advanced + coin_magnet. All cover images in JPG.

| Category | Count | Examples |
|----------|-------|----------|
| Shooters | 9 | Peashooter, Repeater, Gatling Pea, Snow Pea, etc. |
| Producers | 3 | Sunflower, Sun-shroom, Twin Sunflower |
| Explosives | 4 | Cherry Bomb, Potato Mine, Doom-shroom, Jalapeno |
| Defensive | 5 | Wall-nut, Tall-nut, Pumpkin, Garlic, Umbrella Leaf |
| Special | 6 | Lily Pad, Flower Pot, Coffee Bean, Plantern, Blover, Gold Magnet |
| Insta-kill | 3 | Chomper, Chomper2, Squash |
| Catapults | 3 | Cabbage-pult, Kernel-pult, Melon-pult |
| Ground | 3 | Spikeweed, Spikerock, Torchwood |
| Mushrooms | 7 | Puff-shroom, Fume-shroom, Scaredy-shroom, etc. |
| Aquatic | 3 | Sea-shroom, Sea Soldier, Cattail |
| Others | 2 | Cob Cannon, Coin Magnet |

Full stats: 300-8000 HP, 0-1800 ATK, 0-500 Sun cost



| Key | Name | HP | ATK |
|-----|------|----|-----|
| zombie | Normal Zombie | 200 | 100 |
| conehead | Conehead Zombie | 560 | 100 |
| buckethead | Buckethead Zombie | 1300 | 100 |

## Controls

| Action | Input |
|--------|-------|
| Start game | Click START button (home) |
| Open popup | Click buttons 12-14 (home) |
| Quit popup | ESC key (all pages) |
| Toggle plant box | Click arrow button (prepare) |
| Collect sun | Click sun sprite (battle) |
| Debug coords | Mouse click prints console |

## Technical

- Window: NOFRAME fills display, DPI-aware, height-based layout
- Animations: ease-in-out (entrance), ease-out (toggle/fly/collect)
- dt cap: `min(clock.tick(60), 50)` prevents first-frame spike
- Mask: pixel-level hit detection for irregular button shapes

## Level Data

```
data/level_1-N/
  summary.json    {chapter, stage, name, map, total_zombies, total_waves, count}
  waves.json      {waves: [{wave, zombies: [{type, row, time}]}]}
```

## Save API

```python
import store.save as sv
sv.current_level()                 # "level_1-1"
sv.save(chapter, stage)            # Write progress
sv.record_pass(level, seconds)     # Record clear time
```
