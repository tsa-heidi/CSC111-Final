## Heidi Tsang
## Final Project

######## make car list a helper function
import random
from graphics import*
class Car:
    def __init__(self, x, y, speed):
        '''take x, y, speed, and return lists of moving cars
when called'''
        self.part_lst = []
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue  = random.randint(0,255)
        color = color_rgb(red,green, blue)
        self.speed = speed
        
        
        # creating parts of the car
        body = Rectangle(Point(x-40, y-20),Point(x+40, y+20))
        
        if speed > 0: ##going to the right
            head = Circle(Point(x+40, y),20)
            back = Polygon(Point(x-40, y-20), Point(x-45, y-15),Point(x-45, y+15), Point(x-40, y+20))
        else:
            head = Circle(Point(x-40,y),20)
            back = Polygon(Point(x+40, y-20), Point(x+45, y-15),Point(x+45, y+15), Point(x+40, y+20))
        # wheels
        wheel1 = Circle(Point(x-20, y+20), 10)
        wheel2 = wheel1.clone()
        wheel2.move(40,0)

        # top
        top = Oval(Point(x-40, y-40), Point(x+40, y))

        # windows
        window1 = Rectangle(Point(x-25, y -30), Point(x+25, y-15))
        window2 = Rectangle(Point(x-5, y-30), Point(x+5, y-15))

        #set colors
        wheel1.setFill("black")
        wheel2.setFill("black")
        wheel1.setOutline("black")
        wheel2.setOutline("black")
        window1.setOutline(color)
        window1.setFill("grey")
        
        # add the parts to list
        self.part_lst.append(back)
        self.part_lst.append(top)
        self.part_lst.append(head)
        self.part_lst.append(body)
        self.part_lst.append(wheel1)
        self.part_lst.append(wheel2)
        self.part_lst.append(window1)
        self.part_lst.append(window2)

        for part in self.part_lst:
            if part != window1 and part!= wheel1 and part!= wheel2:
                part.setFill(color)
                part.setOutline(color)
        
    def draw(self, window):
        '''take window , output is drawing of the cars in window'''
        for parts in self.part_lst:
            parts.draw(window)

    def getPosition(self):
        ''' get the center position of the tail of the fish'''
        position = self.part_lst[2].getCenter()
        return position
    def getx(self):
        '''return the x position of a point'''
        p = self.getPosition()
        x =  p.getX()
        return x
    def gety(self):
        '''return the y position of a point'''
        p = self.getPosition()
        y =  p.getY()
        return y
        
    def move(self, win_width):
        '''take the window width and move the cars by small amount, cars will reappear from the other side when exit from one side'''
        position = self.getPosition()
        x = position.getX()

        if x > win_width+250:
            for part in self.part_lst:
                part.move(-1*(win_width+250),0)
        elif x < 0 -250 :
            for part in self.part_lst:
                part.move(win_width+250,0)
        else:
            for part in self.part_lst:
                part.move(self.speed, 0)
        
class Banner:
    def __init__(self, lives, scores):
        '''take the countings of lives and scores to create a text box that keep track of the changes'''
        self.lives = lives
        self.scores = scores
        self.text = "lives = %(life)d, scores = %(count)1d" %{"life": self.lives, "count": self.scores}
        self.banner = Text(Point(250, 50), self.text)
        
    def banner_draw(self, window):
        '''input window, output drawing of banner in window'''
        self.banner.draw(window)
    def update(self, up_lives, up_scores):
        '''take updated lives and scores to update the banner'''
        if up_lives < 1:
            self.text = "The prince is dead!"
            self.banner.setText(self.text)
        elif up_scores < 3:
            self.text = "lives = %(life)d, scores = %(count)1d" %{"life": up_lives, "count": up_scores}
            self.banner.setText(self.text)
        elif up_scores == 3 :
            self.text = "The curse is broken!"
            self.banner.setText(self.text)
        
        

        
