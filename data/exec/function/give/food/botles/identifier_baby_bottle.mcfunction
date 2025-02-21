$give @s emerald[custom_model_data={strings:["$(string)"]}, consumable={consume_seconds:10,animation:"drink",sound:"item.honey_bottle.drink",has_consume_particles:false}, custom_data={type:1}] 1


# Esto ayudara a detectar cuando un item no es un biberonz
# SelectedItem data selector
# SelectedItem.components."minecraft:custom_data".type
# execute store result storage lrtest index int 1 run data get entity @p SelectedItem.components."minecraft:custom_data".type
# execute store result score @p lrtestbibe run data get storage minecraft:lrtest index
# data get entity @p SelectedItem.components."minecraft:custom_model_data"."strings"[0]
