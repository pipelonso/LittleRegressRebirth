execute if score @s lrpeeanimplay matches 1 run scoreboard players add @s lrpeeanimtime 1
execute if score @s lrpeeanimplay matches 1 run scoreboard players add @s lrpeeanimupdate 1

execute if score @s lrpeeanimplay matches 1 run execute as @s at @s run particle minecraft:dripping_water
execute if score @s lrpeeanimupdate matches 1 run execute if score @s lrenpeesounds matches 1 run playsound minecraft:custom.p_two master @s ~ ~ ~ 1 1

# sound here
# playsound minecraft:custom.p_two
execute if score @s lrpeeanimupdate matches 1 run scoreboard players add @s lrpeeanimupdate 1
execute if score @s lrpeeanimtime matches 850.. run scoreboard players set @s lrpeemeter 0
execute if score @s lrpeeanimtime matches 850.. run scoreboard players set @s lrpeetime -100
execute if score @s lrpeeanimtime matches 850.. run scoreboard players set @s lrpeeanimupdate 0
execute if score @s lrpeeanimtime matches 850.. run scoreboard players set @s lrpeeanimplay 0
execute if score @s lrpeeanimtime matches 850.. run scoreboard players set @s lrpeeanimtime 0