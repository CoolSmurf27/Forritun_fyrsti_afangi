t = 0
number_of_players = 0

while number_of_players < 2:
    number_of_players = int(input())
for i in range(number_of_players):
    number = int(input())
    t += number
print("The sum of all contributions is " + str(t))
print("When " + str(t) + " is divided by " + str(number_of_players) + ", the remainder is " + str(t % number_of_players))
print("Player " + str(t % number_of_players) + " is the winner!")

