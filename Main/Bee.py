class Bee():

  colors=[[164, 245, 66],[66, 236, 245],[245, 230, 66],[245, 66, 66],[209, 66, 245], [242, 12, 127],[12, 43, 242], [255, 128, 0]]  #8 colores

  orientations=["N","S", "E", "O", "NE", "NO", "SE", "SO"] #8 direcciones

  paths=["P", "A", "R"] # P:profundidad, A: anchura, R:random


  angles=[5, 15, 30, 45, 60, 75, 90, 95]

  radios=[5,15, 25,40,50, 75,85,100]

  #color 3 bits
  #orientation 3 bits
  #angle 3 bits.
  #radio  3 bits . 
  #path 2 bits
  #secondary_search 6 bits y max prob 63

  bin_lens = {
  "color": 3,
  "orientation": 3,
  "angle": 3,
  "radio": 3,
  "path": 2,
  "secondary_search": 6
  }

  def __init__(self,color, orientation, angle, radio,path, second_search):
    self.color = self.colors[color]
    self.orientation = self.orientations[orientation]
    self.angle = self.angles[angle]
    self.radio = self.radios[radio]
    self.path = self.paths[path]
    self.second_search = second_search
    self.flores_visitadas = []
    self.distancia_recorrida = 0
    self.selection_score = 0
    self.normalized_score = 0.0
    self.selection_range = []
    

  def to_string(self):
    print(" color: ", self.color, "\n", "orientacion: ", self.orientation, "\n", "angulo: ", self.angle, "\n", "radio: ", self.radio, "\n", "path: ", self.path, "\n", "prob segunda busqueda: ", self.second_search, "\n", "cromosoma", self.cromosoma, "\n")


  def convert_to_binary(self, gen_value, gen_type):
    bin_len= self.bin_lens[gen_type]
    return bin(gen_value)[2:].zfill(bin_len)
    


  def make_cromosoma(self):
    cromosoma =""
    cromosoma += self.convert_to_binary(self.second_search, "secondary_search")
    cromosoma += self.convert_to_binary(self.paths.index(self.path), "path")
    cromosoma += self.convert_to_binary(self.radios.index(self.radio), "radio")
    cromosoma += self.convert_to_binary(self.angles.index(self.angle), "angle")
    cromosoma += self.convert_to_binary(self.orientations.index(self.orientation), "orientation")
    cromosoma += self.convert_to_binary(self.colors.index(self.color), "color")
    
    return cromosoma
    
    
  #Funcion de adaptabilidad
  def adaptability_function(self):
    self.selection_score = float(len(self.flores_visitadas) / float(self.distancia_recorrida))*100
    return self.selection_score
