$execute as @s at @s run give @s minecraft:iron_leggings[ custom_model_data={strings:['$(name)']}, custom_name='["",{"text":"Blue Nappy","italic":false}]',lore=['["",{"text":"Place on pants slot","italic":false}]'] ,minecraft:equippable={slot:legs, asset_id:"minecraft:$(name)", equip_sound:"block.wool.place"}, minecraft:custom_data={padding: 0, index:1}, unbreakable={show_in_tooltip:true}]