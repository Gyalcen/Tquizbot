#@title Полный код бота для самоконтроля
import aiosqlite
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = '8379334200:AAGO_oMj59m5TZuljy2ZpsBB07eXpbmczoM'

# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()

# Зададим имя базы данных
DB_NAME = 'quiz_bot.db'


# Структура квиза
quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Какой символ используется для комментариев в Python?',
        'options': ['#', '//', '/* */', '<!-- -->'],
        'correct_option': 0
    },
    {
        'question': 'Как объявить переменную в Python?',
        'options': ['name = 5', 'int name = 5', 'var name = 5', 'let name = 5'],
        'correct_option': 0
    },
    {
        'question': 'Какой метод используется для добавления элемента в список?',
        'options': ['append()', 'add()', 'push()', 'insert()'],
        'correct_option': 0
    },
    {
        'question': 'Как вывести текст на экран в Python?',
        'options': ['print()', 'echo()', 'write()', 'display()'],
        'correct_option': 0
    },
    {
        'question': 'Какой результат выражения 2 ** 3 в Python?',
        'options': ['8', '6', '9', '5'],
        'correct_option': 0
    },
    {
        'question': 'Чем заканчивается строка кода в Python?',
        'options': ['Ничем', 'Точкой с запятой', 'Двоеточием', 'Кавычками'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных предназначен для хранения целых чисел?',
        'options': ['int', 'str', 'float', 'char'],
        'correct_option': 0
    },    
    {
        'question': 'Какой из перечисленных циклов есть в Python?',
        'options': ['for', 'repeat', 'until', 'loop'],
        'correct_option': 0
    },
    # Добавьте другие вопросы
]



def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()

    for option in answer_options:
        builder.add(types.InlineKeyboardButton(
            text=option,
            callback_data="right_answer" if option == right_answer else "wrong_answer")
        )


    import logging
    import asyncio
    from aiogram import Bot, Dispatcher
    from bot.config import API_TOKEN
    from bot.db import create_table
    from bot.handlers import register_handlers

import logging
import asyncio
from aiogram import Bot, Dispatcher
from bot.config import API_TOKEN
from bot.db import create_table
from bot.handlers import register_handlers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
register_handlers(dp)

async def main():
    await create_table()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())