from flask import Flask , render_template , request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
app = Flask(__name__)


bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],

trainer='chatterbot.trainers.ListTrainer')
bot.set_trainer(ListTrainer)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))



if __name__ == '__main__':
	app.run(debug=True)

