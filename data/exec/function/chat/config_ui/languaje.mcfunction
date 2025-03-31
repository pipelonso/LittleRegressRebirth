execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": "Select a languaje:", "bold": true, "color": "yellow"}
execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text" : "[ English ]", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/reloads/reloadlanguaje {\"lang\":0}"}}
execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text" : "[ Spanish ]", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/reloads/reloadlanguaje {\"lang\":1}"}}
# SPANISH
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": "Selecciona un idioma:", "bold": true, "color": "yellow"}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text" : "[ Ingles  ]", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/reloads/reloadlanguaje {\"lang\":0}"}}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text" : "[ Español ]", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/reloads/reloadlanguaje {\"lang\":1}"}}

tellraw @s ""
tellraw @s {text:"________________"}
tellraw @s ""

tellraw @s[scores={lrlang=0}] {"text": " [ BACK TO SETTINGS ]", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }
tellraw @s[scores={lrlang=1}] {"text": " [ VOLVER A LA CONFIGURACIÓN ]", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }

execute if score @s lrenguisounds matches 1 run playsound minecraft:custom.tab master @s ~ ~ ~ 1 1