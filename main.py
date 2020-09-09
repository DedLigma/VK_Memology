import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload

from vkbottle.api import Api
Api.get_current()

vk_session = vk_api.VkApi(token = 'd097aaef1942f358b1fa6d943d8938ae824668546ce9dd06c1aa091bd537f7ae7c1f91d9a578aef042bab')
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

from vkbottle import Bot, Message, keyboard_gen, VKError

bot = Bot('d097aaef1942f358b1fa6d943d8938ae824668546ce9dd06c1aa091bd537f7ae7c1f91d9a578aef042bab')

@bot.on.message(text="Привет <name>", lower=True)
async def wrapper(ans: Message, name):
    await ans("Hello, {}".format(name))

from vkbottle.keyboard import Keyboard, Text

keyboard = Keyboard(one_time=False)
keyboard.add_row()
keyboard.add_button(Text(label="Привет иисус"), color="primary")
keyboard.add_button(Text(label="видео"), color="primary")
keyboard.add_button(Text(label="Привет иисус2"), color="primary")



@bot.on.message(text='где кнопки', lower=True)
async def wrapper(ans: Message):
    await ans('Так вот же они', keyboard=keyboard.generate())

bot.run_polling(skip_updates=True)
