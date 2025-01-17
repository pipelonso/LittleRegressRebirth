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

        pass

    @staticmethod
    def _format_texture_name(filename, suffix):
        name = filename.replace(f"_{suffix}.png", "")
        return name.replace("_", " ").title()

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
                    for glasses in self.glass_textures:
                        formated_glass = self._format_texture_name(glasses, 'glass_texture')
                        for covers in self.cover_textures:
                            formated_cover = self._format_texture_name(covers, 'cover')
                            for contents in self.content_textures:
                                formated_content = self._format_texture_name(contents, 'content')

                                array_content['textures'][str(self.order_glass)] = formated_glass
                                array_content['textures'][str(self.order_cover)] = formated_cover
                                array_content['textures'][str(self.order_content)] = formated_content

                                print(array_content)

                                pass
                        pass
                    pass

        pass