from pathlib import Path

from engines.workshop_engine import resolve_workshop



def parse_ini(path):

    data = {}


    if not path.exists():

        return data


    with open(
        path,
        encoding="utf-8",
        errors="ignore"
    ) as file:


        for line in file:


            line = line.strip()


            if "=" not in line:

                continue


            key, value = line.split(
                "=",
                1
            )


            data[key.strip()] = value.strip()


    return data



def split_list(value):

    if not value:

        return []


    return [

        x.strip()

        for x in value.split(";")

        if x.strip()

    ]



def analyze_server(
        server_path,
        mods
):


    server = parse_ini(
        Path(server_path)
    )


    workshop_map = resolve_workshop(
        mods
    )


    result = {

        "missing_mods": [],

        "missing_workshop": [],

        "unused_mods": [],

        "order": []

    }



    #
    # Установленные Mod ID
    #

    installed_ids = {

        m.mod_id

        for m in mods

        if m.mod_id

    }



    #
    # Mods=
    #

    enabled_mods = split_list(

        server.get(
            "Mods",
            ""
        )

    )



    for mod in enabled_mods:


        if mod not in installed_ids:


            result["missing_mods"].append(
                mod
            )



    #
    # WorkshopItems=
    #

    workshop_ids = split_list(

        server.get(
            "WorkshopItems",
            ""
        )

    )



    installed_workshop = {

        m.workshop_id

        for m in mods

    }



    for wid in workshop_ids:


        if wid not in installed_workshop:


            result["missing_workshop"].append(
                wid
            )



    #
    # Лишние моды из Workshop
    #

    enabled_mods_set = set(
        enabled_mods
    )


    for wid, children in workshop_map.items():


        for child in children:


            mod_id = child["mod_id"]


            if (

                mod_id

                and

                mod_id not in enabled_mods_set

            ):


                result["unused_mods"].append(
                    child
                )



    return result