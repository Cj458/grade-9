
class Car:
    

    # instance variables
    def __init__(self, color, model, year, brand):
        """
        a  constructor is a special magic method which is called
        when your an object is created and it initializes the data
        for that object. 
        
        """
        self.color = color
        self.model = model
        self.year = year
        self.brand = brand

    #class method
    def move(self):
        print('The car is moving')

    def stop(self):
        print('The car is stopped')

    def play_music(self, song):
        print(f'{song} is playing')

    def change_gear(self, int):
        print(f'Changing gear to {int}')

    def light_on_off(self):
        print('the lights are on')

#Objects -> instance
elite = Car('Red','elite', 2028, 'pac')
gq = Car()
ais = Car()


elite.play_music('skibidi')
gq.change_gear(2)