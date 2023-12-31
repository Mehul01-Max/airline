import mysql.connector
from tabulate import tabulate
import csv
import os
con = mysql.connector.connect(host = 'localhost' ,
 user = 'root' ,
 passwd = 'OSO$m39{',
)
cursor = con.cursor()
loggedin = False
isAdmin =False
cursor.execute("create database if not exists flight_booking_system")
cursor.execute("use flight_booking_system")
cursor.execute("create table if not exists Available_flights(flight_no int NOT NULL PRIMARY KEY, Airline varchar(30), Departure varchar(30) , Arrival varchar(30) , Departure_time time, Departure_date date , Arrival_time time, Arrival_date date ,Price float, Available_seat int)")
cursor.execute("create table if not exists booking_details(ID bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, Passenger_Name varchar(30) , Booking_ID bigint, PNR_no bigint, Booked_by varchar(40) , flight_no int)")
cursor.execute("create table if not exists Customer_details(CUS_ID bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,Customer_name varchar(30) , Address varchar(100) , Phone_no bigint , email varchar(50))")
cursor.execute("create table if not exists Admin_details(Ad_ID bigint AUTO_INCREMENT NOT NULL PRIMARY KEY,Ad_name varchar(30) , Address varchar(100) , Phone_no bigint , email varchar(50))")
cursor.execute("insert ignore into Available_flights values(401 , 'AIR INDIA EXPRESS' , 'KOLKATA' , 'SURAT' , '11:20:00' , '2023-11-06' , '14:25:00' , '2023-11-06' , 5999, 155)")
cursor.execute("insert ignore into Available_flights values(402 , 'AIR INDIA' , 'MUMBAI' , 'KOLKATA' , '06:00:00' , '2023-11-05' , '08:40:00' , '2023-11-05' ,9227, 90) ")
cursor.execute("insert ignore into Available_flights values(403 , 'VISTARA' , 'NEW DELHI' , 'PARIS' , '13:45:00' , '2023-11-03' , '18:40:00' , '2023-11-03' ,27910,  55)")
cursor.execute("insert ignore into Available_flights values(404 , 'VISTARA' , 'LONDON' , 'MUMBAI' , '20:55:00' , '2023-11-04' , '11:45:00' , '2023-11-05' ,63357,  99)")
cursor.execute("insert ignore into Available_flights values(501 , 'INDIG0' , 'NEW DELHI' , 'MUMBAI' , '14:00:00' , '2023-11-03' , '16:20:00' , '2023-11-03' ,5357,  14)")
cursor.execute("insert ignore into Available_flights values(502 , 'INDIGO' , 'KOLKATA' , 'JAIPUR' , '08:15:00' , '2023-11-02' , '10:45:00' , '2023-11-02' ,8624,  65)")
cursor.execute("insert ignore into Available_flights values(601 , 'SPICEJET' , 'NEW DELHI' , 'DUBAI' , '19:15:00' , '2023-11-03' , '20:05:00' , '2023-11-03' ,13279,  5)")

cursor.execute("insert ignore into Admin_Details (Ad_name , Address , Phone_no , email)  values('Mehul Agarwal' , 'Hindmotor' , 9330562599 , 'agarwalmehul423@gmail.com')")
cursor.execute("insert ignore into customer_Details (customer_name , Address , Phone_no , email)  values('harshil Agarwal' , 'Hindmotor' , 6291771357 , 'harshilagarwal300@gmail.com')")

