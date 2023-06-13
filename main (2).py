#functions go here
def yes_no(question):

  while True:
    response = input(question).lower()

    if response == "yes" or response =="y":
      return "yes"
    elif response == "no" or response == "n":
        return "no"
    else:
      print("please enter yes or no")

#main routine goes here
want_instructions = input("do you want to read the instructions?").lower()
print(want_instructions)

if want_instructions == "yes":
  print("Instructions go here")
elif want_instructions == "no":
  pass
else:
  print("please answer yes or no")

print("we are done")