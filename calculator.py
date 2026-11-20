import math
import random


def cat_comment(result):
   num = float(result)
   if num < 0:
      options = [
         "😾 why are you summoning negative vibes in here",
         "black cat: that number is as dark as my soul",
         "scared cat: did you anger the math gods or what?",
      ]
   elif num == 0:
      options = [
         "snarky cat: zero? bold choice. very minimalist of you",
         "grinning cat: you did all that work for nothing. literally",
         "laughing cat: calculator says: big round nothing, congrats",
      ]
   elif num > 1_000_000:
      options = [
         "laughing cat: okay rich, can I borrow like three of those?",
         "love cat: that number is bigger than my ego",
         "confused cat: you just broke the cat's tiny brain",
      ]
   else:
      options = [
         "really happy cat: look at you doing math and stuff",
         "happy cat: not bad, human, not bad at all",
         "snarky cat: the answer is fine, I'm still prettier",
      ]
   return random.choice(options)


def cat_react(answer):
   if answer > 0:
      print("😸")
   elif answer < 0:
      print("😿")
   else:
      print("😺")


print("welcome to my calculator!")
while True:
   print("what do you want to do?")
   print("1=add\n2=subtract\n3=multiply\n4=divide\n5=power\n6=square root\n7=round\n8=sin\n9=cos\n10=tan\n11=abs\n12=log10\n13=log")
   choice = input("type 1,2,3,4,5,6,7,8,9,10,11,12,or 13:")

   try:
      if choice == "6":
         answer = math.sqrt(float(input("enter a number:")))
      elif choice == "7":
         answer = round(float(input("give me a number:")))
      elif choice == "8":
         answer = math.sin(float(input("enter a number:")))
      elif choice == "9":
         answer = math.cos(float(input("enter a number:")))
      elif choice == "10":
         answer = math.tan(float(input("enter a number:")))
      elif choice == "11":
         answer = abs(float(input("enter a number:")))
      elif choice == "12":
         answer = math.log10(float(input("enter a number")))
      elif choice == "13":
         answer = math.log(float(input("enter a number")))
      elif choice in {"1", "2", "3", "4", "5"}:
         num1 = float(input("enter the first number:"))
         num2 = float(input("enter the second number:"))
         operations = {
            "1": lambda: num1 + num2,
            "2": lambda: num1 - num2,
            "3": lambda: num1 * num2,
            "4": lambda: num1 / num2,
            "5": lambda: num1 ** num2,
         }
         answer = operations[choice]()
      else:
         print("invalid choice")
         continue
      print("Answer:", answer)
      cat_react(answer)
      print(cat_comment(answer))
   except (ValueError, ZeroDivisionError):
      print("Please enter valid numbers.")

   if input("Do you want to go again? type yes or no:").lower() == "no":
      break
   print("let's go again!")
