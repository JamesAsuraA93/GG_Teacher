import os
import keep_alive
from discord.ext import commands
import subprocess

bot = commands.Bot(command_prefix='>')

@bot.command()
async def run(ctx):
    print("running")
    command = ctx.message.content.split('\n')
    command_cleaned = []
    if command == 'hi':
      await ctx.message.channel.send("อิอิ")
      return

    for line in command:
      if ">run" not in line and "```" not in line:
        command_cleaned.append(line)

    temp = open('temp.py',"w+")
    temp.write('\n'.join(command_cleaned))
    temp.close()

    output = subprocess.run(['python', 'temp.py'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    
    await ctx.send(output)


keep_alive.keep_alive()
secret_token = os.getenv("TOKEN")

if secret_token:
  bot.run(secret_token)
else:
  print("Looks like you're not the owner")
