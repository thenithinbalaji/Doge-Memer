import discord
import os
import pymongo
from rapidfuzz.distance import Levenshtein
from typing import Tuple

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception as err:
    print(err)


def secs2str(seconds: int) -> str:
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    if hour == 0 and min != 0:
        return "%02d mins %02d secs" % (min, sec)
    elif hour == 0 and min == 0:
        return "%02d secs" % (sec)
    else:
        return "%d hours %02d mins %02d secs" % (hour, min, sec)


def buildembed(
    heading: str = "Doge Memer",
    subheading: str = None,
    footertext: str = None,
    main_image: str = None,
    footer_image: str = None,
    thumb_image: str = None,
    ecolor=0x3498DB,
    headingurl: str = None,
) -> discord.Embed:

    if subheading != None:
        embed = discord.Embed(title=heading, description=subheading, color=ecolor)
    else:
        embed = discord.Embed(title=heading, color=ecolor)

    if main_image != None:
        embed.set_image(url=main_image)

    return embed


def load_mongo_botdata():
    mongourl = os.environ.get("mongodb_connection_string")
    mongo = pymongo.MongoClient(mongourl)["maindb"]["botdata"]
    return mongo.find_one({"main": True})


def suggestcmd(user_string: str, commands: dict) -> str:
    dist = float("inf")
    for cmd in commands.keys():
        tempdist = Levenshtein.distance(cmd, user_string)
        if dist > tempdist:
            dist = tempdist
            correctcmd = cmd
    return "Did you mean " + correctcmd + "?"


def find_keys(content: list, commands: dict) -> Tuple[int, str, list]:
    number_of_keys = 0
    keys_present_as_string = ""
    keys_present_as_list = []
    for word in content:
        if word in commands.keys():
            number_of_keys += 1
            keys_present_as_string += word + "?" + " "
            keys_present_as_list.append(word)
    return number_of_keys, keys_present_as_string, keys_present_as_list
