class Star_Cinema:
   hall_list = []
   def __init__(self):
       pass
   def entry_hall(self,hall):
       self.hall_list.append(hall)
 
class Hall(Star_Cinema):
   def __init__(self,hall_no,rows,cols):
       self.seats = {}
       self.show_list = []
       self.rows=rows         
       self.cols=cols
       self.hall_no=hall_no
       super().__init__()
       self.entry_hall(self)
 
   def entry_show(self,id,movie_name,time):
       self.show_list.append((id,movie_name,time))
       self.seats[id]=[]
       for i in range(self.rows):
           col = []
           for j in range(self.cols):
               col.append(False)
           self.seats[id].append(col)
 
   @staticmethod
   def convertRowColToSeat(row,col):
       return chr(row+65) + str(col)
 
   @staticmethod
   def convertSeatToRowCOl(seat):
       return (ord(seat[0])-65, int(seat.replace(seat[0],'')))
 
   def book_seats(self,name,phone,id,list_row_col):
       for tup in self.show_list:
           if(tup[0] == id):
               buy_list = []
               for tup_row_col in list_row_col:
                   row = tup_row_col[0]
                   col = tup_row_col[1]
                   if row>=self.rows or col>=self.cols:
                       print("\n___________________________\n")
                       print(f"INVALID SEAT NO - {self.convertRowColToSeat(row,col)}. TRY AGAIN!")
                       print("___________________________\n\n")
                       return
               found = False
               for tup_row_col in list_row_col:
                   row = tup_row_col[0]
                   col = tup_row_col[1]
                   if self.seats[id][row][col]==True:
                       found=True
               if found == True:
                   print("\n________________________________\n")
                   print(f"THESE SEATS WERE BOOKED - ",end="")
                   for tup_row_col in list_row_col:
                       row = tup_row_col[0]
                       col = tup_row_col[1]
                       if self.seats[id][row][col]==True:
                           print(self.convertRowColToSeat(row,col),end=", ")
 
                   print("\n________________________________\n\n")
                   return
               for tup_row_col in list_row_col:
                   row = tup_row_col[0]
                   col = tup_row_col[1]
                   self.seats[id][row][col]=True
                   buy_list.append(self.convertRowColToSeat(row,col))
               print("\n##### TICKET BOOKED SUCCESSFULLY!! #####")
               print("__________________________________________________________________\n")
               print("NAME: ",name)
               print("PHONE NUMBER: ",phone)
 
               print(f"\nMOVIE NAME: {tup[1]}\t\t MOVIE TIME: {tup[2]}")
               print(f"TICKETS: ",end="")
               for i in buy_list:
                   print(i,end=" ")
               print(f"\nHALL: {self.hall_no}")
               print("\n__________________________________________________________________\n\n")
               return
       print("\n______________________________\n")           
       print("Id didn't match with any show!") 
       print("______________________________\n\n") 
       return
 
   def view_show_list(self):
       if len(self.show_list)==0:
           print("\n_______________________\n")
           print("NO SHOWS RUNNING TODAY")
           print("_______________________\n\n")
           return
       print("\n____________________________________________________________________________________\n")
       for show in self.show_list:
           # print(show)
           print(f"MOVIE NAME: {show[1]} \t\tSHOW ID: {show[0]} \t\tTIME: {show[2]}")
       print("____________________________________________________________________________________\n\n")
 
   def view_available_seats(self,id):
       for tup in self.show_list:
           if(tup[0] == id):
               print(f"\n\nMOVIE NAME: {tup[1]} \t\tTIME: {tup[2]}")
               print("X for already booked seats")
               print("__________________________________________________________________\n")
               for i in range (len(self.seats[id])):
                   for j in range(len(self.seats[id][len(self.seats[id])-1])):
                       if self.seats[id][i][j] == False:
                           print(self.convertRowColToSeat(i,j),end="\t\t")
                       else:
                           print("X",end="\t\t")
                   print()
               print("__________________________________________________________________\n\n")
               return
       print("\n______________________________\n")           
       print("Id didn't match with any show!") 
       print("______________________________\n\n") 
       return
 
star = Star_Cinema()
my_hall = Hall("A10",3,5)
my_hall.entry_show("ae123","Black Adam","Oct 26 2022 10:00 PM")
my_hall.entry_show("ae50","Superman","Oct 26 2022 8:00 PM")
# print(my_hall.convertRowColToSeat(2,5))
# print(star.hall_list,my_hall.show_list,my_hall.seats)
# my_hall.book_seats("ae123",2,[(2,1),(2,3)])
 
while True:
   print("1. VIEW ALL SHOWS TODAY")
   print("2. VIEW AVAILABLE SEATS")
   print("3. BOOK TICKET")
   a = int(input("ENTER OPTION: "))
   if a==1:
       my_hall.view_show_list()
   elif a==2:
       id=input("ENTER SHOW ID: ")
       my_hall.view_available_seats(id)
   elif a==3:
       name=input("ENTER CUSTOMER NAME: ")
       phone=input("ENTER CUSTOMER PHONE NUMBER: ")
       id=input("ENTER SHOW ID: ")
       n=int(input("ENTER NUMBER OF TICKETS: "))
       lst=[]
       for i in range(n):
           inp=input("ENTER SEAT NO: ")
           tup=my_hall.convertSeatToRowCOl(inp)
           lst.append(tup)
       my_hall.book_seats(name,phone,id,lst)
   else:
       break
 
print(my_hall.seats["ae123"])

