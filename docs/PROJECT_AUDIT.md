# Exi_Bit project audit and file placement

## Current status

This branch now contains an early Python/Pygame engine foundation plus the separate browser prototype. The Python implementation includes a fixed-timestep loop, keyboard input actions, rectangle physics, a horizontal camera renderer, a world interface, a playable Python platformer example, and starter physics tests.

This is a foundation, not a production-ready engine. The code still needs to be run on a local machine, tested across environments, and extended carefully. Audio, animation, asset loading, scene transitions, controller input, and an editor are not implemented.

## Existing files: keep, remove, or defer

- `LICENSE` — **Keep.** Apache License 2.0 is present. Retain its notices.
- `README.md` — **Keep and update.** It should reflect implemented behavior rather than long-term plans.
- `run.py` — **Keep.** It is now a thin launcher for the Python platformer example.
- Root `__init__.py` — **Not needed at repository root.** The actual package is `exi_bit/`; remove the root marker after checking whether you rely on it for another purpose.
- `include/exi/scenes/Cmakelists.txt` — **Defer or remove** unless a C++/CMake build is intentional. It is a one-byte placeholder; if CMake is adopted, use the conventional name `CMakeLists.txt`.
- `include/exi/scenes/exi_world.obj` — **Defer or remove.** Empty OBJ placeholder, not a usable model.
- `include/exi/scenes/exi_world.mtl` — **Defer or remove.** Empty material placeholder.
- `examples/web_platformer/index.html` — **Keep as a demo.** This is the browser prototype, separate from the Python engine.
- `examples/web_platformer/README.md` — **Keep.** Documents the browser demo.
- `requirements.txt` and `pyproject.toml` — **Keep.** They now declare Pygame and Python package metadata.

Do not delete placeholders blindly if you have local work that has not been pushed. On the inspected branch, the three files under `include/exi/scenes/` contain no usable implementation.

## Current Python structure

```text
exi_bit/
  __init__.py
  engine/
    __init__.py
    config.py       # Window/runtime configuration
    core.py         # Fixed-timestep loop and lifecycle
  input/
    __init__.py
    input_manager.py
  physics/
    __init__.py
    physics.py      # Body, gravity, axis-aligned collisions
  rendering/
    __init__.py
    renderer.py     # Drawing and horizontal camera
  world/
    __init__.py
    world.py        # Abstract scene/world contract
examples/
  __init__.py
  platformer.py    # First playable Python example
  web_platformer/
    index.html     # Separate HTML/CSS/JavaScript prototype
tests/
  __init__.py
  test_physics.py
requirements.txt
pyproject.toml
run.py
README.md
LICENSE
```

## Where code belongs

- `exi_bit/engine/core.py`: initialize Pygame, process events, run fixed-size simulation steps, render, and shut down. Keep level-specific rules out of the engine.
- `exi_bit/engine/config.py`: window dimensions/title, target render FPS, fixed update frequency, background color, and frame-time cap.
- `exi_bit/input/input_manager.py`: translate key events into named actions and distinguish held keys from one-shot presses.
- `exi_bit/physics/physics.py`: reusable body velocity, gravity, and axis-aligned platform collision. It should not know about scores, gems, or level completion.
- `exi_bit/rendering/renderer.py`: draw primitives and apply camera offsets. It should not update gameplay state.
- `exi_bit/world/world.py`: define the interface each scene implements with `update` and `render`.
- `examples/platformer.py`: platform geometry, player movement rules, level bounds, goal behavior, and game-specific HUD.
- `examples/web_platformer/index.html`: standalone browser game. Keep its JavaScript out of the Python modules.
- `tests/test_physics.py`: physics behavior checks, including landing, horizontal collision, and invalid time steps.
- `requirements.txt`: runtime dependencies. Current dependency: Pygame.
- `pyproject.toml`: package metadata, supported Python version, and build configuration.
- `run.py`: a minimal entry point only.

## The loop we should follow from here

1. Run the Python example locally and fix startup/runtime errors.
2. Run `python -m unittest discover -v` and resolve any failures.
3. Add a test before expanding collision behavior.
4. Add hazard/collectible entities and scene reset behavior.
5. Improve physics and camera, then add asset loading only when needed.
6. Review the README and update it in the same change as any user-visible feature.

Do not start a visual editor, plugin system, or 3D renderer before the 2D loop and tests are reliable.
