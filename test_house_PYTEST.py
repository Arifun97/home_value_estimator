import home_value
    #test_housing input
def test_housing_input():
    '''Testing that the House class has the correct parameters'''
    #Passed the argument in the house class
    home = home_value.House(name = 'Ari', place = 'Rockville', num_bedrooms = 6, location = 'suburbs',  condition = 'good', house_type='condo')
    #Assert the place to see if the place name is set correctly
    assert home.place == "Rockville", "The place may not have been set correctly"
    assert home.name == "Ari", "The name may not have been set correctly"
    assert home.house_type == "condo", "The house type may not have been set correctly"
    assert home.condition == "good", "The condition may not have been set correctly"
    assert home.num_bedrooms == 6, "The number of bedrooms may not have been set correctly"
    assert home.location == "suburbs", "The location may not have been set correctly"


def test_location_estimator():
    '''Testing that the dwelling class has the correct parameters'''
    #Passed the arguments in the dwelling class
    estimator = home_value.House( name= 'Ari', place='Rockville',  location = 'suburbs', price = 150_000)
    #Called the location_estimator()
    # estimator.location_estimator()
    #Assert the location to see if the location is set correctly
    assert estimator.price == 150_000, "The price type may not have been set correctly"
    
    
def test_condition_estimator():
    #Passed the argument in the dwellingclass
    condition = home_value.House( name = 'Ari', place = 'Rockville',  price = 250_000, num_bedrooms = 6, house_type='condo', location = 'suburbs',  condition = 'Good')
    #Called the condition_estimator method
    #Assert condition to see if the price is set correctly
    assert condition.price == 250_000, "The price may not have been set correctly"
