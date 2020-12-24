class Scenario():
    def __init__(self):
        pass
        
    def draw(self, w,h, flowers_gen):
        self.draw_hive(w, h)
        self.draw_flowers(flowers_gen, h)
        
    def draw_hive(self, w, h):
        fill(217, 217, 39)
        ellipse(w/2,h/2,20,20)
    def draw_flowers(self, flowers_gen,h):
        for flower in flowers_gen:
            fill(flower.color[0], flower.color[1], flower.color[2])        
            ellipse((((h-50*flower.radio)/100)*cos(radians(flower.angle))),(((h*flower.radio)/100)*sin(radians(flower.angle))),3,3)
