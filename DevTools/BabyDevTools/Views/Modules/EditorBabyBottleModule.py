import customtkinter
from typing import Any


class EditorBabyBottleModule:

    def __init__(self,
                 master: Any,
                 core: Any
                 ):
        self.general_frame = customtkinter.CTkFrame(master)

        header_frame = customtkinter.CTkFrame(self.general_frame)
        header_frame.pack(padx=2, pady=2, fill='x')

        header_tittle = customtkinter.CTkLabel(header_frame, text='Baby bottle Manager')
        header_tittle.pack(padx=2, pady=2, fill='x')

        content_frame = customtkinter.CTkFrame(self.general_frame)
        content_frame.pack(padx=2, pady=2, fill='both', expand=True)

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def unpack(self):
        self.general_frame.pack_forget()
