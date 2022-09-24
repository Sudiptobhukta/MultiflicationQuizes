import pyinputplus as pyip
import random ,time

numberofQuestions = 10
correctAnswers =0
for questionNumber in range(1,numberofQuestions+1):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt= '#%s: %s X %s = ' %(questionNumber,num1,num2)

    try:
        pyip.inputStr(prompt, allowRegexes=[r'^%s$' %(num1*num2)],blockRegexes=[('.*','Incorrect!')],timeout=8,limit=3)

    except pyip.TimeoutException:
        print("Out of Time!!")
    except pyip.RetryLimitException:
        print("Out of tries")

    else:
        print('Correct!')
        correctAnswers+=1

time.sleep(1)
print('Score: %s / %s' %(correctAnswers,numberofQuestions))