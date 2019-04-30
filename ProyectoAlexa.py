from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def start():
    return question('''Je suis Alexa et je suis ici pour t'aider ,Quel est ton nom ?''')

@ask.intent('HelloIntent')
def bonjour(nom):
    if nom is None:
        return statement("Je ne connais cette nom ,desole")
    else:
        return question("Bonjour {} tu veux creer ton planing pour aujourd'hui".format(nom))

@ask.intent('AcesoIntent')
def aceso(reponse):
    if reponse == 'oui' or reponse == 'Oui':
        return question ('''Ok, alors dis-moi le premier événement de la journée. ?''')
    return question ('Ok, alors dis-moi un tache  ?')

@ask.intent('TareasIntent')
def planing (tareas):
    task = []
    if tareas is None:
        task.append(tareas)
        return question('a quel heure ?')
    return question ('a quel heure ?')

@ask.intent('HeureIntent')
def duree(temps):
    if temps is None:
        return question('''c'est tout pour cette tache ?''')
    return question('''c'est tout pour cette tache ?''')



if __name__ == '__main__':
    app.run()