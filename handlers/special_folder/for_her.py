from data.config import IS_ADMIN, IS_HER, ADMINS
from aiogram.dispatcher import FSMContext
from states.states import StatesGroup
from aiogram import types
from loader import dp, bot
from codecs import open


@dp.message_handler(commands=['for_u'])
async def respond_on_special_command(message: types.Message):
    await bot.send_message(text="Отправь боту любое сообщение ;)", chat_id=message.chat.id)
    await StatesGroup.stateInSpecialCommand.set()


@dp.message_handler(state=StatesGroup.stateInSpecialCommand)
async def result_of_special_command(msg: types.Message, state: FSMContext):
    if await IS_HER(msg.chat.id) or await IS_ADMIN(msg.chat.id):
        await bot.send_message(chat_id=int(ADMINS[0]), text=f"she sent: {msg.text}")
        with open("handlers/special_folder/for_her.txt", "r", 'utf-8') as file:
            line = file.read()
        await msg.answer(line)
        file.close()
        await bot.send_sticker(chat_id=msg.chat.id, sticker="CAACAgIAAxkBAAEY5qhjRa7uM0eh6b12vEasG2L95nUkIQACUAgAAkzMgErYSf6qHgzYgyoE")
        await state.finish()
    else:
        await msg.answer(text="Упс =)\nПохоже эта функция не для вас)")
        await state.finish()


@dp.message_handler(commands=['write_save'])
async def some_spoecial_funk(message: types.Message):
    await bot.send_message(text="Отправь боту любое сообщение ;)", chat_id=message.chat.id)
    await StatesGroup.stateInSpecialCommand.set()