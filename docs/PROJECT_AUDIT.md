# Exi_Bit audit and file placement

## Honest current status

Reviewed on the `main` branch: this repository is a scaffold, not a working Python game engine yet. The README describes modules and dependency files that do not currently exist. The browser platformer now lives separately at `examples/web_platformer/index.html`; it uses HTML, CSS, and JavaScript, not Python/Pygame.

## Existing files: keep, remove, or defer

- `LICENSE` — **Keep.** Apache License 2.0 is present. Retain its notices.
- `README.md` — **Keep and update.** Clearly distinguish implemented files from planned architecture.
- `run.py` — **Keep, implement later.** Make it a thin Python entry point. It is currently empty.
- Root `__init__.py` — **Not needed at repository root.** Python package markers should be inside packages such as `exi_bit/`; remove only after checking local intent/history.
- `include/exi/scenes/Cmakelists.txt` — **Defer or remove** unless a C++/CMake build is actually planned. It is a one-byte placeholder; if CMake is adopted, use the conventional name `CMakeLists.txt`.
- `include/exi/scenes/exi_world.obj` — **Defer or remove.** Empty OBJ placeholder, not a usable model.
- `include/exi/scenes/exi_world.mtl` — **Defer or remove.** Empty material placeholder.
- `examples/web_platformer/index.html` — **Keep as a demo.** It is the playable HTML/JavaScript prototype, isolated from the Python engine.
- `examples/web_platformer/README.md` — **Keep.** Demo run instructions and scope.

Do not delete placeholders blindly if you have local work that has not been pushed. Based on the currently visible main branch, the three files under `include/exi/scenes/` contain no usable implementation.

## Recommended Python engine structure

Create these files as the Python engine is implemented. Do not paste browser JavaScript into them.

```text
exi_bit/
  __init__.py
  engine/
    __init__.py
    core.py
    game_loop.py
    config.py
  rendering/
    __init__.py
    renderer.py
  input/
    __init__.py
    input_manager.py
  physics/
    __init__.py
    physics.py
  world/
    __init__.py
    world.py
  assets/
examples/
  basic_game.py
  platformer.py
tests/
  test_physics.py
  test_world.py
requirements.txt
pyproject.toml
run.py
README.md
LICENSE
```

## Exact code placement

- `exi_bit/engine/core.py`: engine facade; constructs and coordinates renderer, input, physics, world, and loop. No level-specific coordinates here.
- `exi_bit/engine/game_loop.py`: Pygame event processing, delta time, update/render cycle, shutdown.
- `exi_bit/engine/config.py`: window size/title, target FPS, and runtime defaults.
- `exi_bit/rendering/renderer.py`: create the Pygame display, draw objects/sprites, apply camera offset. Rendering should not decide whether a gem was collected.
- `exi_bit/input/input_manager.py`: convert Pygame keyboard/mouse events into actions such as left, right, and jump.
- `exi_bit/physics/physics.py`: reusable gravity, velocity, collision detection and collision response.
- `exi_bit/world/world.py`: entities and scene/world state; avoid platformer-specific HUD text here.
- `examples/platformer.py`: platform layout, hazards, collectibles, player behavior, HUD, and win/loss rules, using the engine API.
- `examples/basic_game.py`: smallest example that demonstrates public engine API.
- `tests/test_physics.py`: collision and gravity tests. `tests/test_world.py`: world/entity behavior tests.
- `requirements.txt`: only real Python runtime dependencies (initially Pygame if adopted). It does not install browser APIs.
- `pyproject.toml`: package metadata and build/dev-tool configuration, not gameplay logic.
- `run.py`: thin launcher. Do not put the whole engine in it.
- `examples/web_platformer/index.html`: the browser demo only. Its CSS and JavaScript are embedded in this single file for now.

## Sensible implementation order

1. Keep the browser demo separate and make the README truthful.
2. Implement a minimal Python/Pygame loop and renderer.
3. Add input handling.
4. Add reusable physics/collision.
5. Build a Python platformer example on top.
6. Add tests after the basic path runs.

Do not start a visual editor, plugin system, 3D renderer, or asset manager before the 2D loop works.
