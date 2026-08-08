from analyzers.lua_analyzer import analyze_lua
from analyzers.script_analyzer import analyze_script


def index_mod(mod):


    for lua in mod.lua_files:

        functions = analyze_lua(lua)

        mod.lua_functions.extend(
            functions
        )


    for script in mod.script_files:

        items = analyze_script(script)

        mod.item_ids.update(
            items
        )


    return mod