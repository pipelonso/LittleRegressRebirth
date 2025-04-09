execute if score @s lrpeemeter matches 1 run scoreboard players add @s lrpeetime 1
execute if score @s lrpeemeter matches 2.. run scoreboard players add @s lrpeetime 2
execute if score @s lrpeemeter matches 5.. run scoreboard players add @s lrpeetime 3
execute if score @s lrpeemeter matches 6.. run scoreboard players add @s lrpeetime 10


execute if score @s lrpeetime matches 12000.. run scoreboard players set @s lrpeeanimplay 1
execute if score @s lrpeetime matches 12000.. run execute if score @s lronnappy matches 1 run function exec:animation/diaper/pee/wetting
execute if score @s lrpeetime matches 12000.. run execute if score @s lronnappy matches 0 run function exec:animation/diaper/pee/peeing


