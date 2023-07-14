import disnake
from disnake.ext import commands
from disnake.interactions import MessageInteraction
from disnake import TextInputStyle
from db import DataBase
import config

class MenuNav(disnake.ui.Modal):
    def __init__(self):
        self.DataBase = DataBase("db.db")
        components = [
            disnake.ui.TextInput(
                label="Id",
                custom_id="Id",
                style=TextInputStyle.short
            )
        ]

        super().__init__(
            title="Id навигационного сообщения",
            components=components,
            custom_id="Id"
        )


    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(color=disnake.Color.green() , title="Успех" , description="Настройки были успешно обновлены!")
        for key, value in inter.text_values.items():
            id_navigation = value[:1024]
            self.DataBase.settings(id_navigation , "Nav")

        await inter.send(embed=embed)


class MenuPiar(disnake.ui.Modal):
    def __init__(self):
        self.DataBase = DataBase("db.db")
        components = [
            disnake.ui.TextInput(
                label="Id",
                custom_id="Id",
                style=TextInputStyle.short
            )
        ]

        super().__init__(
            title="Id сообщения пиара",
            components=components,
            custom_id="Id"
        )


    async def callback(self, inter: disnake.ModalInteraction):
        embed = disnake.Embed(color=disnake.Color.green() , title="Успех" , description="Настройки были успешно обновлены!")
        for key, value in inter.text_values.items():
            id_piar = value[:1024]
            self.DataBase.settings(id_piar , "Piar")

        await inter.send(embed=embed)


class Select(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Id навигационного сообщения" , emoji="🌐"),
            disnake.SelectOption(label="Id сообщения пиара" , emoji="🆔")
        ]

        super().__init__(
            placeholder="Настройки",
            min_values=1,
            max_values=1,
            custom_id="Настройки",
            options=options
        )

    async def callback(self, inter: MessageInteraction):
        if self.values[0] == "Id навигационного сообщения":
            await inter.response.send_modal(MenuNav())

        elif self.values[0] == "Id сообщения пиара":
            await inter.response.send_modal(MenuPiar())

class Settings(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.slash_command(description="Настройки бота")
    @commands.has_permissions(administrator=True)
    async def settings(self , ctx):
        embed = disnake.Embed(
            color=disnake.Color.green(),
            title="Настройки сервера",
            description="Взаимодействуйте с выпадающим меню, чтобы настроить сервер"
        )

        view = disnake.ui.View()
        view.add_item(Select())
        await ctx.send(embed=embed , view=view)


def setup(bot):
    bot.add_cog(Settings(bot))