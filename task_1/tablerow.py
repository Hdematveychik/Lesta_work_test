from dataclasses import dataclass


@dataclass
class TableRow:
    website: str
    popularity: str
    frontend: str
    backend: str
    database: str
    notes: str
