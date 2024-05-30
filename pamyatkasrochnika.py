import telebot
from telebot import types, TeleBot
from PIL import Image

bot: TeleBot = telebot.TeleBot('7249612197:AAFcPMAaCJDjWNlXuzEth-zOXmmG6T2PfJg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Нужно знать', 'Физическая подготовка', 'Проверь себя']
    markup.add(*buttons)
    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите раздел:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Нужно знать')
def need_to_know(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Знать наизусть', 'Общая информация', 'Оружие и нормативы', 'Назад']
    markup.add(*buttons)
    bot.send_message(message.chat.id, 'Выберите подраздел:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Знать наизусть')
def know_by_heart(message):
    bot.send_message(message.chat.id, 'Гимн РФ:\n\nРоссия – священная наша держава,\nРоссия – любимая наша '
                                      'страна.\nМогучая воля, великая слава –\nТвоё достоянье на все '
                                      'времена!\nСлавься, Отечество наше свободное,''\nБратских народов союз вековой,'
                                      '\nПредками данная мудрость народная!\nСлавься, страна! Мы гордимся '
                                      'тобой!\nОт южных морей до полярного края\nРаскинулись наши леса и '
                                      'поля.\nОдна ты на свете! Одна ты такая\n -Хранимая Богом родная '
                                      'земля!\nСлавься, Отечество наше свободное,\nБратских народов союз вековой,'
                                      '\nПредками данная мудрость народная!\nСлавься, страна! Мы гордимся '
                                      'тобой!\nШирокий простор для мечты и для жизни\nГрядущие нам открывают '
                                      'года.\nНам силу дает наша верность Отчизне.\nТак было, так есть и так '
                                      'будет всегда!\nСлавься, Отечество наше свободное,\nБратских народов союз '
                                      'вековой,\nПредками данная мудрость народная!\nСлавься, страна! Мы гордимся '
                                      'тобой!\n'
                                      '\nВоинская присяга:\nЯ, гражданин Российской Федерации, '
                                      'вступая на военную службу,\nприсягаю на верность Российской Федерации.\nЯ '
                                      'обязуюсь строго исполнять воинский долг,\nхранить военную тайну,'
                                      '\nбеспрекословно выполнять приказы командиров\nи начальников, '
                                      'защищать свободу,\nнезависимость и конституционный строй\nмоей Отечественной '
                                      'Родины.\nСлава России!')


@bot.message_handler(func=lambda message: message.text == 'Общая информация')
def general_info(message):
    bot.send_message(message.chat.id,
                     'Памятные даты войн РФ:\n\n1812 год – Отечественная война\n1941-1945 годы – Великая '
                     'Отечественная война\n1994-1996 годы – Первая чеченская война\n1999-2009 годы – Вторая чеченская '
                     'война')


@bot.message_handler(func=lambda message: message.text == 'Оружие и нормативы')
def weapons_and_norms(message):
    img = open('kalash.jpg', 'rb')
    bot.send_photo(message.chat.id, img)
    img = open('PM.jpg', 'rb')
    bot.send_photo(message.chat.id, img)
    img = open('RPK.jpg', 'rb')
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, 'Инструкция по сборке/разборке АК-74 (фото 1):\n\n1. Открыть крышку ствольной коробки.\n2. Вынуть'
                                      'возвратную пружину и ударник.\n3. Вынуть затворную группу.\n4. Установить'
                                      'затворную группу обратно.\n5. Установить возвратную пружину и ударник.\n6.'
                                      'Закрыть крышку ствольной коробки.\n7. Установить магазин.\n8. Включить'
                                      'предохранитель.\n9. Готово.\n\n'
                                       'Инструкция по сборке/разборке ПМ (фото 2):\n\n1. Извлечь магазин из основания рукоятки.\n'
                                       '2. Проверить, нет ли в патроннике патрона,' 
                                       'отпустить затвор.\n3. Отделить затвор от рамки.\n4. Отвести затвор в крайнее заднее'
                                      'положение и отделить затвор от рамки.\n5. Снять со ствола возвратную пружину.\n\n'
                                      'Инструкция по сборке/разборке РПК (фото3): \n\n'
                                      '1. Пулемет устанавливается на сошки.\n'
                                        '2. Отделяется от пулемета магазин.\n'
                                        '3. Отделяется шомпол.\n'
                                        '4. Отделяется крышка ствольной коробки.\n'
                                        '5. Отделяется возвратный механизм.\n'
                                        '6. Отделяется затворная рама с затвором.\n'
                                        '7. Отделяется затвор от затворной рамы.\n'
                                        '8. Отделяется газовая трубка со ствольной накладкой.\n'
                                        '9. Производится разборка магазина:\n'
                                        '   а — отделение крышки магазина;\n'
                                        '   б — отделение досылателя;\n'
                                        '   в — отделение пружины подавателя;\n'
                                        '   г — отделение снаряжательного рычага.\n'
                                        '10. Разбирается возвратный механизм.\n'
                                        '11. Разбирается затвор.\n'
                                        '12. Разбирается ударно-спусковой механизм.\n'
                                        '13. Отделяется цевье.')
