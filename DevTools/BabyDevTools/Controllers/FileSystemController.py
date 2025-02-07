import os
from pathlib import Path


class FileSystemController:

    def __init__(self):
        self.path = ''
        pass

    def set_path(self, path: str):
        self.path = path

    def get_folder_list(self):
        return [d for d in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, d))]

    def list_files(self):
        return [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]

    def list_files_and_folders(self):
        content = {"folders": [], "files": []}

        for item in os.listdir(self.path):
            full_path = os.path.join(self.path, item)
            if os.path.isdir(full_path):
                content["folders"].append(item)
            elif os.path.isfile(full_path):
                content["files"].append(item)

        return content
