class House:
    """ 
    This is the parent class. This class takes all the input from the user 
    """

     # Create __init__ method 
    # Set eight attributes place, bathrooms, num_bedrooms, location, price, house_type, condition
    def __init__(self, name =str, place = str,  num_bedrooms = int, location = str, price = float, house_type = str, condition = str):
        self.place = place
        self.num_bedrooms = num_bedrooms
        #self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.house_type = house_type
        self.condition = condition
        self.name = name
        
    # In this function we will get input from the user
    def house_info(self):
        self.name = str(input("What is your name: "))
        self.place = str (input(f'Hello {self.name}, what place in Maryland do you want to buy a house? '))
        self.location = str.lower(input(' Is your House located in the suburbs or the city ? : '))
        self.house_type = str.lower(input(' What type of house are you looking for? Condo or Single House ? : '))
        self.condition = str.lower(input('What condition of the house are you looking for: '))
        self.num_bedrooms = int(input('How many bedrooms do you want in your house? '))
        
        return self.location, self.house_type
        
        
class dwelling(House):
    """ 
    This is the subclass. Its takes all the attributes from House class 
    Calculates the total estimated house price
    
    """
    #We will call the House class in the init method
    def __init__(self, name, place,  num_bedrooms = int, location = str, price = float, house_type =str, condition = str):
        super().__init__(name, place,  num_bedrooms = int, location = str, price = float, house_type =str, condition = str)
  
    #Calculate the house price based on the location
    def location_estimator(self):
        suburbs = 500_000 
        city = 650_000 
        
        if self.location == "suburbs":
            self.price = suburbs
        elif self.location == "city":
            self.price = city
    
            
        return self.price
    
    #Calculate the house price based on the home type
    def house_type_estimator (self):
        condo = 10000
        single_house = 50000
        if self.house_type == "condo":
            self.price += condo
        elif self.house_type == "single house":
            self.price += single_house
            
        return self.price
    
    #Calcualte the house price based on the condition of the house
    def condition_estimator (self):
        good = 100000
        excellent = 20000
        
        if self.condition == "good":
            self.price += good
            
        elif self.condition == "excellent":
            self.price += excellent
            
        return self.price
    
    #Calculate the house price based on the number of bedrooms 
    def bedroom_estimator (self):
        two_bed = 5000
        three_bed = 10000
        
        if self.num_bedrooms <= 2:
            self.price += two_bed
            
        elif self.num_bedrooms > 2 :
            self.price += three_bed
            
        return self.price
              
    #Calculate the house tax based on the total price of the house    
    def housing_tax(self):
        
        total = float(self.price*1.06)
        
        return f'Your taxes for your house at  is 6% the actual price is: ${total}'
    

 # main() function print out all the methods       
def main():  
    """ 
    Prints all the functions
    """
   
    print(housing_boston.house_info())
    
    print(housing_boston.location_estimator())
    print(housing_boston.house_type_estimator())
    print(housing_boston.condition_estimator())
    print(housing_boston.bedroom_estimator())
    print(housing_boston.housing_tax())
  
    
        
#Create instance of House class and Dwelling Class
#Call the main function
if __name__ =='__main__':
    """
    Set instances of House and dwelling class and assign them to a value
    call the main function
    
    """
    housing_boston = dwelling(name = str, place = str, num_bedrooms = int, location = str, price = float,  condition = str)
    housing_location_estimator = House(name = str, place = str, num_bedrooms = int, location = str, price = float)
    main()
