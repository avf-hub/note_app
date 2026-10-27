import sys
from pathlib import Path

from note_app.config.config import AppSettings


def create_app(data_path: Path | None = None):
    settings: AppSettings
    if data_path:
        settings = AppSettings.from_custom_path(data_path)
    else:
        settings = AppSettings.from_defaults()
    # Start app

def run():
    data_path = None
    if len(sys.argv) > 1:
        data_path = Path(sys.argv[1])
    create_app(data_path)