# Execute every time when the user enter to the world
execute as @a at @a if score @s lrlogout matches 1.. run execute if score @s lrfrsenter matches 1.. run function exec:chat/menu
execute as @a at @a unless score @s lrlogout matches 0 run scoreboard players set @s lrlogout 0

execute as @a at @a unless score @s lrage matches 1.. run scoreboard players set @s lrage 0

# Execute just the firts time that the user enter world
execute as @a at @a if score @p lrfrsenter matches 0 run function exec:chat/welcome

# setting up starter values to initial scores
execute as @a at @a unless score @s lrlang matches 0 run execute unless score @s lrlang matches 1 run scoreboard players set @s lrlang 0
execute as @a at @a unless score @s lrenpeesounds matches 0 run execute unless score @s lrenpeesounds matches 1 run scoreboard players set @s lrenpeesounds 0
execute as @a at @a unless score @s lrenpoosounds matches 0 run execute unless score @s lrenpoosounds matches 1 run scoreboard players set @s lrenpoosounds 0
execute as @a at @a unless score @s lrenguisounds matches 0 run execute unless score @s lrenguisounds matches 1 run scoreboard players set @s lrenguisounds 1
execute as @a at @a unless score @s lragescale matches 0 run execute unless score @s lragescale matches 1 run scoreboard players set @s lragescale 0

execute as @a at @a run function exec:detections/is_selected_bottle
execute as @a at @a run execute if score @s lrbottle matches 1 run execute if score @s lrbottleuse matches 1.. run function exec:mechanics/bottles/use_bottle

execute as @a at @a run function exec:detections/is_on_nappy

execute as @a at @a if score @s lrpeemeter matches 1.. run function exec:mechanics/potty/pee_updater


