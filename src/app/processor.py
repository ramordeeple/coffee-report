import csv
from pathlib import Path
from typing import List, Dict

from src.domain.constants import CSV_EXTENSION, ENCODING


class DataProcessor:
    @staticmethod
    def collect_data(paths: List[str]) -> List[Dict]:
        combined_data = []
        for p in paths:
            path = Path(p)
            # Если передается папка, то берутся все .csv из нее, если 1 файл - только его
            files = path.glob(f"*{CSV_EXTENSION}") if path.is_dir() else [path]

            for file_path in files:
                if file_path.suffix == CSV_EXTENSION and file_path.exists():
                    with open(file_path, mode='r', encoding=ENCODING) as f:
                        reader = csv.DictReader(f)
                        combined_data.extend(list(reader))

        return combined_data