import json
import os
from pathlib import Path


class BabyBottleController:

    def __init__(self):

        self.order_glass = 1
        self.order_cover = 2
        self.order_content = 3
        self.order_particle = 'particle'

        current_file = Path(__file__).resolve()
        project_root = current_file.parents[1]

        content_path = project_root / "Resources" / "baby_botle_registry" / "content"
        cover_path = project_root / "Resources" / "baby_botle_registry" / "cover"
        glass_path = project_root / "Resources" / "baby_botle_registry" / "glass"
        self.out_path = project_root / "Resources" / "baby_botle_registry" / "out"

        self.model_list_path = project_root / "Resources" / "baby_botle_registry" / "generated" / "model" / "emerald.json"

        self.cover_textures = [
            f for f in os.listdir(cover_path) if os.path.isfile(os.path.join(cover_path, f))
                                                 and f.endswith('cover.png')
        ]

        self.glass_textures = [
            f for f in os.listdir(glass_path) if os.path.isfile(os.path.join(glass_path, f))
                                                 and f.endswith('glass_texture.png')
        ]

        self.content_textures = [
            f for f in os.listdir(content_path) if os.path.isfile(os.path.join(content_path, f))
                                                   and f.endswith('content.png')
        ]

        self.generated_file_names = []
        self.generated_human_names = []

        pass

    @staticmethod
    def _format_texture_name(filename, suffix):
        name = filename.replace(f"_{suffix}.png", "")
        return name.replace("_", " ").title()

    @staticmethod
    def _format_to_file_name(glass_file: str, content_file: str, cover_file: str):
        glass_name = glass_file.replace(f"_glass_texture.png", "")
        cover_name = cover_file.replace(f"_cover.png", "")
        content_name = content_file.replace(f"_content.png", "")

        if content_name != 'empty':
            built_in = f'{content_name}_in_a_{glass_name}_{cover_name}_baby_bottle'
        else:
            built_in = f'{content_name}_{glass_name}_{cover_name}_baby_bottle'

        return built_in

    @staticmethod
    def _format_to_human_name(content_file: str):
        extract = content_file.replace('_content.png', '')
        if extract == 'empty':
            name = (extract.replace('_', ' ').title() + ' Baby Bottle')
        else:
            name = (extract.replace('_', ' ').title() + ' in a Baby Bottle')
        return name

    def generate_variations(self):

        current_file = Path(__file__).resolve()
        project_root = current_file.parents[1]
        resource_path = project_root / "Resources" / "baby_botle_registry" / "generated" / "baby_botle_base.json"

        if os.path.exists(resource_path):
            content = open(resource_path, 'r').read()
            array_content = json.loads(content)

            if 'textures' in array_content:

                if (
                        str(self.order_glass) in array_content['textures']
                        and str(self.order_content) in array_content['textures']
                        and str(self.order_cover) in array_content['textures']
                        and str(self.order_particle) in array_content['textures']
                ):

                    human_names = []
                    file_names = []

                    for glasses in self.glass_textures:
                        for covers in self.cover_textures:
                            for contents in self.content_textures:
                                array_content['textures'][str(self.order_glass)] = (
                                        'item/glass/' + glasses.replace('.png', '')
                                )
                                array_content['textures'][str(self.order_cover)] = (
                                        'item/cover/' + covers.replace('.png', '')
                                )
                                array_content['textures'][str(self.order_content)] = (
                                        'item/content/' + contents.replace('.png', '')
                                )

                                file_name = self._format_to_file_name(glasses, contents, covers)

                                file_names.append(file_name)
                                human_names.append(self._format_to_human_name(contents))

                                with (open(os.path.join(self.out_path, f'{file_name}.json'), "w") as
                                      file
                                      ):
                                    file.write(json.dumps(array_content, indent=10, skipkeys=True))

                                pass
                        pass
                    pass

                    self.generated_file_names = file_names
                    self.generated_human_names = human_names

                    print(file_names)
                    print(human_names)

        pass

    def generate_model_content(self):

        if os.path.exists(self.model_list_path):
            content = open(self.model_list_path, 'r').read()
            array_content = json.loads(content)

            cases_array = []

            for file_name in self.generated_file_names:

                bottle = {
                    "when": file_name,
                    "model": {
                        "type": "model",
                        "model": f"item/{file_name}"
                    }
                }

                cases_array.append(bottle)

            array_content['model']['cases'] = cases_array

            with (open(os.path.join(self.model_list_path), "w") as
                  file
                  ):
                file.write(json.dumps(array_content, indent=2, skipkeys=True))

