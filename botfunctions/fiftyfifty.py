import json
import os
from random import choice
from discord import Embed
import requests

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception as err:
    print(err)

# (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
def result(subbreddit: str, *args):
    response = requests.get(
        str(os.getenv("reddit_api")) + subbreddit
    )  # subbreddit here is always fiftyfifty
    imagedata = json.loads(response.text)

    title1, title2 = imagedata["title"].split("|")
    title1 = title1[8:]

    title1 = title1.lstrip()
    title2 = title2.lstrip()

    url = imagedata["url"]

    embed = Embed(title="50/50 Take The Leap!", color=0x3498DB)

    embed.add_field(
        name=title1.capitalize(), value=f"Has 50% chance of occurring", inline=False
    )
    embed.add_field(
        name=title2.capitalize(), value=f"Has 50% chance of occurring", inline=False
    )

    embed.add_field(
        name="What's This?",
        value="Out of the two possibilities only one is the actual result. \nSince you don't know which you'll get until you click the link, you have a 50/50 chance of getting one or the other.",
        inline=False,
    )

    embed.add_field(name="Click the Below Link!", value=url)
    embed.set_image(
        url=choice(
            [
                "https://imgur.com/rXqB1Vn.png",
                "https://imgur.com/AmAT0mV.png",
                "https://imgur.com/ce5OTTz.png",
                "https://imgur.com/xc7Lxni.png",
                "https://imgur.com/rdP7U4N.png",
            ]
        )
    )

    return (None, embed, True, False, False)
