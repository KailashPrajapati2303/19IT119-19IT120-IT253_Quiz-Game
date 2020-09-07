def c():
    print('\nQ.1 What Will be output of the following c program? \n #include\n int main()\n {\n  int print=12;\n  print("%d",print);\n  return 0;\n }')
    print("1. 12\n2. 0\n3. 5\n4. compilation error\n")
    w=int(input("Answer : "))
    if w==4:
        print("correct answer")
    else :
        print("wrong answer")
        print('Right answer : compilation error')

    print('\n.......................\n')
    print("\nQ.2 The keyword used to transfer control from a function back to the calling function is\n")
    print("1. switch\n2. goto\n3. go back\n4. return\n")
    w = int(input("Answer : "))
    if w == 4:
      print("correct answer")
    else:
      print("wrong answer")
      print('Right answer : return')

    print('\n.......................\n')

    print('\nQ.3 What will be output if you will execute following c code?\n #include\n int main()\n {\n  print("%c",*"abcde");\n  return 0\n }')
    print("1. abcde\n2. e\n3. a\n4. NULL\n")
    w = int(input("Answer : "))
    if w == 3:
      print("correct answer")
    else:
      print("wrong answer")
      print('Right answer : abcde')

    print('\n.......................\n')

    print('\nQ.4 Which standard library function will you use to find the last occurance of a character in a string in C?\n')
    print("1. strnchar()\n2. strchar()\n3. strrchar()\n4. strrchr\n")
    w = int(input("Answer : "))
    if w == 4:
      print("correct answer")
    else:
      print("wrong answer")
      print('Right answer : strnchar()')

    print('\n.......................\n')

    print('\nQ.5 What will be output if you will compile and execute the following c code?\n void main()\n {\n  print("%s","c""question""bank);\n }\n')
    print("1. c question bank\n2. c\n3. bank\n4. cquestionbank\n")
    w = int(input("Answer : "))
    if w == 4:
      print("correct answer")
    else:
      print("wrong answer")
      print('Right answer : c')
def cplus():
    print('\nQ.1 Each pass through a loop is called a/an')
    print("1. enumeration\n2. iteration\n3. culmination\n4. pass through\n")
    s = int(input("Answer : "))
    if s == 2:
        print("correct answer")
    else:
        print("wrong answer")
        print('Right answer : iteration')

    print('\n.......................\n')
    print("\nQ.2 Which of the following is/are advantage of cellular partitioned structure:\n")
    print("1. Simultaneous read operations can be overlapped\n2. Search \n3. both a & b\n4. None of the above\n")
    s = int(input("Answer : "))
    if s == 3:
        print("correct answer")
    else:
        print("wrong answer")
        print('Right answer : Both a & b')

    print('\n.......................\n')

    print('\nQ.3 The C++ language is\n')
    print("1. case-sensitive\n2. Not case-sensitive\n3. It depends\n4. None of these\n")
    s = int(input("Answer : "))
    if s == 1:
        print("correct answer")
    else:
        print("wrong answer")
        print('Right answer : case-sensitive')

    print('\n.......................\n')

    print('\nQ.4 Which of the following is the boolean operator for logical-and?\n')
    print("1. &\n2. &amp;.\n3. &&")
    s = int(input("Answer : "))
    if s == 3:
        print("correct answer")
    else:
        print("wrong answer")
        print('Right answer : &&')

    print('\n.......................\n')

    print('\nQ.5 which of the following classes handlers file input?\n')
    print("1. ofstream\n2. ifstream\n3. instream\n4. inputfile\n")
    s = int(input("Answer : "))
    if s == 2:
        print("correct answer")
    else:
        print("wrong answer")
        print('Right answer : ifstream')



def start(a):

    print("\t\t>>>>>>>>>>>Start Quiz<<<<<<<<<<\n")
    print("                                           press 1 C\n")
    print("                                           press 2 C++\n")
    print("                                           press 3 Java\n")

    a = int(input("Enter Your Subject : "))
  #  switcher={
   #   1:c(),
    #  2:cplus(),
    #  3:"JAVA",
   # }

    #return switcher.get(a,"Enter right choice")
    if a==1:
        c()
    elif a==2:
        cplus()
    elif a==3:
        print("java")
    else:
        print("Enter Right choice")
def switch(x):
    if x==1:
        start(1)
    elif x==2:
        print("about")
    elif x==3:
        exit(1)
    else:
        print("Enter Right choice")






print("                                    >>>>>>>>>>>QUIZ GAME<<<<<<<<<<\n")
print("                                           press 1 Start Game\n")
print("                                           press 2 About Game\n")
print("                                           press 3 Exit\n")
n=int(input("Enter Your Choice : "))
c=switch(n)
print(c)

