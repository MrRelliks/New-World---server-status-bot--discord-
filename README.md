# New-World---server-status-bot--discord-
#### Update 18/01/2022
Refactored the code to work better with JSON data from the nwdb API - You will need to contact the nwdb devs to arrange a unique user agent that identifys you, Its not strictly necessary, but will help if you get rate limited.

#### Update 10/01/2022
Have recoded the bot to work with nwdb since they have merged with newworldstatus and the old method no longer works, as soon as a public API is released I'll update it again but this is the best we have so far.

In order for the bot to work, please replace your worldupdate.py with the new one and change your worldname in config.py to your unique identifier, this can be found at https://nwdb.info/server-status/servers.json

## Description
This is a stripped down version of the Marauder Bot I coded for the bifrost server. It will update (every 180 seonds) the status of a particular world on new world.

The code is pretty simple and can be added in to any existing bot. I have omitted any of the more custom commands/functions of the Marauder bot as they are generally
server specific and most people will be more interested in the world update function anyway.

Your bot needs to have admin permissions as well as intent privileges.

To set up just edit the config.py file with all of the information to make the bot work.

<h2>Docker-ise The Bot</h2>

Thanks to [ChristianRiesen](https://github.com/ChristianRiesen/) for creating a working Docker Image for the bot.

You can run it locally or as this version is meant to, as a docker container.

You will need the following env variables set for it to work:


`WORLD_NAME` - because of how the new system works, world names are unique identifiers, you can find yours at https://nwdb.info/server-status/servers.json
`BOT_SECRET` is the secret your bot has on Discord. When you register an app, you get this from Discord.
`CATEGORY_ID` is the id of the category you put the voice channels into. It maybe be a bit tricky to find it, but you can inspect the code if you load Discord in browser and copy the number out there.
`PLAYERS_CHANNEL` is the voice channel that should display the numbers of players (1234 / 2000 for example).
`QUEUE_CHANNEL` is the voice channel to show the number of people in queue.
`WAIT_CHANNEL` is the voice channel to show how long you might have to wait in queue if there is one.
`LOG_CHANNEL` is a text channel you might want to only have visible to you, so the bot can log messages into it if there is an issue.

Your bot needs to have admin permissions as well as intent privileges.

An example on how to run this (replacing each XYZ with actual values) would be this command:
`docker run --env API_TOKEN=XYZ --env WORLD_NAME=XYZ --env BOT_SECRET=XYZ --env CATEGORY_ID=XYZ --env PLAYERS_CHANNEL=XYZ --env QUEUE_CHANNEL=XYZ --env WAIT_CHANNEL=XYZ --env LOG_CHANNEL=XYZ christianriesen/new-world-server-status-discord-bot`

To make it slightly easier, you can copy the `env_file.dist` to `env_file` and edit the file to add the values there. Then you can launch it with just this:
`docker run --env-file env_file christianriesen/new-world-server-status-discord-bot`

If you made sure that all works well, you can add `-d` to run it in the background.

<h2>Like my work?</h2>

If you like my work, buy me a coffee. https://ko-fi.com/mrrelliks


Need specific help? - https://discord.gg/wtTwa3ZCwF
