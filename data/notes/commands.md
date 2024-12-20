# Comandos

Este comando es un ejemplo de como generar una entidad interactuable con escala 1 x 2

```
/summon minecraft:interaction ~ ~5 ~ {width:1,height:2,response:1b, Tags:[mitag]}
```

Este otro comando sirve para asignarle un evento a esa interacción 

```
execute as @e[type=minecraft:interaction,nbt={interaction:{}},tag=mitag] at @s run say hello
```

Si se quiere que la entidad detecte click izquierdo se usa:

```
execute as @e[type=minecraft:interaction,nbt={attack:{}},tag=mitag] at @s run
```

Este comando se puede usar para remover una interacción de una entidad especifica o de todas las entidades.

```
# todas la entidades
execute as @e[type=minecraft:interaction,nbt={interaction:{}}] run data remove entity @s interaction

# Solo una en especifico
execute as @e[type=minecraft:interaction,nbt={interaction:{}}, tag=mitag] run data remove entity @s interaction

```