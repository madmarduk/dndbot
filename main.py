import disnake
from disnake.ext import commands
import config
import random

intents = disnake.Intents.all()
client = commands.Bot(command_prefix = '.', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
async def ф(ctx, *, user_message):
    if ctx.message.author.id == 356461576930459648: #id ведущего (Game Master) в Discord
        await ctx.send(user_message)
        await ctx.message.delete()


@client.command()
async def r(ctx, roll: str):
    """Бросает кость формата ndk, где n - количество костей, k - количество граней каждой кости
    """

    resultTotal = 0
    resultString = ''
    try:
        try:
            numDice = roll.split('d')[0]
            diceVal = roll.split('d')[1]
        except Exception as e:
            print(e)
            await ctx.send("Команда должна быть формата ndk s" % ctx.message.author.name)
            return


        rolls, limit = map(int, roll.split('d'))

        for r in range(rolls):
            number = random.randint(1, limit)
            resultTotal = resultTotal + number

            if resultString == '':
                resultString += str(number)
            else:
                resultString += ', ' + str(number)

        if numDice == '1':
            await ctx.send(ctx.message.author.mention + "  :game_die:\n**Результат броска:** " + resultString)
        else:
            await ctx.send(
                ctx.message.author.mention + "  :game_die:\n**Результат броска:** " + resultString + "\n**Сумма:** " + str(
                    resultTotal))

    except Exception as e:
        print(e)
        return


client.run(config.DISCORD_TOKEN)
