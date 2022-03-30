from main import bot, dp
from aiogram.types import Message
from config import my_id

async def send_to_admin(dp):
    await bot.send_message(chat_id = my_id, text = 'Sup man !'
                           '\nWanna make music ?')

@dp.message_handler()
async def echo(message:Message):
    text = f"If u wanna make music , {message.text} so you on the address"
    await bot.send_message(chat_id = message.from_user.id , text = text)