scoreboard objectives add cfwmultdigit dummy
scoreboard objectives add cfwmultoperator dummy
scoreboard objectives add cfwmultresult dummy

$scoreboard players set $(player) cfwmultdigit $(number)
$scoreboard players set $(player) cfwmultoperator $(operator)

$scoreboard players operation $(player) cfwmultresult = $(player) cfwmultdigit
$scoreboard players operation $(player) cfwmultresult *= $(player) cfwmultoperator

$return run scoreboard players get $(player) cfwmultresult