@bot.message_handler(func=lambda message: message.text == 'Физическая подготовка')
def physical_training(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Ввести данные', 'Назад']
    markup.add(*buttons)
    bot.send_message(message.chat.id, 'Стандарты ВС РФ:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Нормативы физической подготовки ВС РФ:')
    bot.send_message(message.chat.id, 'Отжимания: 25-30 (мужчины), 15-20 (женщины)')
    bot.send_message(message.chat.id, 'Подтягивания: 5-7 (мужчины), 3-5 (женщины)')
    bot.send_message(message.chat.id, 'Бег на 100м: 12.5-13.5 сек (мужчины), 14.5-15.5 сек (женщины)')
    bot.send_message(message.chat.id, 'Бег на 1км: 4-5 минут (мужчины), 5-6 минут (женщины)')
    bot.send_message(message.chat.id, 'Прыжок в длину(с разбега): 5.5-6.5 м (мужчины), 4.5-5.5 м (женщины)')
    bot.send_message(message.chat.id, 'Толкание ядра (16кг): 10-12 м (мужчины), 8-10 м (женщины)')
    bot.send_message(message.chat.id, 'Бег на 3000м: 12-15 минут (мужчины), 15-18 минут (женщины)')

    norms={}
    @bot.message_handler(func=lambda message: message.text == 'Ввести данные')
    def input_data(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Отжимания', 'Бег на 100м', 'Бег на 1км', 'Подтягивания','Прыжок в длину','Толкание ядра','Бег на 3000м','Назад']
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Выберите норматив для ввода данных:', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Отжимания')
    def push_ups(message):
        bot.send_message(message.chat.id, 'Введите количество отжиманий:')
        bot.register_next_step_handler(message, process_push_ups)

    def process_push_ups(message):
        push_ups_count = int(message.text)
        norms[message.chat.id] = norms.get(message.chat.id, {})
        norms[message.chat.id]['push_ups'] = push_ups_count
        bot.send_message(message.chat.id, f'Вы ввели {push_ups_count} отжиманий.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Отжимания', 'Бег на 100м', 'Бег на 1км', 'Подтягивания','Прыжок в длину','Толкание ядра','Бег на 3000м','Назад']
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Выберите следующий норматив:', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Бег на 100м')
    def run100(message):
        bot.send_message(message.chat.id, 'Введите время:')
        bot.register_next_step_handler(message, process_run100)

    def process_run100(message):
        run100_count = int(message.text)
        norms[message.chat.id] = norms.get(message.chat.id, {})
        norms[message.chat.id]['run100'] = run100_count
        bot.send_message(message.chat.id, f'Вы ввели {run100_count} сек.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Отжимания', 'Бег на 100м', 'Бег на 1км', 'Подтягивания','Прыжок в длину','Толкание ядра','Бег на 3000м','Назад']
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Выберите следующий норматив:', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Бег на 1км')
    def run1000(message):
        bot.send_message(message.chat.id, 'Введите время:')
        bot.register_next_step_handler(message, process_run1000)

    def process_run1000(message):
        run1000_count = int(message.text)
        norms[message.chat.id] = norms.get(message.chat.id, {})
        norms[message.chat.id]['run1000'] = run1000_count
        bot.send_message(message.chat.id, f'Вы ввели {run1000_count} мин.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Отжимания', 'Бег на 100м', 'Бег на 1км', 'Подтягивания', 'Прыжок в длину', 'Толкание ядра',
                   'Бег на 3000м', 'Назад']
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Выберите следующий норматив:', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Подтягивания')
    def pod(message):
        bot.send_message(message.chat.id, 'Введите количество подтягиваний:')
        bot.register_next_step_handler(message, process_pod)

    def process_pod(message):
        pod_count = int(message.text)
        norms[message.chat.id] = norms.get(message.chat.id, {})
        norms[message.chat.id]['pod'] = pod_count
        bot.send_message(message.chat.id, f'Вы ввели {pod_count} подтягиваний.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Отжимания', 'Бег на 100м', 'Бег на 1км', 'Подтягивания','Прыжок в длину','Толкание ядра','Бег на 3000м','Назад']
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Выберите следующий норматив:', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Прыжок в длину')
    def jump(message):
        bot.send_message(message.chat.id, 'Введите длину:')
        bot.register_next_step_handler(message, process_jump)

    def process_jump(message):
        jump_count = int(message.text)
        norms[message.chat.id] = norms.get(message.chat.id, {})
        norms[message.chat.id]['jump'] = jump_count
        bot.send_message(message.chat.id, f'Вы ввели {jump_count} м.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Отжимания', 'Бег на 100м', 'Бег на 1км', 'Подтягивания','Прыжок в длину','Толкание ядра','Бег на 3000м','Назад']
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Выберите следующий норматив:', reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Толкание ядра')
    def shot_put(message):
        bot.send_message(message.chat.id, 'Введите длину:')
        bot.register_next_step_handler(message, process_shot_put)

    def process_shot_put(message):
        shot_put_count = int(message.text)
        norms[message.chat.id] = norms.get(message.chat.id, {})
        norms[message.chat.id]['shot_put'] = shot_put_count
        bot.send_message(message.chat.id, f'Вы ввели {shot_put_count} м.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Отжимания', 'Бег на 100м', 'Бег на 1км', 'Подтягивания', 'Прыжок в длину', 'Толкание ядра',
                   'Бег на 3000м', 'Назад']
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Выберите следующий норматив:', reply_markup=markup)
    @bot.message_handler(func=lambda message: message.text == 'Бег на 3000м')
    def run3000(message):
        bot.send_message(message.chat.id, 'Введите время:')
        bot.register_next_step_handler(message, process_run3000)

    def process_run3000(message):
        run3000_count = int(message.text)
        norms[message.chat.id] = norms.get(message.chat.id, {})
        norms[message.chat.id]['run3000'] = run3000_count
        bot.send_message(message.chat.id, f'Вы ввели {run3000_count} мин.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Посмотреть результаты', 'Назад']
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Вы ввели все нормативы, желаете ознакомиться с результатом?',
                         reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'Посмотреть результаты')
    def view_norms(message):
        if message.chat.id in norms:
            norms_message = 'Ваши нормативы:\n'
            norms_message += f'Отжимания: {norms[message.chat.id].get("push_ups", "Не введено")}\n'
            norms_message += f'Бег на 100м: {norms[message.chat.id].get("run100", "Не введено")}\n'
            norms_message += f'Бег на 1км: {norms[message.chat.id].get("run1000", "Не введено")}\n'
            norms_message += f'Подтягивания: {norms[message.chat.id].get("pod", "Не введено")}\n'
            norms_message += f'Прыжок в длину: {norms[message.chat.id].get("jump", "Не введено")}\n'
            norms_message += f'Толкание ядра: {norms[message.chat.id].get("shot_put", "Не введено")}\n'
            norms_message += f'Бег на 3000м: {norms[message.chat.id].get("run3000", "Не введено")}'
            bot.send_message(message.chat.id, norms_message)
        else:
            bot.send_message(message.chat.id, 'Вы не ввели нормативы.')

