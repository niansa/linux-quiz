# import time (for waiting events) and os (for clearing old content)
import time
import os

# create function for the basic question structure
answer_count = 0
question_count = 0
def question(question_title, answer_1, answer_2, answer_3, answer_right):
    global answer_count, question_count
    question_count = question_count + 1
    print(str(question_count) + ". " + question_title)
    time.sleep(0.2)
    print("a) " + answer_1 +"\nb) " + answer_2 + "\nc) " + answer_3, end="")
    answer_user = input("\n ———> ")
    if answer_user == answer_right:
        print("Richtig")
        answer_count = answer_count + 1
    else:
        print("Falsch")
    time.sleep(0.6)
    os.system('clear')
     
# start promt when code runs
start = input('Willkommen zum Linux Quiz. Du musst jetzt alle Fragen mit "a" "b" oder "c" beantworten. Um das Quiz zu starten, drücke Enter: ')

if start == "":
    print("Loading...")
    time.sleep(0.4)
    os.system('clear')
    time.sleep(0.2)

# defined all questions, the specific answers, and the correct answer (a, b, or c)
question("Was ist Linux?", "Eine Desktopumgebung", "Ein Kernel", "Ein Betriebssystem", "b")
question("Wie heißt das Maskottchen von Linux?", "Tuz", "Tux", "Tuc", "b")
question("Wer ist der Erfinder von Linux?", "Linux Torvalds", "Christiano Ronaldo", "Judd Vinet", "a")
question("Welche Distribution ist die älteste, die noch weiterentwickelt wird?", "Ubuntu", "OpenSuse", "Slackware", "c")
question("Welche Distribution basiert nicht auf Debian?", "Arch Linux", "Raspbian", "Ubuntu", "a")
question("Seit wann gibt es Linux?", "seit 1991", "seit 1985", "seit 2004", "a")
question("Unter welcher Lizenz wird Linux herausgegeben?", "Apache 2.0", "Mozilla Public Licence", "GPLv2", "c")
question("Welche dieser Distribution wird allgemein für Anfänger empfohlen?", "OpenSuse", "Linux Mint", "Kali Linux", "b")
question("Welcher Paketmanager wird bei der Distributuin Fedora eingesetzt?", "apt", "zypper", "dnf", "c")
# ^more questions in progress 

# displays some motivating words and the final result 
ratio = answer_count / question_count
if ratio >= 0.8:
    result = "—> Super! Du scheinst dich echt sehr gut mit Linux auszukennen."
elif ratio >= 0.5:
    result = "—> Relativ gut! Hier und dort könntest du aber noch Wissenslücken füllen. ;)"
else:
    result = "–> Naja... Informiere dich eventuell noch einmal etwas mehr über Linux, und probiere es anschließend erneut. Denn Übung macht den Meister!"
    
score = "—————————————–\nDas Quiz ist zu Ende. Dein Ergebnis sind " + str(answer_count*2) + " von " + str(question_count*2) + " erreichbaren Punkten!\n" + result
print(score)
