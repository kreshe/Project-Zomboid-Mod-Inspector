from pathlib import Path
import re



def analyze_script(file: Path):

    items = []


    try:

        text = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except:

        return items



    #
    # Project Zomboid scripts:
    #
    # item Name
    #
    # recipe Name
    #


    item_pattern = r"\bitem\s+([A-Za-z0-9_]+)"


    for match in re.findall(
        item_pattern,
        text,
        re.IGNORECASE
    ):

        item = match


        if item.isdigit():

            continue


        if len(item) < 3:

            continue


        items.append(item)


    return items