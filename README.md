# logbot

logbot is a basic Discord bot written in Python using the discord.py API wrapper.

The only dependency is discord.py which can be installed [from here.][dpy] Python 3.x is required to run the bot.
[dpy]: https://github.com/Rapptz/discord.py

In order to run the bot you need to create a Discord application at the link [here.][app] Give the app a name and then turn it into a bot user.
Get the App Bot User Token and edit logbot.py by putting your token in the last line where it says 'bot token here'. Note: your token must be
surrounded by single quotes (' '). Invite the bot to your server by replacing bot-id in the following URL with your bot's specific client ID,
which is also found on the applications page. Invite URL: https://discordapp.com/oauth2/authorize?client_id=bot-id&scope=bot&permissions=0
[app]: https://discordapp.com/developers/applications/me

After adding the bot to your server you can run it by typing "python logbot.py" in a terminal from the directory that logbot was put in.

To get a log of a channel, just type "!dump filename" in the desired channel. If you fail to specify a filename the returned file will be named
whatever the channel is named. If you specify more than two arguments, the file will also be named whatever the channel name is. You will be sent
the log in a direct message.