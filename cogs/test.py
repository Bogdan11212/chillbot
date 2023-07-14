import disnake
from disnake.ext import commands
import config
import random

class Test(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    # @commands.slash_command(description="Тест")
    # async def test(self , ctx , member: disnake.Member):
    #     urls = ["https://mobimg.b-cdn.net/v3/fetch/50/50e8c5faf95d0c8ce5d1d48efcdbfbf8.jpeg" , "https://cdn.discordapp.com/attachments/850808002545319957/859359637106065408/bg.png" , "https://phonoteka.org/uploads/posts/2021-07/1625782843_14-phonoteka-org-p-gori-fentezi-art-krasivo-15.jpg" , "https://phonoteka.org/uploads/posts/2021-07/1625782899_11-phonoteka-org-p-gori-fentezi-art-krasivo-11.jpg" , "http://mobimg.b-cdn.net/v3/fetch/4d/4dd373b84cfcd5be4e334ef5f69730e0.jpeg"]
    #     image = random.choice(urls)
    #     url = f"https://api.popcat.xyz/welcomecard?background={image}&text1={member.name}&text2=Hello&text3=Members+{member.guild.member_count}&avatar={member.display_avatar.url}"
    #     embed = disnake.Embed(
    #     color=0xffffff
    #     )
    #     embed.set_image(url=url)

    #     await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Test(bot))