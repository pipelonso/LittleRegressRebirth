#scoreboard declaration
function exec:.scoreboards/init

# process base storages
function exec:lists/clotles/diapers

#english
tellraw @a[scores={lrlang = 0}] {"text": "---------" , "color": "yellow"}
tellraw @a[scores={lrlang = 0}] {"text": "LittleRegress Rebirth [ACTIVATED DATAPACK] V DEV 01 ","color": "yellow"}
tellraw @a[scores={lrlang = 0}] {"text": "---------" , "color": "yellow"}
tellraw @a[scores={lrlang = 0}] {"text": "This version could contain bugs you can report that sending a mail to abthinksdl@gmail.com" , "color": "red"}
tellraw @a[scores={lrlang = 0}] ""
tellraw @a[scores={lrlang = 0}] {"text": " [ SETTINGS ] ", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }

#spanish
tellraw @a[scores={lrlang = 1}] {"text": "---------" , "color": "yellow"}
tellraw @a[scores={lrlang = 1}] {"text": "LittleRegress Rebirth [PAQUETE DE DATOS ACTIVADO] V DEV 01 ","color": "yellow"}
tellraw @a[scores={lrlang = 1}] {"text": "---------" , "color": "yellow"}
tellraw @a[scores={lrlang = 1}] {"text": "Esta version puede contener bugs, puedes reportalos al correo abthinksdl@gmail.com" , "color": "red"}
tellraw @a[scores={lrlang = 1}] ""
tellraw @a[scores={lrlang = 1}] {"text": " [ CONFIGURACION ] ", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }

# songs implements https://www.curseforge.com/minecraft/texture-packs/custom-sound-template


