class Bookmyshow:
    
    @staticmethod
    def menu():
        print("1-> SHOW THE SEATS: ")
        print("2-> BUY A TICKET: ")
        print("3-> STATISTICS: ")
        print("4-> TICKET INFO: ")
        print("5-> EXIT: ")

    @staticmethod
    def seats():
        #column_lst = []
        for x in range(row):
            row_lst = []
            for y in range(col):
                row_lst.append("S")
            column_lst.append(row_lst)
        return column_lst

    @staticmethod
    def show_the_seats():
        print("CINEMA:")
        print(" ", end="  ")
        for seat in range(1, col + 1):
            if seat <= 9:
                print(seat, " ", end="")
            else:
                print(f'{seat:}', "", end="")
        print()
        for k in range(row):
            if k <= 9:
                print(f'{k + 1:=2}', end=" ")
            else:
                print(k + 1, end=" ")
            for seat in range(col):
                print(column_lst[k][seat], "", end=" ")
            print()

    @staticmethod
    def percentage():
        per = (booked_seats / total_seats) * 100
        return per


if __name__ == '__main__':
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of seats in each row: "))
    column_lst = []
    total_seats = row * col
    ticket = Bookmyshow()
    ticket.seats()
    audience_lst = [[None for j in range(col)] for i in range(row)]
    booked_seats = 0
    ticket_price = 0
    if total_seats<61:
        total_income=total_seats * 10
    else:
        total_income=(total_seats * 10)-(row*col)
    row_no = 0
    col_no = 0

    c = 0
    while c == 0:
        ticket.menu()
        x = int(input())
        if x == 1:
            ticket.show_the_seats()
            vacant_seats = total_seats - booked_seats
            if vacant_seats == total_seats:
                print(" ", "ALL SEATS ARE VACANT")
            else:
                print(f"This seat number us Booked :( ")
            c = 0
        elif x == 2:
            seat_row = int(input("Enter the row number:"))
            if seat_row in range(1, row + 1):
                seat_col = int(input("Enter the column number:"))
                if seat_col in range(1, col + 1):
                    if column_lst[seat_row - 1][seat_col - 1] == "S":
                        row_no = seat_row
                        col_no = seat_col
                        if row * col < 61:
                            ticket_price = 10
                        elif seat_row <= int(row / 2):
                            ticket_price = 10
                        else:
                            ticket_price = 8
                        print(f"PRICE - ${ticket_price}")
                        confirmation = input("Yes for Booking and No for exit(Yes/No):")
                        person_dict = {}
                        if confirmation == "Yes":
                            person_dict['Name'] = input("ENTER NAME:")
                            person_dict['Gender'] = input("GENDER(M/F/O):")
                            person_dict['Age'] = int(input("YOUR AGE:"))
                            person_dict['Phone_no'] = int(input("YOUR PHONE NO.:"))
                            person_dict["Ticket_Price"] = ticket_price
                            column_lst[seat_row - 1][seat_col - 1] = "B"
                            booked_seats += 1
                        else:
                            continue
                        audience_lst[seat_row - 1][seat_col - 1] = person_dict
                        print("Your Ticket is successfully Booked")
                        print("\n")
                    else:
                        print("Seat is already Booked By someone")
                        print("\n")
                else:
                    print("Sorry,You Have entered invalid Seat Column")
                    print("  Seat col must be atmost:", col)
                    print("  Try again with valid data")
                    print("\n")
            else:
                print("Sorry,You Have entered invalid Seat Row")
                print("   Seat Row must be atmost:", row)
                print("  Try again with valid data")
                print("\n")
            c = 0

        elif x == 3:
            ticket.show_the_seats()
            print()
            print("Number of Purchased Ticket:", booked_seats)
            print("Percentage-", ticket.percentage())
            print("Current Income-", "$", ticket_price)
            print("Total Income-", "$", total_income)
            print()
            c = 0

        elif x == 4:
            r = int(input("enter which row you want to check"))
            c = int(input("enter which seat number you want to check"))
            if r in range(1, row + 1) and c in range(1, col + 1):
                if column_lst[r - 1][c - 1] != "B":
                    print("Seat is unocuupied U can book it")
                    print()
                    c = 0
                else:
                    person: None = audience_lst[r - 1][c - 1]
                    print("Name:", person["Name"])
                    print("Gender:", person["Gender"])
                    print("Age:", person["Age"])
                    print("Ticket Price:", person["Ticket_Price"])
                    print("Phone No:", person["Phone_no"])
                    print()
                    c = 0
            else:
                print("Invalid Entry please type valid row and col to check")
                print()
                c = 0
        elif x == 5:
            break