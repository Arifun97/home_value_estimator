from argparse import ArgumentParser
import sys


class House:
    def __init__(self, place, num_bedrooms, price):
        self.place = place
        self.num_bedrooms = num_bedrooms
        self.price = price
        
    def get_place(self):
        return f'Your house in {self.place} cost: ${self.price}'
    
    def housing_tax(self,state):
        return f'Your taxes for your house at {state} is 6% the actual price is: ${self.price*1.06}'


def parse_args(args_list):
    parser = ArgumentParser()
    parser.add_argument('place', type=str, help="Please enter the name of the place")
    parser.add_argument('state', type=str, help="Please enter state")
    parser.add_argument('num_bedrooms', type=int, help="Please enter the number of bedrooms")
    parser.add_argument('price', type=float, help="Please enter the price")
    args = parser.parse_args(args_list) 
    return args


def main():
    print(boston.get_place())
    print(boston.housing_tax(arguments.state))


if __name__ =='__main__':
    arguments = parse_args(sys.argv[1:]) 
    boston = House(arguments.place, arguments.num_bedrooms, arguments.price)
    main()
 
