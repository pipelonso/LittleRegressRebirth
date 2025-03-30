tellraw @s[scores={lrlang = 0}] {"text": "-- AGE SETTINGS --", "color" : "yellow", "bold": true}
tellraw @s[scores={lrlang = 1}] {"text": "-- CONFIGURAR EDAD --",  "color" : "yellow", "bold": true}
tellraw @s ""
tellraw @s {"text": "[<] ", "color": "green", "bold": true, "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/reloads/reloadagemenu {\"operator\":\"remove\", \"count\" : 1}"}, "extra": [{"score": {"name": "@s", "objective": "lrage"}, "color": "yellow"},{"text": " [>]", "color": "green", "click_event": {"action": "run_command", "command": "/function exec:chat/config_ui/reloads/reloadagemenu {\"operator\":\"add\", \"count\" : 1}"}}]}
tellraw @s ""
tellraw @s[scores={lrlang = 0, lragescale=1}] {"text": "[✅] Adjust height according to age", "color": "green", "click_event": {"action": "run_command","command": "/function exec:chat/config_ui/reloads/reloadagemenuscale {\"active\":0}"}}
tellraw @s[scores={lrlang = 1, lragescale=1}] {"text": "[✅] Ajustar la altura conforme la edad", "color": "green", "click_event": {"action": "run_command","command": "/function exec:chat/config_ui/reloads/reloadagemenuscale {\"active\":0}"}}

tellraw @s[scores={lrlang = 0, lragescale=0}] {"text": "[❌] Adjust height according to age", "color": "green", "click_event": {"action": "run_command","command": "/function exec:chat/config_ui/reloads/reloadagemenuscale {\"active\":1}"}}
tellraw @s[scores={lrlang = 1, lragescale=0}] {"text": "[❌] Ajustar la altura conforme la edad", "color": "green", "click_event": {"action": "run_command","command": "/function exec:chat/config_ui/reloads/reloadagemenuscale {\"active\":1}"}}
tellraw @s ""
tellraw @s {text:"________________"}
tellraw @s ""

tellraw @s[scores={lrlang=0}] {"text": " [ BACK TO SETTINGS ]", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }
tellraw @s[scores={lrlang=1}] {"text": " [ VOLVER A LA CONFIGURACIÓN ]", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }

execute if score @s lrenguisounds matches 1 run playsound minecraft:custom.tab master @s ~ ~ ~ 1 1
