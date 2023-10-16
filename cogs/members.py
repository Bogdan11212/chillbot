import disnake
from disnake.ext import commands
import config
import random


class Members(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = self.bot.get_channel(1150139899224268919)
    role = member.guild.get_role(1143176311402135570)
    await member.add_roles(role)

    urls = ["https://mobimg.b-cdn.net/v3/fetch/50/50e8c5faf95d0c8ce5d1d48efcdbfbf8.jpeg" , "https://cdn.discordapp.com/attachments/850808002545319957/859359637106065408/bg.png" , "https://phonoteka.org/uploads/posts/2021-07/1625782843_14-phonoteka-org-p-gori-fentezi-art-krasivo-15.jpg" , "https://phonoteka.org/uploads/posts/2021-07/1625782899_11-phonoteka-org-p-gori-fentezi-art-krasivo-11.jpg" , "http://mobimg.b-cdn.net/v3/fetch/4d/4dd373b84cfcd5be4e334ef5f69730e0.jpeg" , "https://avatars.mds.yandex.net/i?id=7af776607f4b477293df245d22dce064399fce38-9068727-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=c1a40b78bba7b87310c04cf7ed3aa5762c3a3e43-9144630-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=70835350011ef17beef5b47b6d6b44b8d147e67c-5233722-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=bf7e899f598945b6d7fc10d691f55142ab654320-8497639-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=f72541859e41b607ad3782b29d85660aae6277f2-8206955-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=8ee08e15c8a998016bcd87a2ae771f57d9c3c474-8244056-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=9dbba79778078912b01ac1d8c504c887d4ef73a7-7469517-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=bed7fcde713fc0f5f43eec602c12169a6072e3a7-9181195-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=9129f47e0aea06e29485679195f160a4a2f6e0b8-8181844-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=ddcf654fc72e0f6ce90cbd6afadebf1408d0ce94-6339443-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=5488138537359838443dc79ae31c01cf38997566-3964310-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=530ed99d6035b14e818d197a194c9e8dca897104-8311862-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=711b2b84a52bd3ea0a61b94bc680d5cacc281def-8506348-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=ce9832fcab4f469a59e2f3d3e6a92322f0c0adb0-8185493-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=954e776149dc0857a436eb48f0b87d032239481c-8187038-images-thumbs&n=13" , "https://avatars.mds.yandex.net/i?id=6fd2190243c15a801e1dda55facf1d3df169d084-4571706-images-thumbs&n=13","https://cdn.discordapp.com/attachments/1118958367524802692/1118981521454419968/9bac356f66103269fc568bdef4ceb17b.jpg"]
    image = random.choice(urls)
    url = f"https://api.popcat.xyz/welcomecard?background={image}&text1={member.name}&text2=Hello&text3=Members+{member.guild.member_count}&avatar={member.display_avatar.url}"
    embed = disnake.Embed(
        color=0xffffff,
        description=f"Добро пожаловать {member.mention} на сервер😊 а я тут бот-помощник😋♥️"
    )
    embed.set_image(url=url)

    await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    channel = self.bot.get_channel(1150139899224268919)

    urls = ["https://mobimg.b-cdn.net/v3/fetch/50/50e8c5faf95d0c8ce5d1d48efcdbfbf8.jpeg" , "https://cdn.discordapp.com/attachments/850808002545319957/859359637106065408/bg.png" , "https://phonoteka.org/uploads/posts/2021-07/1625782843_14-phonoteka-org-p-gori-fentezi-art-krasivo-15.jpg" , "https://phonoteka.org/uploads/posts/2021-07/1625782899_11-phonoteka-org-p-gori-fentezi-art-krasivo-11.jpg" , "http://mobimg.b-cdn.net/v3/fetch/4d/4dd373b84cfcd5be4e334ef5f69730e0.jpeg"]
    image = random.choice(urls)
    url = f"https://api.popcat.xyz/welcomecard?background={image}&text1={member.name}&text2=Goodbye&text3=Members+{member.guild.member_count}&avatar={member.display_avatar.url}"
    embed = disnake.Embed(
        color=0xffffff,
        description=f"Прощай {member.mention}"
    )
    embed.set_image(url=url)

    await channel.send(embed=embed)


def setup(bot):
  bot.add_cog(Members(bot))
