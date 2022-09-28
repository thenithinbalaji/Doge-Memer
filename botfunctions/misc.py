import requests
import json
from discord import Embed
import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception as err:
    print(err)

# (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
def bored(author_name: str, *args):
    response = requests.get(str(os.getenv("bored_api")))
    json_data = json.loads(response.text)

    embed = Embed(
        title=f"Oh {author_name}! Are you bored?? Try this."
        + " "
        + json_data["activity"],
        description="You can sharpen your"
        + " "
        + json_data["type"]
        + " "
        + "skills by doing this",
        color=0x3498DB,
    )

    return (None, embed, True, False, False)


def vote(*args):
    embed = Embed(
        title="Vote and Earn Coins!",
        url="https://discordbotlist.com/bots/doge-memer/upvote",
        description="Earn 1000 NiTs for every vote you make",
        color=0x3498DB,
    )

    embed.set_footer(text=f"You can only vote once in 12hrs")

    return (None, embed, True, False, False)


def coffee(author_name: str, author_icon: str):
    embed = Embed(
        title="Support Doge Memer",
        url="https://www.buymeacoffee.com/thenithinbalaji",
        description="Are you satisfied with Doge Memer's Performance?!! If you want to talk about it over some coffee, feel free to press support",
        color=0x3498DB,
    )

    embed.set_footer(
        text=f"Hey {author_name}! We need your help to maintain our server and database.",
        icon_url=author_icon,
    )

    return (None, embed, True, False, False)
