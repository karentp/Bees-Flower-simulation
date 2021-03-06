class Flower():

  colors=[[164, 245, 66],[66, 236, 245],[245, 230, 66],[245, 66, 66],[209, 66, 245], [242, 12, 127],[12, 43, 242], [255, 128, 0]]  #8 colores

  radios=[6, 12, 18, 25, 30, 37, 45, 50, 56, 65, 70,75,80,84,89, 94]

  angles=[0,6,12,18,24,30,36,42,48,54,60,66,72,78,84,90]



  bin_lens = {
  "color": 3,
  "angle": 4,
  "radio": 4,
  "quadrant": 2,
  }

  def __init__(self,color, radio, angle, quadrant):
    self.color = self.colors[color]
    self.angle = self.angles[angle]
    self.angle_original = self.angles[angle]
    self.radio = self.radios[radio]
    self.quadrant = quadrant + 1 
    self.polen_other_flowers = []
    self.transform_angle()
    #print("Angle",self.angle)
    
    
  def add_polen(self, flower):
    self.polen_other_flowers.append(flower)


  def convert_to_binary(self, gen_value, gen_type):
    bin_len= self.bin_lens[gen_type]
    return bin(gen_value)[2:].zfill(bin_len)
  
  def make_flower_cromosoma(self):
    cromosoma =""
    cromosoma += self.convert_to_binary(self.quadrant, "quadrant")
    cromosoma += self.convert_to_binary(self.radios.index(self.radio), "radio")
    
    #print("angulos", self.angles)
    #print("inidice", self.angles.index(self.angle_original))
    cromosoma += self.convert_to_binary(self.angles.index(self.angle_original), "angle")
    cromosoma += self.convert_to_binary(self.colors.index(self.color), "color")
    
    self.cromosoma = cromosoma
    return cromosoma

  def to_string(self):

    print(" color: ", self.color, "\n", "cuadrante: ", self.quadrant, "\n", "angulo: ", self.angle, "\n", "radio: ", self.radio,"\n", "Polen de que tiene",self.polen_other_flowers, "\n")

  def transform_angle(self):
    if self.quadrant == 1:
        self.angle = 90 + self.angle
    elif self.quadrant == 2:
        self.angle = 180 + self.angle
    elif self.quadrant == 3:
        self.angle = 270 + self.angle
        
