#!/usr/bin/python3
# -*- coding: utf-8 -*-
from aiogram import Bot, Dispatcher,executor,types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import hlink
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from answers import ans2,ans3_1,ans3_3_1,ans3_3_2,ans3_3_3,ans3_3_4,ans4_1,ans4_2,ans4_3,ans4_4,ans3_3_5,\
    ans3_3_6,ans3_3_7,ans3_3_8,ans3_3_9,ans3_3_10,ans3_3_11,ans3_3_12,ans3_3_13,ans3_3_14,ans3_3_15, ans5
from link import link4_1,link4_4,link3_3_1,link3_3_2,link4_3_1,link4_2,link3_3_3,link3_3_4,link4_3_2, \
    link2,link3_3_5,link3_3_6,link3_3_7,link3_3_8,link3_3_9,link3_3_10,link3_3_11,link3_3_12,link3_3_13,link3_3_14,\
    link3_3_15,link_site

PATH = os.path.split(os.path.abspath(__file__))[0]
token_file = PATH + '/token.txt'

token = open(token_file).read().strip('\n\t ')
bot=Bot(token=token,parse_mode=types.ParseMode.HTML)
dp=Dispatcher(bot, storage=MemoryStorage())

available_categories = ['банковская тайна']
available_variants = ['что такое банковская тайна','защита банковской тайны',
                      'контроль деятельности по защите банковской тайне','назад']
available_variants_safety = ['субъекты, отвечающие за защиту банковской тайны','действия субъектов по защите банковской тайны',
                              'документы, регулирующие действия по защите бт','назад']
available_variants_control = ['фсб','роспотребнадзор','фстэк','банк россии','назад']
available_documents = ['ст. 26 фз № 395-1 «о банках и банковской деятельности»','ст. 857 гражданского кодекса рф','ст. 183 уголовного кодекса рф',
                       'фз "о национальной платежной системе" от 27.06.2011 № 161-фз','фз "о кредитных историях" от 30.12.2004 № 218-фз',
                       'сто бр иббс-1.0-2014','указание банка россии от 27.02.2017 № 4301-у','положение банка россии от 09.12.2020 № 745-п (ред. от 04.08.2021)',
                       'закон рф от 07.02.1992 № 2300-1 (ред. от 11.06.2021) "о защите прав потребителей"','приказ фстэк россии от 11 февраля 2013 г. № 17',
                       'приказ фстэк россии от 25 декабря 2017 г. № 239','федеральный закон о федеральной службе безопасности',
                       'положение о фед. службе по надзору в сфере защиты прав потребителей',
                       'федеральный закон  «о потребительском кредите (займе)»','федеральный закон "о центральном банке российской федерации"', 'назад']
class Bank_security(StatesGroup):
    waiting_for_choosing_1 = State()
    waiting_for_choosing_2 = State()
    waiting_for_choosing_3 = State()
    waiting_for_choosing_4 = State()
    waiting_for_choosing_5 = State()

@dp.message_handler(commands="start")
async def start_choosing (message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in available_categories:
        keyboard.add(category)
    await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
    await Bank_security.waiting_for_choosing_1.set()

@dp.message_handler(state=Bank_security.waiting_for_choosing_1)
async def category_1_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_1.set()
    if message.text.lower() not in available_categories:
        await message.answer("Пожалуйста, выберете тайну с помощью клавиатуры")
        return
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for variant in available_variants:
        keyboard.add(variant)
    await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
    await Bank_security.waiting_for_choosing_2.set()

@dp.message_handler(state=Bank_security.waiting_for_choosing_2)
async def category_2_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_1.set()
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
        await message.answer(hlink('ст. 26 закона «О банках и банковской деятельности»', link2))
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
async def category_3_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_1.set()
    if message.text.lower() not in available_variants_safety:
        await message.answer("Пожалуйста, выберете категорию с помощью клавиатуры")
        return
    if message.text.lower()=='субъекты, отвечающие за защиту банковской тайны':
        await message.answer(ans3_1)
    if message.text.lower()=='документы, регулирующие действия по защите бт':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant_document in available_documents:
            keyboard.add(variant_document)
        await message.answer('Выберете интересующий вас документ',reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_5.set()
    if message.text.lower()=='действия субъектов по защите банковской тайны':
        await message.answer(ans5)
        await message.answer(hlink('Подробнее по ссылке', link_site))
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant in available_variants:
            keyboard.add(variant)
        await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_2.set()

@dp.message_handler(state=Bank_security.waiting_for_choosing_4)
async def category_4_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_1.set()
    if message.text.lower() not in available_variants_control:
        await message.answer("Пожалуйста, выберете категорию с помощью клавиатуры")
        return
    if message.text.lower()=='фсб':
        await message.answer(ans4_1)
        await message.answer(hlink('Федеральный закон 0 Федеральной Службе Безопасности', link4_1))
    if message.text.lower()=='роспотребнадзор':
        await message.answer(ans4_2)
        await message.answer(hlink('Федеральный закон от 21 декабря 2013 года № 353-ФЗ «О потребительском кредите (займе)»', link4_2))
    if message.text.lower()=='фстэк':
        await message.answer(ans4_3)
        await message.answer(hlink('Приказ ФСТЭК России от 11 февраля 2013 г. № 17', link4_3_1))
        await message.answer(hlink('Приказ ФСТЭК России от 25 декабря 2017 г. № 239', link4_3_2))
    if message.text.lower()=='банк россии':
        await message.answer(ans4_4)
        await message.answer(hlink('ФЗ “О Центральном банке Российской Федерации (Банке России)', link4_4))
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant in available_variants:
            keyboard.add(variant)
        await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_2.set()

@dp.message_handler(state=Bank_security.waiting_for_choosing_5)
async def category_5_choosed (message: types.Message):
    if message.text.lower() == '/start':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in available_categories:
            keyboard.add(category)
        await message.answer('О какой тайне вы бы хотели узнать?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_1.set()
    if message.text.lower() not in available_documents:
        await message.answer("Пожалуйста выберете категорию с помощью клавиатуры")
        return
    if message.text.lower() == 'ст. 26 фз № 395-1 «о банках и банковской деятельности»':
        await message.answer(ans3_3_1)
        await message.answer(hlink('Ст. 26 ФЗ № 395-1 «О банках и банковской деятельности»',link3_3_1))
    if message.text.lower() == 'ст. 857 гражданского кодекса рф':
        await message.answer(ans3_3_2)
        await message.answer(hlink('Ст. 857 Гражданского Кодекса РФ',link3_3_2))
    if message.text.lower() == 'ст. 183 уголовного кодекса рф':
        await message.answer(ans3_3_3)
        await message.answer(hlink('Ст. 183 Уголовного Кодекса РФ',link3_3_3))
    if message.text.lower() == 'фз "о национальной платежной системе" от 27.06.2011 № 161-фз':
        await message.answer(ans3_3_4)
        await message.answer(hlink('ФЗ "О национальной платежной системе"',link3_3_4))
    if message.text.lower() == 'фз "о кредитных историях" от 30.12.2004 № 218-фз':
        await message.answer(ans3_3_5)
        await message.answer(hlink('Федеральный закон "О кредитных историях"',link3_3_5))
    if message.text.lower() == 'сто бр иббс-1.0-2014':
        await message.answer(ans3_3_6)
        await message.answer(hlink('СТО БР ИББС-1.0-2014',link3_3_6))
    if message.text.lower() == 'указание банка россии от 27.02.2017 № 4301-у':
        await message.answer(ans3_3_7)
        await message.answer(hlink('Указание Банка России от 27.02.2017 N 4301-У',link3_3_7))
    if message.text.lower() == 'положение банка россии от 09.12.2020 № 745-п (ред. от 04.08.2021)':
        await message.answer(ans3_3_8)
        await message.answer(hlink('Положение Банка России от 09.12.2020 N 745-П (ред. от 04.08.2021)',link3_3_8))
    if message.text.lower() == 'закон рф от 07.02.1992 № 2300-1 (ред. от 11.06.2021) "о защите прав потребителей"':
        await message.answer(ans3_3_9)
        await message.answer(hlink('Закон РФ от 07.02.1992 N 2300-1 (ред. от 11.06.2021)',link3_3_9))
    if message.text.lower() == 'приказ фстэк россии от 11 февраля 2013 г. № 17':
        await message.answer(ans3_3_10)
        await message.answer(hlink('Приказ ФСТЭК России от 11 февраля 2013 г. N 17',link3_3_10))
    if message.text.lower() == 'приказ фстэк россии от 25 декабря 2017 г. № 239':
        await message.answer(ans3_3_11)
        await message.answer(hlink('Приказ ФСТЭК России от 25 декабря 2017 г. N 239',link3_3_11))
    if message.text.lower() == 'федеральный закон о федеральной службе безопасности':
        await message.answer(ans3_3_12)
        await message.answer(hlink('Федеральный закон о федеральной службе безопасности от 22 февраля 1995 года',link3_3_12))

    if message.text.lower() == 'положение о фед. службе по надзору в сфере защиты прав потребителей':
        await message.answer(ans3_3_13)
        await message.answer(hlink('Положение о федеральной службе по надзору в сфере защиты прав потребителей и '
                                   'благополучия человека от 30 июня 2004 г. № 322',link3_3_13))
    if message.text.lower() == 'федеральный закон  «о потребительском кредите (займе)»':
        await message.answer(ans3_3_14)
        await message.answer(hlink('Федеральный закон от 21 декабря 2013 года № 353-ФЗ «О потребительском кредите '
                                   '(займе)»',link3_3_14))
    if message.text.lower() == 'федеральный закон "о центральном банке российской федерации"':
        await message.answer(ans3_3_15)
        await message.answer(hlink('Федеральный закон от 10.07.2002 N 86-ФЗ (ред. от 02.07.2021) "О Центральном банке '
                                   'Российской Федерации (Банке России)"',link3_3_15))
    if message.text.lower()=='назад':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for variant in available_variants_safety:
            keyboard.add(variant)
        await message.answer('Что бы вы хотели узнать о данной тайне?', reply_markup=keyboard)
        await Bank_security.waiting_for_choosing_3.set()
def main():
    executor.start_polling(dp)

if __name__ == "__main__":
    main()
