import os

import customtkinter
from typing import Any
from Views.components.CanvasButton import CanvasButton
from PIL import Image, ImageTk
from Views.Modules.EditorWorldExport import EditorWorldExport
from Views.Modules.EditorBabyBottleModule import EditorBabyBottleModule


class EditorMain:

    def __init__(self, master: Any, core: Any):

        self.general_frame = customtkinter.CTkFrame(master, fg_color='#e1d1b8')
        self.world = ''

        self.core = core

        sidebar_frame = customtkinter.CTkFrame(self.general_frame)
        sidebar_frame.pack(padx=5, pady=5, fill='y', side=customtkinter.LEFT)

        self.module_frame = customtkinter.CTkFrame(self.general_frame, fg_color='#6e5124')
        self.module_frame.pack(padx=5, pady=5, fill='both', expand=True, side=customtkinter.RIGHT)

        self.sidebar_icons = []

        actual_folder = os.path.dirname(__file__)
        parent_folder = os.path.dirname(actual_folder)

        toy_image_path = os.path.join(parent_folder, "resources/icons", "toy.png")
        bib_image_path = os.path.join(parent_folder, "resources/icons", "bib.png")
        diaper_image_path = os.path.join(parent_folder, "resources/icons", "diaper.png")
        feeding_bottle_image_path = os.path.join(parent_folder, "resources/icons", "feeding-bottle.png")
        pacy_image_path = os.path.join(parent_folder, "resources/icons", "pacy.png")

        pencils_bitmap = Image.open(toy_image_path)
        bib_bitmap = Image.open(bib_image_path)
        diaper_bitmap = Image.open(diaper_image_path)
        feeding_bottle_bitmap = Image.open(feeding_bottle_image_path)
        pacy_bitmap = Image.open(pacy_image_path)

        pencils_bitmap = pencils_bitmap.resize((64, 64))
        bib_bitmap = bib_bitmap.resize((64, 64))
        diaper_bitmap = diaper_bitmap.resize((64, 64))
        feeding_bottle_bitmap = feeding_bottle_bitmap.resize((64, 64))
        pacy_bitmap = pacy_bitmap.resize((64, 64))

        self.pencils_img_tk = ImageTk.PhotoImage(pencils_bitmap)
        self.bib_img_tk = ImageTk.PhotoImage(bib_bitmap)
        self.diaper_img_tk = ImageTk.PhotoImage(diaper_bitmap)
        self.feeding_bottle_img_tk = ImageTk.PhotoImage(feeding_bottle_bitmap)
        self.pacy_img_tk = ImageTk.PhotoImage(pacy_bitmap)

        self.sidebar_icons.append(self.pencils_img_tk)
        self.sidebar_icons.append(self.bib_img_tk)
        self.sidebar_icons.append(self.diaper_img_tk)
        self.sidebar_icons.append(self.feeding_bottle_img_tk)
        self.sidebar_icons.append(self.pacy_img_tk)

        export_module_button = CanvasButton(sidebar_frame, width=64, height=64, fg_color='#808b96',
                                            command=lambda: self.show_export_module())
        export_module_button.pack(padx=2, pady=2)
        export_module_button.get_canvas().create_image(32, 32, image=self.pencils_img_tk)

        bib_module_button = CanvasButton(sidebar_frame, width=64, height=64, fg_color='#808b96')
        bib_module_button.pack(padx=2, pady=2)
        bib_module_button.get_canvas().create_image(32, 32, image=self.bib_img_tk)

        diaper_module_button = CanvasButton(sidebar_frame, width=64, height=64, fg_color='#808b96')
        diaper_module_button.pack(padx=2, pady=2)
        diaper_module_button.get_canvas().create_image(32, 32, image=self.diaper_img_tk)

        feeding_bottle_module_button = CanvasButton(sidebar_frame, width=64, height=64, fg_color='#808b96',
                                                    command=lambda: self.show_baby_bottle_module())
        feeding_bottle_module_button.pack(padx=2, pady=2)
        feeding_bottle_module_button.get_canvas().create_image(32, 32, image=self.feeding_bottle_img_tk)

        pacy_module_button = CanvasButton(sidebar_frame, width=64, height=64, fg_color='#808b96')
        pacy_module_button.pack(padx=2, pady=2)
        pacy_module_button.get_canvas().create_image(32, 32, image=self.pacy_img_tk)

        self.baby_bottle_module = EditorBabyBottleModule(self.module_frame, core, self)

        self.editor_world_export_module = EditorWorldExport(self.module_frame, core)
        self.show_export_module()

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def unpack_all_modules(self):
        self.editor_world_export_module.unpack()
        self.baby_bottle_module.unpack()
        pass

    def show_export_module(self):
        self.unpack_all_modules()
        self.editor_world_export_module.pack(padx=2, pady=2, fill='both', expand=True)
        pass

    def show_baby_bottle_module(self):
        self.unpack_all_modules()
        self.baby_bottle_module.pack(padx=2, pady=2, fill='both', expand=True)

    def set_world(self, world: str):
        self.world = world
        pass
