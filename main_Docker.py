
## Import discord libraries
import discord 
from discord.ext import commands
from discord import app_commands

#### Import Open AI libraries and the api_key
import os
from dotenv import load_dotenv
from openai import OpenAI
####

### Load enviormental Variables 

# Load the .env file
load_dotenv()

# Loads env variables from .env file
api_key = os.getenv("API_KEY")
channel_id= os.getenv("channel_id")
server_id=os.getenv("server_id")
bot_api_key=os.getenv("bot_api_key")

## checks to see there is a valid API key
if api_key is None:
    print("missing API Key")
##########################


#Creates class Client
class Client(commands.Bot):

    async def on_ready(self): #runs when program starts and is "ready"
        print(f'Logged on as {self.user}!') #Tells you that the bot logged on

        try: ##Syncs commands and ensures commands are synced 
            guild =discord.Object(server_id) #The server ID goes here/load from .env
            synced= await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        #Exceptions if commands aren't loaded 
        except Exception as e:
            print(f'Error syncing commands {e}')


        # attempts to find channel in cache
        channel = client.get_channel(channel_id) ## Channel ID
        
        # Send a message when the bot starts
        #if it can't find channel it will fetch it
        if channel is None:
            print(f'Channel not found in chache, attempting to fetch')
            try:
                channel = await client.fetch_channel(channel_id) # fetching channel from API
                if channel:
                    print(f'Channel fetched succesfully') # showing you that it found it
            except discord.NotFound:
                print(f'Channel not found!') #error messages
                return
            except discord.Forbidden:
                print(f'Bot lacks permissions for this channel') #error messages
                return
            except discord.HTTPException as e:
                print(f'Error fetching channel: {e}') #error messages
                return
        if channel:
            await channel.send("Hello! The bot is now online, made by NoMangosForYou") #print message on startup
        else:
            print("Channel not found!") #put the above to avoid this (aka fetching channel)



## sets intents of dicord (ie permissions of bot)
intents = discord.Intents.default() #what events it can read from discord 
intents.message_content=True #allows bot access to message content
client=Client(command_prefix="!", intents=intents) #bot will recognize commands


# loads Open API Client as bait_bot
bait_bot = OpenAI(api_key=api_key)


GUILD_ID =discord.Object(server_id) #The server ID goes here to send to server, held in .env

#Grabs Profiles of players from text file 

with open("profiles.txt", "r") as file:
    profiles=file.read()

## First /command

@client.tree.command(name="roast", description="Roasts a person add a reason if you wish", guild=GUILD_ID)

async def roast(interaction: discord.Interaction, person: str, rationale: str = "Being bad at video games"):

    
    await interaction.response.defer() # tells discord to wait for the message instead of timing-out

    completion = bait_bot.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an aggressive and mean coach for the video games, you are brutal to the players you coach, Only one player at a time and only when someone tells you which player that is. Only anwser in a max of 5 sentences\n"
        f"Here are your players profiles: {profiles}"
        "Any name you don't know make fun of them for being bad at videogames"
        ""},
        {
            "role": "user",
            "content": f"{person} for {rationale}"
        }
    ]
)
    await interaction.followup.send(completion.choices[0].message.content) 

#####################


@client.tree.command(name="cs2question", description="Ask a CS2 Question", guild=GUILD_ID)

async def cs2q(interaction: discord.Interaction, csquestion: str):

    
    await interaction.response.defer() # tells discord to wait for the message instead of timing-out

    completion = bait_bot.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a coach for the video game counter-strike 2, you will be as helpful as possible with players questions, but only put the instructions in do not explain the relevance or best practices"
       
        },
        {
            "role": "user",
            "content": csquestion
        }
    ]
)
    await interaction.followup.send(completion.choices[0].message.content) 


@client.tree.command(name="question", description="Ask a Question", guild=GUILD_ID)

async def question(interaction: discord.Interaction, question: str):

    
    await interaction.response.defer() # tells discord to wait for the message instead of timing-out

    completion = bait_bot.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant, but will not anwser in more than 20 sentences. You always print: Thank you for using Bait-Bot at the end of every reply"
       
        },
        {
            "role": "user",
            "content": question
        }
    ]
)
    await interaction.followup.send(completion.choices[0].message.content) 

client.run(bot_api_key) # API Key for discord Running