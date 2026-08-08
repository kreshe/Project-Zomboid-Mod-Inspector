import re

from pathlib import Path

from core.models import LuaFunction



def analyze_lua(file: Path):

    result = []


    try:

        text = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )


    except:

        return result



    #
    # ищем:
    #
    # function Class:method()
    #

    pattern = (
        r"function\s+"
        r"([A-Za-z0-9_]+)"
        r":"
        r"([A-Za-z0-9_]+)"
    )


    matches = re.findall(
        pattern,
        text
    )


    for cls, func in matches:

        result.append(

            LuaFunction(
                class_name=cls,
                function_name=func,
                file=file,
                relative_file=str(file)
            )
        )


    return result