import smtplib
import random

num = eval(input("How many single friends want to join?\n"))
cpl = eval(input("How many couples want to join \n"))
cpl = cpl * 2
friends = [None]*num
couples = [None]*cpl
emails =[None]*num

count = 0
while (count < num):
    friends[count] = input("Enter name of single friend: ")
    emails[count] = input("Enter email of ", friends[count])
    count ++

#count = 0
#arr = 0
#while (count < cpl)
#    arr = [None]*2
#    arr[count] = input("Enter name of partner 1: ")
#    arr.append = input("Enter name of partner 2: ")
#    arr = arr + 1
#    count = count + 1

count = 0
while (count < cpl):
    couples[count] = input("Enter name of friend in a couple: ")
    emails.append = input("Enter email of ", couples[count])
    count ++

random.shuffle(friends)
random.shuffle(couples)

#test
for friend in friends:
    print(friend)

#smtpserver auth
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("youremailusername", "password")

#an jede email adresse einen namen schicken, beginnend mit namen aus couples
#email adressen beginnend mit single friends
#nicht so cool >> es muss immer mehr single friends geben als couple friends
#außerdem können alle leute aus couple array einander nix schenken...
count = 0
for email in emails:
    if (count <= cpl):
        msg = couples[count]
        server.sendmail("you@gmail.com", "target@example.com", msg)
        count = count + 1
    else:
        msg = friends[count]
        server.sendmail("you@gmail.com", "target@example.com", msg)
        count = count + 1
