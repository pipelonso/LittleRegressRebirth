execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": "--- MECHANICS ---", "bold": true, "color": "yellow"}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": "--- MECANICAS ---", "bold": true, "color": "yellow"}
tellraw @s ""
execute as @s at @s run tellraw @s[scores={lrlang = 0}] {"text": "There are options disabled by default for user security.", "bold": true, "color": "white"}
execute as @s at @s run tellraw @s[scores={lrlang = 1}] {"text": "Hay mecanicas desactivadas por defecto para la seguridad del usuario.", "bold": true, "color": "white"}

tellraw @s ""

tellraw @s[scores={lrlang=0, lrenpeesounds=1}] {text: "[ [✅] Inmersive pee sounds ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenpeesounds\", value:0}"}}
tellraw @s[scores={lrlang=0, lrenpeesounds=0}] {text: "[ [❌] Inmersive pee sounds ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenpeesounds\", \"value\":1}"}}
tellraw @s[scores={lrlang=1, lrenpeesounds=1}] {text: "[ [✅] Sonidos inmersivos de orina ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenpeesounds\", value:0}"}}
tellraw @s[scores={lrlang=1, lrenpeesounds=0}] {text: "[ [❌] Sonidos inmersivos de orina ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenpeesounds\", \"value\":1}"}}

tellraw @s[scores={lrlang=0, lrenpoosounds=1}] {text: "[ [✅] Inmersive poo sounds ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenpoosounds\", value:0}"}}
tellraw @s[scores={lrlang=0, lrenpoosounds=0}] {text: "[ [❌] Inmersive poo sounds ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenpoosounds\", \"value\":1}"}}
tellraw @s[scores={lrlang=1, lrenpoosounds=1}] {text: "[ [✅] Sonidos inmersivos de popo ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenpoosounds\", value:0}"}}
tellraw @s[scores={lrlang=1, lrenpoosounds=0}] {text: "[ [❌] Sonidos inmersivos de popo ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenpoosounds\", \"value\":1}"}}

tellraw @s[scores={lrlang=0, lrenguisounds=1}] {text: "[ [✅] User interface sounds ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenguisounds\", value:0}"}}
tellraw @s[scores={lrlang=0, lrenguisounds=0}] {text: "[ [❌] User interface sounds ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenguisounds\", \"value\":1}"}}
tellraw @s[scores={lrlang=1, lrenguisounds=1}] {text: "[ [✅] Sonidos de interfaz ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenguisounds\", value:0}"}}
tellraw @s[scores={lrlang=1, lrenguisounds=0}] {text: "[ [❌] Sonidos de interfaz ]", color:"green", click_event: {"action":"run_command", command:"/function exec:chat/config_ui/reloads/reload_mechanics {\"score\":\"lrenguisounds\", \"value\":1}"}}

tellraw @s ""
tellraw @s[scores={lrlang=0}] {"text": " [ BACK TO SETTINGS ]", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }
tellraw @s[scores={lrlang=1}] {"text": " [ VOLVER A LA CONFIGURACIÓN ]", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }
tellraw @s ""

execute if score @s lrenguisounds matches 1 run playsound minecraft:custom.tab master @s ~ ~ ~ 1 1
