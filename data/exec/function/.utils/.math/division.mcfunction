
scoreboard objectives add cfwdigit dummy
scoreboard objectives add cfwoperator dummy
scoreboard objectives add cfwresult dummy


$scoreboard players set $(player) cfwdigit $(number)
$scoreboard players set $(player) cfwoperator $(operator)


$scoreboard players operation $(player) cfwresult = $(player) cfwdigit
$scoreboard players operation $(player) cfwresult /= $(player) cfwoperator


$return run scoreboard players get $(player) cfwresult
