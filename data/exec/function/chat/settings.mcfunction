execute if score @s lrenguisounds matches 1 run playsound minecraft:custom.tab master @s ~ ~ ~ 1 1
execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": "-- SETTINGS --", "color": "yellow", "bold": true}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": "-- CONFIGURACIONES --", "color": "yellow", "bold": true}

execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": " [  Languaje ] ", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/languaje"}}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": " [   Idioma  ] ", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/languaje"}}

execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": " [ Mechanics ] ", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/mechanics"}}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": " [ Mecanicas ] ", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/mechanics"}}

execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": " [    Age    ] ", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/agemenu"}}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": " [    Edad   ] ", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/agemenu"}}