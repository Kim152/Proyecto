from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def start():
    return question('Quel est votre nom ?')


@ask.intent('HelloIntent')
def bonjour(nom):
    if nom is None:
        return statement('Je ne connais pas ce nom, desole')
    return question("Bonjour {} tu veux creer ton planing pour aujourd'hui ? ".format(nom))

@ask.intent('AcesoIntent')
def acceso(affirmacion):
    if afirmacion == oui or afirmacion == Oui:
        return question ('''Qu'est-ce que tu vas faire aujourd'hui ?''')

@ask.intent('TareasIntent')
def planing (tareas):
    task = []
    if tareas is None:
        task.append(tareas)
    return statement('''Les tâches pour aujourd'hui sont les suivantes {} '''.format(tareas))




if __name__ == '__main__':
    app.run()
