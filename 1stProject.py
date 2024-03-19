print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

question = ["What does CPU stand for? ", "What does GPU stand for? ", "What does RAM stand for? ", "What does PSU stand for? "]
answer = ["central processing unit", "graphics processing unit", "random access memory", "power supply"]

for i in range(len(question)):
    ans = input(question[i])
    if ans.lower() == answer[i]:
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

print("\nYou got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
