import customtkinter
from typing import Any


class EditorWorldExport:

    def __init__(self,
                 master: Any,
                 core: Any
                 ):

        self.general_frame = customtkinter.CTkFrame(master)

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def unpack(self):
        self.general_frame.pack_forget()
