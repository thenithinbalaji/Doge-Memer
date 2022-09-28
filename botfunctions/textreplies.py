from random import choice
from typing import Tuple
from botfunctions.utility import load_mongo_botdata

# botdata collection from maindb is loaded
data = load_mongo_botdata()

# (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
def result(action_type: str, roasted_user_id: int = None):

    if action_type == "hello":
        return (choice(data["hellolist"]), None, True, True, False)

    elif action_type == "roast":
        if roasted_user_id != None:
            return (
                f"<@{roasted_user_id}> {choice(data['roastlist'])}",
                None,
                False,
                False,
                False,
            )
        else:
            return (
                "Hey Boomer! Tag someone along with the message to roast them",
                None,
                True,
                True,
                False,
            )

    elif action_type == "name":
        return (choice(data["namereplylist"]), None, True, False, False)
