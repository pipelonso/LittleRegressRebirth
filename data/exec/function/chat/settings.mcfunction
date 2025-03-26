tellraw @a "patito"

execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": "-- SETTINGS --", "color": "yellow", "bold": true}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": "-- CONFIGURACIONES --", "color": "yellow", "bold": true}

execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": " [  Languaje ] ", "color": "green", "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/languaje"}}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": " [   Idioma  ] ", "color": "green", "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/languaje"}}

execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": " [ Mechanics ] ", "color": "green"}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": " [ Mecanicas ] ", "color": "green"}

execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": " [    Age    ] ", "color": "green", "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/agemenu"}}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": " [    Edad   ] ", "color": "green", "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/agemenu"}}