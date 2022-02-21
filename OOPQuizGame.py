from mimetypes import guess_all_extensions


class Question:
    def __init__(self,question,answers,correctAnswer):
        self.question = question
        self.answers = answers
        self.correctAnswer = correctAnswer

class User:
    def __init__(self,name):
        self.name = name

class QuizGame:

    gameStatus = True
    correctQuestionCount = 0

    def __init__(self,questions,user):
        self.questions=questions
        self.user = user

    def checkCorrectAnswer(self,answers,correctAnswer,guessedAnswer):
        testAnswer = ['A','B','C','D']
        indexCount = testAnswer.index(guessedAnswer.upper())
        if(answers[indexCount] == correctAnswer): return True
        else: return False

    def introduceGame(self):
        print('Quiz oyununa hosgeldiniz')

    def startGame(self):
        count=0
        self.introduceGame()
        while self.gameStatus and count!=len(self.questions):
            print(f'Soru {count+1} : {self.questions[count].question}')
            guessedAnswer = input(f'A: {self.questions[count].answers[0]} , B: {self.questions[count].answers[1]} , C: {self.questions[count].answers[2]} , D: {self.questions[count].answers[3]} : ')
            correctStatus = self.checkCorrectAnswer(self.questions[count].answers,self.questions[count].correctAnswer,guessedAnswer)
            if(not correctStatus):
                print(f'Yanlis cevap , dogru cevap {self.questions[count].correctAnswer}.')
                self.gameStatus = False
            else:
                self.correctQuestionCount += 1
                count += 1

        if(self.gameStatus): print('Tebrikler , oyunu kazandiniz')
        else: print(f'Kaybettiniz . {self.correctQuestionCount} soru bildiniz')

user = User('Sahin MARAL')



question1 = Question('Who are you',['1','2','3','4'],'4')
question2 = Question('Who are you',['1','2','3','4'],'4')
question3 = Question('Who are you',['1','2','3','4'],'4')

questionList = [question1,question2,question3]

quizGame = QuizGame(questionList,user)
quizGame.startGame()