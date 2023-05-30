import json
import os

import discord
import requests

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception as err:
    print(err)

# (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
def result(subbreddit: str = None, *args):
    if subbreddit == "default":
        response = requests.get(str(os.getenv("reddit_api")))
        imagedata = json.loads(response.text)
    else:
        response = requests.get(str(os.getenv("reddit_api")) + "/" + subbreddit)
        imagedata = json.loads(response.text)

    try:
        image_title = imagedata["title"]
        post_link = imagedata["postLink"]
        image_url = imagedata["url"]
        nsfw_bool = imagedata["nsfw"]
    except:
        image_title = "Error. Try something else"
        post_link = "https://i.redd.it/j7nutaa69ej51.png"
        image_url = "https://i.redd.it/j7nutaa69ej51.png"
        nsfw_bool = False

    if "irl" in image_title.lower():
        image_title = "Here is what you asked for"

    embed = discord.Embed(title=image_title, url=post_link)
    embed.set_image(url=image_url)

    if nsfw_bool == False:
        return (None, embed, True, False, False)
    else:
        return (None, embed, True, False, True)
