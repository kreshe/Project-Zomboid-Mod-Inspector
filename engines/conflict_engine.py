from collections import defaultdict

from engines.risk_engine import calculate_lua_risk



def check_lua_conflicts(mods):

    conflicts = []

    index = defaultdict(set)


    #
    # индексируем Lua
    #

    for mod in mods:

        for func in mod.lua_functions:

            key = (
                func.class_name,
                func.function_name
            )

            index[key].add(mod)



    #
    # ищем пересечения
    #

    for key, owners in index.items():


        if len(owners) < 2:
            continue


        class_name, function_name = key


        risk = calculate_lua_risk(

            class_name=class_name,

            function_name=function_name

        )


        if risk == 0:
            continue



        mods_list = sorted(
            {
                m.name
                for m in owners
            }
        )


        conflicts.append({

            "type": "lua",

            "class": class_name,

            "function": function_name,

            "mods": mods_list,

            "risk": risk

        })


    return conflicts


def check_item_conflicts(mods):

    from collections import defaultdict


    index = defaultdict(list)


    for mod in mods:

        for item in mod.item_ids:

            index[item].append(
                mod
            )


    conflicts = []


    for item, owners in index.items():


        if len(owners) < 2:
            continue


        conflicts.append({

            "type": "item",

            "item": item,

            "mods": [
                m.name
                for m in owners
            ],

            "risk": 100

        })


    return conflicts

def check_lua_conflicts(mods):

    from collections import defaultdict


    index = defaultdict(list)


    for mod in mods:

        for func in mod.lua_functions:

            key = (
                func.class_name,
                func.function_name
            )

            index[key].append(
                mod
            )


    conflicts = []


    for key, owners in index.items():


        if len(owners) < 2:
            continue


        class_name, function_name = key

        
            
        risk = calculate_lua_risk(

            class_name=class_name,

            function_name=function_name

        )

        if risk == 0:

         continue

        conflicts.append({

            "type": "lua",

            "class": class_name,

            "function": function_name,

            "mods": sorted(
                {
                    x.name
                    for x in owners
                }
            ),

            "risk": risk

        })

    return conflicts

def calculate_risk(mods):

    count = len(mods)


    if count >= 3:
        return 98


    if count == 2:
        return 94


    return 50