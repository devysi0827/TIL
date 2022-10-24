n = int(input())
five_bags = int(n//5)
reminders = n - five_bags*5
if reminders %3 == 0:
    print(five_bags+int(reminders//3))
else :
    check = 0
    while five_bags >0:
        five_bags -= 1
        reminders += 5
        if reminders % 3 == 0:
            print(five_bags + int(reminders // 3))
            check = 1
            break
    if check == 0:
        print(-1)