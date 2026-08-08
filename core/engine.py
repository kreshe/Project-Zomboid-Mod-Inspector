from engines.conflict_engine import (
    check_lua_conflicts,
    check_item_conflicts
)

from analyzers.dependency import (
    check_missing_dependencies,
    check_load_order
)


class ModChecker:


    def __init__(self, mods):

        self.mods = mods



    def run(self):

        return {

            "lua":
                check_lua_conflicts(
                    self.mods
                ),


            "items":
                check_item_conflicts(
                    self.mods
                ),


            "missing":
                check_missing_dependencies(
                    self.mods
                ),


            "order":
                check_load_order(
                    self.mods
                )
        }