import os.path
from pathlib import Path
from Controllers.FileSystemController import FileSystemController
import shutil


class ExportController:

    def __init__(self):

        self.world = ''
        self.file_system_controller = FileSystemController()

        pass

    def set_world(self, name: str):
        self.world = name
        pass

    def dev_compile_template(self):

        current_file = Path(__file__).resolve()
        project_root = current_file.parents[3]

        print(project_root)

        self.file_system_controller.set_path(str(project_root))
        files_and_folders = self.file_system_controller.list_files_and_folders()

        folders = files_and_folders['folders']
        files = files_and_folders['files']

        icon_find = 'pack.png' in files
        data_find = 'data' in folders
        mcmeta_find = 'pack.mcmeta' in files

        datapack_folder = 'datapacks'
        folder_name = 'buildd'

        datapack_folder_path = os.path.join(self.file_system_controller.get_worlds_path(), self.world,
                                            datapack_folder, folder_name)

        if not os.path.exists(datapack_folder_path):
            self.file_system_controller.make_folder_tail(datapack_folder_path)
            pass

        if icon_find:
            icon_path = os.path.join(project_root, 'pack.png')
            shutil.copy(icon_path, datapack_folder_path)

        if mcmeta_find:
            mcmeta_path = os.path.join(project_root, 'pack.mcmeta')
            shutil.copy(mcmeta_path, datapack_folder_path)

        if data_find:
            data_path = os.path.join(project_root, 'data')
            data_folder = os.path.join(datapack_folder_path, 'data')
            if os.path.exists(data_folder):
                shutil.rmtree(data_folder)

            self.file_system_controller.make_folder_tail(data_folder)
            shutil.copytree(data_path, data_folder, dirs_exist_ok=True)

        pass

    def dev_compile_test_textures(self):

        current_file = Path(__file__).resolve()
        project_root = current_file.parents[3]

        self.file_system_controller.set_path(os.path.join(str(project_root), "Resources/LR2"))
        files_and_folders = self.file_system_controller.list_files_and_folders()

        folders = files_and_folders['folders']
        files = files_and_folders['files']

        icon_find = 'pack.png' in files
        data_find = 'assets' in folders
        mcmeta_find = 'pack.mcmeta' in files

        resources_folder_path = os.path.join(self.file_system_controller.get_general_resources_path(), "LR2")

        if not os.path.exists(resources_folder_path):
            self.file_system_controller.make_folder_tail(resources_folder_path)
            pass

        if icon_find:
            icon_path = os.path.join(project_root, 'Resources/LR2/pack.png')
            print(icon_path)
            print(resources_folder_path)
            shutil.copy(icon_path, resources_folder_path)

        if mcmeta_find:
            mcmeta_path = os.path.join(project_root, 'Resources/LR2/pack.mcmeta')
            shutil.copy(mcmeta_path, resources_folder_path)

        if data_find:
            data_path = os.path.join(project_root, 'Resources/LR2')

            if os.path.exists(resources_folder_path):
                shutil.rmtree(resources_folder_path)

            self.file_system_controller.make_folder_tail(resources_folder_path)
            shutil.copytree(data_path, resources_folder_path, dirs_exist_ok=True)

        pass
