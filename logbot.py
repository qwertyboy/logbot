import discord
import asyncio

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
        fname = message.content.split()[1]
        msgs = []

        # get all the messages
        tmp = await client.send_message(message.channel, 'Getting messages...')
        async for log in client.logs_from(message.channel, limit=10000):
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

client.run('bot token here')