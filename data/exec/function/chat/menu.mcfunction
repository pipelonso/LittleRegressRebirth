tellraw @s[scores={lrlang=0}] {"text": " -- Welcome to LittleRegress Rebirth --","color":"yellow"}
tellraw @s[scores={lrlang=1}] {"text": " -- Bienvenido a LittleRegress Rebirth --","color":"yellow"}
tellraw @s ""

# click event is broken, more details in https://www.minecraft.net/es-es/article/minecraft-java-edition-1-21-5
# https://minecraft.wiki/w/Commands/tellraw {action:'run_command',command:'/tp @e @s'}

tellraw @s[scores={lrlang=0}] {"text": " [ SETTINGS ]", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }
tellraw @s[scores={lrlang=1}] {"text": " [ CONFIGURACIÓN ]", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }
