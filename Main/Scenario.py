class Scenario():
    def __init__(self):
        pass
        
    def draw(self, w,h, flowers_gen):
        self.draw_hive()
        self.draw_flowers(flowers_gen, h)
        
    def draw_hive(self):
        fill(217, 217, 39)
        ellipse(0,0,20,20)
        
    def draw_flowers(self, flowers_gen,h):
        for flower in flowers_gen:
            fill(flower.color[0], flower.color[1], flower.color[2])        
            ellipse((((h+230*flower.radio)/100)*cos(radians(flower.angle))),(((h+230*flower.radio)/100)*sin(radians(flower.angle))),7,7)
