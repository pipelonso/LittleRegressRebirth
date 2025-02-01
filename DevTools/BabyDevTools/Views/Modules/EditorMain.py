import customtkinter
from typing import Any


class EditorMain:

    def __init__(self, master: Any, core: Any):

        self.general_frame = customtkinter.CTkFrame(master)
        self.world = ''

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def set_world(self, world: str):
        self.world = world
        pass
