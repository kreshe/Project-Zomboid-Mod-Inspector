from core.rules import (
    CRITICAL_CLASSES,
    IMPORTANT_FUNCTIONS
)

def risk_text(value):

    if value >= 90:
        return "🔴 CRITICAL"

    elif value >= 60:
        return "🟠 HIGH"

    elif value >= 30:
        return "🟡 MEDIUM"

    else:
        return "🟢 LOW"


def calculate_lua_risk(
        class_name="",
        function_name="",
        same_file=False
):

    risk = 0


    if class_name in CRITICAL_CLASSES:

        risk += 40


    if function_name in IMPORTANT_FUNCTIONS:

        risk += 30


    if same_file:

        risk += 30



    return min(risk,100)

    