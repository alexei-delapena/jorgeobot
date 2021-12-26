import discord
from discord.ext import commands
import youtube_dl
import validators
import urllib.request
import re

class music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def come(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Not in voice channel :(")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, *searchString):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client
        query = ' '.join(searchString)

        if validators.url(query) is True:
            url = query
        else:
            url = getYoutubeURL(query)

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Resume")

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.stop()
        await ctx.send("Stopped")

def getYoutubeURL(query):
    print(query)

    searchLink = "http://www.youtube.com/results?search_query=" + '+'.join(query.split())
    print(searchLink)
    html = urllib.request.urlopen(searchLink)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    link = "https://www.youtube.com/watch?v=" + video_ids[0]
    print(link)

    return link

def setup(client):
    client.add_cog(music(client))