import speech_recognition as sr
import pyttsx3

from speech_to_text import goldprice

r = sr.Recognizer()
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Loop infinitely for user to
# speak


def goldprice():

    # # Step 1 : import module
    import pymysql as p


    # # # # Step 2 : connect to database
    kekedb = p.connect(host = 'localhost', user = 'root', password = 'root', db = 'keke')
    print("connected successfully")


    # # # # # # # Step3  : create cursor
    mypage = kekedb.cursor()


    # # # # # # # # # #### selelect query ....
    # # # # # # # Step 4 : Prepare the query
    q1 = 'select * from stockprices where company="infosys";'

    # Step 5 : execute the query
    mypage.execute(q1)

    # Step 6 : fetch all result
    res = mypage.fetchall()

    # Step7 : close DB
    santhoshdb.close()
    return res[0][0]

while True:

        # Exception handling to handle exceptions at the runtime
        try:

            print("Please speak = ")
            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say ", MyText)
                SpeakText(MyText)

                # nlpwords = text_parser_synonym_antonym_finder(MyText)
                # print(nlpwords)

                if 'stop' in MyText.lower():
                    SpeakText("Thanks for using voice service Have a good day")
                    break

                if 'politics' in MyText.lower():
                    fvar = open('politics.txt', 'r')
                    var = fvar.read()
                    fvar.close()
                    SpeakText(var)

                if 'jewels' in MyText.lower():
                    fvar = open('metal.txt', 'r')
                    var = fvar.read()
                    fvar.close()
                    SpeakText(var)

                if 'price' in MyText.lower():
                    res = goldprice()
                    var = "the stock price of the infosys is " + str(res) + " rupees"
                    print(var)
                    SpeakText(var)

                if 'sports' in MyText.lower():
                    SpeakText("I will read the sports news")

                if 'movies' in MyText.lower():
                    fvar = open('movies.txt', 'r')
                    var = fvar.read()
                    fvar.close()
                    SpeakText(var)


        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")


