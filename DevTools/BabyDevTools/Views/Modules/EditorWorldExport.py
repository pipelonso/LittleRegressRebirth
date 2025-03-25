import customtkinter
from typing import Any
from Controllers.ExportController import ExportController
from Controllers.FileSystemController import FileSystemController


class EditorWorldExport:

    def __init__(self,
                 master: Any,
                 core: Any,
                 father: Any
                 ):

        self.file_system_controller = FileSystemController()
        self.worlds_path = self.file_system_controller.get_worlds_path()

        self.export_controller = ExportController()

        self.father = father
        self.master = master
        self.core = core

        self.general_frame = customtkinter.CTkFrame(master)

        dev_export_button = customtkinter.CTkButton(self.general_frame, text='Compile',
                                                    command=lambda: self.dev_compile_template())

        dev_export_button.pack(padx=2, pady=2, fill='both', expand=True)

        texture_test_export_button = customtkinter.CTkButton(self.general_frame, text="Export textures",
                                                             command=lambda : self.dev_compile_textures())
        texture_test_export_button.pack(padx=2, pady=2, fill='both', expand=True)

        self.assets_template_name = 'LR2'
        self.compile_folder = 'out'

        pass

    def pack(self, **kwargs):
        self.general_frame.pack(**kwargs)

    def unpack(self):
        self.general_frame.pack_forget()

    def dev_compile_template(self):
        self.export_controller.set_world(self.father.world)
        self.export_controller.dev_compile_template()
        pass

    def dev_compile_textures(self):
        self.export_controller.set_world(self.father.world)
        self.export_controller.dev_compile_test_textures()
        pass
