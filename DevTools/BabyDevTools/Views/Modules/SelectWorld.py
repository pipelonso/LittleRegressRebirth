import customtkinter
import os
from Controllers.FileSystemController import FileSystemController
from typing import Any
from PIL import Image, ImageTk
from Views.Modules.EditorMain import EditorMain


class SelectWorld:

    def __init__(self, master: Any,
                 core: Any):

        self.core = core

        if os.name == "nt":  # Windows
            self.worlds_path = os.path.join(os.getenv("APPDATA"), ".minecraft", "saves")
        else:
            self.worlds_path = os.path.join(os.path.expanduser("~"), ".minecraft", "saves")

        self.general_frame = customtkinter.CTkFrame(master, fg_color='#e1d1b8')

        self.header_frame = customtkinter.CTkFrame(self.general_frame)
        self.header_frame.pack(padx=5, pady=4, fill='x')

        self.header_title = customtkinter.CTkLabel(self.header_frame, text='WORLDS LIST')
        self.header_title.pack(padx=2, pady=2, fill='x')

        self.content_frame = customtkinter.CTkFrame(self.general_frame)
        self.content_frame.pack(padx=5, pady=5, fill='both', expand=True)

        select_world_label = customtkinter.CTkLabel(self.content_frame, text='Select a world to continue',
                                                    anchor='center'
                                                    )
        select_world_label.pack(padx=2, pady=2, fill='x')

        self.worlds_frame = customtkinter.CTkScrollableFrame(self.content_frame)
        self.worlds_frame.pack(padx=2, pady=2, fill='both', expand=True)

        self.images = []
        worlds = self.read_worlds_folders()
        self.seek_and_render_worlds(worlds)

        pass

    def place(self, **kwargs):
        self.general_frame.place(**kwargs)

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def pack_forget(self):
        self.general_frame.pack_forget()

    def select_world(self, world: str):
        self.pack_forget()
        self.core.init_editor_in_world(world)
        pass

    def seek_and_render_worlds(self, worlds: list):
        self.images = []
        for world in worlds:

            world_frame = customtkinter.CTkFrame(self.worlds_frame, fg_color='#bdc3c7')
            world_frame.pack(padx=2, pady=2, fill='x')

            world_title_label = customtkinter.CTkLabel(world_frame, text=world)
            world_title_label.pack(padx=5, pady=5, fill='x', side=customtkinter.LEFT)

            canvas_image = customtkinter.CTkCanvas(world_frame, width=32, height=32, bg='#eadbcb')
            canvas_image.pack(padx=5, pady=5, side=customtkinter.RIGHT)

            select_button = customtkinter.CTkButton(world_frame, text='SELECT', fg_color='#fff3e0', text_color='black',
                                                    border_color='gray', border_width=2, hover_color='gray',
                                                    command=lambda e=world: self.select_world(e))

            select_button.pack(padx=5, pady=5, fill='both', side=customtkinter.RIGHT)

            image_path = os.path.join(self.worlds_path, world, 'icon.png')
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = image.resize((64, 64))
                img_tk = ImageTk.PhotoImage(image)
                canvas_image.create_image(0, 0, image=img_tk, anchor="center")
                self.images.append(img_tk)
                pass
        pass

    def read_worlds_folders(self):
        file_system_controller = FileSystemController()
        if os.path.exists(self.worlds_path):
            file_system_controller.set_path(self.worlds_path)
            return file_system_controller.get_folder_list()
        else:
            return None
        pass
