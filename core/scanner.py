from pathlib import Path

from core.parser import parse_mod


def scan_workshop(workshop_path):

    mods = []


    workshop_path = Path(
        workshop_path
    )


    if not workshop_path.exists():

        return mods



    for workshop_id in workshop_path.iterdir():

        if not workshop_id.is_dir():
            continue


        mod_infos = list(
            workshop_id.rglob(
                "mod.info"
            )
        )


        if not mod_infos:
            continue


        # берем только первый mod.info
        info = mod_infos[0]


        mod_folder = info.parent


        mod = parse_mod(
            mod_folder
        )


        mod.workshop_id = workshop_id.name


        mods.append(mod)
    return mods