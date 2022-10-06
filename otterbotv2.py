import discord

intents = discord.Intents.default()
intents.message_content = True

TOKEN = "TOKEN HERE"

client = discord.Client(intents=intents)

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')
        
        
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to CaptainOtterz discord server~! / {member.name}님, 캡틴오터의 디코서버에 오신걸 환영합니다~!'
    )
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('+hello'):
        await message.channel.send(f'Hello {message.author.name}! / 안녕하세요! {message.author.name}님!')
client.run(TOKEN)