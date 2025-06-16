import tkinter

import customtkinter
from typing import Any
from Controllers.BabyBottleController import BabyBottleController


class EditorBabyBottleModule:

    def __init__(self,
                 master: Any,
                 core: Any,
                 editor: Any
                 ):

        self.core = core
        self.master = master
        self.editor = editor

        self.baby_bottle_controller = BabyBottleController()

        self.general_frame = customtkinter.CTkFrame(master)

        header_frame = customtkinter.CTkFrame(self.general_frame)
        header_frame.pack(padx=2, pady=2, fill='x')

        header_tittle = customtkinter.CTkLabel(header_frame, text='Baby bottle Manager')
        header_tittle.pack(padx=2, pady=2, fill='x')

        content_frame = customtkinter.CTkFrame(self.general_frame)
        content_frame.pack(padx=2, pady=2, fill='both', expand=True)

        control_bar_frame = customtkinter.CTkFrame(content_frame)
        control_bar_frame.pack(padx=2, pady=2, fill='x')

        register_texture_button = customtkinter.CTkButton(control_bar_frame, text='+ Add Texture')
        register_texture_button.pack(padx=2, pady=2, fill='x', side=tkinter.LEFT)

        generate_variations_button = customtkinter.CTkButton(control_bar_frame, text='generate variations',
                                                             command=lambda: self.generate_presets()
                                                             )
        generate_variations_button.pack(padx=2, pady=2, fill='x', side=tkinter.LEFT)

        existing_combinations_frame = customtkinter.CTkFrame(content_frame)
        existing_combinations_frame.pack(padx=2, pady=2, fill='both', side=tkinter.LEFT)

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def unpack(self):
        self.general_frame.pack_forget()

    def get_existing_bottles_in_world(self):
        world = self.editor.world
        pass

    def generate_presets(self):
        self.baby_bottle_controller.generate_empty_variations()
        self.baby_bottle_controller.generate_model_content()
        self.baby_bottle_controller.generate_crafting_content_exports()
        pass
