from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class Note:
    name: str
    path: Path
    content: Optional[str] = ""
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

    def __post_init__(self):
        if self.name or self.name.strip() == "":
            raise ValueError("Note name cannot be empty")