print("Welcome to the Quiz!")

playing=input("Do you want to play?")

score=0

if playing.lower()!="yes":
    quit()
print("okay lets play")

answer=input("What does CPU stand for? ")
if answer.lower()=="central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer=input("What does MAN stand for? ")
if answer.lower()=="metropolitan area network":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer=input("What does CAD stand for? ")
if answer.lower()=="computer aided design":
    print("correct!")
    score += 1
else:
    print("Incorrect")

answer=input("What does OMR stand for? ")
if answer.lower()=="optical mark reader":
    print("correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + " %")