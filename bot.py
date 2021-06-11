from discord.ext import commands
import uuid
import pyimgur
import os

client = commands.Bot(command_prefix='.')


def test(imageName):
    CLIENT_ID = "Client-ID"
    PATH = imageName

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    print(uploaded_image.title)
    print(uploaded_image.link)
    print(uploaded_image.size)
    print(uploaded_image.type)
    return uploaded_image.link

@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def save(ctx):
    imageName = str(uuid.uuid4()) + '.jpg'
    await ctx.message.attachments[0].save(imageName)
    print (imageName)
    msg=test(imageName)
    os.remove(imageName)



    channel = client.get_channel("Channel ID")
    await channel.send(msg)

client.run('Discord Token')

