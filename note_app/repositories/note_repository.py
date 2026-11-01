from pathlib import Path

from note_app.domain import Note
from note_app.repositories.base_note_repository import BaseNoteRepository


class NoteRepository(BaseNoteRepository):
    def __init__(self, base_path: Path):
        self.base_path = base_path.resolve()

    def get_notes_by_path(self, path: Path) -> list[Note]:
        """Получение заметок"""
        path = path.resolve()
        self._check_path(path)

        notes: list[Note] = []

        for sub_path in path.iterdir():
            if sub_path.is_file() and not sub_path.name.startswith(".") and sub_path.suffix == ".md":
                notes.append(Note(name=sub_path.name, path=sub_path))
        return sorted(notes, key=lambda note: note.name)

    def create_note(self, path: Path, name: str) -> Note:
        """Создание директории"""
        self._check_path(path)

        if path.name or "/" in path.name or "\\" in path.name:
            raise ValueError("Invalid note name")

        path.mkdir(parents=True, exist_ok=False)
        return Note(name=name, path=path)

    def delete_note(self, note: Note) -> None:
        """Удаление заметки"""
        path = note.path.resolve()
        self._check_path(path)
        path.unlink()

    def _check_path(self, path: Path):
        """Проверка пути"""
        if not path.exists() or not path.is_dir():
            raise ValueError(f"Note {path} does not exist")

        if self.base_path not in path.parents and path != self.base_path:
            raise ValueError(f"Accessing note {path} is not allowed")
