ticket_Num = input("Enter a six-digit ticket number: ")

digit1 = int(ticket_Num) // 100000
digit2 = (int(ticket_Num) // 10000) % 10
digit3 = (int(ticket_Num) // 1000) % 10
digit4 = (int(ticket_Num) // 100) % 10
digit5 = (int(ticket_Num) // 10) % 10
digit6 = int(ticket_Num) % 10

sum_first_three = digit1 + digit2 + digit3

sum_last_three = digit4 + digit5 + digit6

if sum_first_three == sum_last_three:
    print("Happy")
else:
    print("Ordinary")