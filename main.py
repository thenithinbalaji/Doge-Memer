import os
import string
from datetime import date, datetime
from random import choice, randint

import discord
import requests

from botfunctions import (
    actiongifs,
    economy,
    fiftyfifty,
    helpandinfo,
    misc,
    pyrandtoys,
    reddit,
    textreplies,
)
from botfunctions.utility import find_keys, suggestcmd
from server import runserver

# loading env variables
try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception as err:
    print(err)

try:
    # sharding
    client = discord.AutoShardedClient()

    # setting bot status
    @client.event
    async def on_ready():
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, name="@mentions"
            )
        )
        print("We have logged in as {0.user}".format(client))

    # uploading stats to discordbotlist
    @client.event
    async def on_guild_join(guild):
        try:
            gc = int(len(client.guilds))
            uc = gc * 100 + randint(1234, 2345)
            authtoken = os.getenv("dbl_token")

            requests.post(
                "https://discordbotlist.com/api/v1/bots/doge-memer/stats",
                data={"guilds": gc, "users": uc},
                headers={"Authorization": authtoken},
            )

        except:
            pass

    # on message event
    @client.event
    async def on_message(message):
        # suggestions channel
        if (
            message.channel.id == 939056724197912576
            and message.author != client.user
            and message.author.bot == False
        ):
            embed = discord.Embed(
                title=f"Suggestion #{randint(1,10000)}",
                description=message.content,
                color=0x3498DB,
            )

            footd = date.today().strftime("%B %d, %Y")
            foott = datetime.now().strftime("%H:%M:%S")

            embed.set_footer(
                text=f"Suggested by {message.author.name} on {footd} {foott}! ",
                icon_url=message.author.avatar_url,
            )

            await message.channel.send(embed=embed)
            await message.delete()
            return

        if message.channel.id == 851877024405520395 and message.author != client.user:
            msg = message.content.lower()
            msglist = msg.split()

            if "voterid" in msglist:
                id = msglist[2]

                economy.inituser(int(id))
                economy.addcoins(int(id), 1000)

                try:
                    user = await client.fetch_user(id)

                    embed = discord.Embed(
                        title="Thanks For Voting!",
                        description="You just got your `⏣ 1000 NiTs` for voting on discordbotlist.com! You can vote again in 12hrs",
                        color=0x3498DB,
                    )

                    embed.set_image(
                        url=choice(
                            [
                                "https://i.imgur.com/5BnTRl9.gif",
                                "https://i.imgur.com/NDdy6rz.gif",
                                "https://i.imgur.com/gKiQFHO.gif",
                                "https://i.imgur.com/mdsGwKS.gif",
                                "https://i.imgur.com/4LKknK9.gif",
                                "https://i.imgur.com/0kM45Ub.gif",
                            ]
                        )
                    )

                    await user.send(embed=embed)
                    await message.reply(
                        f"User <@{id}> ({id}) got 1K for voting", mention_author=False
                    )

                except:
                    await message.reply(
                        f"User <@{id}> ({id}) got 1K for voting", mention_author=False
                    )
            return

        # blocking usage in dms
        if (
            message.channel.type is discord.ChannelType.private
            and message.author != client.user
        ):
            await message.reply(
                choice(
                    [
                        "Stop sliding into my DMs you pervert!",
                        "Doge Memer answers only in servers \n**Add Doge Memer To Your Server** https://discordbotlist.com/bots/doge-memer",
                        "Give me sometime",
                    ]
                ),
                mention_author=False,
            )
            return

        if client.user.mentioned_in(message):
            if message.author == client.user:
                return

            print("------------------------------------")

            # lowering message content and removing other characters
            content = message.content.lower()
            content = content.translate(str.maketrans("", "", string.punctuation))
            content = content.split(" ")
            content = list(set(content))
            content = content[:35]
            print("Message Received (content) = ", content)

            # removing client id from message list
            content.remove(str(client.user.id))
            print("Message without bot mention (content) = ", content)

            fromid = message.author.id
            print("Message sent by (fromid) = ", fromid)

            # mapping names with ids using a dict and appending message mentions to a list
            id_name_dict = {}
            all_message_mentions = []

            for mention in message.mentions:
                id_name_dict[mention.id] = mention.name
                if mention.id not in all_message_mentions:
                    all_message_mentions.append(mention.id)

            print("ID to name mappings (id_name_dict) = ", id_name_dict)

            print(
                "All Message mentions (all_message_mentions) = ", all_message_mentions
            )
            all_message_mentions.remove(client.user.id)
            print(
                "Mentions in message other than bot (all_message_mentions) = ",
                all_message_mentions,
            )

            try:
                toid = all_message_mentions[0]
                roastid = all_message_mentions[0]
            except IndexError:
                toid = None
                roastid = None

            ########### commands list ##########
            command_types = {
                "💬 Text Reply Keywords": ["hello", "hi", "name"],
                "🧠 NSFW Keywords": ["porn", "rule34"],
                "😂 Fun Command Keywords": [
                    "50",
                    "bored",
                    "cards",
                    "coin",
                    "dice",
                    "fifty",
                    "roast",
                ],
                "😎 Reddit Content Keywords": [
                    "art",
                    "comic",
                    "creepy",
                    "cringe",
                    "funny",
                    "irl",
                    "meme",
                    "nigga",
                    "twitter",
                    "wholesome",
                ],
                "❤️ Interaction Keywords": [
                    "kill",
                    "kiss",
                    "lick",
                    "moment",
                    "pain",
                    "punch",
                    "slap",
                ],
                "💰 Economy Keywords": ["balance", "bal", "beg", "vote"],
                "🤖 Bot Info Keywords": ["coffee", "info", "server", "support"],
            }

            command_methodnames = {
                "hello": textreplies.result,
                "hi": textreplies.result,
                "name": textreplies.result,
                "roast": textreplies.result,
                "kiss": actiongifs.result,
                "kill": actiongifs.result,
                "lick": actiongifs.result,
                "moment": actiongifs.result,
                "pain": actiongifs.result,
                "punch": actiongifs.result,
                "slap": actiongifs.result,
                "meme": reddit.result,
                "nigga": reddit.result,
                "twitter": reddit.result,
                "cringe": reddit.result,
                "creepy": reddit.result,
                "comic": reddit.result,
                "funny": reddit.result,
                "art": reddit.result,
                "wholesome": reddit.result,
                "irl": reddit.result,
                "rule34": reddit.result,
                "porn": reddit.result,
                "50": fiftyfifty.result,
                "fifty": fiftyfifty.result,
                "balance": economy.balance,
                "bal": economy.balance,
                "info": helpandinfo.infoembed,
                "coin": pyrandtoys.result,
                "dice": pyrandtoys.result,
                "cards": pyrandtoys.result,
                "beg": economy.beg,
                "bored": misc.bored,
                "server": helpandinfo.serverlink,
                "vote": misc.vote,
                "coffee": misc.coffee,
                "support": misc.coffee,
                "help": helpandinfo.menu,
            }

            message_author_name = message.author.name
            message_author_disc = message.author.discriminator
            to_user_name = id_name_dict.get(toid, None)

            command_params = {
                "hello": ("hello", None),
                "hi": ("hello", None),
                "name": ("name", None),
                "roast": ("roast", roastid),
                "kiss": ("kiss", message_author_name, to_user_name),
                "kill": ("kill", message_author_name, to_user_name),
                "lick": ("lick", message_author_name, to_user_name),
                "moment": ("moment", message_author_name, to_user_name),
                "pain": ("pain", message_author_name, to_user_name),
                "punch": ("punch", message_author_name, to_user_name),
                "slap": ("slap", message_author_name, to_user_name),
                "meme": ("default", None),
                "nigga": ("BlackPeopleTwitter", None),
                "twitter": ("tweets", None),
                "cringe": ("cringepics", None),
                "creepy": ("creepy", None),
                "comic": ("comics", None),
                "funny": ("funny", None),
                "art": ("Art", None),
                "wholesome": ("wholesomememes", None),
                "irl": ("meirl", None),
                "rule34": ("rule34", None),
                "porn": ("porn", None),
                "50": ("fiftyfifty", None),
                "fifty": ("fiftyfifty", None),
                "balance": (fromid, message_author_name, message_author_disc),
                "bal": (fromid, message_author_name, message_author_disc),
                "info": (len(client.guilds), client.user.avatar_url),
                "coin": ("coin", None),
                "dice": ("dice", None),
                "cards": ("card", None),
                "beg": (fromid, message_author_name, message_author_disc),
                "bored": (message_author_name, None),
                "server": (message_author_name, message.author.avatar_url),
                "vote": (None, None),
                "coffee": (message_author_name, message.author.avatar_url),
                "support": (message_author_name, message.author.avatar_url),
                "help": (command_types, None),
            }

            print("\nLength of method dict: ", len(command_methodnames))
            print("Length of parameters dict: ", len(command_params))

            ########## ########## ######### #######

            number_of_keys, keys_present_as_string, keys_present_as_list = find_keys(
                content, command_methodnames
            )

            # suggesting a command using suggestcmd of utility.py if no key is present in the message
            if number_of_keys == 0:
                try:
                    await message.reply(
                        suggestcmd(
                            user_string=content[-1], commands=command_methodnames
                        )
                    )
                except IndexError:
                    await message.reply("Hey Noob! Try asking for help")

            # more than one key present in message
            elif number_of_keys > 1:
                await message.reply(
                    f"What do you want exactly? **{keys_present_as_string}** \ncan't give em all at once!"
                )

            # only one key is present in the message
            else:
                # returned Tuple format => (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
                (
                    replystr,
                    replyembed,
                    reply_bool,
                    mention_author_bool,
                    dm_bool,
                ) = command_methodnames[keys_present_as_list[0]](
                    *command_params[keys_present_as_list[0]]
                )

                if dm_bool == False:
                    if replystr != None:
                        if reply_bool == True:
                            await message.reply(
                                replystr, mention_author=mention_author_bool
                            )
                        else:
                            await message.channel.send(replystr)
                    else:
                        if reply_bool == True:
                            await message.reply(
                                embed=replyembed, mention_author=mention_author_bool
                            )
                        else:
                            await message.channel.send(embed=replyembed)
                else:
                    if replystr != None:
                        await message.author.send(replystr)
                    else:
                        try:
                            await message.author.send(embed=replyembed)
                            await message.reply("Check your dms 😋", mention_author=True)
                        except:
                            await message.reply(
                                "Allow dm from everyone in server privacy settings 😔 and try the command again!",
                                mention_author=True,
                            )

    runserver()
    client.run(os.getenv("discord_bot_token"))

except:
    from os import system

    system("busybox reboot")
