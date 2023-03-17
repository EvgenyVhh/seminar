from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




bot_gb = Bot("5601332796:AAEHRLMkigWsMK3CRgIabc6s5SMn-7tWuSY")
dp =Dispatcher(bot_gb)
async def on_start(_):
    print('Бот запущен')


urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='МНИ - задания', url='https://t.me/c/1843625959/3922/4401')
urlButton2 = InlineKeyboardButton(text='Англ.яз- требования', url='https://t.me/c/1843625959/3924/4010')
urlButton3 = InlineKeyboardButton(text='Философия - вопросы', url='https://docs.google.com/spreadsheets/d/1hPryi0a1Fa8SX99KCTDnIMmIEn07DbXB6GzmaOLAgvo/edit#gid=0')
urlButton4 = InlineKeyboardButton(text='Расписание экзаменов', url='https://t.me/AspirantATiSO/2929')
urlkb.add(urlButton, urlButton2, urlButton3, urlButton4)






@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Нужна помощь"),
            types.KeyboardButton(text="Уже все сдал"),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer("Привет!\nЯ создан облегчить твое обучение\n Выбери пункт меню",
                        reply_markup=keyboard)
    print(message)

@dp.message_handler()
async  def com_help(message: Message):
    if message.text == "Нужна помощь":

         await message.answer(
            f'{message.from_user.first_name}, я помогу тебе сдать сессию')
         await message.answer('выбери предмет:', reply_markup=urlkb)
    elif message.text == 'Уже все сдал':
        await message.answer(f'{message.from_user.first_name},молодец, так держать')
    print(message)

# @dp.message_handler(commands=['start'])
# async def com_start(message: Message):
#     await message.reply(f'{message.from_user.first_name},привет, я Бот и я запущен и готов к работе.Жека придуывает функционал.Пока что я бесполезный бот..')
#     print(message)


# @dp.message_handler()
# async def anythink(message: Message):
#     await message.answer(f'{message.from_user.first_name}, '
#                         f'{message.text}')
#     print(message)


executor.start_polling(dp, skip_updates=True, on_startup=on_start)


