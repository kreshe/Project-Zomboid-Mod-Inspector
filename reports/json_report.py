import json
from datetime import datetime



def save_json_report(
        filename,
        mods,
        lua_conflicts,
        item_conflicts,
        missing,
        order
):

    report = {

        "created":

            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            ),


        "summary": {

            "mods":

                len(mods),


            "lua_conflicts":

                len(lua_conflicts),


            "item_conflicts":

                len(item_conflicts),


            "missing_dependencies":

                len(missing),


            "load_order_problems":

                len(order)

        },


        "conflicts": []

    }



    #
    # LUA
    #

    for c in lua_conflicts:


        report["conflicts"].append({

            "type":
                "lua",


            "class":
                c["class"],


            "function":
                c["function"],


            "mods":
                c["mods"],


            "risk":
                c["risk"]

        })



    #
    # ITEMS
    #

    for c in item_conflicts:


        report["conflicts"].append({

            "type":
                "item",


            "id":
                c["item"],


            "mods":
                c["mods"],


            "risk":
                c["risk"]

        })



    #
    # DEPENDENCIES
    #

    report["dependencies"] = {

        "missing":

            missing,


        "load_order":

            order

    }



    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:


        json.dump(

            report,

            file,

            indent=4,

            ensure_ascii=False

        )

