from pathlib import Path

from note_app.domain import Folder
from note_app.repositories.base_folder_repository import BaseRepository


class FolderRepository(BaseRepository):
    def __init__(self, base_path: Path):
        self.base_path = base_path.resolve()

    def get_folders_by_path(self, path: Path) -> list[Folder]:
        path = path.resolve()

        if not path.exists() or not path.is_dir():
            raise ValueError(f"Folder {path} does not exist")

        if self.base_path not in path.parents and path != self.base_path:
            raise ValueError(f"Accessing folder {path} is not allowed")

        folders: list[Folder] = []

        for sub_path in path.iterdir():
            if sub_path.is_dir() and not sub_path.name.startswith("."):
                folders.append(Folder(name=sub_path.name, path=sub_path))
        return sorted(folders, key=lambda folder: folder.name)
