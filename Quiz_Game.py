def c():
   score = 0
   import mysql.connector
   xyz = mysql.connector.connect(host="localhost", user="savan", passwd="savan4141", database="savan")
   mycursor = xyz.cursor()
   mycursor.execute("select * from clanguage")
   for i in mycursor:
      print('\n>>>>>>>>><<<<<<<<<')
      print(i[0])
      print(i[1])
      print('(A) ' + i[2])
      print('(B) ' + i[3])
      print('(C) ' + i[4])
      print('(D) ' + i[5])

      a = input("\nyour choice")

      if a.capitalize() == i[6]:
         print("correct answer")
         score=score + 1
      else:
         print("Wrong answer")
         print("Right Answer : " + i[7])
         score = score - 0.25

   print("\n>>>>>>>><<<<<<<<")
   print('Final score=', score,'/15')

   if score <= 0:
      print("Final percentage : 0%")
      print(">>>>>>>><<<<<<<<")
   else:
      v = (float(score)) * 100 / 15
      b=round(v,2)
      print("Final percentage : " + str(b) + "%")
      print(">>>>>>>><<<<<<<<")

def cplus():
    score = 0
    import mysql.connector
    xyz = mysql.connector.connect(host="localhost", user="savan", passwd="savan4141", database="savan")
    mycursor = xyz.cursor()
    mycursor.execute("select * from cplus")
    for i in mycursor:
        print('\n>>>>>>>>><<<<<<<<<')
        print(i[0])

        print(i[1])
        print('(A) ' + i[2])
        print('(B) ' + i[3])
        print('(C) ' + i[4])
        print('(D) ' + i[5])

        a = input("\nyour choice")

        if a.capitalize() == i[6]:
            print("correct answer")
            score = score + 1
        else:
            print("Wrong answer")
            print("Right Answer : " + i[7])
            score = score - 0.25

    print("\n>>>>>>>><<<<<<<<")
    print('Final score=', score, '/15')
    if score <= 0:
        print("Final percentage : 0%")
        print(">>>>>>>><<<<<<<<")
    else:
        v = (float(score)) * 100 / 15
        b = round(v, 2)
        print("Final percentage : " + str(b) + "%")
        print(">>>>>>>><<<<<<<<")

def java():
    score = 0
    import mysql.connector
    xyz = mysql.connector.connect(host="localhost", user="savan", passwd="savan4141", database="savan")
    mycursor = xyz.cursor()
    mycursor.execute("select * from java")
    for i in mycursor:
        print('\n>>>>>>>>><<<<<<<<<')
        print(i[0])
        print(i[1])
        print('(A) ' + i[2])
        print('(B) ' + i[3])
        print('(C) ' + i[4])
        print('(D) ' + i[5])

        a = input("\nyour choice")

        if a.capitalize() == i[6]:
            print("correct answer")
            score = score + 1
        else:
            print("Wrong answer")
            print("Right Answer : " + i[7])
            score = score - 0.25

    print("\n>>>>>>>><<<<<<<<")
    print('Final score=', score,'/15')
    if score <= 0:
        print("Final percentage : 0%")
        print(">>>>>>>><<<<<<<<")
    else:
        v = (float(score)) * 100 / 15
        b = round(v, 2)
        print("Final percentage : " + str(b) + "%")
        print(">>>>>>>><<<<<<<<")
def python():
    score = 0
    import mysql.connector
    xyz = mysql.connector.connect(host="localhost", user="savan", passwd="savan4141", database="savan")
    mycursor = xyz.cursor()
    mycursor.execute("select * from python")
    for i in mycursor:
        print('\n>>>>>>>>><<<<<<<<<')
        print(i[0])
        print(i[1])
        print('(A) ' + i[2])
        print('(B) ' + i[3])
        print('(C) ' + i[4])
        print('(D) ' + i[5])

        a = input("\nyour choice")

        if a.capitalize() == i[6]:
            print("correct answer")
            score = score + 1
        else:
            print("Wrong answer")
            print("Right Answer : " + i[7])
            score = score - 0.25

    print("\n>>>>>>>><<<<<<<<")
    print('Final score=', score, '/15')
    if score <= 0:
        print("Final percentage : 0%")
        print(">>>>>>>><<<<<<<<")
    else:
        v = (float(score)) * 100 / 15
        b = round(v, 2)
        print("Final percentage : " + str(b) + "%")
        print(">>>>>>>><<<<<<<<")
