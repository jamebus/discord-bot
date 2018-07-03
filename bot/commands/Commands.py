# Filename: Commands.py
# Author: mfwass
# Date: January 8th, 2017
#
# The Legend of Pirates Online Software
# Copyright (c) The Legend of Pirates Online. All rights reserved.
#
# All use of this software is subject to the terms of the revised BSD
# license.  You should have received a copy of this license along
# with this source code in a file named "LICENSE."

from discord.ext import commands

from bot.language import BotLocalizer
from bot.core import BotGlobals

from datetime import datetime
from random import choice as randomchoice

class Commands:
    """
    The Commands class will house all commands provided by the
    TLOPO Discord Bot.

    This will hopefully make it easier for any developers to add
    further commands to this bot.
    """

    def __init__(self):
        # Right now, this is really disgusting - but it works!
        # TODO: Rewrite.

        @self.bot.command()
        async def oceans(*args):
            """
            Returns server populations.
            """

            output = ""
            oceans = self.taskMgr.getOceanPopulations()
            s = self.taskMgr.getSystemStatus()
            total = 0

            for i, k in sorted(oceans.items()):
                output += "%s: %s\n" % (i, k)
                total += k

            if s.get('status', 0) == 3:
                output = 'The Legend of Pirates Online is currently closed for an update. Ocean data is unavailable.'
            else:
                output += BotLocalizer.OCEANS_TOTAL % total

            # Response.
            await self.bot.say(output)

        @self.bot.command()
        async def fleets(*args):
            """
            Returns active fleets.
            """

            fleets = self.taskMgr.getActiveFleets()
            s = self.taskMgr.getSystemStatus()
            output = ""

            if s.get('status', 0) == 3:
                output = 'The Legend of Pirates Online is currently closed for an update. Fleet data is unavailable.'
            elif fleets:
                for i, k in sorted(fleets.items()):
                    output += BotLocalizer.FLEET_ITEM_INFO % (i,
                                                            k.get('type'),
                                                            k.get('state'),
                                                            k.get('shipsRemaining'))
            else:
                output = "No active fleets."

            # Response.
            await self.bot.say(output)

        @self.bot.command()
        async def invasions(*args):
            """
            Returns active invasions.
            """

            invasions = self.taskMgr.getActiveInvasions()
            s = self.taskMgr.getSystemStatus()
            output = ""

            if s.get('status', 0) == 3:
                output = 'The Legend of Pirates Online is currently closed for an update. Invasion data is unavailable.'
            elif invasions:
                for i, k in sorted(invasions.items()):
                    output += BotLocalizer.INVASION_ITEM_INFO % (i,
                                                              k.get('location'),
                                                              k.get('state'),
                                                              k.get('phase'),
                                                              k.get('numPlayers'))
            else:
                output = "No active invasions."

            # Response.
            await self.bot.say(output)

        @self.bot.command()
        async def status(*args):
            """
            Returns current server status.
            """

            s = self.taskMgr.getSystemStatus()

            if s:
                notices = s.get('notices')
                status = BotGlobals.GLOB_CODE_TO_STATUS.get(int(s.get('status')), 'Unknown')
                outages = s.get('outages')

                if notices:
                    tmp = ""
                    for i in notices.keys():
                        notice = notices[i]
                        msg = notice.get('text')
                        flag = BotGlobals.SRV_CODE_TO_STATUS.get(int(notice.get('flag')))

                        tmp += "\n**%s** | %s\n**Message:** *%s*\n" % (
                                                    flag, i, msg)
                elif s.get('status', 0) == 3:
                    tmp = "\nThe Legend of Pirates Online is currently closed for an update. Check https://status.tlopo.com for more information!\n"
                else:
                    tmp = "\nNo known notices."

                output = BotLocalizer.SYSTEM_STATUS_INFO % (status, tmp, outages)
            else:
                output = "System status is unknown."

            await self.bot.say(output)

        @self.bot.command()
        async def ping(*args):
            """
            Returns a simple message to check if the bot is operating properly.
            """

            output = 'Pong!'

            # Response
            await self.bot.say(output)

        @self.bot.command(pass_context=True)
        async def beer(ctx):
            """
            Returns a beer to a thirsty pirate.
            """

            output = BotLocalizer.BEER % ctx.message.author.id

            # Response
            await self.bot.say(output)

        @self.bot.command(pass_context=True)
        async def rum(ctx):
            """
            But why is the rum gone?!
            """

            phrase = randomchoice(BotLocalizer.RUM)
            try:
                output = phrase % ctx.message.author.id
            except TypeError:
                output = phrase

            # Response
            await self.bot.say(output)

        @self.bot.command(pass_context=True)
        async def wine(ctx):
            """
            Have some wine to unwind after a hard day of plunderin'.
            """

            output = BotLocalizer.WINE % ctx.message.author.id

            # Response
            await self.bot.say(output)

        @self.bot.command(pass_context=True)
        async def stranded(ctx):
            """
            You seem to have become stranded on an island again.
            """

            output = BotLocalizer.STRANDED % ctx.message.author.id

            # Response
            await self.bot.say(output)
