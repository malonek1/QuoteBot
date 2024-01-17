import discord
from discord.ext import commands
from resources import EnvironmentVariables as ev


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # gamecube controller issues
    @commands.command(help="details for setting up a gamecube controller with project rio")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def gcc(self, ctx):
        embed = discord.Embed()
        embed.add_field(name="Setting up a GameCube Controller", value="""
    To use a GameCube Controller with Rio, follow these steps:
    - Install the proper drivers <https://wiki.dolphin-emu.org/index.php?title=How_to_use_the_Official_GameCube_Controller_Adapter_for_Wii_U_in_Dolphin#Avoid_vJoy>
    - Change the controller port to "GameCube Adapter for WiiU" in the Controller settings
    - If your adapter has a switch, set it to WiiU mode instead of PC mode
    - Use port 1; only player 1 can control the menus in Mario Baseball
    - Make sure no other Dolphin/Rio tabs are open at the same time. The controller can only connect to one window at a time
        """)
        await ctx.send(embed=embed)

    # displays server rules
    @commands.command(help="type !rule followed by numbers 1-13 to see server rules")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def rule(self, ctx, rule: int):
        embed = discord.Embed()
        if rule == 1:
            embed.add_field(name="Hate Speech",
                            value="• Includes but is not limited to: racism, homophobia, transphobia, ableism, threats\n"
                                  "• This includes profile pictures, usernames and custom statuses")
        elif rule == 2:
            embed.add_field(name="Posting NSFW Content",
                            value="• This includes pictures, long text copy pastas, spam pinging, posting discord links, having sexual and or graphic conversations in voice or text channels, or other disruptive content.\n"
                                  "• NSFW topics include but are not limited to: pornographic, excessively disturbing, sexually suggestive, or topics concerning past sexual experiences, sexual desires, gore, disturbing conversations about abuse, images of scantily clad people, images that make any allusion to sexual fetishes (vore, etc.), images of sex toys, or using trigger words.\n"
                                  "• Extremely edgy content is content that is ‘excessively dark, often overbearingly depressive in nature could be considered humorous, or posts related to recent tragedies.\n"
                                  "• This includes profile pictures, usernames and custom statuses.")
        elif rule == 3:
            embed.add_field(name="Posting harmful or malicious links",
                            value="• This includes posting links to malicious websites.\n"
                                  "• Any post that crashes or attempts to crash Discord or a user's computer.\n"
                                  "• Any post that pretends to or does send malware to a user will be met with a ban, no questions asked.")
        elif rule == 4:
            embed.add_field(name="Doxxing",
                            value="• Do not post personal details or identifying information of any users without that user's express permission.\n"
                                  "• Do not post pictures of other people without their consent")

        elif rule == 5:
            embed.add_field(name="Money Matching",
                            value="• Money-matching (playing in a match in exchange for money) or other forms of gambling are not permitted. \n"
                                  "• Do not approach other users of this server in DMs for the purpose of playing for money.")

        elif rule == 6:
            embed.add_field(name="Spamming",
                            value="• Keep discussions on topic to their respective channels\n"
                                  "• Messages in <#628353660698624024> must follow all other rules in the server\n"
                                  "• Self-promotion outside of the self-promotion channel is not permitted\n"
                                  "• Please only use Pings for their intended purpose. This includes @Netplayers and @New Netplayers for finding games in <#948321928760918087>")
        elif rule == 7:
            embed.add_field(name="Instigating Fights",
                            value="• Intentional and continuous drama baiting/instigating is not allowed. Drama baiting/instigating is defined as constantly flaming/being toxic to users after being informally/formally warned.\n"
                                  "• Members of the server must also be fair and understanding to those with different opinions.\n"
                                  "• Mods or Admins may ask the discussion to end if it gets too heated.")
        elif rule == 8:
            embed.add_field(name='No "Crossing The Line"',
                            value="• Please don't be too vitriolic, edgy, derogatory, or abrasive with your posts. Don’t be rude.\n"
                                  "• Bullying and berating someone will not be tolerated. \n"
                                  "• If you're unsure your communication is appropriate, then ask a moderator first.")
        elif rule == 9:
            embed.add_field(name="Having Non-English Conversations",
                            value="• Please keep all text conversations in English. Most of the admins and mods in the server are native English speakers, so keeping conversations to English is most appreciated.\n"
                                  "• Non-English media is allowed, however it may be removed at the mods discretion if they think it might be breaking a rule in another language.")
        elif rule == 10:
            embed.add_field(name="Posting Excessively Loud Videos",
                            value="• Excessively loud videos are not allowed in media channels.")
        elif rule == 11:
            embed.add_field(name="Asking for an ISO / ROM",
                            value="• Asking for an ISO / ROM of any game is prohibited.\n"
                                  "• Users must obtain these files on their own accord")
        elif rule == 12:
            embed.add_field(name="Netplay Specific Rules",
                            value="• Users can only submit games to the ranked leaderboards from one account. No smurfing.\n"
                                  "• Dropping out of active tournaments will result in action from the moderation team depending on circumstances. Multiple offenses are more likely to result in bans from future tournaments.")
        elif rule == 13:
            embed.add_field(name="No politics",
                            value="• Please refrain from bringing up controversial political opinions. This is a place to chat about Mario Baseball and other games.")
        await ctx.send(embed=embed)

    # stadium boundary chart
    @commands.command(help="returns image of stadium boundaries")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def stadium(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='STADIUM BOUNDARY CHART',
                        value='The following image displays the boundaries of all stadiums:\n')
        embed.set_image(
            url="https://media.discordapp.net/attachments/628354009865912350/943980502510104636/unknown.png")
        await ctx.send(embed=embed)

    # about rio stat files
    @commands.command(help="describes how to access project rio stat files")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def stats(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='RIO STATS:',
                        value='By default, Project Rio records stats throughout a game and generates a stat json file to your computer.\n\n'
                              'You can view these stat files by opening the "StatFiles" folder in your Project Rio user directory (on Windows, this is likely in your Documents folder).')
        await ctx.send(embed=embed)

    # datamined stats
    @commands.command(help="returns spreadsheet of datamined stats")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def datamine(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='DATAMINED STATS:',
                        value='We have uncovered many hidden stats in the game through datamining. See our full datamined stat spreadsheet here:\n'
                              'https://docs.google.com/spreadsheets/d/16cEcCq-Gkudx5ESfqzS0MJlQI7WTvSIWsHVZS8jv750/edit?usp=sharing')
        await ctx.send(embed=embed)

    # reset a crashed game
    @commands.command(help="describes what to do to reset a game that wasn't completed")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def reset(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='RESET GAME:',
                        value='In the event that a ranked/tournament game crashes or disconnects, players will recreate the game and continue playing from the point of the crash\n\n'
                              'Here\'s a guide on how to proceed:')
        embed.set_image(url="https://cdn.discordapp.com/attachments/634046643330613248/947262814261755994/Rio_Crash_Reset_Guide_3.png")
        await ctx.send(embed=embed)

    # ranked drafting details
    @commands.command(help="Returns the current ranked draft rules")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def draft(self, ctx, *draft_type):
        if 'off' in draft_type:
            embed = discord.Embed(title='Stars-Off Draft Rules:')
            embed.set_image(url="https://cdn.discordapp.com/attachments/823805174811197470/1066092568712073286/DraftRules.png")
            await ctx.send(embed=embed)
        elif 'on' in draft_type:
            embed = discord.Embed(title='Stars-On Draft Rules:')
            embed.set_image(url="https://cdn.discordapp.com/attachments/939254901047951410/1065779869780299786/Season4StarsOnDraft.png")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0xEA7D07)
            embed.add_field(name='Please use the following options to see draft rules:',
                            value='`!draft off` - For draft ruleset in ranked stars-off\n'
                                  '`!draft on` - For draft ruleset in ranked stars-on')
            await ctx.send(embed=embed)

    # ranked mode
    @commands.command(help="includes all info needed before playing ranked mssb")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ranked(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='RANKED:',
                        value=f'We run a ranked online ladder through this server. You can find the ranked leaderboards by typing !ladder <mode> <#{ev.get_var("bot_spam_channel_id")}>\n\n'
                              'Our full ruleset can be seen in <#841761307245281320>. To play a ranked game, use the buttons in the channel to queue for a game.\n'
                              'To ensure the game counts for ranked, make sure the host selects the appropriate Game Mode when hosting the Rio lobby.')
        await ctx.send(embed=embed)

    # explain auto golf mode
    @commands.command(help="description for auto golf mode")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def golf(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='AUTO GOLF MODE:',
                        value='Auto Golf Mode is the specific type of netcode that Project Rio uses for playing games online. It works giving one player 0 latency (the golfer) while the other player '
                              '(the non-golfer) has an extra latency penalty.\n\nAuto Golf Mode automatically sets the batter to the golfer while in the pitching/batting state of the game, and then swaps the fielder to the golfer while in the fielding/baserunning state.')
        await ctx.send(embed=embed)

    # message for helping new people figure out Rio
    @commands.command(help="guide for getting project rio client setup")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def rioGuide(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='RIO GUIDE:',
                        value='For a tutorial on setting up Project Rio, check out <#823805174811197470> or head to our website <https://www.projectrio.online/tutorial>\nIf you need further help, please use <#823805409143685130> to get assistance.')
        await ctx.send(embed=embed)

    # ball flickering
    @commands.command(help="how to fix 'ball flicker' glitch in project rio client")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def flicker(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='HOW TO FIX FLICKER ISSUE:',
                        value='If you notice the ball flickering, you can solve the issue by changing your graphics backend.\n\n'
                              'Open Rio, click graphics, then change the backend. The default is OpenGL. Vulkan or Direct3D11/12 should work, but which one specifically is different for each computer, so you will need to test that on your own')
        await ctx.send(embed=embed)

    # optimization guide
    @commands.command(help="guide for optimizing project rio client")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def optimize(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='OPTIMIZING PROJECT RIO:',
                        value='Many settings on Project Rio are already optimized ahead of time; however, there is no one-size-fits-all option for different computers. Here is a guide on optimization to help help you started\n> <https://www.projectrio.online/optimize>')
        await ctx.send(embed=embed)

    # tell what Rio is
    @commands.command(help="project rio description and download")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def rio(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='PROJECT RIO:',
                        value='Project Rio is a custom build of Dolphin Emulator which is built specifically for Mario Superstar Baseball. It contains optimized online play, automatic stat tracking, built-in gecko codes, and soon will alos host a database and webapp on the website.\n\nYou can download it here: <:ProjectRio:866436395349180416>\n> <https://www.projectrio.online/>')
        await ctx.send(embed=embed)

    # gecko code info
    @commands.command(help="description of gecko codes")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def gecko(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='GECKO CODES:',
                        value='Gecko Codes allow modders to inject their own assembly code into the game in order to create all of the mods we use.\n\n'
                              'You can change which gecko codes are active by opening Project Rio and clicking the "Gecko Code" tab on the top of the window. Simply checko off which mods you want to use. You can obtain all of out gecko codes by clicking "Download Codes" at the bottom right corner of the Gecko Codes window.\n\n'
                              '**NOTES**:\n-Do **NOT** disable any code which is labeled as "Required" otherwise many Project Rio functionalites will not work\n-If you run into bugs when using gecko codes, you may have too many turned on. Try turning off the Netplay Event Code\n-The Netplay Event Code is used for making online competitive games easy to set up. It is only required for ranked online games')
        await ctx.send(embed=embed)

    # inform users about roles
    @commands.command(help="info on user roles")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def roles(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='ROLES:', value='Set roles for yourself in <#945478927214866522>!')
        await ctx.send(embed=embed)

    # mario superstar baseball wiki
    @commands.command(help="returns link for mssb wikipedia page")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def wiki(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='MARIO SUPERSTAR BASEBALL WIKI:',
                        value='The link below takes you to the official mario superstar baseball wikipedia page that our dedicated community is actively making additions to!\n\n'
                              'https://mario-superstar-baseball.fandom.com/wiki/Mario_Superstar_Baseball_Wiki')
        await ctx.send(embed=embed)

    # feedback link
    @commands.command(help="returns link to suggestion form for RioBot features")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def feedback(self, ctx):
        embed = discord.Embed()
        embed.add_field(name='Send your RioBot ideas here:',
                        value='https://docs.google.com/forms/d/e/1FAIpQLSfXWbWMkMnaP7xcinJob9YD4L-D_f3bKyHL9mC5ktqI-XKAhw/viewform?usp=sf_link')
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Misc(client))
