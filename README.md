# Exi_Bit
# 🎮 Exi_Bit

> **A modular, Python-based game engine built from the ground up.**

Exi_Bit is an open-source game engine project focused on providing a **simple, modular, customizable, and developer-friendly foundation for building games**.

The project is being developed with Python, with individual engine systems separated into independent modules such as rendering, input, physics, world management, and the core game loop.

---

## 🚀 Project Vision

Exi_Bit aims to become a lightweight and highly customizable game-engine framework that allows developers to:

- 🎮 Create and run games
- 🖥️ Build 2D and eventually 3D experiences
- 🎨 Manage rendering
- ⌨️ Handle keyboard, mouse, and controller input
- 🌍 Create and manage game worlds
- ⚙️ Implement physics and collision systems
- 📦 Manage game assets
- 🧩 Extend the engine with custom modules
- 🔧 Build games using a clean Python API

The long-term goal is to evolve Exi_Bit into a complete game-development ecosystem.

---

# 🏗️ Architecture

Exi_Bit follows a modular architecture:

```text
                    ┌───────────────────┐
                    │     Developer     │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    Game Project   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │     Exi_Bit       │
                    │    Game Engine    │
                    └─────────┬─────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
      ┌───────────┐    ┌───────────┐    ┌───────────┐
      │ Rendering │    │   Input   │    │  Physics  │
      └─────┬─────┘    └─────┬─────┘    └─────┬─────┘
            │                │                 │
            └────────────────┼─────────────────┘
                             ▼
                    ┌───────────────────┐
                    │   Game World      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Game Loop       │
                    └───────────────────┘
```

---

# 📁 Project Structure

```text
Exi_Bit/
│
├── exi_bit/
│   ├── engine/
│   │   ├── core.py
│   │   ├── game_loop.py
│   │   └── config.py
│   │
│   ├── rendering/
│   │   └── renderer.py
│   │
│   ├── input/
│   │   └── input_manager.py
│   │
│   ├── physics/
│   │   └── physics.py
│   │
│   ├── world/
│   │   └── world.py
│   │
│   └── assets/
│
├── examples/
│   └── basic_game.py
│
├── tests/
│
├── run.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# 🐍 Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Initial Rendering | Pygame |
| Physics | Custom Python system |
| Input | Pygame |
| Testing | Pytest |
| Package Management | pip |
| Build System | Python / pyproject.toml |
| Version Control | Git + GitHub |

---

# ⚡ Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/ttttttteeeeee/Exi_Bit.git
cd Exi_Bit
```

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Exi_Bit

```bash
python run.py
```

---

# 🎮 Creating Your First Game

Example:

```python
from exi_bit.engine.core import ExiBit


engine = ExiBit()

engine.run()
```

More examples will be added as the engine develops.

---

# 🧩 Core Engine Modules

### Engine Core

Responsible for coordinating the different engine systems.

```text
Engine
 ├── Game Loop
 ├── Rendering
 ├── Input
 ├── Physics
 ├── World
 └── Assets
```

### Rendering

Responsible for displaying game objects and scenes.

Future goals include:

- 2D rendering
- Sprite rendering
- Camera systems
- Animation
- 3D rendering
- Lighting

### Input

Handles interaction between the player and the game.

Planned support:

- Keyboard
- Mouse
- Controller
- Custom input mapping

### Physics

Responsible for:

- Collision detection
- Collision response
- Gravity
- Velocity
- Acceleration
- Rigid bodies

### World

Responsible for managing:

- Scenes
- Game objects
- Entities
- Components
- World state

---

# 🗺️ Roadmap

## Phase 1 — Foundation

- [x] Repository setup
- [x] Python architecture
- [ ] Engine core
- [ ] Game loop
- [ ] Configuration system

## Phase 2 — 2D Engine

- [ ] Pygame renderer
- [ ] Sprite system
- [ ] Camera
- [ ] Input manager
- [ ] Basic physics
- [ ] Collision detection
- [ ] Scene management

## Phase 3 — Developer Tools

- [ ] Asset manager
- [ ] Debug console
- [ ] Logging system
- [ ] Configuration editor
- [ ] Game project templates

## Phase 4 — Advanced Engine

- [ ] 3D rendering
- [ ] 3D physics
- [ ] Animation system
- [ ] Lighting
- [ ] Audio
- [ ] Particle system

## Phase 5 — Exi_Bit Ecosystem

- [ ] Visual editor
- [ ] Plugin system
- [ ] Game packaging
- [ ] Executable generation
- [ ] Documentation
- [ ] Developer SDK

---

# 🔐 Security

Security is an important part of Exi_Bit's development.

The engine will follow secure development practices including:

- Dependency management
- Input validation
- Safe asset handling
- Secure configuration
- Dependency updates
- Code reviews
- Automated testing

**Never commit passwords, API keys, tokens, or other secrets to the repository.**

Use environment variables for sensitive configuration.

---

# 🧪 Testing

Tests will be maintained inside:

```text
tests/
```

Run the test suite with:

```bash
pytest
```

---

# 🤝 Contributing

Contributions are welcome.

Typical contribution workflow:

```text
Fork
  ↓
Clone
  ↓
Create Branch
  ↓
Make Changes
  ↓
Test
  ↓
Commit
  ↓
Push
  ↓
Pull Request
```

Example:

```bash
git checkout -b feature/my-feature

git add .

git commit -m "Add my feature"

git push origin feature/my-feature
```

Then open a Pull Request on GitHub.

---

# 📜 License

The repository currently includes the Apache License 2.0 in `LICENSE`. Keep the license text and required notices when distributing the project.

---

# 👨‍💻 Project

**Exi_Bit**

An open-source game engine project by **tèE_J**.

GitHub:

https://github.com/ttttttteeeeee/Exi_Bit

---

> **Exi_Bit — Build. Create. Play.**


---

# Current Implementation Status

**Blunt status:** Exi_Bit is still a scaffold, not yet a runnable Python game engine. The Python modules shown in the architecture and roadmap are planned work, not implemented files.

## Play the browser demo

Open [`examples/web_platformer/index.html`](examples/web_platformer/index.html) in a modern browser. It uses HTML, CSS, and JavaScript and needs no installation. Controls are documented in [the demo README](examples/web_platformer/README.md).

**Important:** the browser demo does not use the Python/Pygame engine. It is kept as a standalone example while the Python engine is developed.

## File-by-file project review

See [`docs/PROJECT_AUDIT.md`](docs/PROJECT_AUDIT.md) for the blunt assessment of existing files, what to keep/remove/defer, recommended Python package structure, and the exact responsibility of each planned module.
