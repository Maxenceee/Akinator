
'''
*
*
*   Akinator project
*
*
'''


endRep = False
supposedNum = 0
max = 0
min = 0
supposedList = []


def numFounded(supposedNum):
    print(f"\n\033[0;32mTon nombre est {supposedNum} !")

def isAnswerYes(a):
    if a == 'oui' or a == 'o':
        return True
    else:
        return False

def isAnswerNo(a):
    if a == 'non' or a == 'n':
        return True
    else:
        return False


def init():
    global min, max
    print(
        "\033[4;1;31mRègles\033[0;0m \033[1;31m:" + "\nNe pas mentir" + "\nUniquement répondre par \033[4moui/o\033[0;1;31m ou par \033[4mnon/n\033[0;0m\n" + "\033[4;1;34m\nConseils\033[0;0m \033[1;34m:\nNe pas choisir un nombre trop grand comme fin (risque prendre du temps à résoudre)")
    print("\n\033[0;37mDéfinir l'interval...")
    initMin()
    initMax()
    print(
        f"\n\033[4;1;34mRecap :\n\033[0;0m \n\t\033[1;35mDébut : \033[0;0m\033[3;36m{min} \n\t\033[1;35mFin : \033[0;0m\033[3;36m{max}" + f"\033[0;0m \033[1;34m\n\nChoisi un nombre entre {min} et {max}.")
    main()


def initMin():
    global min
    min = input("\n\033[0;37mNombre de début : ")
    try:
        type(int(min)) != int
        return min
    except:
        print("\033[1;31m" + f"\"{min}\" n'est pas un entier\nEntrez de nouveau la valeur désirée...")
        return initMin()


def initMax():
    global max
    max = input("\n\033[0;37mNombre de fin : ")
    try:
        type(int(max)) != int
        return max
    except:
        print("\033[1;31m" + f"\"{max}\" n'est pas un entier\nEntrez de nouveau la valeur désirée...")
        return initMax()


def main():
    global endRep, supposedNum, min, max
    supposedNum = int(int(max) / 2)
    while endRep != True:
        if int(max) - supposedNum <= 5 or supposedNum - int(min) <= 5:
            if isNum(supposedNum):
                numFounded(supposedNum)
                break
            final(min, max, supposedNum)
            break
        else:
            userAnswer = input(f"\n\033[0;37mTon nombre est plus grand que {supposedNum} ? ").lower()

        if isAnswerYes(userAnswer):
            min = supposedNum
            supposedNum = round((int(min) + int(max)) / 2)
            if supposedNum == (int(max)) or supposedNum == (int(min)):
                endRep = True
                numFounded(supposedNum)
                break
        elif isAnswerNo(userAnswer):
            max = supposedNum
            supposedNum = round((int(min) + int(max)) / 2)
            if supposedNum == int(max) or supposedNum == int(min):
                endRep = True
                numFounded(supposedNum)
                break
        else:
            print("\033[1;31m" + "Réponse non valide...\nEntrez de nouveau la réponse.")


def final(min, max, supposedNum):
    global supposedList
    min = int(min)
    max = int(max)
    answer = input(f"\n\033[0;37mTon nombre est plus grand que {supposedNum} ? ").lower()
    if isAnswerYes(answer):
        min = supposedNum
        supposedNum = ((max - 2) if (max - 2) != min else min + 1) if max - min > 2 else (max - 1 if isNum(supposedNum) else max)
    elif isAnswerNo(answer):
        max = supposedNum
        supposedNum = ((min + 2) if (min + 2) != max else max - 1) if max - min > 2 else (min + 1 if isNum(supposedNum) else min)
    else:
        print("\033[1;31m" + "Réponse non valide...\nEntrez de nouveau la réponse.")
        final(min, max, supposedNum)

    if supposedNum - min <= 1 and max - supposedNum <= 1 or min + 1 == max - 1:
        numFounded(supposedNum)
        return
    elif supposedNum - min <= 2 and max - supposedNum <= 2:
        supposedNum = supposedNum if supposedNum not in supposedList else supposedNum - 1
        if isNum(supposedNum):
            numFounded(supposedNum)
            return
        else:
            supposedList.append(supposedNum)
            supposedNum = supposedNum if supposedNum not in supposedList else max -1
            if isNum(supposedNum):
                numFounded(supposedNum)
                return
            else:
                supposedList.append(supposedNum)
                final(min, max, supposedNum)
    else:
        supposedList.append(supposedNum)
        final(min, max, supposedNum)

def isNum(sup):
    a = input(f"\n\033[0;37m{sup} est-il ton nombre ? ").lower()
    if isAnswerYes(a):
        return True
    elif isAnswerNo(a):
        return False
    else:
        print("\033[1;31m" + "Réponse non valide...\nEntrez de nouveau la réponse.")
        return isNum(sup)


if __name__ == "__main__":
    init()
