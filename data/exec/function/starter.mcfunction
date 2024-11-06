#The score value that activate datapack function to a specific
scoreboard objectives add lragree dummy
#Select if the starter message apears at the moment to enter to the world
scoreboard objectives add lrstarter dummy
#Check the firts join to the world
scoreboard objectives add lrfrsenter minecraft.custom:leave_game
#Select the admin password [Not used]
scoreboard objectives add lradmin dummy "admin"
#Select the role for the player
scoreboard objectives add lrroles dummy
#Check the time that the player is sneaking
scoreboard objectives add lrsneakytime minecraft.custom:sneak_time
#Value of the number of events that causes pee
scoreboard objectives add lrpeemeter dummy
#Value of the number of events that can causes poo
scoreboard objectives add lrpoometer dummy
#Time to go to pee
scoreboard objectives add lrpeetime dummy
#Time to go to poo
scoreboard objectives add lrpootime dummy
#The level of thirst that make the user drink
scoreboard objectives add lrsed dummy
#Value that check if the user is using a nappy at the moment with delay of 5 seconds
scoreboard objectives add lronnappy dummy
#Value that check if the player is wet for diferents reasons
scoreboard objectives add lriswet dummy
#Value that check if the player had a accident
scoreboard objectives add lrispoo dummy
#Value that check if the player uses the bathroom [Unused]
scoreboard objectives add lrbathuse dummy
#used for turn on the value if the user is uning the potty training
scoreboard objectives add lrtraininguse dummy
#Score that detects if ythe player is using a baby bottle
scoreboard objectives add lroncarbibe minecraft.used:carrot_on_a_stick
#Score that increaser 1 point per tps to 50 points and execute a function that detects if the players is using some of the diferents variations of nappy
scoreboard objectives add lrareadetection dummy
#scoreboard that indreases with the use of all datapacks food items
scoreboard objectives add lruseabfood minecraft.used:cooked_mutton
#Score used to detect the click for clean pee
scoreboard objectives add lrusetrapeador minecraft.used:carrot_on_a_stick
#scoreboard used to use the crib/cot
scoreboard objectives add lrsneakcuna minecraft.custom:jump
#Detects if the player is using the cot
scoreboard objectives add lrsneakusecuna dummy
#Used to use the changer
scoreboard objectives add lrjumpChange minecraft.custom:jump
#Used to use the potty trainning 
scoreboard objectives add lrjumpTrain minecraft.custom:jump
#Used to use the bath
scoreboard objectives add lrjumpbath minecraft.custom:jump
#Value that check the value since tle player sleep
scoreboard objectives add lrtiredtime minecraft.custom:time_since_rest
#Score that is used for check the tired state of the player
scoreboard objectives add lrtiredcheck dummy
#Scoreabord that count the time using the cot
scoreboard objectives add lrcunatime dummy
#Scoreabord that evaluates the use of the cot and execute speacial mechanic functions
scoreboard objectives add lrsleeptime dummy
#Scorea that is active mean while the player have a nappy in the inventory
scoreboard objectives add lrnapintory dummy
#Scoreabord that show the activate editor menu
scoreboard objectives add lreditorshow minecraft.custom:bell_ring
#This score activate if the editor mode is active
scoreboard objectives add lreditormode dummy
#scoreabord that execute the base menu of the editor menu
scoreboard objectives add lrsneakedit minecraft.custom:sneak_time
#used to activate the moving element in tps
scoreboard objectives add lrmovemode dummy
#used for check the rotation mode [Unused Deprecated]
scoreboard objectives add lrrotatemode dummy
#Detects the place of a item frame for block development test [Testing]
scoreboard objectives add lrplaceitemframe minecraft.used:item_frame
#Used to set a idenfier to a datapack entity that can move towars the cursor of the player
scoreboard objectives add lronmovingsome dummy
#Used for use the wash
scoreboard objectives add lrjumpwash minecraft.custom:jump
#used for use the baby chair
scoreboard objectives add lrjumpchair minecraft.custom:jump
#Used to evaluate the level of dirtiness
scoreboard objectives add lrdirt dummy "Dirtiness"
#Fear increases with the nearest mobs, it will be reset after five minutes
scoreboard objectives add lrfear dummy "Fear"
#padding parameter that  indicates the move difficutlty to the player
scoreboard objectives add lrpadding dummy
#padding value that verify the last napp padding
scoreboard objectives add lrlastpadding dummy
#scoreboar to place de crib on world
scoreboard objectives add lraddcot minecraft.used:carrot_on_a_stick
#scoreboar to place de crib on world
scoreboard objectives add lraddchanger minecraft.used:carrot_on_a_stick
#scoreboar to place de bath on world
scoreboard objectives add lraddbath minecraft.used:carrot_on_a_stick
#scoreboar to place de chair on world
scoreboard objectives add lraddchair minecraft.used:carrot_on_a_stick
#scoreboar to place de trainer on world
scoreboard objectives add lraddtrain minecraft.used:carrot_on_a_stick
#scoreboar to place de closet on world
scoreboard objectives add lraddcloss minecraft.used:carrot_on_a_stick
#scoreboar to place de wash on world
scoreboard objectives add alraddwash minecraft.used:carrot_on_a_stick
#scoreboard that verify if user leave world
scoreboard objectives add lrlogout minecraft.custom:leave_game
#scoreboard that verify the user languaje
scoreboard objectives add lrlang dummy
#scoreboard encargado de transformar un valor en negativo o positivo NO FUNCIONA PORQUE MOJANG SE LE OCURRIO NO SEGUIR LA LEY DE SIGNOS
scoreboard objectives add lrtrans dummy
scoreboard players set abplayer lrtrans -1
#scoreboard that saves de last sleep place of the player
scoreboard objectives add lrxspawn dummy
#score that used to place blocks
scoreboard objectives add lrplace minecraft.used:minecraft.allay_spawn_egg
#score used to activate de pacifier
scoreboard objectives add lrpaci minecraft.used:carrot_on_a_stick
#scoreboard objectives add abtbchone minecraft.used:minecraft:allay_spawn_egg "Allay"
scoreboard objectives add lrselection dummy "Selection"
#value that save the editor rotation at the moment
scoreboard objectives add lrrotation dummy
#scoreboard used to force the rotation to a element
scoreboard objectives add lrforcerotation dummy
#used for save the last gamemode
scoreboard objectives add lrlastgamemode dummy
#used to represent the player age
scoreboard objectives add lrage dummy "Age"
#used to save the age state of the player [static,incremental]
scoreboard objectives add lrstateage dummy
#used like a cronomert to increment the age
scoreboard objectives add lrageincrease dummy
#used to detect when the user brake a blue tapiz block
scoreboard objectives add lrbrakeblue minecraft.mined:minecraft.glass
#used when the user brake de blue tapiz block
scoreboard objectives add lrbluedelete dummy
#used to stablish a limit to the fear mechanic
scoreboard objectives add lrfearlimit dummy
#used to show a spacific text on ui
scoreboard objectives add lruidisplay dummy
#used to execute a function that show a text in 15 seconds
scoreboard objectives add lruiloop dummy "uiloop"
#used to select the type of ui that will be shown
scoreboard objectives add lruitype dummy
#state of activate or deactivate to feel fear
scoreboard objectives add lrfearstate dummy
#score to activate or deactivate nappy alert on potty
scoreboard objectives add lrnappalert dummy
#scoreboard to select a languaje default 0 english
scoreboard objectives add abtlang dummy


function exec:lists/clotles/diapers

tellraw @a {"text": "---------" , "color": "yellow"}
tellraw @a {"text": "LittleRegress Rebirth [ACTIVATED DATAPACK] V DEV 01 ","color": "yellow"}
tellraw @a {"text": "---------" , "color": "yellow"}
tellraw @a {"text": "This version could contain bugs you can report that sending a mail to abthinksdl@gmail.com" , "color": "red"}

tellraw @a {"text": " [ SETTINGS ] ", "color": "green" , "clickEvent": {"action": "run_command", "value": "/function exec:chat/settings"} }