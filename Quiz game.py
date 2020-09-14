def con():
    print("\n\t\t\t\t\t\t\t\t\t>>>>>>>>>>>>>>><<<<<<<<<<<<<")
    print('\n\t\t\t\t\t\t\t\t\t\t PRESS 1 Main Menu ')
    print('\t\t\t\t\t\t\t\t\t\t PRESS 2 Exit\n')
    f=int(input("Enter your choice : "))
    if f==1:
        switch()
    else:
        exit(1)
def java():
    score=0
    print('\nQ.1  which of the following is the valid statement to create object? Consider Myclass.class is available')
    print("1. Myclass m = new Myclass;\n2. Myclass m = Myclass();\n3. Myclass() m = new Myclass();\n4.  Myclass() m = new Myclass;\n")
    w = int(input("Answer : "))
    if w == 3:
        print("correct answer")
        score=score+1
    else:
        print("wrong answer")
        print('Right answer : Myclass() m = new Myclass();')
        score=score-0.25
    #print('score=',score)

    print('\n.......................\n')
    print("\nQ.2 If no constructor is declared in the class then default constructor will be created by  Java Runtime Environment:\n")
    print("1. True\n2. False\n")
    w = int(input("Answer : "))
    if w == 1:
        print("correct answer")
        score = score + 1
    else:
        print("wrong answer")
        print('Right answer : True')
        score = score - 0.25
    #print('score=', score)

    print('\n.......................\n')

    print('\nQ.3 To declare class method, which of the following keyword is used?\n }')
    print("1. static\n2. new\n3. public\n4. class\n")
    w = int(input("Answer : "))
    if w == 1:
        print("correct answer")
        score=score+1

    else:
        print("wrong answer")
        print('Right answer : static')
        score = score - 0.25
    #print('score=', score)

    print('\n.......................\n')

    print('\nQ.4 Which of the following(s) is(are) valid declaration of java class?\n')
    print("1. public class Myclass{}\n2. public class Myclass{int i:}\n3. public class Myclass{void demo(){}}\n4. All of the above\n")
    w = int(input("Answer : "))
    if w == 4:
        print("correct answer")
        score=score+1

    else:
        print("wrong answer")
        print('Right answer : All of the above')
        score = score - 0.25
    #print('score=', score)

    print('\n.......................\n')

    print('\nQ.5 Which of the following is not a Java features?\n')
    print("1. c Dynamic\n2. Architecture Neutral\n3. Use of pointers\n4. Object-oriented\n")
    w = int(input("Answer : "))
    if w == 3:
        print("correct answer")
        score=score+1

    else:
        print("wrong answer")
        print('Right answer : Use of pointers')
        score = score - 0.25
    #print('score=', score)

    print('\nQ.6 What is the use of the intern() method?')
    print("1. It returns the existing string from memory\n2. It creates a new string in the database\n3. It modifies the existing string in the database\n4. None of the above\n")
    w = int(input("Answer : "))
    if w == 1:
        print("correct answer")
        score = score + 1
    else:
        print("wrong answer")
        print("Right answer : It returns the existing string from memory")
        score = score - 0.25
    # print('score=',score)

    print('\n.......................\n')
    print(
        "\nQ.7 What is the return type of the hashCode() method in the Object class?\n")
    print("1. Object\n2. int\n3. long\n4. void\n")
    w = int(input("Answer : "))
    if w == 2:
        print("correct answer")
        score = score + 1
    else:
        print("wrong answer")
        print('Right answer : int')
        score = score - 0.25
    # print('score=', score)

    print('\n.......................\n')

    print('\nQ.8 Which method of the Class.class is used to determine the name of a class represented by the class object as a String?\n')
    print("1. getClass()\n2. intern()\n3. getName()\n4. toString()\n")
    w = int(input("Answer : "))
    if w == 3:
        print("correct answer")
        score = score + 1

    else:
        print("wrong answer")
        print('Right answer : getName()')
        score = score - 0.25
    # print('score=', score)

    print('\n.......................\n')

    print('\nQ.9 Which package contains the Random class?\n')
    print("1. java.util package\n2. java.lang package\n3. java.awt package\n4. java.io package\n")
    w = int(input("Answer : "))
    if w == 1:
        print("correct answer")
        score = score + 1

    else:
        print("wrong answer")
        print('Right answer : java.util package')
        score = score - 0.25
    # print('score=', score)

    print('\n.......................\n')

    print('\nQ.10 An interface with no fields or methods is known as a ______.\n')
    print("1. Runnable Interface\n2. Marker Interface\n3. Abstract Interface\n4. CharSequence Interface\n")
    w = int(input("Answer : "))
    if w == 2:
        print("correct answer")
        score = score + 1

    else:
        print("wrong answer")
        print('Right answer : Marker Interface')
        score = score - 0.25

    print("\n>>>>>>>>>>><<<<<<<<<<<\n")
    print('Final score=', score)
    if score <= 0:
        print("Final percentage : 0%")
    else:
        z = (float(score)) * 100 / 10
        print("Final percentage : " + str(z) + "%")


