import customtkinter
import os
from Controllers.FileSystemController import FileSystemController
from typing import Any


class SelectWorld:

    def __init__(self, master: Any):
        if os.name == "nt":  # Windows
            self.worlds_path = os.path.join(os.getenv("APPDATA"), ".minecraft", "saves")
        else:
            self.worlds_path = os.path.join(os.path.expanduser("~"), ".minecraft", "saves")

        self.general_frame = customtkinter.CTkFrame(master)
        pass

    def place(self, **kwargs):
        self.general_frame.place(**kwargs)

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def read_worlds_folders(self):
        file_system_controller = FileSystemController()
        if os.path.exists(self.worlds_path):
            file_system_controller.set_path(self.worlds_path)
            worlds = file_system_controller.get_folder_list()
        else:
            return None
        pass

