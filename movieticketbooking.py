import datetime
users=[]
MovieListItems=[]
seats=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
bookings_list = []
class MovieList:
    def __init__(self, id, moviename, rating, price):
        self.movieId = id
        self.movieName = moviename
        self.rating = rating
        self.Price = price

class Bookings:
    def __init__(self, BookingID, userId, BookedAt,moviedetails):
        self.booking_id = BookingID
        self.userId = userId
        self.booked_at = BookedAt
        self.moviedetails= moviedetails
class Movie():
    booking_count = 0
    def __init__(self, id: int, Name: str, Email: str, Password: str):
        self.userID = id
        self.name = Name
        self.email = Email
        self.password = Password
    def hardCodedData(self):
        users.append(self)
        return users
    def validateLogin(self,email, password):
        for user in users:
            if user.email == email and user.password == password:
                return user
        return None
class movie_ticket_booking(Movie):
    def __init__(self, id, Name, Email, Password):
        super().__init__(id, Name, Email, Password)
        self.moviebook = []
    def Menu(self):
        Tilllogin = True
        while Tilllogin:
            print("\n------------------")
            print("Customer Menu")
            print("1. Display the Movie List")
            print("2. Movie Ticket Booking")
            print("3. Payment Option ")
            print("4. Booking History")
            print("5. Logout")
            choice = int(input("Enter your Choice: "))
            if choice == 1:
                grocery1 = MovieList(1, 'LEO', '5 OUT OF 5', '240')
                grocery2 = MovieList(2, 'MASTER', '5 OUT OF 5', '200')
                grocery3 = MovieList(3, 'BIGIL', '5 OUT OF 5', '150')
                MovieListItems.append(grocery1)
                MovieListItems.append(grocery2)
                MovieListItems.append(grocery3)

                for Movie in MovieListItems:
                    print("MovieId:",Movie.movieId)
                    print("MovieName:",Movie.movieName)
                    print("Rating:",Movie.rating)
                    print("Ticket_Price:",Movie.Price)
                    print('----------------------------------------------')
            if choice==2:
                while True:
                    print("Grocery List:")
                    for movie in MovieListItems:
                        print(movie.movieId, movie.movieName, movie.rating, movie.Price)
                    movie_id = int(input("Enter the ID of the item to add to cart (or 0 to stop adding): "))
                    if movie_id == 0:
                        break
                    print("Select Your Seats:")
                    print("__________________________________________")
                    c=0

                    for i in seats:
                        print(i,end=" ")
                        c=c+1
                        if c>5:
                            print("")
                            c=0
                    num=int(input("Enter selected Seat Number:"))
                    seats.remove(num)

                    selected_item = None
                    for movie in MovieListItems:
                        if movie.movieId == movie_id:
                            selected_item = movie
                            break

                    if selected_item is None:
                        print("Invalid item ID. Please try again.")
                    else:
                        cart_item = {
                            'movieId': selected_item.movieId,
                            'movieName': selected_item.movieName,
                            'Rating': selected_item.rating,
                            'Price': selected_item.Price
                        }
                        self.moviebook.append(cart_item)
                    mge=input("If you want to book Another Ticket(y/n):")
                    if mge.lower()=="n":
                        view_cart = input("Do you want to see the Booking History? (y/n): ")
                        if view_cart.lower() == "y":
                            if len(self.moviebook) == 0:
                                print("Your Booking is empty.")
                            else:
                                print("Your Booking:")
                                for item in self.moviebook:
                                    print("Movie ID:", item['movieId'])
                                    print("Movie Name:", item['movieName'])
                                    print("Rating:", item['Rating'])
                                    print("Price:", item['Price'])
                                    print('---------------------------------------------')

            if choice==3:
                 print("Payment Options:")
                 print("1. Card")
                 print("2. UPI")
                 print("3. Cash on Delivery")
                 payment_choice = int(input("Choose a payment option: "))
                 if payment_choice == 1:
                     print("Payment successful. Thank you for using card.")
                 elif payment_choice == 2:
                     print("Payment successful. Thank you for using UPI.")
                 elif payment_choice == 3:
                     print("Payment successful. Thank you for choosing Cash on Delivery.")
                 else:
                     print("Invalid payment option.")
                 booking_data = Bookings(self.booking_count, self.userID, datetime.datetime.now(), self.moviebook)
                 bookings_list.append(booking_data)
                 self.booking_count += 1

            if choice == 4:
                for booking in bookings_list:
                    print(f"Booking ID: {booking.booking_id}")
                    print(f"User ID: {booking.userId}")
                    print(f"Booked At: {booking.booked_at}")
                    for item in self.moviebook:
                        print("Movie Name:", item['movieName'])
                        print("Rating:", item['Rating'])
                        print("Price:", item['Price'])
                    print('---------------------------------------------')
            if choice==5:
                print("Logout Successfully")
                exit(0)

if __name__ == "__main__":
    app = Movie(1, "Raj", "ganesh@gmail.com", "raj1234")
    app.hardCodedData()
    app = Movie(2, "prasanth", "santh@gmail.com", "prasanth123")
    app.hardCodedData()
    app = Movie(3, "kalai", "kalai@gmail.com", "kalai123")
    app.hardCodedData()
    login_user = app.validateLogin("kalai@gmail.com", "kalai123")
    if  login_user:
        print("Login Successfully")
        user1=movie_ticket_booking(login_user.userID, login_user.name, login_user.email, login_user.password)
        user1.Menu()