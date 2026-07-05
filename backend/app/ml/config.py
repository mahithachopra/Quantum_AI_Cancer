from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

OUTPUT_DIR = PROJECT_ROOT / "backend" / "app" / "ml" / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)