questions = [
    {"question": "Какое звание имеет командир роты?", "answers": ["Капитан", "Майор", "Полковник"], "correct": 0},
    {"question": "Какое звание имеет командир батальона?", "answers": ["Майор", "Полковник", "Генерал-майор"],
     "correct": 1},
    {"question": "Какое звание имеет командир полка?", "answers": ["Полковник", "Генерал-майор", "Генерал-лейтенант"],
     "correct": 0},
    {"question": "Какое звание имеет командир дивизии?",
     "answers": ["Генерал-майор", "Генерал-лейтенант", "Генерал-полковник"], "correct": 0},
    {"question": "Какое звание имеет командир корпуса?",
     "answers": ["Генерал-лейтенант", "Генерал-полковник", "Генерал армии"], "correct": 0},
    {"question": "Какое звание имеет командир армии?",
     "answers": ["Генерал-полковник", "Генерал армии", "Маршал Российской Федерации"], "correct": 1},
    {"question": "Какое звание имеет командир флота?",
     "answers": ["Адмирал", "Адмирал флота", "Адмирал флота Советского Союза"], "correct": 0},
    {"question": "Какое звание имеет командир военного округа?",
     "answers": ["Генерал-полковник", "Генерал армии", "Маршал Российской Федерации"], "correct": 1},
    {"question": "Какое звание имеет командир военно-воздушных сил?",
     "answers": ["Генерал-лейтенант", "Генерал-полковник", "Генерал армии"], "correct": 1},
    {"question": "Какое звание имеет командир военно-морского флота?",
     "answers": ["Адмирал", "Адмирал флота", "Адмирал флота Советского Союза"], "correct": 0},
    {"question": "Какое звание имеет командир Сухопутных войск?",
     "answers": ["Генерал-лейтенант", "Генерал-полковник", "Генерал армии"], "correct": 1},
    {"question": "Какое звание имеет командир Воздушно-космических сил?",
     "answers": ["Генерал-лейтенант", "Генерал-полковник", "Генерал армии"], "correct": 1},
    {"question": "Какое звание имеет командир Ракетных войск стратегического назначения?",
     "answers": ["Генерал-лейтенант", "Генерал-полковник", "Генерал армии"], "correct": 1},
    {"question": "Какое звание имеет командир Войск воздушно-космической обороны?",
     "answers": ["Генерал-лейтенант", "Генерал-полковник", "Генерал армии"], "correct": 1},
    {"question": "Какое звание имеет командир Войск специального назначения?",
     "answers": ["Генерал-лейтенант", "Генерал-полковник", "Генерал армии"], "correct": 1},
    {"question": "Какое звание имеет командир Береговых войск?",
     "answers": ["Адмирал", "Адмирал флота", "Адмирал флота Советского Союза"], "correct": 0},
    {"question": "Какое звание имеет командир Морской пехоты?",
     "answers": ["Генерал-лейтенант", "Генерал-полковник", "Генерал армии"], "correct": 1},
    {"question": "Какое звание имеет командир Войск гражданской обороны?",
     "answers": ["Генерал-лейтенант", "Генерал-полковник", "Генерал армии"], "correct": 1}
    ]
