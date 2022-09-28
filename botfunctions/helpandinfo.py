from random import choice
from discord import Embed

# (message reply string, message reply embed, reply to message bool, mention author bool, dm bool)
def infoembed(guilds_count: int, thumb_url: str):

    embed = Embed(
        title="Doge Memer Information",
        description="Mention the bot to get started! \nTry `@Doge Memer help` to get keywords list\nAnswers based on keywords detected in your message",
        color=0x3498DB,
    )

    embed.add_field(name="Support Keywords", value="`help` | `server` ", inline=True)

    embed.add_field(name="Server Count", value=f"`{guilds_count}`", inline=False)

    embed.add_field(name="Current Language", value="`English`", inline=True)

    embed.add_field(
        name="Created By",
        value="`thenithinbalaji`",
        inline=False,
    )
    embed.set_thumbnail(url=thumb_url)
    embed.set_footer(text="Doge Memer Discord Bot ©️ 2021 thenithinbalaji")

    return (None, embed, True, False, False)


def serverlink(message_author: str, img_url: str):
    embed = Embed(
        title="Join Official Server of Doge Memer",
        url="https://discord.gg/SuxjTdEcEm",
        description="Get Pre-Updates, Check Bot Status, Test Beta Features, Submit Bug Reports, Become a Developer and get Extra Perks",
        color=0x3498DB,
    )

    embed.set_footer(
        text=f"Invite Link generated for {message_author}",
        icon_url=img_url,
    )

    return (None, embed, True, False, False)


def menu(command_types: dict, *argv):
    embed = Embed(
        title="Doge Memer Keywords List",
        description="Mention the bot to get started! \nTry `@Doge Memer help` to get keywords list\nAnswers based on keywords detected in your message\n\nExample: `@Doge Memer show me a meme`",
        color=0x3498DB,
    )

    for type in command_types.keys():
        cmdstr = "|" + " "
        for cmd in command_types[type]:
            cmdstr = cmdstr + f"`{cmd}` |" + " "

        if len(command_types[type]) > 5:
            inline_bool = False
        else:
            inline_bool = True

        embed.add_field(name=type, value=cmdstr, inline=inline_bool)

    embed.set_image(
        url=choice(
            [
                "https://i.imgur.com/lySHs1n.gif",
                "https://i.imgur.com/WgXqGxh.gif",
            ]
        )
    )

    return (None, embed, True, False, False)
