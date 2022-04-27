from aiogram import Bot, Dispatcher,executor,types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from answers import ans2,ans3_1,ans3_2,ans3_3,ans3_4,ans4_1,ans4_2,ans4_3,ans4_4

token = open('token.txt').read()
bot=Bot(token=token)
dp=Dispatcher(bot, storage=MemoryStorage())

available_categories = ['банковская тайна']
available_variants = ['что такое банковская тайна','защита банковской тайны',
                      'контроль деятельности по защите банковской тайне','назад']
available_variants_safety = ['перечень субъектов, отвечающих за защиту банковской тайны','перечень действий '
                              'субъектов по защите банковской тайны', 'план реализации конкретного действия',
                              'документы, регулирующие действия по защите бт','назад']
available_variants_control = ['фсб','роспотребнадзор','фстэк','банк россии','назад']

class Bank_security(StatesGroup):
    waiting_for_choosing_1 = State()
    waiting_for_choosing_2 = State()
    waiting_for_choosing_3 = State()
    waiting_for_choosing_4 = State()

@dp.message_handler(commands="start")
async def start_choosing (message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in available_categories:
        keyboard.add(category)
    await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
    await Bank_security.waiting_for_choosing_1.set()

@dp.message_handler(state=Bank_security.waiting_for_choosing_1)
async def category_1_choosed (message: types.Message, state: FSMContext):
    if message.text.lower() not in available_categories:
        await message.answer("Пожалуйста, выберете тайну с помощью клавиатуры")
        return
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for variant in available_variants:
        keyboard.add(variant)
    await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
    await Bank_security.waiting_for_choosing_2.set()

@dp.message_handler(state=Bank_security.waiting_for_choosing_2)
async def category_2_choosed (message: types.Message, state: FSMContext):
    if message.text.lower() not in available_variants:
        await message.answer("Пожалуйста, выберете категорию с помощью клавиатуры")
        return
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_1.set()
    if message.text.lower()=='что такое банковская тайна':
        await message.answer(ans2)
    if message.text.lower()=='защита банковской тайны':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant_safety in available_variants_safety:
            keyboard.add(variant_safety)
        await message.answer('Выберете дальнейшую категорию', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_3.set()
    if message.text.lower() == 'контроль деятельности по защите банковской тайне':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant_control in available_variants_control:
            keyboard.add(variant_control)
        await message.answer('Выберете орган, действия которого по контролю деятельности субъектов защищающих БТ и документы, регулирующие данные действия,будут показаны', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_4.set()

@dp.message_handler(state=Bank_security.waiting_for_choosing_3)
async def category_3_choosed (message: types.Message, state: FSMContext):
    if message.text.lower() not in available_variants_safety:
        await message.answer("Пожалуйста, выберете категорию с помощью клавиатуры")
        return
    if message.text.lower()=='перечень субъектов, отвечающих за защиту банковской тайны':
        await message.answer(ans3_1)
    if message.text.lower()=='план реализации конкретного действия':
        await message.answer(ans3_2)
    if message.text.lower()=='документы, регулирующие действия по защите бт':
        await message.answer(ans3_3)
    if message.text.lower()=='перечень действий субъектов по защите банковской тайны':
        await message.answer(ans3_4)
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant in available_variants:
            keyboard.add(variant)
        await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_2.set()

@dp.message_handler(state=Bank_security.waiting_for_choosing_4)
async def category_4_choosed (message: types.Message, state: FSMContext):
    if message.text.lower() not in available_variants_control:
        await message.answer("Пожалуйста, выберете категорию с помощью клавиатуры")
        return
    if message.text.lower()=='фсб':
        await message.answer(ans4_1)
    if message.text.lower()=='роспотребнадзор':
        await message.answer(ans4_2)
    if message.text.lower()=='фстэк':
        await message.answer(ans4_3)
    if message.text.lower()=='банк россии':
        await message.answer(ans4_4)
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant in available_variants:
            keyboard.add(variant)
        await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_2.set()

def main():
    executor.start_polling(dp)

if __name__ == "__main__":
    main()