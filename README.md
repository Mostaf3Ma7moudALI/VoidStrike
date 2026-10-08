# VoidStrike

A 2D Asteroids-style shooter built with `pygame`. Fly a triangular ship, dodge and split asteroids, shoot them for score events. Logs game state for testing/debugging.

## Requirements

* Python `>=3.13` (see `.python-version`)
* `pygame==2.6.1` (see `pyproject.toml` / `uv.lock`)
* `uv` recommended

## Install

```sh
# clone
git clone git@github.com:Mostaf3Ma7moudALI/VoidStrike.git
cd VoidStrike

# install deps
uv sync
```

Alternative without `uv`:

```sh
python -m venv .venv
source .venv/bin/activate
pip install pygame==2.6.1
```

## How to use / Run

```sh
uv run main.py
# or:
# python main.py
```

* A black `1280x720` window opens at 60 FPS (`constants.py:1-2`, `main.py:54`).
* Close with window X button (`pygame.QUIT` in `main.py:34-36`) or `Ctrl+C` in terminal.
* On player-asteroid collision: prints `Game over!` and exits (`main.py:47-50`).

### Controls (`player.py:28-43`)

| Key | Action |
|-----|--------|
| `W` | Thrust forward (`PLAYER_SPEED = 200`) |
| `S` | Thrust backward |
| `A` | Rotate left (`PLAYER_TURN_SPEED = 300`) |
| `D` | Rotate right |
| `SPACE` | Shoot (cooldown `0.3s`, speed `500`, radius `5`) |

Shoot spawns a `Shot` at ship position with velocity `Vector2(0,1).rotate(rotation) * PLAYER_SHOOT_SPEED` (`player.py:51-53`).

### Rules

* Asteroids spawn from screen edges every `0.8s` with speed `40-100` (`asteroidfield.py:47-59`, `constants.py:9`).
* Sizes: `20 * kind`, kinds `1-3`, max `60` (`constants.py:7-10`).
* Shot + asteroid -> `asteroid_shot` event, asteroid `split()` into 2 faster children, bullet removed (`main.py:42-46`, `asteroid.py:22-34`).
* Split below `ASTEROID_MIN_RADIUS` just despawns.
* Player + asteroid -> `player_hit` event, exit.

## Project structure

```
main.py           game loop, groups, collision, drawing
player.py         Player(CircleShape): triangle, move/rotate/update/shoot
asteroid.py       Asteroid(CircleShape): move, split
asteroidfield.py  spawner on 4 screen edges
shot.py           Shot(CircleShape): circle, linear move
circleshape.py    base CircleShape(Sprite): position/velocity/radius, collides_with()
constants.py      screen, speeds, radii, spawn rate, cooldown
logger.py         log_state() per-second snapshot, log_event()
pyproject.toml    deps, requires-python >=3.13
```

Groups in `main.py:19-26`:

* `updatable`, `drawable`, `asteroids`, `shots`
* `Player.containers = (updatable, drawable)`
* `Asteroid.containers = (asteroids, updatable, drawable)`
* `Shot.containers = (shots, updatable, drawable)`

Update order per frame: `log_state()` -> events -> `updatable.update(dt)` -> collisions -> `draw` -> `flip()` -> `dt = clock.tick(60)/1000`.

## Tuning (`constants.py`)

```python
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_RADIUS = 20
PLAYER_SPEED = 200
PLAYER_TURN_SPEED = 300
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN_SECONDS = 0.3
SHOT_RADIUS = 5
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
```

## Features coming soon

* Add a scoring system
* Implement multiple lives and respawning
* Add an explosion effect for the asteroids
* Add acceleration to the player movement
* Make the objects wrap around the screen instead of disappearing
* Add a background image
* Create different weapon types
* Make the asteroids lumpy instead of perfectly round
* Make the ship have a triangular hit box instead of a circular one
* Add a shield power-up
* Add a speed power-up
* Add bombs that can be dropped
