from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import config
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

bot_token = config.bot_token
bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.add(button, button2, button3, button4)


kb2 = InlineKeyboardMarkup()
but_in = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
but2_in = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.add(but_in, but2_in)

kb3 = InlineKeyboardMarkup()
but_in = InlineKeyboardButton(text='Product1', callback_data='product_buying')
but2_in = InlineKeyboardButton(text='Product2', callback_data='product_buying')
but3_in = InlineKeyboardButton(text='Product3', callback_data='product_buying')
but4_in = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb3.add(but_in, but2_in, but3_in, but4_in)


initiate_db()
check_and_populate_products()
products = get_all_products()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if is_included(username):
        await message.answer('Пользователь существует, введите другое имя')
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    email = message.text
    await state.update_data(email=email)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    age = message.text
    age = int(age)
    user_data = await state.get_data()
    username = user_data['username']
    email = user_data['email']
    add_user(username, email, age)
    await message.answer(f'Регистрация завершена! Добро пожаловать, {username}.')
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in get_all_products():
        id_, title, description, price = product
        img_path = f'files/{id_}.jpg'
        with open(f'{img_path}', 'rb') as img:
            await message.answer_photo(img, caption=f'Название: {title} | Описание: {description} | Цена: {price}p')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('calories = 10 * weight + 6.25 * growth - 5 * age - 161')
    await call.answer()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weigth(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = int(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    await message.answer(f'Ваша норма калорий {result} в день' )
    await state.finish()

# @dp.message_handler(text='Купить')
# async def get_buying_list(message: types.Message):
#     for number in range(1, 5):
#         await message.answer(f'Название:Продукт{number}/Описание: описание {number} / Цена: {number * 100}')
#         with open(f'{number}.jpg', 'rb') as file:
#             await message.answer_photo(file)
#     await message.answer(f'Выберите продукт для покупки.', reply_markup=kb3)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)