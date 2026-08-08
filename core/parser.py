from pathlib import Path

from core.models import ModInfo



def parse_mod(folder: Path):

    mod = ModInfo()

    mod.path = folder

    mod.workshop_id = folder.name


    #
    # ищем mod.info
    #

    info_files = list(folder.rglob("mod.info"))


    if info_files:

        info = info_files[0]


        with open(
            info,
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


                key = key.lower()


                if key == "id":
                    mod.mod_id = value


                elif key == "name":
                    mod.name = value


                elif key == "description":
                    mod.description = value


                elif key == "version":
                    mod.version = value

                elif key == "require":

                    deps = value.replace(",", ";").split(";")

                    mod.dependencies.extend(
                        x.strip()
                        for x in deps
                        if x.strip()
                    )


    #
    # поиск файлов
    #

    for file in folder.rglob("*"):


        if not file.is_file():
            continue


        suffix = file.suffix.lower()


        if suffix == ".lua":

            mod.lua_files.append(file)


        elif suffix == ".txt":

            if "scripts" in str(file).lower():

                mod.script_files.append(file)


        elif "media\\maps" in str(file).lower():

            mod.map_files.append(file)



    return mod