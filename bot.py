import nextcord
from nextcord.ext import commands

client = commands.Bot()

token = open('token.txt').read()
print(len(token))

@client.event
async def on_ready():
    print("Bot is now online, proceed to run the command '/badge'")

@client.slash_command(description="Use this command to receive the 'Active Developer' badge!")
async def badge(interaction: nextcord.Interaction):
    await interaction.send("You have used the command successfully! You will be able to claim your badge within 1 week; the link to claim has been pasted into the command prompt as well as under this text!\nhttps://discord.com/developers/active-developer")
    print("https://discord.com/developers/active-developer\nYou can now close the command prompt!")

client.run(token)