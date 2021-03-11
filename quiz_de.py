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
    print("a)" + answer_1 +"\nb)" + answer_2 + "\nc)" + answer_3, end="")
    answer_user = input(" |  ")
    if answer_user == answer_right:
        print("Right.")
        answer_count = answer_count + 1
    else:
        print("Wrong.")
    time.sleep(0.6)
    os.system('clear')
     
# start promt when code runs
start = input('Willkommen zum Linux Quiz. Du musst jetzt alle Fragen beantworten (mit "a" "b" oder "c"). Um das Quiz zu starten, drücke Enter: ')

if start == "":
    print("Loading...")
    time.sleep(0.4)
    os.system('clear')
    time.sleep(0.2)

# defined all questions, the specific answers, and the correct answer (a, b, or c)
question("Was ist Linux?", "Eine Desktopumgebung", "Ein Kernel", "Ein Betriebssystem", "b")
question("Welche Distribution ist die älteste, die noch weiterentwickelt wird?", "Ubuntu", "OpenSuse", "Slackware", "c")
question("Wie heißt das Maskottchen von Linux?", "Tuz", "Tux", "Tuc", "b")
question("Welche Distribution basiert nicht auf Debian?", "Arch Linux", "Raspbian", "Ubuntu", "a")
# ^more questions in progress 

# displays some motivating words and the final result 
ratio = answer_count / question_count
if ratio >= 0.8:
    result = "—> Super! Du scheinst dich echt sehr gut mit Linux auszukennen."
elif ratio >= 0.5:
    result = "—> Es geht! Hier und dort könntest du noch Wissenslücken füllen. ;)"
else:
    result = "–> Naja. Informiere dich eventuell noch einmal etwas mehr über Linux, und probiere es anschließend erneut. – Übung macht den Meister!"
    
score = "—————————————–\nDas Quiz ist zu Ende. Dein Ergebnis sind " + str(answer_count*2) + " von " + str(question_count*2) + " erreichbaren Punkten!\n" + result
print(score)
