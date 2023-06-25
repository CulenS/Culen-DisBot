import discord
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
TOKEN = os.environ['DISCORD_TOKEN']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print(f'Message from {message.author} : {message.content}')
        if self.user != message.author:
            if self.user in message.mentions:
                response = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = message.content,
                    temperature = 1,
                    max_tokens = 256,
                    top_p = 1,
                    frequency_penalty = 0,
                    presence_penalty = 0
                )
                channel = message.channel
                messageToSend = response.choices[0].text
                await channel.send(messageToSend)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)