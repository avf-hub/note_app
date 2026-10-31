from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from note_app.domain import Folder


class BaseRepository(ABC):
    @abstractmethod
    def get_all_folders(self) -> List[Folder]:
        pass

    @abstractmethod
    def get_folder_by_path(self, path: Path) -> Folder:
        pass

    @abstractmethod
    def create_folder(self, name: str) -> Folder:
        pass

    @abstractmethod
    def delete_folder(self, folder: Folder) -> None:
        pass