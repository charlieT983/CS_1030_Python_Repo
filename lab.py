# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix


#the print function below is not closed. the print function should look like this
#  print("Welcome to the Debugging Lab!")       
print("Welcome to the Debugging Lab!")       

name = input("Enter your name: ")
print("Hello " + name + "!" + " Let's calculate your test scores.")

# 88 is a literal (string)
scores = [85, 90, 78, 88, 92]

total = 0
for score in scores:         #forgot : at the end of the for loop
    total = total + score

average = total / len(scores)
print("Your average score is:", + average)     #didn't caoncatenate the average 

highest = 0
for s in scores:
    if s > highest:
        highest = s

print("Your highest score was:", + highest)