# discordchatbot
import discord

# This step is important to establish our Discord client.
# The bot client that is connecting to discord.
client = discord.Client()

TOKEN = "NTA1MTYyODI0MjEzODU2MjU2.DrRxzA.AejgQIuwCIx6WGIZBFv0H-fGHrA"
# We can detect if a message has been sent with this function
# that takes in the parameter “message”.
@client.event
async def on_message(message):
    content = message.content
    user = message.author
    channel = message.channel

    # However, we never want the bot to be able to respond to itself,
    # so if the user of the message is equal to the client, we stop the function.
    if user == client.user:
        return

    # This prints how what message was received in the terminal
    # This step can be useful to track the conversation that goes on in Discord.
    # It also helped to identify where exactly the code crashed.
    print("Received a message:", content)

    if content.strip() == "hello" or content.strip() == "hi":
        await client.send_message(channel, "Hi!")

    if content.strip() == "bye":
        await client.send_message(channel, "See you later!")
        client.close()

    if content.startswith('!encrypt'):
        await client.send_message(channel, "I am here to help with encryption!")

# Whenever the bot is ready for use after this program had been run,
# it will print out “The bot is READY!”.
# It will also print out which specific bot is being used.
@client.event
async def on_ready():
    print("The bot is READY!")
    print("Logged in as: {}".format(client.user.name))

# This step is the most important part because it runs our bot.
# Without this, the bot would not run.
client.run(TOKEN)
