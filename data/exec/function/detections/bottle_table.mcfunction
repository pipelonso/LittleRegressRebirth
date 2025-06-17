
execute as @e[type=minecraft:interaction,nbt={interaction:{}},tag=bttest] at @s run tellraw @a "hello"
execute as @e[type=minecraft:interaction,nbt={interaction:{}},tag=bttest] run data remove entity @s interaction