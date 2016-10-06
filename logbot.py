import os
import discord
import asyncio

MAXMESSAGES = 10000

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!dump'):
        # get file name
        args = message.content.split()
        if len(args) != 2:
            print('Invalid argument list, using default file name.')
            fname = str(message.channel) + '.txt'
        else:
            fname = args[1]

        msgs = []

        # get all the messages
        tmp = await client.send_message(message.channel, 'Getting messages...')
        async for log in client.logs_from(message.channel, limit=MAXMESSAGES):
            msgs.append(log)

        #open file for writing in binary mode
        log = open('log', 'wb')

        # dump everything into the file
        msgs.reverse()
        for msg in msgs:
            name = str(msg.author.display_name) + ' '
            date = str(msg.timestamp.month) + '-' + str(msg.timestamp.day) + \
                    '-' + str(msg.timestamp.year) + ' '
            time = str(msg.timestamp.hour) + ':' + str(msg.timestamp.minute) + \
                    ':' + str(msg.timestamp.second)

            msgstr = name + date + time + '\n\t' + str(msg.clean_content) + '\n\n'
            log.write(msgstr.encode('utf8'))
        # done, so close the file
        log.close()

        await client.edit_message(tmp, fname + ' written. Check your Direct Messages.')

        # send the log to the user who requested it
        await client.send_message(message.author, 'Here is the requested log:')
        await client.send_file(message.author, 'log', filename=fname)
        os.remove('log')

client.run('bot token here')
# https://discordapp.com/oauth2/authorize?client_id=bot-id&scope=bot&permissions=0
