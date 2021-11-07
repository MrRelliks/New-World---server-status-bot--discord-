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
CategoryName = 904763473265823756 #Put channel ID You want here.
Playerschannel = 904763518971166730 #Put channel ID You want here.
QueueChannel = 904763557093203978 #Put channel ID 2 You want here.
MinutesToWaitChannel = 904763596712603698 #Put channel ID 3 You want here.




client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
bot = discord.Client()
guilds = len(list(bot.guilds))