def c():
    score=0
    print('\nQ.1 What Will be output of the following c program? \n #include\n int main()\n {\n  int print=12;\n  print("%d",print);\n  return 0;\n }')
    print("1. 12\n2. 0\n3. 5\n4. compilation error\n")
    w=int(input("Answer : "))
    if w==4:
        print("correct answer")
        score=score+1

    else :
        print("wrong answer")
        print('Right answer : compilation error')
        score = score -0.25
   # print('score=', score)

    print('\n.......................\n')
    print("\nQ.2 The keyword used to transfer control from a function back to the calling function is\n")
    print("1. switch\n2. goto\n3. go back\n4. return\n")
    w = int(input("Answer : "))
    if w == 4:
      print("correct answer")
      score = score + 1

    else:
      print("wrong answer")
      print('Right answer : return')
      score = score - 0.25
    #print('score=', score)

    print('\n.......................\n')

    print('\nQ.3 What will be output if you will execute following c code?\n #include\n int main()\n {\n  print("%c",*"abcde");\n  return 0\n }')
    print("1. abcde\n2. e\n3. a\n4. NULL\n")
    w = int(input("Answer : "))
    if w == 3:
      print("correct answer")
      score = score + 1

    else:
      print("wrong answer")
      print('Right answer : abcde')
      score = score - 0.25
    #print('score=', score)

    print('\n.......................\n')

    print('\nQ.4 Which standard library function will you use to find the last occurance of a character in a string in C?\n')
    print("1. strnchar()\n2. strchar()\n3. strrchar()\n4. strrchr\n")
    w = int(input("Answer : "))
    if w == 4:
      print("correct answer")
      score = score + 1

    else:
      print("wrong answer")
      print('Right answer : strnchar()')
      score = score -0.25
    #print('score=', score)

    print('\n.......................\n')

    print('\nQ.5 What will be output if you will compile and execute the following c code?\n void main()\n {\n  print("%s","c""question""bank);\n }\n')
    print("1. c question bank\n2. c\n3. bank\n4. cquestionbank\n")
    w = int(input("Answer : "))
    if w == 4:
      print("correct answer")
      score = score + 1

    else:
      print("wrong answer")
      print('Right answer : c')
      score = score - 0.25

    print("\n>>>>>>>>>>><<<<<<<<<<<\n")
    print('score=', score)
    if score<=0:
        print("Final percentage : 0%")
    else:
        q = (float(score)) * 100 / 5
        print("Final percentage : " + str(q) + "%")


def cplus():
    score=0
    print('\nQ.1 Each pass through a loop is called a/an')
    print("1. enumeration\n2. iteration\n3. culmination\n4. pass through\n")
    s = int(input("Answer : "))
    if s == 2:
        print("correct answer")
        score=score+1

    else:
        print("wrong answer")
        print('Right answer : iteration')
        score = score - 0.25
    #print('score=', score)

    print('\n.......................\n')
    print("\nQ.2 Which of the following is/are advantage of cellular partitioned structure:\n")
    print("1. Simultaneous read operations can be overlapped\n2. Search \n3. both a & b\n4. None of the above\n")
    s = int(input("Answer : "))
    if s == 3:
        print("correct answer")
        score=score+1

    else:
        print("wrong answer")
        print('Right answer : Both a & b')
        score = score - 0.25
   # print('score=', score)

    print('\n.......................\n')

    print('\nQ.3 The C++ language is\n')
    print("1. case-sensitive\n2. Not case-sensitive\n3. It depends\n4. None of these\n")
    s = int(input("Answer : "))
    if s == 1:
        print("correct answer")
        score=score+1

    else:
        print("wrong answer")
        print('Right answer : case-sensitive')
        score = score - 0.25
   # print('score=', score)

    print('\n.......................\n')

    print('\nQ.4 Which of the following is the boolean operator for logical-and?\n')
    print("1. &\n2. &amp;.\n3. &&")
    s = int(input("Answer : "))
    if s == 3:
        print("correct answer")
        score=score+1

    else:
        print("wrong answer")
        print('Right answer : &&')
        score = score - 0.25
    #print('score=', score)

    print('\n.......................\n')

    print('\nQ.5 which of the following classes handlers file input?\n')
    print("1. ofstream\n2. ifstream\n3. instream\n4. inputfile\n")
    s = int(input("Answer : "))
    if s == 2:
        print("correct answer")
        score=score+1

    else:
        print("wrong answer")
        print('Right answer : ifstream')
        score = score - 0.25

    print("\n>>>>>>>>>>><<<<<<<<<<<\n")
    print('Final score=', score)
    if score <= 0:
        print("Final percentage : 0%")
    else:
        v = (float(score)) * 100 / 5
        print("Final percentage : " + str(v) + "%")




def start(a):

    print("                                   >>>>>>>>>>>Start Quiz<<<<<<<<<<\n")
    print("                                           press 1 C\n")
    print("                                           press 2 C++\n")
    print("                                           press 3 Java\n")

    a = int(input("Enter Your Subject : "))


    #return switcher.get(a,"Enter right choice")
    if a==1:
        c()
        con()
    elif a==2:
        cplus()
        con()
    elif a==3:
        java()
        con()
    else:
        print("Enter Right choice")
def switch():
    print("                                    >>>>>>>>>>>QUIZ GAME<<<<<<<<<<\n")
    print("                                           press 1 Start Game\n")
    print("                                           press 2 About Game\n")
    print("                                           press 3 Rules\n")
    print("                                           press 4 Exit\n")
    n = int(input("Enter Your Choice : "))


    if n==1:
        start(1)
    elif n==2:
        print("This Project created by Kailash Prajapati & Savan Prajapati in 3rd semester.")
        con()
    elif n==3:
        print("if user pick right answer so user get 1 point sand if user pick Wrong answer so user lose 0.25 point.")
        con()
    elif n==4:
        exit(1)
    else:
        print("Enter Right choice")


if __name__ == "__main__":
 switch()






