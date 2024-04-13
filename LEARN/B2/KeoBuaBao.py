from random import randint

print("Nhap Keo, Bua, Bao: ")
player = input()
computer = randint(0, 2)

if computer == 0:
    computer = "Keo"
elif computer == 1:
    computer = "Bua"
else:
    computer = "Bao"
    
print("Your choose is: " + player)
print("Chosen for computer is: " + computer)


if player == computer:
    print("Draw")
elif (
    (player == "Keo" and computer == "Bao")
    or (player == "Bua" and computer == "Keo")
    or (player == "Bao" and computer == "Bua")
):
    print("You Win")
else:
    print("You Lose")
