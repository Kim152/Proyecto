from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def start():
    return question('''Je suis Alexa et je suis ici pour t'aider a contruir ton planning , mais laisse moi savoir Quel est ton nom ?''')

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
    else:
        task.append(tareas)
        return question('a quel heure ?')
    return question ('Tu as adjunte {} , cette tache tu vas le faire a quel heure ?' .format (tareas))

@ask.intent('HeureIntent')
def duree(temps):
    if temps is None:
        return question('''c'est tout pour cette tache ?''')
    else:
        task.append(temps)
    return question('''c'est tout pour cette tache ?''')

@ask.intent('TacheIntent')
def fin(acti):
    if acti is None:
        return statement ('Ton activite est {} a {}'.format (tareas, temps))
    return statement ('Ton activite est {} a {}'.format (tareas, temps))



if __name__ == '__main__':
    app.run()