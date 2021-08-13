# import time (for waiting events) and os (for clearing old content)
import time
import os
import active as txt
import datetime
# create function for the basic question structure
answer_count = 0
question_count = 0

# class for custom styles 
class style:
   BLACK = '\033[30m'
   BOLD = '\033[1m'
   END = '\033[0m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   YELLOW = '\033[93m'
   BG = '\033[46m'
   BG2 = '\033[43m'
   U='\033[04m'
   IN='\033[08m'

def question(question_title, answer_1, answer_2, answer_3, answer_right):
    global answer_count, question_count
    question_count = question_count + 1
    print(style.BG + str(question_count) + ".) " + question_title + style.END)
    time.sleep(0.2)
    print(style.YELLOW + "a) " + answer_1 +"\nb) " + answer_2 + "\nc) " + answer_3 + style.END, end="")
    answer_user = input("\n\n" + style.BG2 + style.BLACK + "———>" + style.END + " " + style.U)
    if answer_user == answer_right:
        print(style.BOLD + style.GREEN + txt.r + style.END)
        answer_count = answer_count + 1
    else:
        print(style.BOLD + style.RED + txt.w + style.END)
    time.sleep(0.6)
    os.system('clear')
     
os.system('clear')
# start promt when code runs
start = input(txt.prompt)

if start == "":
    print(txt.load)
    time.sleep(0.4)
    os.system('clear')
    time.sleep(0.2)

# defined all questions, the specific answers, and the correct answer (a, b, or c)
# question(txt.qNUMBER, txt.aNUMBERa, txt.aNUMBERb, txt.aNUMBERc, txt.X/Y/Z)
question(txt.q1, txt.a1a, txt.a1b, txt.a1c, txt.Y)
question(txt.q2, txt.a2a, txt.a2b, txt.a2c, txt.X)
question(txt.q3, txt.a3a, txt.a3b, txt.a3c, txt.X)
question(txt.q4, txt.a4a, txt.a4b, txt.a4c, txt.Z)
question(txt.q5, txt.a5a, txt.a5b, txt.a5c, txt.X)
question(txt.q6, txt.a6a, txt.a6b, txt.a6c, txt.Y)
question(txt.q7, txt.a7a, txt.a7b, txt.a7c, txt.Z)
question(txt.q8, txt.a8a, txt.a8b, txt.a8c, txt.Y)
question(txt.q9, txt.a9a, txt.a9b, txt.a9c, txt.Z)

# displays some motivating words and the final result 
ratio = answer_count / question_count
if ratio >= 0.8:
    result = "—> " + txt.verygood
elif ratio >= 0.5:
    result = "—> " + txt.good
else:
    result = "–> " + txt.bad
    
score = "—————————————–\n" + txt.end1 + str(answer_count*2) + txt.end2 + str(question_count*2) + txt.end3 + "\n" + result
print(score)

log = txt.log1 + str(answer_count*2) + txt.log2 + str(question_count*2) + txt.log3


time = time.strftime('%m/%d/%Y %H:%M:%S')
os.system("echo '{}' >> results.txt".format(str("----------------\n" + str(time) + "\n\n" + log + "\n----------------\n")))

