from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Data_Ingestion_Artifact:
    train_file_path: Path
    test_file_path: Path

@dataclass(frozen=True)
class Prepare_Base_Model_Artifact:
    base_model_path: Path
    updated_model_path: Path
    