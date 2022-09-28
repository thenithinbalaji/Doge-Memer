from discord import Color
from random import choice
from typing import Tuple
from botfunctions.utility import load_mongo_botdata, buildembed

# botdata collection from maindb is loaded
data = load_mongo_botdata()

# grammer correction to actions
edeed = {
    "kill": "killed",
    "kiss": "kissed",
    "lick": "licked",
    "punch": "punched",
    "slap": "slapped",
    "moment": "is having their moment with",
    "pain": "caused unbearable pain to",
}

embed_color = {
    "kill": Color.from_rgb(255, 0, 60),
    "kiss": Color.from_rgb(255, 0, 212),
    "lick": Color.from_rgb(0, 213, 255),
    "punch": Color.from_rgb(255, 0, 60),
    "slap": Color.from_rgb(255, 0, 60),
    "moment": Color.from_rgb(0, 213, 255),
    "pain": Color.from_rgb(255, 0, 60),
}

# (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
def result(action_type: str, from_whom: str, to_whom: str = None):

    if to_whom != None:
        embedtitle = f"{from_whom} {edeed[action_type]} {to_whom}!"
        if to_whom != from_whom:
            gifurl = choice(data[action_type + "_giflist"])
        else:
            if action_type == "kiss":
                gifurl = "https://imgur.com/tDqySEz"
            elif action_type == "lick":
                gifurl = "https://imgur.com/PkxWIH5"
            else:
                gifurl = "https://imgur.com/YtP9Vgx"
        return (
            None,
            buildembed(
                heading=embedtitle, main_image=gifurl, ecolor=embed_color[action_type]
            ),
            False,
            False,
            False,
        )

    else:
        return (
            f"Mention the person you want to **{action_type.upper()}** with the message",
            None,
            True,
            True,
            False,
        )
