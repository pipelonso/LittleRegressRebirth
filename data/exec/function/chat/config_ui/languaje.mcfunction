execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": "Select a languaje:", "bold": true, "color": "yellow"}
execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text" : "[ English ]", "color": "green", "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/reloads/reloadlanguaje {\"lang\":0}"}}
execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text" : "[ Spanish ]", "color": "green", "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/reloads/reloadlanguaje {\"lang\":1}"}}
# SPANISH
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": "Selecciona un idioma:", "bold": true, "color": "yellow"}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text" : "[ Ingles  ]", "color": "green", "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/reloads/reloadlanguaje {\"lang\":0}"}}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text" : "[ Español ]", "color": "green", "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/reloads/reloadlanguaje {\"lang\":1}"}}