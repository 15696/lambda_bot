import discord
import asyncio

token = "TOKEN"

(lambda run, *args: run(discord.Client(), *args))((lambda client, *args: [func(client) for func in args]), (lambda c: [setattr(c, key, value) for key, value in {'on_ready': asyncio.coroutine((lambda: print('Logged in as\n{0}\n{1}\n------'.format(c.user.name, c.user.id)))), 'on_message': asyncio.coroutine((lambda m: ({'ping': (lambda m: c.loop.create_task(m.channel.send('pong')))}[m.content[2:]](m) if m.content.startswith('!!') else c.on_message)))}.items()]), (lambda c: print(c.run(token))))
