import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='!')

player1=""
player2=""
turn=""
gameOver=True
board=[]

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]




@client.command()
async def tictactoe(ctx,p1:discord.Member,p2:discord.Member):
    global player1
    global player2
    global turn
    global gameOver
    global count

    if gameOver:
        global board
        board=[":white_large_square:",":white_large_square:",":white_large_square:",
               ":white_large_square:",":white_large_square:",":white_large_square:",
               ":white_large_square:",":white_large_square:",":white_large_square:"]
        turn=""
        gameOver=False
        count=0

        player1=p1
        player2=p2

        line=""
        for x in range(len(board)):
            if x==2 or x==5 or x==8:
                line+=" "+board[x]
                await ctx.send(line)
                line=""
            else:
                line+=" "+board[x]

        num=random.randint(1,2)
        if num==1:
            turn=player1
            await ctx.send(" <@"+ str(player1.id)+">)"+"دورك يا هطف ")
        else:
            turn=player2
            await ctx.send(" <@"+ str(player2.id)+">)"+"دورك يا هطف ")
    else:
        await ctx.send("انتظر دورك يا ورع ")


@client.command()
async def place(ctx,pos:int ):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark=""
        if turn==ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0<pos<10 and board[pos-1]==":white_large_square:":
                board[pos-1]=mark
                count+=1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                cheackWinner(winningConditions,mark)
                if gameOver:
                    await ctx.send(mark+"فاز")
                elif count>=9:
                    await ctx.send("تعادل ")

                if turn ==player1:
                    turn=player2
                elif turn == player2:
                    turn=player1





            else:
                await ctx.send("اختار رقم من 1 الى 9 , اختار مكان فاضي ")

            pass
        else:
            await ctx.send("موب دروك ")
    else:
        await ctx.send("مافي احد يلعب  ")


@tictactoe.error
async def tictactoe_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await  ctx.send(" منشن واحد عشان تلعب معه")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@930510564688556063>).")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("دخل رقم ياذكي  ")
    elif isinstance(error, commands.BadArgument):
        await ctx.send(" دخل رقم ")

def cheackWinner(winningConditions,mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]]==mark and board[condition[1]]==mark and board[condition[2]]==mark:
            gameOver=True












@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def oda(ctx):
    await  ctx.send("""ودا ماذا فعلت ماذا فعلت يا اودا شسالفة شسالفة يا اودا يا مجنون حرام عليك بوف ضربة جديدة صدمة جديدة يخرب بيتك يا اودا كلا يا اودا ماذا تفعل بنا كلا دمار شامل تفجير خربها اودا شلي بتوصله حرام عليك في ناس هنا عقولهم لا تتحمل هل الي انت قاعد تسويه هشتكنا وبشتكنا يا ريس دنتا ريس والنعمة كويس يمدلعنا يمشخلعنا قول لعدوك روح تليس هشتكنا وبشتكنا ياريس اوودااا اودا ما الذي جالس تفعله فينا انت ياخي والله العظيم اودا كل ماقلنا خلاص برافو برافو برافو اودا شلي بقى ماقلته اودا انت رسميًا بالرسمي بالحرف الواحد مجنون يا الله عليك يا اودا ياحرام عليك يا اودا
    """)

@client.command(aliases=['8ball'])
async  def _8ball(ctx,*,question):
    responses = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.",
                 "Very doubtful.", "Without a doubt.",
                 "Yes.", "Yes – definitely.", "You may rely on it."]
    await ctx.send(f' {random.choice(responses)}')










@client.event
async def on_message(message):
    if message.content=='سلام':
        await message.channel.send('وعليكم السلام')
    elif message.content=='برب' :
        await message.channel.send('تيت')
    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')
    await client.process_commands(message) #OverRiding

@client.event
async  def on_typing(channel, user, when):#when the username you put in fun the bot send a message.
    if user.name=='username':
        await channel.send("put your message here"
                           "")
    if user.name=='Username':
        await  channel.send('put your message here')





client.run('###################################')


