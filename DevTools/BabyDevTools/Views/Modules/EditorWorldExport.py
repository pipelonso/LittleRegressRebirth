import customtkinter
from typing import Any


class EditorWorldExport:

    def __init__(self,
                 master: Any,
                 core: Any
                 ):

        self.master = master
        self.core = core

        self.general_frame = customtkinter.CTkFrame(master)

        self.assets_template_name = 'LR2'
        self.compile_folder = 'out'

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def unpack(self):
        self.general_frame.pack_forget()
