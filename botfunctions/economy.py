import pymongo
import os
from discord import Embed
from random import randint

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception as err:
    print(err)


def inituser(userid: int):
    mongourl = os.environ.get("mongodb_connection_string")
    mongo = pymongo.MongoClient(mongourl)["maindb"]["userdata"]

    if mongo.count_documents({"_id": userid}) == 0:
        mongo.insert_one({"_id": userid, "bal": 500})


# (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
def balance(userid: int, username: str, disc: str):

    mongourl = os.environ.get("mongodb_connection_string")
    mongo = pymongo.MongoClient(mongourl)["maindb"]["userdata"]

    bal = 0

    if mongo.count_documents({"_id": userid}) == 0:
        mongo.insert_one({"_id": userid, "bal": 500, "name": username, "disc": disc})
        bal = 500
    else:
        try:
            mongo.update_one(
                {"_id": userid}, {"$set": {"name": username, "disc": disc}}
            )
            bal = mongo.find_one({"_id": userid})["bal"]
        except KeyError:
            mongo.update_one(
                {"_id": userid}, {"$set": {"bal": 500, "name": username, "disc": disc}}
            )
            bal = 500

    embed_title = f"{username}'s Bank Balance"
    embed_desc = f"**Wallet:** ⏣ {bal} NiTs"

    embed = Embed(title=embed_title, description=embed_desc, color=0xF1C40F)

    return (None, embed, True, True, False)


# (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
def beg(userid: int, username: str, disc: str):

    mongourl = os.environ.get("mongodb_connection_string")
    mongo = pymongo.MongoClient(mongourl)["maindb"]["userdata"]

    inituser(userid)

    coin = randint(-15, 25)

    if coin <= 0:
        coin = 0
        message = f"and got a punch on the face, poor begger!"
        embed_color = 0xE74C3C
    else:
        message = f"and got ⏣ {coin} NiTs damn lucky peep"
        embed_color = 0x2ECC71

        bal = mongo.find_one({"_id": userid})["bal"]
        bal = bal + coin
        mongo.update_one(
            {"_id": userid}, {"$set": {"bal": bal, "name": username, "disc": disc}}
        )

    embed = Embed(
        title=f"{username} Started Begging", description=message, color=embed_color
    )

    return (None, embed, True, True, False)


def addcoins(userid: int, amount: int):

    inituser(userid)

    mongourl = os.environ.get("mongodb_connection_string")
    mongo = pymongo.MongoClient(mongourl)["maindb"]["userdata"]

    mongo.update_one({"_id": userid}, {"$inc": {"bal": amount}})