def road(win_height, win_width, window):
    '''draws the road and streets'''
    up_road = Rectangle(Point(0,0), Point(win_width, win_height/4))
                                                    
    down_road = Rectangle(Point(0,win_width), Point(win_width, 3*win_height/4))
    street = Rectangle(Point(0, win_height/4), Point(win_width, 3*win_height/4))
    yellow_line = Rectangle(Point(0, win_height/2+8), Point(win_width, win_height/2-8))
    yellow_line.setFill("gold")
    street.setFill("dim grey")
    down_road.setFill("forest green")
    up_road.setFill("forest green")
    street.draw(window)                         
    up_road.draw(window)
    down_road.draw(window)
    yellow_line.draw(window)
                          
def car_lst(x, y, speed):
    '''create lists of cars'''
    car_lst = []
    for i in range(3):
        car = Car(i*x,y,speed)
        car_lst.append(car)
    return car_lst
    
        
def frog_move(image, win_width, window, scores, original_po):
    '''move the frog according to location of user's click, return the new position and new score'''
    
    p = image.getAnchor()   
    if p.getY() < win_width/4-20:
        scores +=1
        image.move(0, original_po.getY()-p.getY())

    click_frog = window.checkMouse()
    if click_frog != None:
        y_click = click_frog.getY()
       
        # if user click below road, frog move back
        if y_click > 3*win_width/4:
            image.move(0, 40)
            p = image.getAnchor()
            
        # if user click above road, from move up
        elif y_click < win_width/4:
            image.move(0, -40)
            p = image.getAnchor()
    return p, scores


    
def main():
    
#### set up the initial window
    width = 500
    height = 500
    win = GraphWin("game", width, height)
    road(height, width, win)

    # create lists of cars
    speed = 2
    car1_lst = car_lst(width/2, height/3, speed)
    car2_lst = car_lst(width/2, 2*height/3, -speed)    
    for car in range(len(car1_lst)):
        car1_lst[car].draw(win)
        car2_lst[car].draw(win)
    
    instruction = Text(Point(width/2, 25), "The prince is cursed, cross the road to get the magic potions!")
    instruction.draw(win)
    frog_image = Image(Point(width/2, 7*height/8), "frog_king2.png")
    potion = Image(Point(width/2, 100), "potion1.png")
    potion.draw(win)
    frog_image.draw(win)

#### interactive and moving features
    scores = 0
    lives = 3
    original_po = frog_image.getAnchor()
    banner = Banner(scores, lives)
    banner.banner_draw(win)
    while lives > 0 and scores < 3:
        ## make the cars move and get their position
        car_po = []
        for car1 in car1_lst:
            car1.move(width)
            cp = car1.getPosition()
            car_po.append(cp)
        for car2 in car2_lst:
            car2.move(width)
            cp2 = car2.getPosition()
            car_po.append(cp2)
        # check if frog is hit by car
        p, scores = frog_move(frog_image,width, win, scores, original_po)
        p_x1 = p.getX()-40
        p_x2 = p.getX()+40
        p_y1 = p.getY()-40
        p_y2 = p.getY()+40
        for point in car_po:
            car_x = point.getX()
            car_y = point.getY()
            #if the frog hit a car, move back to original place and count = 0, life-1
            if (p_x1<car_x<p_x2 and p_y1<car_y<p_y2): #or (p_x1<car_x<p_x2 and p_y1<car_y<p_y2):
                lives -=1
                frog_image.move(0, original_po.getY()-p.getY())
        banner.update(lives, scores)
    #change banner according to result
    if scores > 2:
        frog_image.undraw()
        prince = Image(Point(width/2, 7*height/8), "prince.png")
        prince.draw(win)        
    elif lives <1:
        banner.update(lives, scores)
        frog_image.undraw()
        grave = Image(Point(width/2, 7*height/8), "grave.png")
        grave.draw(win)



main()


