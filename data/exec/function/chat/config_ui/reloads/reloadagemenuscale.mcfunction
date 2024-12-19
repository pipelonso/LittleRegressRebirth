$scoreboard players set @s lragescale $(active)
execute if score @s lragescale matches 0 run attribute @s scale base set 1
function exec:mechanics/diapers/updateplayerscale
function exec:chat/config_ui/agemenu