from engines.risk_engine import risk_text


def generate_report(
        mods,
        lua_conflicts,
        item_conflicts,
        missing,
        order
):

    print("\n")
    print("=" * 50)
    print(" PROJECT ZOMBOID MOD INSPECTOR")
    print("=" * 50)


    print()

    print(
        "Модов проверено:",
        len(mods)
    )


    #
    # DEPENDENCIES
    #

    print("\nDEPENDENCY CHECK")
    print("-" * 30)


    print(
        "🔴 Missing dependencies:",
        len(missing)
    )


    print(
        "🟠 Load order problems:",
        len(order)
    )


    #
    # LUA
    #

    print("\nLUA ANALYSIS")
    print("-" * 30)


    critical = 0
    high = 0
    medium = 0


    for c in lua_conflicts:


        if c["risk"] >= 90:

            critical += 1


        elif c["risk"] >= 60:

            high += 1


        else:

            medium += 1



    print(
        "🔴 Critical:",
        critical
    )


    print(
        "🟠 High:",
        high
    )


    print(
        "🟡 Medium:",
        medium
    )



    #
    # ITEMS
    #

    print("\nITEM ANALYSIS")
    print("-" * 30)


    print(
        "🔴 Duplicate IDs:",
        len(item_conflicts)
    )



    #
    # TOP RISKS
    #

    print("\nTOP RISKS")
    print("-" * 30)



    all_conflicts = (
        lua_conflicts +
        item_conflicts
    )


    all_conflicts.sort(
        key=lambda x: x["risk"],
        reverse=True
    )



    for i, conflict in enumerate(
        all_conflicts[:10],
        1
    ):


        print()

        print(
            i,
            "."
        )


        if conflict["type"] == "lua":

            print(
                conflict["class"]
                +
                "::"
                +
                conflict["function"]
            )


        else:

            print(
                "Item:",
                conflict["item"]
            )


        print(
            "Mods:"
        )


        for mod in conflict["mods"]:

            print(
                " -",
                mod
            )


        print(
            "Risk:",
            conflict["risk"],
            "%",
            risk_text(
                conflict["risk"]
            )
        )