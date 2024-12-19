data modify storage cubikframework validations.value set from entity @s Inventory[{Slot:101b}].components."minecraft:custom_data".padding
execute store result score @s ckfvalidcase run data get storage cubikframework validations.value
return run scoreboard players get @s ckfvalidcase