def php():
    score = 0
    import mysql.connector
    xyz = mysql.connector.connect(host="localhost", user="savan", passwd="savan4141", database="savan")
    mycursor = xyz.cursor()
    mycursor.execute("select * from java")
    for i in mycursor:
        print('\n>>>>>>>>><<<<<<<<<')
        print(i[0])
        print(i[1])
        print('(A) ' + i[2])
        print('(B) ' + i[3])
        print('(C) ' + i[4])
        print('(D) ' + i[5])

        a = input("\nyour choice")

        if a.capitalize() == i[6]:
            print("correct answer")
            score = score + 1
        else:
            print("Wrong answer")
            print("Right Answer : " + i[7])
            score = score - 0.25

    print("\n>>>>>>>><<<<<<<<")
    print('Final score=', score, '/15')
    if score <= 0:
        print("Final percentage : 0%")
        print(">>>>>>>><<<<<<<<")
    else:
        v = (float(score)) * 100 / 15
        b = round(v, 2)
        print("Final percentage : " + str(b) + "%")
        print(">>>>>>>><<<<<<<<")
def javascript():
    score = 0
    import mysql.connector
    xyz = mysql.connector.connect(host="localhost", user="savan", passwd="savan4141", database="savan")
    mycursor = xyz.cursor()
    mycursor.execute("select * from java")
    for i in mycursor:
        print('\n>>>>>>>>><<<<<<<<<')
        print(i[0])
        print(i[1])
        print('(A) ' + i[2])
        print('(B) ' + i[3])
        print('(C) ' + i[4])
        print('(D) ' + i[5])

        a = input("\nyour choice")

        if a.capitalize() == i[6]:
            print("correct answer")
            score = score + 1
        else:
            print("Wrong answer")
            print("Right Answer : " + i[7])
            score = score - 0.25

    print("\n>>>>>>>><<<<<<<<")
    print('Final score=', score, '/15')
    if score <= 0:
        print("Final percentage : 0%")
        print(">>>>>>>><<<<<<<<")
    else:
        v = (float(score)) * 100 / 15
        b = round(v, 2)
        print("Final percentage : " + str(b) + "%")
        print(">>>>>>>><<<<<<<<")
def con():
   print("\n\t\t\t\t\t\t\t\t\t>>>>>>>>>>>>>>><<<<<<<<<<<<<<")
   print('\n\t\t\t\t\t\t\t\t\t\t PRESS 1 Main Menu ')
   print('\t\t\t\t\t\t\t\t\t\t PRESS 2 Exit\n')
   f = int(input("Enter your choice : "))
   if f == 1:
      switch()
   else:
      exit(1)


def start(a):

    print("                                   >>>>>>>>>>>Start Quiz<<<<<<<<<<\n")
    print("                                           press 1 C\n")
    print("                                           press 2 C++\n")
    print("                                           press 3 Java\n")
    print("                                           press 4 Python\n")
    print("                                           press 5 Php\n")
    print("                                           press 6 JavaScript\n")

    a = int(input("Enter Your Subject : "))



    if a==1:
        c()
        con()
    elif a==2:
        cplus()
        con()
    elif a==3:
        java()
        con()
    elif a==4:
        python()
        con()
    elif a==5:
        php()
        con()
    elif a==6:
        javascript()
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

          if n == 1:
             start(1)
          elif n == 2:
             print("This Project created by Kailash Prajapati & Savan Prajapati in 3rd semester.")
             con()
          elif n == 3:
             print("if user pick right answer so user get 1 point and if user pick Wrong answer so user lose 0.25 point.")
             con()
          elif n == 4:
             exit(1)
          else:
             print("Enter Right choice")

if __name__ == "__main__":
      switch()

