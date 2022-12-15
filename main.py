import os
import openai
import discord
from dotenv import load_dotenv

load_dotenv()
DC_BOT_TOKEN = os.getenv('DC_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Set up the OpenAI API client
openai.api_key = OPENAI_API_KEY

# Set up the Discord bot client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user or message.channel.id != 1052584808351539270:
        return
    print(message.content)
    # Use the OpenAI API to generate a response to the message
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Human: {message.content} \n AI:",
        temperature=0.9,
        max_tokens=999,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    # Send the generated response back to the Discord channel
    await message.channel.send(response["choices"][0]["text"])

client.run(DC_BOT_TOKEN)
