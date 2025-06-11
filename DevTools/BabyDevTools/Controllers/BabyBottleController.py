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

        self.crafting_out_path = project_root / "Resources" / "baby_botle_registry" / "craftings" / "generated"

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

        self.crafting_glass_assignment = [
            {"file": "blue_glass_texture.png", "item_name": "minecraft:blue_stained_glass"},
            {"file": "green_glass_texture.png", "item_name": "minecraft:green_stained_glass"},
            {"file": "red_glass_texture.png", "item_name": "minecraft:red_stained_glass"},
            {"file": "transparent_glass_texture.png", "item_name": "minecraft:glass"},
            {"file": "yellow_glass_texture.png", "item_name": "minecraft:yellow_stained_glass"}
        ]

        self.crafting_cover_assignment = [
            {"file": "blue_cover.png", "item_name": "minecraft:blue_concrete"},
            {"file": "green_cover.png", "item_name": "minecraft:green_concrete"},
            {"file": "pink_cover.png", "item_name": "minecraft:pink_concrete"},
            {"file": "yellow_cover.png", "item_name": "minecraft:yellow_concrete"}
        ]

        self.crafting_content_assignment = [
            {"file": "apple_juice_content.png", "item_name": "minecraft:apple"},
            {"file": "berry_juice_content.png", "item_name": "minecraft:sweet_berries"},
            {"file": "empty_content.png", "item_name": ""},
            {"file": "milk_content.png", "item_name": "minecraft:milk_bucket"},
            {"file": "water_content.png", "item_name": "minecraft:water_bucket"}
        ]

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
                    empty_generations = []

                    for glasses in self.glass_textures:
                        for covers in self.cover_textures:
                            for contents in self.content_textures:

                                empty_generations.append(
                                    self._format_to_file_name(glasses, 'empty_content.png', covers)
                                )
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
                    # print(empty_generations)
                    #
                    # print(file_names)
                    # print(human_names)

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

    def generate_crafting_content_exports(self):

        current_file = Path(__file__).resolve()
        project_root = current_file.parents[1]
        resource_path = project_root / "Resources" / "baby_botle_registry" / "craftings" / "base" /"bottle.json"
        empty_resource_path = project_root / "Resources" / "baby_botle_registry" / "craftings" / "base" /"empty_bottle.json"

        if os.path.exists(resource_path):

            with_content = open(resource_path, 'r').read()
            without_content = open(empty_resource_path, 'r').read()

            base_with_content_recipe = json.loads(with_content)
            base_empty_recipe = json.loads(without_content)

            for glasses in self.glass_textures:
                for covers in self.cover_textures:
                    for contents in self.content_textures:

                        file_name = self._format_to_file_name(glasses, contents, covers)
                        human_name = self._format_to_human_name(contents)

                        if contents == 'empty_content.png':
                            # Handle empty bottles
                            array_content = json.loads(json.dumps(base_empty_recipe)) # Deep copy

                            # Ensure result uses "item" instead of "id"
                            if "result" in array_content and "id" in array_content["result"]:
                                array_content["result"]["item"] = array_content["result"].pop("id")

                            if "key" in array_content:
                                # For empty bottles, keys are simple strings as per empty_bottle.json and original logic
                                for glass_item in self.crafting_glass_assignment:
                                    if glass_item["file"] == glasses:
                                        array_content["key"]["G"] = glass_item["item_name"]
                                for cover_item in self.crafting_cover_assignment:
                                    if cover_item["file"] == covers:
                                        array_content["key"]["C"] = cover_item["item_name"]

                            if "result" in array_content and "components" in array_content["result"]:
                                # Ensure these components are correctly structured as per base files
                                array_content["result"]["components"]["minecraft:custom_model_data"] = {"strings": [file_name]}
                                array_content["result"]["components"]["minecraft:custom_name"] = human_name

                                # Ensure use_remainder also uses "item" if it exists and has an id
                                if "minecraft:use_remainder" in array_content["result"]["components"] and \
                                   "id" in array_content["result"]["components"]["minecraft:use_remainder"]:
                                    array_content["result"]["components"]["minecraft:use_remainder"]["item"] = \
                                        array_content["result"]["components"]["minecraft:use_remainder"].pop("id")
                                # Original logic for empty bottle's use_remainder (if any specific variation is needed)
                                # This part might need review based on how empty_bottle.json is structured
                                # For now, assume it correctly sets up the empty bottle output
                                empty_variation_name_for_remainder = self._format_to_file_name(glasses, 'empty_content.png', covers)
                                empty_human_name_for_remainder = self._format_to_human_name('empty_content.png')
                                if "minecraft:use_remainder" in array_content["result"]["components"]:
                                    if "components" in array_content["result"]["components"]["minecraft:use_remainder"]:
                                        remainder_comps = array_content["result"]["components"]["minecraft:use_remainder"]["components"]
                                        if "minecraft:custom_name" in remainder_comps:
                                            remainder_comps["minecraft:custom_name"] = empty_human_name_for_remainder
                                        if "minecraft:custom_model_data" in remainder_comps:
                                             remainder_comps["minecraft:custom_model_data"]["strings"] = [empty_variation_name_for_remainder]

                        else:
                            # Handle bottles with content
                            array_content = json.loads(json.dumps(base_with_content_recipe)) # Deep copy

                            empty_bottle_filename = self._format_to_file_name(glasses, 'empty_content.png', covers)

                            if "key" in array_content:
                                # Set glass, cover, and content materials
                                for glass_item in self.crafting_glass_assignment:
                                    if glass_item["file"] == glasses:
                                        array_content["key"]["G"] = {"item": glass_item["item_name"]}
                                for cover_item in self.crafting_cover_assignment:
                                    if cover_item["file"] == covers:
                                        array_content["key"]["C"] = {"item": cover_item["item_name"]}
                                for content_item in self.crafting_content_assignment:
                                    if content_item["file"] == contents:
                                        array_content["key"]["M"] = {"item": content_item["item_name"]}

                                # Add empty bottle as an ingredient
                                array_content["key"]["E"] = {
                                    "item": "minecraft:emerald", # As per instruction
                                    "components": {
                                        "minecraft:custom_model_data": {
                                            "strings": [empty_bottle_filename]
                                        }
                                    }
                                }

                            if "result" in array_content:
                                array_content["result"]["item"] = "minecraft:emerald" # Assuming the result item is also an emerald
                                if "components" in array_content["result"]:
                                    array_content["result"]["components"]["minecraft:custom_model_data"] = {"strings": [file_name]}
                                    array_content["result"]["components"]["minecraft:custom_name"] = human_name

                                    # Remove use_remainder for content bottles
                                    if "minecraft:use_remainder" in array_content["result"]["components"]:
                                        del array_content["result"]["components"]["minecraft:use_remainder"]

                        # Write the modified recipe to a JSON file
                        if not os.path.exists(self.crafting_out_path):
                            os.makedirs(self.crafting_out_path)

                        with open(os.path.join(self.crafting_out_path, f'{file_name}.json'), "w") as file:
                            file.write(json.dumps(array_content, indent=4, skipkeys=True))
            pass

        pass
