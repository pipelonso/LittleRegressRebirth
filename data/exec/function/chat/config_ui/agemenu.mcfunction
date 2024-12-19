tellraw @s[scores={lrlang = 0}] {"text": "-- AGE SETTINGS --", "color" : "yellow", "bold": true}
tellraw @s[scores={lrlang = 1}] {"text": "-- CONFIGURAR EDAD --",  "color" : "yellow", "bold": true}
tellraw @s ""
tellraw @s {"text": "[<] ", "color": "green", "bold": true, "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/reloads/reloadagemenu {\"operator\":\"remove\", \"count\" : 1}"}, "extra": [{"score": {"name": "@s", "objective": "lrage"}, "color": "yellow"},{"text": " [>]", "color": "green", "clickEvent": {"action": "run_command", "value": "/function exec:chat/config_ui/reloads/reloadagemenu {\"operator\":\"add\", \"count\" : 1}"}}]}
tellraw @s ""
tellraw @s[scores={lrlang = 0, lragescale=1}] {"text": "[✅] Adjust height according to age", "color": "green", "clickEvent": {"action": "run_command","value": "/function exec:chat/config_ui/reloads/reloadagemenuscale {\"active\":0}"}}
tellraw @s[scores={lrlang = 1, lragescale=1}] {"text": "[✅] Ajustar la altura conforme la edad", "color": "green", "clickEvent": {"action": "run_command","value": "/function exec:chat/config_ui/reloads/reloadagemenuscale {\"active\":0}"}}

tellraw @s[scores={lrlang = 0, lragescale=0}] {"text": "[❌] Adjust height according to age", "color": "green", "clickEvent": {"action": "run_command","value": "/function exec:chat/config_ui/reloads/reloadagemenuscale {\"active\":1}"}}
tellraw @s[scores={lrlang = 1, lragescale=0}] {"text": "[❌] Ajustar la altura conforme la edad", "color": "green", "clickEvent": {"action": "run_command","value": "/function exec:chat/config_ui/reloads/reloadagemenuscale {\"active\":1}"}}