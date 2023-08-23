class Flight_Details:
    def __init__(self, flight_id,From,To,Price):
        self.flight_id= flight_id
        self.From= From
        self.To= To
        self.Price= Price
    
    def to_city(self,city):
        if (city.lower() == self.To.lower()):
            print("Flight ID: ", self.flight_id)
            print("From: ", self.From)
            print("Price: ", self.Price,"\n")

    
    def from_city(self, city):
        if ((city).lower()==  self.From.lower()) :
            print("Flight ID: ", self.flight_id)
            print("To: ", self.To)
            print("Price: ", self.Price,"\n")

        
    def to_from(self,from_city,to_city):
            if((from_city==self.From and to_city==self.To)):
                print('Flight ID:', self.flight_id )
                print ('From City', self.From,'\t','To City ', self.To ,'\t' ,'Price', self.Price,"\n")

def main():
    cities_dict = {'Bengaluru': 'BLR' ,  'Mumbai': 'BOM',  'Bhubaneswar' : 'BBI', 'Hyderabad' :'HYD' , 'Jabalpur' : 'JLR' }
    #Creating a list of objects for the different cities
    flights = [Flight_Details('AI161E90', 'BLR' ,'BOM', 5600), Flight_Details('BR161F91' ,'BOM' ,'BBI' ,6750),Flight_Details('AI161F99', 'BBI', 'BLR' ,8210) , Flight_Details('VS171E20' , 'JLR', 'BBI' ,5500) ,Flight_Details('AS171G30', 'HYD', 'JLR' ,4400),Flight_Details('AI131F49' ,'HYD', 'BOM' ,3499)]
    while True:
        print("1. Flights for a particular City\n")
        print("2. Flights From a city\n")
        print("3. Flights between two given cities\n")
        choice = int(input("Enter choice: \n"))
        if choice==1:
            inp = input("Enter City: \n")
            try:
                city = cities_dict[inp.capitalize()]
                for i in range(len(flights)) :
                    obj = flights [i]
                    obj.to_city(city)
            except KeyError:
                print("\nNo Flights Found\n")
            


        elif choice==2:
            inp = input("Enter City: ")
            try:

                city = cities_dict[inp.capitalize()]
                for j in range(len(flights)):
                    objj = flights[j]
                    objj.from_city(city)
            except KeyError:
                print('\n No Flight available')
                    
        elif choice==3:
            fromplace = input("\n Enter Source City:")
            toplace= input('\n Enter Destination City:')
            try:

                fromcity = cities_dict[fromplace.capitalize()]
                tocity   =cities_dict[toplace.capitalize()]
                for k in range ( len(flights)):
                    objk = flights[k]
                    objk.to_from(fromcity,tocity)
            except KeyError:
                print('\n No Fligths available ')
        
        flag = input("Do you wish to continue(yes/no) : ")
        if flag.lower()=="yes":
            pass
        else :
            break

main()




