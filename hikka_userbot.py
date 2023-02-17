from hikka import Hikka
from hikka.modules import Filters

import re

hikka = Hikka()

@hikka.on_message(Filters.regex(r'https://t.me/tonRocketBot\?start=\w+'))
async def activate_tonRocketBot_check(client, message):
    code = re.findall(r'https://t.me/tonRocketBot\?start=(\w+)', message.text)[0]
    await client.send_message('@tonRocketBot', f'/start {code}')
    print(f'Активирован чек с кодом: {code}')
