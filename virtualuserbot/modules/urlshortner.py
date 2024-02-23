import pyshorteners

from virtualuserbot import CMD_HELP
from virtualuserbot.utils import friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern="urlshort (.*)"))
@friday.on(sudo_cmd(pattern="urlshort (.*)", allow_sudo=True))
async def vom(event):
    try:
        link = event.pattern_match.group(1)
        sed = pyshorteners.Shortener()
        kek = sed.tinyurl.short(link)
        bestisbest = (
            f"<b>Url Shortened</b> \n<b><u>Given Link</u></b> ➠ {link}\n"
            f"<b><u>Shortened Link</u></b> ➠ {kek}"
        )
        await event.edit(bestisbest, parse_mode="HTML")
    except Exception as e:
        await event.edit("SomeThing Went Wrong. \nError : " + e)


CMD_HELP.update(
    {
        "urlshortner": "**URL shortner**\
\n\n**Syntax : **`.urlshort <url link>`\
\n**Usage :** Shortens the given URL."
    }
)
