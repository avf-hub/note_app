from pathlib import Path

import shutil

from note_app.domain import Folder
from note_app.repositories.base_folder_repository import BaseFolderRepository


class FolderRepository(BaseFolderRepository):
    def __init__(self, base_path: Path):
        self.base_path = base_path.resolve()

    def get_folders_by_path(self, path: Path) -> list[Folder]:
        """Получение директорий"""
        path = path.resolve()
        self._check_path(path)

        folders: list[Folder] = []

        for sub_path in path.iterdir():
            if sub_path.is_dir() and not sub_path.name.startswith("."):
                folders.append(Folder(name=sub_path.name, path=sub_path))
        return sorted(folders, key=lambda folder: folder.name)

    def create_folder(self, path: Path, name: str) -> Folder:
        """Создание директории"""
        self._check_path(path)

        if path.name or "/" in path.name or "\\" in path.name:
            raise ValueError("Invalid folder name")

        path.mkdir(parents=True, exist_ok=False)
        return Folder(name=name, path=path)


    def delete_folder(self, folder: Folder) -> None:
        """Удаление папки"""
        path = Folder.path.resolve()
        self._check_path(path)

        if path == self.base_path:
            raise ValueError("Can't delete base folder")

        shutil.rmtree(path)

    def _check_path(self, path: Path):
        """Проверка пути"""
        if not path.exists() or not path.is_dir():
            raise ValueError(f"Folder {path} does not exist")

        if self.base_path not in path.parents and path != self.base_path:
            raise ValueError(f"Accessing folder {path} is not allowed")
