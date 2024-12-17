# 1.Импорт библиотек
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message             # ловим все обновления этого типа 
from aiogram.filters.command import Command   # обрабатываем команды /start, /help и другие

# 2. Инициализация объектов

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)    # Создаем объект бота
dp = Dispatcher()                             # Создаем объект диспетчера. Все хэндлеры(обработчики) должны быть подключены к диспетчеру
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Функция для транслитерации текста с кириллицы на латиницу
def transliterate(name):
    translit_dict = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh',
'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts',
'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu',
'Я': 'Ya',
        # Нижний регистр
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
'я': 'ya'
    }
    result = []
    for char in name:
        result.append(translit_dict.get(char, char))
    return ''.join(result)  


# 3. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Введите ФИО на кириллице'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)
   
# 4. Обработка/Хэндлер на любые сообщения
@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    original_text = message.text 
    transliterated_text = transliterate(original_text)  # Транслитерация текста
    logging.info(f'{user_name} {user_id}: {original_text}')
    await message.answer(text=transliterated_text)
    

# 5. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)