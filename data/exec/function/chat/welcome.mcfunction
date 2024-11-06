tellraw @s {"text": " [Welcome first time to little Regress] [2.0 Rebirth]", "color":"green"}
tellraw @s {"text": "This message only appears the first time you enter the world.", "color": "red"}
tellraw @s {"text": "Little Regress is a datapack designed to allow Minecraft users to customize their age regression experience within Minecraft."}
tellraw @s {"text": "We can start with some quick configurations:."}
tellraw @s [{"text": "[More info]","color":"blue", "clickEvent": {"action": "open_url", "value": "https://pipelonso.github.io/LittleRegress-WebSite/"}}, {"text": " [Settings]", "color": "blue", "clickEvent": {"action": "run_command", "value": "/function exec:chat/settings"}}]
tellraw @s {"text": " [ SETTINGS ] ", "color": "green" , "clickEvent": {"action": "run_command", "value": "/function exec:chat/settings"} }
execute if score @s lrfrsenter matches ..0 run scoreboard players set @s lrfrsenter 1