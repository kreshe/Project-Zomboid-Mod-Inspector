from pathlib import Path



def resolve_workshop(mods):

    result = {}


    for mod in mods:


        workshop = mod.workshop_id


        if not workshop:
            continue



        if workshop not in result:

            result[workshop] = []



        result[workshop].append({

            "mod_id": mod.mod_id,

            "name": mod.name,

            "path": str(mod.path)

        })


    return result