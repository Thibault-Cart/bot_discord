import discord
from menu import Recevoir_menu

TOKEN = "MTAzOTUxODc3MTQzMTM2MjU5Mg.GGeiof.C2e74AyGxzpMl3vOL98HNlTqYhhWBWBy8sqbyM"


intents = discord.Intents.all()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Le bot est prêt !")


@client.event
async def on_message(message):
    if (message.content == "--menu"):
        print("toto\n")
        menu = ""
        channel = message.channel
        for i in Recevoir_menu():
            menu += f"\n le menu de {i[0]} est :\n "
            menu += f"\n:hamburger:{i[1]}  \n :money_with_wings: {i[2]} , {i[3]}"
            menu += f"\n:hamburger:{i[4]}  \n :money_with_wings: {i[5]} , {i[6]}"
            menu += f"\n:hamburger:{i[7]}  \n :money_with_wings: {i[8]} , {i[9]}"
            menu += f"\n:hamburger:{i[10]} \n :money_with_wings: {i[11]} , {i[12]}\n\n\n"
            await channel.send(menu)
            menu = ""

client.run(TOKEN)
