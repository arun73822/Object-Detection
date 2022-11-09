from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Data_Ingestion_Artifact:
    train_file_path: Path
    test_file_path: Path