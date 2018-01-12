######################################################
## Internship @ KRC: DAY 2                          ##
## ANIMIKH AICH                                     ##
## RNS Institute of Technology, Bengaluru, India    ##
######################################################


#Problem 1: Find the volume of a sphere with radius r=5
from math import pi
print ("\nTo find the volume of a sphere with radius r=5")
r = 5   #radius is 5 meters
volume = pi*(3/4)*(r**3)
print('The Volume in meters is: %0.4f' %volume)

#Problem 2: Cover Price of Book = $24.95
#Bookstores get 40% discount.
#Shipping $3 for first copy and $0.75 for each additional copy
#Find total wholesale price of 60 copies
from math import ceil
print("\nTo find price of 60 copies")
cover_price = 24.95     #Cover Price = $24.95
disc_price = 0.60*cover_price   #Discounted Price is 40% Cover Price
ship_first_book = 3     #Shipping cost for 1st book
ship_rest_book = 0.75    #Shipping cost for rest books
final_cost = disc_price + ship_first_book   #Price for the first book
for i in range (1,60):                      #price for the rest of the books
    final_cost = final_cost + ship_rest_book + disc_price
print("The final cost of 60 books is: $%0.2f" %final_cost) #The value is rounded off

#Problem 3: leave home at 6:52 AM
#Run 1 mile easy pace (8:15 per mile)
#Run 3 miles fast pace (7:12 per mile)
#Run 1 mile easy pace (8:15 per mile)
print ("\nTo find the time at which he/she comes back home")
fast_pace = [0, 7, 12]      #Hours, Minutes, Seconds
easy_pace = [0, 8, 15]
leaves_home = [6, 52, 0]
time_taken = [0,0,0]
total_time = [0,0,0]
for i in range (0,3):
    time_taken[i] = easy_pace[i]*2+fast_pace[i]*3   #2 hours easy pace and 1 hour fast pace
time_taken = [i*2 for i in time_taken]              #For going and coming back
for i in range (0,3):                               #Calculate the total time from the time of departure
    total_time[i] = time_taken[i]+leaves_home[i]
for i in range (2,0,-1):                            #Convert back to Hours, Minutes, Seconds
    while total_time[i]>=60:
        total_time[i-1] += 1
        total_time[i] -= 60
print("The time of return is: {}:{}:{} AM".format(total_time[0],total_time[1],total_time[2]))


#Recursion Example 1:
print("\nThis is an example for recursion")
def countdown(n):
    if n<=0:
        print("Blast Off!")
    else:
        print(n)
        countdown(n-1)

countdown(5)

#Recursion Example 2:
def print_n(s, n):
    if n<=0:
        return
    else:
        print(s)
        print_n(s, n-1)

print_n("Animikh",7)
