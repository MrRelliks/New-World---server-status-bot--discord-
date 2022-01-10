from config import *
from memberevents import *
from worldupdate import *
from commandsslash import *
from NewWorldCommands import *
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
#Clears console on launch to keep things tidy.
clearConsole()

guild_data = []



@client.event
async def on_ready():

    members = 0
    
    for guild in client.guilds:
        members += guild.member_count - 1 
    #await client.change_presence(activity=discord.Game(name=f"New World with {members} members."))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{members} members."))
    print(colored (f"{prefix} Ready and Watching {str(members)} members.", 'grey','on_white'))
    print(colored (f"{prefix} Please Wait whilst I gather the server information for {worldname}.", 'grey','on_white'))
    #f = open(f'json/Guilds/{guild.name}.json')
    #guild_data = json.load(f)
    #category_old = guild_data[f'{guild.name}']['Game Name']

    #guild_data[f'{guild.name}'] = {"Category_ID": "","Players_ID: ", "Queue_ID": "", "Wait_ID": ""}
    #role_old = user_data[f'{ctx.author.name}']['Role']
    #level_old = user_data[f'{ctx.author.name}']['Level']
    #user_data[f'{ctx.author.name}'] = {'User ID': f"{ctx.author.id}", 'Game Name': f"{ingamename_old}", 'Level': f"{level_old}",'Role': f"{role_old}",'Company': f"{company}"}
    #with open(f'json/Users/{ctx.author.name}_user_data.json', 'w') as f:
    #    json.dump(user_data, f)
    #await ctx.send(f"{ctx.author.name}, Your company has been updated.")
    ServerStats.start()


   
    
client.run(my_secret)