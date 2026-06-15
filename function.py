#def function_name():
 #   return "hello"
#datafromfunction = function_name()
#print(datafromfunction)


#def                     =>Function keyword [define]
#say_hello()             =>Function name
#name                    =>parameter
#print(f"hello{name}")   =>task
#say_hello("yazan")      =>yazan is the argument

#a, b, c = "leen", "yazan", "Taim"
#def say_hello(name):
 #   print(f"hello {name}")

#say_hello("yazan")

#******

#def addition(n1, n2):

 #   if type(n1) != int or type(n2) != int:
  #      print("only integer allowed")

   # else:
    #print(n1 + n2)

#addition(20 , 7)

#******

#def full_name(first, middle, last):
 #   print(f"hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")
#full_name("leen", "yazan", "shorman")

#******

#def say_hello(*peoples):

 #  for name in peoples:
  #     print(f"hello {name}")

#ay_hello("leen", "ahmed", "rami", "awos")

#******

#def say_hello(name, age, country = "unknown"):
   # print("hello {name} your age {age} and your country is {country}")

#say_hello("sameh", "23",)

#******

#myskills = {
 #   "html": "80%",
  #  "css": "60%",
   # "js": "50%"
#}

#def show_skills(**skills):#**dictionary
 #   print(type(skills))

  #  for skills, value in skills.items():
   #     print(f"{skills} => {value}")

#show_skills(**myskills)

#scope**********************************

#def one():
 #   global x
 #  x = 2
 #    print(f"print variable from function scope {x}")

#def two():
 #   x = 10
 #  print(f"print variable from global scope {x}")

#one()
#print(f"print variable from global scope {x}")
#two()
#print(f"print variable from global scope after one function is called{x}")

#*****************************************************************************
#recursion function

#def cleanword(word):
    
#    if len(word) == 1:
#        return word
    
#    print(f"print start function {word}")
    
#    if word[0] == word[1]:
        
#        print(f"print before condition {word}")
#        return cleanword(word[1:])
    
#    print(f"print before return{word}")
    
#    return word[0] + cleanword(word[1:])

#print(cleanword("wwwoooorrrldd"))

#*********************************************************************
#lambda function

#def say_hello(name, age): return f"hello {name} your age is: {age}"

#hello = lamba name, age:  f"hello {name} your age is: {age}"

#print(say_hello("leen", 20))
#print(hello("leen", 20))

#print(say_hello._name_)
#print(hello._name_)
#print(type(hello))

#***************************************************************************
#file handling

#file = open("D:\python\Files\leen.txt")

#import le
#main current working directory

#print(le.getcwd())

#directory for the opened file
#print(le.path.dirname(le.path.abspath(_file_)))

#le.chdir(le.path.dirname(le.path.abspath(_file_)))
#print(le.getcwd())
#file = open("leen.txt")


#read file
#myfile = open("D:\python\Files\leen.txt", "r")
#print(myFile) #file data object
#print(myFile.name)
#print(myFile.mode)
#print(myFile.encoding)

#print(myFile.read())
#print(myFile.readline(10))
#print(type(myFile.readlines()))

#for line in myfile:
   #print(line)
   #if lin.startswith("07")
      #break
#myfile.close()

#write & append file

#myfile = open("D:\python\Files\leen.txt", "w")
#myFile.write("hello from python File")

#myList = ["leen\n", "ahmed\n", "rama\n"]
#myFile= open("D:\python\Files\leen.txt", "w")
#myFile.writelines(myList)

#myfile = open("D:\python\Files\leen.txt", "a") #append
#myFile.write("hello from python File")

#importantFile info

#myfile = open("D:\python\Files\leen.txt", "a")
#myFile.truncate(5) #byte num

#**************************************************

#x = [2, 4, 6, 7, ]
#if any(x):
 #   print("there is at least one element is true")# any is for all elements true 
#else:
 #   print(there no any true element is true)
#print(bin(100))#binary
#a = 1
#print(id(a))

#*********************************************************

#sum(iterable, start)
#a = [2, 4, 10, 30]
#print(sum(a))
#print(sum(a, 10))

#round(number, numofdigits)
#print(round(150.501))
#print(round(150.554, 2))

#range(start, end, step)
#print(list(range(0)))
#print(list(range(10)))
#print(list(range(0, 20, 2)))

#print()
#print("hello @ leen @ how @ are @ you")
#print("hello" , "leen" , "how" , "are" , "you", sep= "|")

#print("first line", end= "look its me end ")
#print("secound line")
#print("third line")


#with open("example.txt", "w", encoding = "utf-8") as file:
#    file.write("hi leen!, this is the first file for you" )

#with open("example.txt", "r", encoding = "utf-8") as file:
#    content = file.read()
#    print(content)

#**********************************************************************************

#def show_menu():
#    print("\n--- menu ---")
#    print("1. add task ")
#    print("2. show tasks")
#    print("3. delet task")
#    print("4. save tasks in file")
#    print("5. finish")

#tasks = []

#while True:
 #   show_menu()
  #choice = input("choice num:")
    #if choice == "1":
     #   task = input("enter task:")
      #  tasks.append(task)
       # print("the task added!")
        #print("current tasks:")
        ##   print(i, "-", t)

  #  elif choice == "2":
   #     for i, task in enumerate(tasks, start = 1):
    ##elif choice == "3":
      ##     num = input("enter the num of task to delete:")
        #    tasks.pop(num-1)
         #   print("task seleted!")
      #  except (ValueError, IndexError):
       ##elif choice == "4":
        #with open ("tasks.txt", "w", encoding = "utf-8") as file:
         #   for task in tasks:
          #      file.write(task + "\n")
       # print("task saved in file.")

    #elif choice == "5":
     #   print("good buy!")
      #  break
    #else:
     #   print("false, try again")

#//////////////////////////////////////////////////////////////////////

while True:
    print("\n--- calculator ---")
    num1 = float(input("enter num1:"))
    num2 = float(input("enter num2:"))

    print("choice operation:")
    print("1. addition.")
    print("2. subtraction.")
    print("3. multiplication")
    print("4. division")
    print("5. finish")

    choice = input("enter num of operation:")

    if choice == "1":
        print("the result:", num1 + num2)
    elif choice == "2":
        print("the result:", num1 - num2)
    elif choice == "3":
        print("the result:", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print("the result:", num1 / num2)
        else:
            print("error: It cannot be divided by zero.")
    elif choice == "5":
        print("good buy")
        break
    else:
        print("false choice.")