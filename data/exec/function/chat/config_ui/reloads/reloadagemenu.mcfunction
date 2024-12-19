$scoreboard players $(operator) @s lrage $(count)
execute if score @s lrage matches ..0 run scoreboard players set @s lrage 0
execute if score @s lrage matches 130.. run scoreboard players set @s lrage 130
function exec:mechanics/diapers/updateplayerscale
function exec:chat/config_ui/agemenu