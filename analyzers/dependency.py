from collections import defaultdict



def build_mod_index(mods):

    index = {}

    for mod in mods:

        if mod.mod_id:

            index[mod.mod_id] = mod


    return index



def check_missing_dependencies(mods):

    errors = []

    index = build_mod_index(mods)


    for mod in mods:


        for dep in mod.dependencies:


            if dep not in index:


                errors.append({

                    "type": "missing_dependency",

                    "mod": mod.name,

                    "dependency": dep

                })


    return errors



def check_load_order(mods):

    problems = []


    positions = {}


    for i, mod in enumerate(mods):

        positions[mod.mod_id] = i



    for mod in mods:


        for dep in mod.dependencies:


            if dep in positions:


                if positions[dep] > positions[mod.mod_id]:


                    problems.append({

                        "type": "load_order",

                        "mod": mod.name,

                        "dependency": dep

                    })


    return problems