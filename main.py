import telebot

bot = telebot.TeleBot('8851448003:AAE-6Dwpz28BEAiWILkr2QAuT-w0lRcvlKE')

questions = [
    {
        "question": "ЖАНРЫ: Какая игра популяризировала жанр Battle Royale?\nВарианты: PUBG, Minecraft, Dota 2, GTA V",
        "right": "PUBG"
    },
    {
        "question": "ПЕРСОНАЖИ: Как зовут главного героя серии игр 'The Witcher'?\nВарианты: Лютик, Геральт, Весемир, Эцио",
        "right": "Геральт"
    },
    {
        "question": "СЮЖЕТ: В каком городе происходят события игры 'Cyberpunk 2077'?\nВарианты: Найт-Сити, Лос-Сантос, Либерти-Сити, Новиград",
        "right": "Найт-Сити"
    },
    {
        "question": "РЕКОРДЫ: Какая игра является самой продаваемой в истории?\nВарианты: Tetris, GTA V, Minecraft, Wii Sports",
        "right": "Minecraft"
    }
]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет,давай начинать, я буду задавать вопросы о пупулярных играх, жанрах, персонажах, сюжетах и рекордах.')
    send_question(message, 0, 0)


def send_question(message, q_index, score):
    if q_index >= len(questions):
        bot.send_message(message.chat.id, f'Викторина окончена! Твой результат: {score} из {len(questions)}.')
        return


    q_data = questions[q_index]

    msg = bot.send_message(message.chat.id, q_data["question"])

    bot.register_next_step_handler(msg, check_answer, q_index, score)



def check_answer(message, q_index, score):
    q_data = questions[q_index]
    user_answer = message.text.strip()


    if user_answer.lower() == q_data["right"].lower():
        bot.send_message(message.chat.id, "Правильно!")
        score += 1
    else:
        bot.send_message(message.chat.id, f"Неправильно! Правильный ответ: {q_data['right']}")

    send_question(message, q_index + 1, score)




bot.infinity_polling()