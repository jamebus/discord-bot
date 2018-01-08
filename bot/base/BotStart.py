# Filename: BotStart.py
# Author: mfwass
# Date: January 8th, 2017
#
# The Legend of Pirates Online Software
# Copyright (c) The Legend of Pirates Online. All rights reserved.
#
# All use of this software is subject to the terms of the revised BSD
# license.  You should have received a copy of this license along
# with this source code in a file named "LICENSE."

from bot.base import BotCore

print(":BotStart: Initializing core...")

core = BotCore.BotCore()

print(":BotStart: Connecting...")
core.bot.run(core.settings.getSetting('appToken'))