con.commit()
user = []
f = open('logindetails.csv' , 'w')
f.close()
f = open('consolation.csv' , 'w')
f.close()
with open('logindetails.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        user.append(row)

if user == []:
    pass
else:
    for i in user:
        user = i
        if i[-1] == 'Admin':
            loggedin = True
            isAdmin = True
            print('you are successfully logged as' , i[1],'(Admin)')
        elif i[-1] == 'Customer':
            loggedin = True
            print('you are successfully logged as' , i[1])

f.close()


def consolation_messages():
    if loggedin:
        display = []
        global user
        current_user = user[1]+"("+str(user[0])+")"
        with open('consolation.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                display.append(row)
        f.close()
        for i in display:
            if current_user == i[4]:
                print(i[-1])
                break
        with open("consolation.csv","r+") as r, open("output.csv","w") as f:
            writer=csv.writer(f)
            reader = csv.reader(r)
            for row in reader:
                if  current_user == row[4]:
                    pass
                else:
                    writer.writerow(row)
        os.remove('consolation.csv')
        os.rename('output.csv', "consolation.csv")

def Add_new_Flight():
    if isAdmin:
        flight_no = int(input('Enter the flight number: '))
        Airline = input('Enter the name of the Airline: ').upper()
        Departure = input('Enter the Departure city: ').upper()
        Arrival = input('Enter the Arrival city: ').upper()
        Departure_time = input('Enter Departure time(00:00:00 format): ')
        Departure_Date = input('enter the departure date(yy-mm-dd): ')
        Arrival_time = input('Enter Arrival time(00:00:00 format): ')
        Arrival_Date = input('enter the Arrival date(yy-mm-dd): ')
        Price = float(input('enter ticket price: '))
        Available_seat = int(input('Enter the Available_seats: '))
        sql = "insert ignore into Available_flights values(%s, %s , %s , %s , %s , %s , %s , %s , %s , %s)"
        values = (flight_no , Airline , Departure ,Arrival, Departure_time, Departure_Date , Arrival_time , Arrival_Date , Price , Available_seat)
        cursor.execute(sql  , values)
        con.commit()
        print('New flight is successfully added to the booking list')
    else:
        print('you are not a admin')

def Available_flights():
    cursor.execute('Select * from Available_flights where Available_seat <> 0') 
    display = cursor.fetchall()
    head = ['Flight No' , 'Airline' , 'Departure' , 'Arrival' , 'Departure time' , 'Departure Date' , 'Arrival Time' , 'Arrival Date' , 'Price' , 'Available Seat']
    print(tabulate(display , headers=head, tablefmt='grid'))
def create_CUS_ID():
    Account_Exist = False
    Name = input('Enter your Name: ')
    Address = input('Enter your Address: ')
    Phone_no = input('Enter your phone no: ')
    email = input('Enter your email id: ')
    
    cursor.execute('Select * from customer_details ')
    
    display = cursor.fetchall()
    for i in display:
        if email ==  str(i[4]) or Phone_no == int(i[3]):
            Account_Exist = True
    if Account_Exist:
        print('This details already exist in the database')
    else:
        sql = "insert into Customer_details (CUSTOMER_Name , Address ,  Phone_no  ,  email) values( %s , %s , %s, %s);"
        values = (Name , Address , Phone_no , email)
        cursor.execute(sql , values)
        con.commit()
        print('Your account is successfully created')
def login():
    global loggedin
    global user
    global isAdmin
    email = input('enter your email address: ')
    global cus_info
    cursor.execute('Select * from customer_details')
    display = cursor.fetchall()
    for i in display:
        if email ==  str(i[4]):
            cus_info = i
            print('you are successfully logged as' , i[1])
            loggedin = True
            isAdmin = False 
            user = i
            with open('logindetails.csv' , 'w' ) as f:
                writer = csv.writer(f)
                writer.writerow([i[0], i[1] , i[2] , i[3] , i[4],  'Customer'])
            f.close()
            break
        else:
            loggedin = False
            
    if loggedin == False:
        print('invalid credentials please try again or create a new account')
    
def Adminlogin():
    global loggedin
    global user
    global isAdmin
    email = input('enter your email address: ')
    global cus_info
    cursor.execute('Select * from Admin_details')
    display = cursor.fetchall()
    for i in display:
        if email ==  str(i[4]):
            cus_info = i
            print('you are successfully logged as' , i[1],'(Admin)')
            loggedin = True
            isAdmin = True
            user = i
            with open('logindetails.csv' , 'w' ) as f:
                writer = csv.writer(f)
                writer.writerow([i[0] , i[1] , i[2] , i[3] , i[4] ,  'Admin'])
            f.close()
            break
        else:
            loggedin = False
            isAdmin = False
    if loggedin == False:
        print('invalid credentials please try again or create a new account')
       
    
def bookings():
    global Booking_Id
    global user
    global isAdmin
    Available_flights()
    
    flight_no = input('Enter Flight number: ')
    if flight_no.isnumeric():
        flight_no = int(flight_no)
    else:
        print('invalid flight no')
    isflight = False
    passengers =[]
    passengers.clear()
    display_lst = []
    display_lst.clear()
    cursor.execute('Select * from Available_flights')
    display = cursor.fetchall()
    if loggedin:
        for i in display:
            if flight_no == i[0] and i[-1] != 0:
                head = ['Flight No' , 'Airline' , 'Departure' , 'Arrival' , 'Departure time' , 'Departure Date' , 'Arrival Time' , 'Arrival Date' , 'Price' , 'Available Seat']
                print(tabulate([i], headers=head, tablefmt='grid'))
                isflight = True
                total_seats = i[-1] 
        if isflight == True:
            while True:   
                no_of_tickets = input('Enter the number of tickets you what to buy(exit to stop the proccess): ')
                if no_of_tickets.isnumeric():
                    no_of_tickets = int(no_of_tickets)
                    break
                elif no_of_tickets.lower() == 'exit':
                    break
                else:
                    print('please enter a number')
                    
            if str(no_of_tickets).isnumeric():  
                if total_seats >= no_of_tickets:
                    for i in range(no_of_tickets):
                        Name = input('enter the name of passenger: ')
                        passengers.append(Name)
                    
                    cursor.execute('Select Booking_ID from Booking_details')
                    p = cursor.fetchall()
                    if p == []:
                        Booking_Id = 1000
                    else: 
                        Booking_Id = p[-1][0] + 1
                    for i in passengers:
                        
                        if isAdmin == False:
                            values = (i , Booking_Id , int(str(flight_no) + str(Booking_Id)) , user[1]+'('+str(user[0])+')' , flight_no )
                        elif isAdmin:
                            values = (i , Booking_Id , int(str(flight_no) + str(Booking_Id)) , user[1]+'(Admin('+str(user[0])+'))' , flight_no )
                        display_lst.append(list(values))
                    header = ['Name' , 'Booking ID' , 'PNR NO' , 'BOOKED BY' , 'Flight No']
                    print(tabulate(display_lst , headers=header, tablefmt='grid'))
                    
                    while True:
                        confirmer = input('do you want to proceed? (Y/N)')
                        if confirmer == 'Y' or confirmer == 'y':
                            for i in passengers:
                                sql = "insert into Booking_Details (Passenger_Name , Booking_ID,  PNR_no  ,  Booked_By , Flight_no) values( %s , %s , %s, %s ,%s);"
                                if isAdmin == False:
                                    values = (i , Booking_Id , int(str(flight_no) + str(Booking_Id)) , user[1]+'('+str(user[0])+')' , flight_no )
                                elif isAdmin:
                                    values = (i , Booking_Id , int(str(flight_no) + str(Booking_Id)) , user[1]+'(Admin('+str(user[0])+'))' , flight_no )
                                cursor.execute(sql , values)
                                con.commit()
                            seats_left = total_seats - no_of_tickets
                            sql = ('UPDATE Available_flights SET Available_seat = %s where flight_no = %s')
                            values = (seats_left , flight_no)
                            cursor.execute(sql , values)
                            con.commit()
                            print('you tickets has been successfully booked')
                            break
                        elif confirmer == 'N' or confirmer == 'n':
                            
                            break
                        else:
                            print('please type Y for yes or N for no')
                        
                else:
                    print('Not enough seats')
                
        else: 
            print('No flight match the criteria')
            
    else:
        print('Please login to book tickets')
        
def showBookings():
    global isAdmin
    global loggedin
    if loggedin:

        if isAdmin == False:
            sql = ("select * from booking_details where Booked_By = %s")
            values = (user[1]+'('+str(user[0])+')',)
            cursor.execute(sql , values)
        elif isAdmin == True:
            cursor.execute("select * from booking_details")
        display = cursor.fetchall()
        header = ['Name' , 'Booking ID' , 'PNR NO' , 'BOOKED BY' , 'Flight No']
        print(tabulate(display , headers=header, tablefmt='grid'))
    else:
        print('Account not logged in')
def cancel_booking():
    global isAdmin
    global loggedin
    if loggedin:
        while True:
            cancelled_passengers = []
            cancelled_passengers.clear()
            if isAdmin == False:
                sql = ("select * from booking_details where Booked_By = %s")
                values = (user[1]+'('+str(user[0])+')',)
                cursor.execute(sql , values)
            elif isAdmin == True:
                cursor.execute("select * from booking_details")
            display = cursor.fetchall()
            header = ['Name' , 'Booking ID' , 'PNR NO' , 'BOOKED BY' , 'Flight No']
            print(tabulate(display , headers=header, tablefmt='grid'))
            booked_by = user[1]+'('+str(user[0])+')'
            print('1.For cancelling individual tickets')    
            print('2.For cancelling all the tickets you booked together') 
            
            choice = input('Enter your choice: ')
            if choice.isnumeric():
                choice = int(choice)
            else:
                print('invalid choice')
                
            if choice == 1:
                Available = False
                name = input('enter the name of the person: ')
                
                pnr_no = input('enter PNR NO: ')
                if pnr_no.isnumeric():
                    pnr_no = int(pnr_no)
                else:
                    print('invalid pnr no')
                    break
                for i in display:
                    if isAdmin == False:
                        if i[1] == name and i[3] == pnr_no and i[4] == booked_by:
                            cancelled_passengers.append(i)
                            Available = True
                    elif isAdmin == True:
                        if i[1] == name and i[3] == pnr_no:
                            cancelled_passengers.append(i)
                            Available = True
                    header = ['Name' , 'Booking ID' , 'PNR NO' , 'BOOKED BY' , 'Flight No']
                print(tabulate(cancelled_passengers , headers=header, tablefmt='grid'))
                if Available:
                    while True:
                        confirmer = input('the above booking will be cancelled! the action is undo able do you what to cancel the ticket (Y/N)')
                        if confirmer == 'Y' or confirmer == 'y':
                            sql = 'DELETE FROM booking_details WHERE Passenger_Name = %s and PNR_no = %s'
                            values = (name , pnr_no)
                            cursor.execute(sql , values)
                            con.commit()
                            sql = ('Select available_seat from Available_flights where flight_no = %s' )
                            values = (int(cancelled_passengers[0][-1]) ,)
                            cursor.execute(sql , values)
                            display = cursor.fetchall()
                            sql = 'UPDATE Available_flights SET Available_seat = %s WHERE Flight_No = %s '
                            values = (int(display[0][0] + len(cancelled_passengers)) , cancelled_passengers[0][-1])
                            cursor.execute(sql , values)
                            con.commit()
                            print('your flight booking is cancelled sucessfully')
                            break
                        elif confirmer == 'N' or confirmer == 'n':
                            print('the ticket is not cancelled')  
                            break 
                        else:
                            print('Enter Y or N')
                else:
                    print('you have no tickets booked with given criteria')
            elif choice == 2:
                
                pnr_no = input('enter PNR NO: ')
                if pnr_no.isnumeric():
                    pnr_no = int(pnr_no)
                else:
                    print('invalid choice')
                available = False
                for i in display:
                    if i[3] == pnr_no and i[4] == booked_by:
                        cancelled_passengers.append(list(i))
                        available = True
                    
                header = ['Name' , 'Booking ID' , 'PNR NO' , 'BOOKED BY' , 'Flight No']
                print(tabulate(cancelled_passengers , headers=header, tablefmt='grid'))
                    
                if available == True:
                    while True:
                        confirmer = input('the above booking will be cancelled! the action is undo able do you what to cancel the ticket (Y/N)')
                        if confirmer == 'Y' or confirmer == 'y':
                            sql = 'DELETE FROM booking_details WHERE PNR_no = %s'
                            values = (pnr_no , )
                            cursor.execute(sql , values)
                            con.commit()
                            sql = ('Select available_seat from Available_flights where flight_no = %s' )
                            values = (int(cancelled_passengers[0][-1]) ,)
                            cursor.execute(sql , values)
                            display = cursor.fetchall()
                            sql = 'UPDATE Available_flights SET Available_seat = %s WHERE Flight_No = %s '
                            values = (int(display[0][0] + len(cancelled_passengers)) , cancelled_passengers[0][-1])
                            cursor.execute(sql , values)
                            con.commit()
                            print('your flight booking is cancelled sucessfully')
                            break
                        elif confirmer == 'N' or confirmer == 'n':
                            print('the ticket is not cancelled')  
                            break 
                        else:
                            print('Enter Y or N')
                else:
                    print('you have no tickets booked with given criteria')
                    break
                    
            break   
    else:
        print('Not logged in')

def cancel_flight():
    Available_flights()
    if isAdmin:
        
        flight_no = input('enter the flight to be cancelled: ')
        if flight_no.isnumeric():
            flight_no = int(flight_no)
        else:
            print('enter a valid flight number')
        sql = 'select * from Available_flights where flight_no = %s'
        values = (flight_no , )
        cursor.execute(sql , values)
        display = cursor.fetchall()
        head = ['Flight No' , 'Airline' , 'Departure' , 'Arrival' , 'Departure time' , 'Departure Date' , 'Arrival Time' , 'Arrival Date' , 'Price' , 'Available Seat']
        print(tabulate(display , headers=head, tablefmt='grid'))
        confirmer = input('Are you sure you want to cancel the flight?(this process cannot be undone)(y/n/exit)): ')
        if confirmer == 'y' or confirmer == 'Y':
            sql = 'DELETE FROM available_flights where flight_no = %s'
            values = (flight_no , )
            cursor.execute(sql , values)
            con.commit()
            consolation_message = 'the flight with flight no :' + ' ' + str(flight_no) + ' ' + 'has been cancelled! , your amount will be refunded to your back account! sorry for incovience caused'
            sql = 'select * from booking_details where flight_no = %s'
            values = (flight_no , )
            cursor.execute(sql , values)
            display = cursor.fetchall()
            with open('consolation.csv' , 'w' ) as f:
                writer = csv.writer(f)
                for i in display:
                    writer.writerow([i[0], i[1] , i[2] , i[3] , i[4], consolation_message])
            f.close()
            sql = 'DELETE FROM booking_details where flight_no = %s'
            values = (flight_no , )
            cursor.execute(sql , values)
            con.commit()
        elif confirmer == 'n' or confirmer == 'N':
            print('flight not cancelled!')
        elif confirmer.lower() == 'exit':
            print('you are back to main menu')
        else:
            print('enter a valid option')

def exit():
    print('The program is succesfully ended')
while True:
    consolation_messages()
    print('1.Available flights')
    if loggedin == False:
        print('2. Create your account')
        print('3. login')
        print('4.Admin login')
   
    if loggedin and isAdmin == False:
        print('5.Booking tickets')
        print('7.Cancel tickets')
    if loggedin:
        print('6.Show Booking details')
        
    if isAdmin:
        print('8.Add new flight details')
        print('9. cancel flights')
    if loggedin:
        print('10.log out')
    print('0.exit')  
    
    choice = input('enter your choice: ')
    if choice.isnumeric():
        choice = int(choice)
        if choice == 1:
            Available_flights()
        elif choice == 2 and loggedin == False:
            create_CUS_ID()
        elif choice == 3 and loggedin == False:
            login()
        elif choice == 4 and loggedin == False:
            Adminlogin()
        elif choice == 5 and loggedin and isAdmin == False:
            bookings() 
        elif choice == 6 and loggedin:
            showBookings()  
        elif choice == 7 and loggedin and isAdmin == False:
            cancel_booking()
        elif choice == 8 and isAdmin:
            Add_new_Flight()
        elif choice == 9 and isAdmin:
            cancel_flight()
        elif choice == 10 and loggedin: 
            f = open('logindetails.csv' , 'w')
            f.close()
            loggedin = False
            isAdmin = False
            print('you are successfully logged out')
            list(user).clear()
        elif choice == 0:
            exit()
            break
    else:
            print('invalid choice')
        
    
    
    
        
