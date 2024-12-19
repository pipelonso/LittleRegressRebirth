tellraw @s[scores={lrlang=0}] {"text": " -- Welcome to LittleRegress Rebirth --","color":"yellow"}
tellraw @s[scores={lrlang=1}] {"text": " -- Bienvenido a LittleRegress Rebirth --","color":"yellow"}
tellraw @s ""
tellraw @s[scores={lrlang=0}] {"text": " [ SETTINGS ]", "color": "green" , "clickEvent": {"action": "run_command", "value": "/function exec:chat/settings"} }
tellraw @s[scores={lrlang=1}] {"text": " [ CONFIGURACIÓN ]", "color": "green" , "clickEvent": {"action": "run_command", "value": "/function exec:chat/settings"} }
