import speech_recognition as sr
import pyttsx3
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)
engine.setProperty('voice', voices[1].id)


# noinspection PyUnreachableCode
def take_command():
    """It takes Microphone input from user and returns as string"""
    global r
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Answer Now 🤔")
        r.energy_threshold = 700
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Answered: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please!")
        r.energy_threshold += 250
        return "None"

        if r.energy_threshold >= 1000:
            r.energy_threshold = 300

    return query


def PercentageCalculation(Correct, Wrong, AskingNum):
    Percentage = (Correct / AskingNum) * 100
    Percentage = round(Percentage, 2)
    print(f"You Scored : {Percentage} %\n\n")
    speak(f"You Scored : {Percentage} %\n\n")
    Answers = ""
    if Correct < 2:
        Answers = "Answer"
    if Correct > 1:
        Answers = "Answers"

    WAnswers = ""
    if Wrong < 2:
        WAnswers = "Answer"
    if Wrong > 1:
        WAnswers = "Answers"

    print(f"You told {Correct} Correct Answers.\nAnd {Wrong} Wrong {Answers}.")
    speak(f"You told {Correct} Correct Answers.\nAnd {Wrong} Wrong {WAnswers}.")


def speak(audio, additional=""):
    engine.say(audio + additional)
    engine.runAndWait()


def Random(name):
    aa = random.sample(name, 1)
    return list(aa)


def main():
    errorCount = 0
    while True:
        try:
            if errorCount < 1:
                print("How Many Times You want me to Ask you the Questions ?\t")
                speak("How Many Times You want me to Ask you the Questions ?")
            else:
                print("Please tell me clearly how many questions I must ask you\t?")
                speak("Please tell me clearly how many questions I must ask you")

            QuestionRounds = int(take_command().lower())
            break
        except:
            print("Please Tell in Numbers.")
            speak("Please Tell in Numbers.")
            try:
                QuestionRounds = int(take_command().lower())
                break
            except:
                errorCount += 1

    DynastyMapping = {
        "Rajput": {
            "Tomaras": "Early twelfth century to 1165",
            "Ananga Pala": "1130 to 1145",
            "Chauhans": "1165 to 1192",
            "Prithviraj Chauhan": "1175 to 1192",
        },

        "Early Turkish Rulers": {"Early Turkish Rulers": "1206 to 1290",
                                 "Qutbuddin Aybak": "1206 to 1210",
                                 "Shamsuddin Iitutmish": "1210 to 1236",
                                 "Raziyya": "1236 to 1240",
                                 "Ghiyasuddin Balban": "1266 to 1287"},
        "Khalji": {"Khalji Dynasty": "1290 to 1320",
                   "Jalaluddin Khalji": "1290 to 1296",
                   "Alauddin Khalji": "1296 to 1316"},

        "Tuughluq": {"Tuughluq Dynasty": "1320 to 1414",
                     "Ghiyasuddin Tuughluq": "1320 to 1324",
                     "Muhammad Tuughluq": "1324 to 1351",
                     "Firuz Shah Tuughluq": "1351 to 1388"},
        "Sayyid": {"Sayyid Dynasty": "1414 to 1451",
                   "Khizr Dynasty": "1414 to 1421"},
        "Lodhi": {"Lodhi Dynasty": "1451 to 1526",
                  "Bahlul Lodhi": "1451 to 1489"}
    }

    CorrectAnswer = 0
    WrongAnswer = 0

    Dynasties = []
    for i in DynastyMapping.keys():
        Dynasties.append(i)
    for number in range(QuestionRounds):

        item = Random(Dynasties)
        print(f"Now I am asking about {item[0]} Dynasty")
        speak(f"Now I am asking about {item[0]} Dynasty")
        DynastyRandomSelected = DynastyMapping[item[0]]
        AskMeQuestion = Random(list(DynastyRandomSelected.keys()))[0]
        print(f"Tell me About : {AskMeQuestion}")
        speak(f"Tell me About : {AskMeQuestion}")

        print("Answer the Question : ", end="")
        Answer = take_command().lower()

        if str(DynastyRandomSelected[AskMeQuestion]) == str(Answer):
            print("You Answered Me Correct\n")
            speak("You Answered Me Correct\n")
            CorrectAnswer += 1
        else:
            print("You Answered Incorrect\n")
            speak("You Answered Incorrect\n")
            WrongAnswer += 1

    PercentageCalculation(CorrectAnswer, WrongAnswer, QuestionRounds)


main()