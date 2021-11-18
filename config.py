import discord
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from discord import Activity, ActivityType

from discord_slash import SlashCommand
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.utils.manage_components import wait_for_component
from discord_slash.model import ButtonStyle
import requests
from requests.structures import CaseInsensitiveDict
import json
import os

import asyncio
from termcolor import colored
from datetime import datetime



intents = discord.Intents.default()
discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)


worldname = "bifrost" # Change this to the world you want to track.
guild_ids = [] # Put your server ID in this array.
my_secret = "" # Add your Bot secret here.
prefix = f"@New World Bot :" #Change this if you want, its just what displays in the console.


BearerTokenAPI = "" #Grab your Bearer Token from https://newworldstatus.com/unofficial-status-api

# Create three channels and grab the ID's for these variables.
CategoryName = 905480752056107078 #Put channel ID You want here.
Playerschannel = 905480752727216128 #Put channel ID You want here.
QueueChannel = 905480753335386202 #Put channel ID 2 You want here.
MinutesToWaitChannel = 905480753960353812 #Put channel ID 3 You want here.
Log_Channel = 534534543543534534




client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
bot = discord.Client()
guilds = len(list(bot.guilds))