current_question = 0

@bot.message_handler(func=lambda message: message.text == 'Проверь себя')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Начать тест', 'Назад']
    markup.add(*buttons)
    bot.send_message(message.chat.id, 'Добро пожаловать! Начните тест на знание званий ВС РФ:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Начать тест')
def start_test(message):
    global current_question, correct_answers
    current_question = 0
    correct_answers = 0
    ask_question(message)

def ask_question(message):
    question = questions[current_question]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = question["answers"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, question["question"], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in [answer for question in questions for answer in question["answers"]])
def answer(message):
    global current_question, correct_answers
    question = questions[current_question]
    if message.text == question["answers"][question["correct"]]:
        bot.send_message(message.chat.id, "Верно!")
        correct_answers += 1
    else:
        bot.send_message(message.chat.id, "Неверно!")
    current_question += 1
    if current_question < len(questions):
        ask_question(message)
    else:
        bot.send_message(message.chat.id, f"Вы ответили правильно на {correct_answers} из {len(questions)} вопросов.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['Да']
        markup.add(*buttons)
        bot.send_message(message.chat.id, 'Вернуться в главное меню?', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Да')
def back_to_main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Нужно знать', 'Физическая подготовка', 'Проверь себя']
    markup.add(*buttons)
    bot.send_message(message.chat.id, 'Вы вернулись назад:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Назад')
def back_to_main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Нужно знать', 'Физическая подготовка', 'Проверь себя']
    markup.add(*buttons)
    bot.send_message(message.chat.id, 'Вы вернулись назад:', reply_markup=markup)



bot.polling()