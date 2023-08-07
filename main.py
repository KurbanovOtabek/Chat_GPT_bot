
import telebot
import openai

bot = telebot.TeleBot("6082080509:AAEo-93iuMSLugaTBBcPvmeU27p-uBAF41k")
openai.api_key = "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"


@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)


bot.polling()
