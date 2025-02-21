execute as @s at @s run data modify storage minecraft:cubikframework model.cache.user.uuid0 append from entity @s UUID[0]
execute as @s at @s run data modify storage minecraft:cubikframework model.cache.user.uuid1 append from entity @s UUID[1]
execute as @s at @s run data modify storage minecraft:cubikframework model.cache.user.uuid2 append from entity @s UUID[2]
execute as @s at @s run data modify storage minecraft:cubikframework model.cache.user.uuid3 append from entity @s UUID[3]




# $data modify storage cubikframework users."$(user)" append from storage cubikframework model.cache.user



# Guardamos el UUID en la cache temporal
# execute as @s run data modify storage cubikframework model.cache.user set from entity @s UUID
# vale con esto acceso al UUID del jugador, puedo crear varios indices unicos con esto
# Creamos el path usando los 4 valores del UUID
# esto se ejecutara dentro de otra funcion y se le pasara como parametro model.cache.user ya formateado en este docuento
# data modify storage cubikframework users."$(user[0])"."$(user[1])"."$(user[2])"."$(user[3])" set from storage cubikframework model.cache.user

# {
#   "users": { storage general
#     "uuid_part1": { UUID1
#       "uuid_part2": { UUID2
#         "uuid_part3": { UUID3
#           "uuid_part4": { UUID4
#             "data": { 
#               "name": "SnuggleBebe",
#               "level": 42
#             }
#           }
#         }
#       }
#     }
#   }
# }