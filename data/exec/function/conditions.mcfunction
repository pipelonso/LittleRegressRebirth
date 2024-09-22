# Execute every time when the user enter to the world
execute as @a at @a if score @s lrlogout matches 1.. run execute if score @s lrfrsenter matches 1.. run function exec:chat/menu
execute as @a at @a unless score @s lrlogout matches 0 run scoreboard players set @s lrlogout 0

# Execute just the firts time that the user enter world
execute as @a at @a if score @p lrfrsenter matches 0 run function exec:chat/welcome



