import pyrandtoys as pp


def result(toytype: str, *args):
    if toytype == "coin":
        message = f"The coin landed on {pp.coin()[0]}"
    elif toytype == "dice":
        message = f"The die landed on {pp.dice()[0]}"
    elif toytype == "card":
        message = f"You got {pp.card()[0]}"
    else:
        message = "You got nothing"

    # (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
    return (message, None, True, True, False)
