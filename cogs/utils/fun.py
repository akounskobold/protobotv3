import discord
from discord.ext import commands

import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.owo_msg = "Rawr x3 nuzzles how are you pounces on you you're so warm o3o notices you have a bulge o: someone's happy ;) nuzzles your necky wecky~ murr~ hehehe rubbies your bulgy wolgy you're so big :oooo rubbies more on your bulgy wolgy it doesn't stop growing ·///· kisses you and lickies your necky daddy likies (; nuzzles wuzzles I hope daddy really likes $: wiggles butt and squirms I want to see your big daddy meat~ wiggles butt I have a little itch o3o wags tail can you please get my itch~ puts paws on your chest nyea~ its a seven inch itch rubs your chest can you help me pwease squirms pwetty pwease sad face I need to be punished runs paws down your chest and bites lip like I need to be punished really good~ paws on your bulge as I lick my lips I'm getting thirsty. I can go for some milk unbuttons your pants as my eyes glow you smell so musky :v licks shaft mmmm~ so musky drools all over your cock your daddy meat I like fondles Mr. Fuzzy Balls hehe puts snout on balls and inhales deeply oh god im so hard~ licks balls punish me daddy~ nyea~ squirms more and wiggles butt I love your musky goodness bites lip please punish me licks lips nyea~ suckles on your tip so good licks pre of your cock salty goodness~ eyes role back and goes balls deep mmmm~ moans and suckles"
        self.nut = "█▀█ █▄█ ▀█▀"
        self.seals = [
            "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.",
            "What in Davy Jones’ locker did ye just bark at me, ye scurvy bilgerat? I’ll have ye know I be the meanest cutthroat on the seven seas, and I’ve led numerous raids on fishing villages, and raped over 300 wenches. I be trained in hit-and-run pillaging and be the deadliest with a pistol of all the captains on the high seas. Ye be nothing to me but another source o’ swag. I’ll have yer guts for garters and keel haul ye like never been done before, hear me true. You think ye can hide behind your newfangled computing device? Think twice on that, scallywag. As we parley I be contacting my secret network o’ pirates across the sea and yer port is being tracked right now so ye better prepare for the typhoon, weevil. The kind o’ monsoon that’ll wipe ye off the map. You’re sharkbait, fool. I can sail anywhere, in any waters, and can kill ye in o’er seven hundred ways, and that be just with me hook and fist. Not only do I be top o’ the line with a cutlass, but I have an entire pirate fleet at my beck and call and I’ll damned sure use it all to wipe yer arse off o’ the world, ye dog. If only ye had had the foresight to know what devilish wrath your jibe was about to incur, ye might have belayed the comment. But ye couldn’t, ye didn’t, and now ye’ll pay the ultimate toll, you buffoon. I’ll shit fury all over ye and ye’ll drown in the depths o’ it. You’re fish food now.",
            "What the fuck did you just fucking type about me, you little bitch? I’ll have you know I graduated top of my class at MIT, and I’ve been involved in numerous secret raids with Anonymous, and I have over 300 confirmed DDoSes. I am trained in online trolling and I’m the top hacker in the entire world. You are nothing to me but just another virus host. I will wipe you the fuck out with precision the likes of which has never been seen before on the Internet, mark my fucking words. You think you can get away with typing that shit to me over the Internet? Think again, fucker. As we chat over IRC I am tracing your IP with my damn bare hands so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your computer. You’re fucking dead, kid. I can be anywhere, anytime, and I can hack into your files in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in hacking, but I have access to the entire arsenal of every piece of malware ever created and I will use it to its full extent to wipe your miserable ass off the face of the world wide web, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking fingers. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit code all over you and you will drown in it. You’re fucking dead, kiddo.",
            "Arf arf arf!"
        ]

    @commands.command()
    async def owo(self, ctx):
        """ What's this? """
        author = ctx.author
        await ctx.send(f"{author.mention},\n{self.owo_msg}")

    @commands.command()
    async def bignut(self, ctx):
        """ █▀█ █▄█ ▀█▀ """
        await ctx.send(self.nut)

    @commands.command()
    async def seal(self, ctx):
        """ Prints random navy seal copypasta! """
        await ctx.send(random.choice(self.seals))


def setup(bot):
    bot.add_cog(Fun(bot))