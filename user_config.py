import json
from pathlib import Path

class user_config:
    def __init__(self):
        self.file_location = Path("configuration.JSON")

    def load_from_file(self):
        """Loads data from a JSON file if it exists."""
        if self.file_location.exists():
            with self.file_location.open('r') as file:
                return json.load(file)
        else:
            print(f"Eror: FILE_PATH is incompatible")
            return None
