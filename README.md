# AssetLoader

A basic, object-oriented asset loader for Autodesk Maya (2024), with ShotGrid integration.

This tool is my first step into building production-facing pipeline utilities as a Pipeline TD. It focuses on loading assets via Maya ASCII (`.ma`) or Alembic (`.abc`) files, with support for referencing where needed. It’s intended as a proof-of-concept for future iterations of a more complete pipeline toolset.

## 🔧 Features

- Loads assets from a structured project directory.
- Supports both `.ma` and `.abc` file formats.
- Option to import assets or load them as references.
- Integrates with ShotGrid for asset information retrieval.
- Clean object-oriented structure for extensibility and clarity.

## 💡 Usage

The entry point is `main.py`. Run it within a Maya Python environment:

```python
import main
main.run()
```

Before launching, make sure Maya is configured to run custom Python scripts and has access to ShotGrid (if enabled).

> Note: `maya.cmds` and `shotgun_api3` are required. Ensure they are accessible in your Python environment.

## 📁 Project Structure

```
AssetLoader/
│
├── core/               # Core functionality (loading, referencing, file management)
├── interface/          # UI components (WIP or placeholders)
├── utils/              # Utility functions (pathing, ShotGrid, etc.)
├── main.py             # Entry point
├── README.md           # This file
└── TODO.md             # Development roadmap
```

## ⚙️ Dependencies

- Autodesk Maya 2024
- Python 3 (Maya's embedded interpreter)
- ShotGrid API (`shotgun_api3`) if ShotGrid integration is used

## 🗒️ Notes

This loader is intentionally minimal. It’s built to demonstrate:

- Solid code structure over complete functionality
- My familiarity with Maya’s Python API and ShotGrid integration
- An early, honest iteration in building production tools from scratch

## 📬 Contact

If you're a fellow TD, recruiter, or pipeline developer interested in collaboration or feedback, feel free to reach out via GitHub or LinkedIn.
