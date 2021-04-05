from pathlib import Path

_this_file = Path(__file__).resolve()

DIR_REPO = _this_file.parent.parent.parent.resolve()

DIR_CONFIG = DIR_REPO / "config"
DIR_IDEA = DIR_REPO / ".idea"
DIR_SRC = DIR_REPO / "src"
DIR_TESTS = DIR_REPO / "tests"

DIR_FRAMEWORK = DIR_SRC / "framework"
DIR_SCRIPTS = DIR_SRC / "scripts"
DIR_TEMPLATES = DIR_SRC / "main" / "templates"

DIR_STORAGE = DIR_REPO / "storage"
DIR_STORAGE.mkdir(exist_ok=True)

DIR_PROJECT = DIR_SRC / "project"
