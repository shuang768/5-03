import sys
def question():
  q=input("what is your multiple choice question\n")+'\n'
  a="a)"+input("what is the answer for choice a\n")+'\n'
  b="b)"+input("what is the answer for choice b\n")+'\n'
  c="c)"+input("what is the answer for choice c\n")+'\n'
  d="d)"+input("what is the answer for choice d\n")+'\n'+'\n'
  cc=input("what is the correct answer a, b, c or d\n")
  if cc!='a' and cc!='b' and cc!='c' and cc!='d':
    print('must have a correct answer', file=sys.stderr)
    exit()
  name=input("what name do you want your file for your question called\n")
  filehandle = open(name,'w')
  filehandle.write(q+a+b+c+d+cc)
  filehandle.close()
  print("your file is called",name)
def answer():
  name=input("which question file do you want?")
  inFile = open(name, 'r')
  line = inFile.readline()
  print ("what is the answer for",line.strip('\n'))
  while line != '\n':
    line = inFile.readline()
    print (line.strip('\n'))
  line = inFile.readline()
  inFile.close()
  an=input("what is your choice?\n")
  if an!=line:
    print("your answer is wrong, the correct answer is",line, '\n')
    menu()
  else:
    print("correct answer")
    menu()
def menu():
  task=0
  while True:
    try:
      print("proceed or ask another question")
      print("1- answer question")
      print("2- input another question")
      print("0- exit")
      task=int(input("enter your choice"))
    except ValueError:
        print("Please enter a number")
        continue
      
    else:
      if task==1:
        answer()
        break
      elif task==2:
        question()
        break
      elif task==0:
          print("exit")
          break
      else: 
        print("please enter a valid number")
        continue
question()
menu()