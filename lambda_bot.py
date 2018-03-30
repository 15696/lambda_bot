import discord
import asyncio

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

token = "TOKEN"

(lambda run, *args: run(discord.Client(), *args))((lambda client, *args: [func(client) for func in args]),(lambda client: setattr(client, '__await', client.loop.create_task)),(lambda client: setattr(client, '__commands', {'ping': (lambda message: client.__await(message.channel.send('pong'))), 'whoami': (lambda message: client.__await(message.channel.send('You are %s' %(message.author)))), 'help': (lambda message: client.__await(message.channel.send('```\n{0}```'.format('\n'.join(name for name in client.__commands)))))})), (lambda c: [setattr(c, key, value) for key, value in {'on_ready': asyncio.coroutine((lambda: print('Logged in as\n%s\n%s\n------' %(c.user.name, c.user.id)))), 'on_connect': asyncio.coroutine(lambda: print('Connected!')), 'on_error': asyncio.coroutine(lambda ctx, error: c.__await(ctx.channel.send(error))), 'on_message': asyncio.coroutine((lambda m: ((c.__commands[m.content[2:]](m), c.on_message)[1] if m.content.startswith('!!') else c.on_message)))}.items()]), (lambda c: [print('Running...'), c.run(token)]))
