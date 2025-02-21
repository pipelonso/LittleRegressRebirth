execute as @s at @s run function exec:.users/model/select_current_user
execute as @s at @s run function exec:.users/model/read/get_user with storage cubikframework model.cache.user
return run data get storage cubikframework model.users.cache.user.selected