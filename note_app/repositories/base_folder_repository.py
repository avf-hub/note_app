from abc import ABC, abstractmethod
from pathlib import Path

from note_app.domain import Folder


class BaseRepository(ABC):
    @abstractmethod
    def get_folders_by_path(self, path: Path) -> list[Folder]:
        pass

    @abstractmethod
    def create_folder(self, name: str) -> Folder:
        pass

    @abstractmethod
    def delete_folder(self, folder: Folder) -> None:
        pass
