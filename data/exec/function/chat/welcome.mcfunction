tellraw @s {"text": " [Welcome first time to little Regress] [2.0 Rebirth]", "color":"green"}
tellraw @s {"text": "This message only appears the first time you enter the world.", "color": "red"}
tellraw @s {"text": "Little Regress is a datapack designed to allow Minecraft users to customize their age regression experience within Minecraft."}
tellraw @s {"text": "We can start with some quick configurations:."}
tellraw @s [{"text": "[More info]","color":"blue", "click_event": {"action": "open_url", "url": "https://pipelonso.github.io/LittleRegress-WebSite/"}}, {"text": " [Settings]", "color": "blue", "click_event": {"action": "run_command", "command": "/function exec:chat/settings"}}]
tellraw @s {"text": " [ SETTINGS ] ", "color": "green" , "click_event": {"action": "run_command", "command": "/function exec:chat/settings"} }
execute if score @s lrfrsenter matches ..0 run scoreboard players set @s lrfrsenter 1