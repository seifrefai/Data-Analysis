import turtle
import time
import random



class game:


    WIDTH, HIGHT=500,500
    COLOR=['red','green','blue','beige','black','orange','pink','purple','cyan','brown']
    
    def __init__(self) -> None:
        racers = self.get_number_racers()   
        self.init_turtle()

        random.shuffle(self.COLOR)
        colors=self.COLOR[:racers]

        winner=self.race(colors,racers)
        print('\nWinner is: {}\n'.format(winner))


    
    def get_number_racers(self):
        while True:

            number=input('please provide the number of turtles for this race: ')

            if number.isdigit():
                racers = int(number)
                
                
            else:
                print('number was not a digit. please try again')
                continue

            if 2< racers <10:
                return racers
            else: 
                print('Number provided is not between 2 and 10. Try again, ')


    
    def init_turtle(self):
        screen=turtle.Screen()
        screen.setup(self.WIDTH, self.HIGHT)
        screen.title('Turtle Racing Game')
        

    
    def create_turtles(self,colors,racers):
        turtles=[]
        spacingx=self.WIDTH//(racers+1)
        for i,color in enumerate(colors):
            racer=turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.left(90)
            racer.penup()
            racer.setpos(-self.WIDTH//2+(i+1)*spacingx,-self.HIGHT//2+20)
            racer.pendown()
            turtles.append(racer)
        return turtles
        

        
    def race(self,colors,racers):
            turtles= self.create_turtles(colors,racers)
            while True:
                for racer in turtles:
                    distance= random.randrange(1,20)
                    racer.forward(distance)

                    x,y = racer.pos()
                    if y>= self.HIGHT //2 :
                        return colors[turtles.index(racer)]

if __name__=='__main__':
    game()
    print('Game Complete. Hope you Enjoyed :)')







