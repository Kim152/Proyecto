from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def start():
    return question('''Je suis Alexa et je suis ici pour t'aider a creer ton planing jour a jours . Dis moi ton nom ?''')

@ask.intent('HelloIntent')
def bonjour(nom):
    if nom is None:
        return statement("Je ne connais pas ce nom ,desole")
    else:
        return question("Bonjour {} tu veux creer ton planing pour aujourd'hui ?".format(nom))

@ask.intent('AcesoIntent')
def aceso(reponse):
    if reponse == 'oui' or reponse == 'Oui':
        return question ('Ok, alors dis moi le premier événement de la journée. ?')
    return question ('Ok, alors dis-moi une tache  ?')
task = []

@ask.intent('TareasIntent')
def planing (tareas):
    if tareas is None:
        task.append(tareas)
        return question('a quel heure ?')
    else:
        task.append(tareas)
    return question ('Tu as ajoute : {} a ton planning . cette tache tu vas la faire a quel heure ?'.format(tareas))


@ask.intent('HeureIntent')
def duree(temps):
    if temps is None:
        return question('La tache va se passer a {} : tout pour cette tache ?'''.format(temps))
    else:
        return question('La tache va se passer a {} : tout pour cette tache ?'''.format(temps))

@ask.intent('TerminarIntent')
def fini(terminar):
    if terminar is None :
        return statement('La nouvelle tache est ajoutee avec succes a ton planing. AU REVOIR ')
    else:
        return statement('La nouvelle tache est ajoutee avec succes a ton planing. au revoir. ')

if __name__ == '__main__':
    app.run()

