from random import randrange
from Bee import Bee
from Flower import Flower
from Scenario import Scenario

#Main settings
w = h = 100
scenario = Scenario()

bees_quantity = 20
flowers_quantity = 4
current_generation=[]
field_height = 100
flowers_generation=[]
new_generation_flowers = []

def settings():
    size(w,h)
    
def setup():
    background(0)
    colorMode(HSB)
    global scenario
    scenario.draw()
    
def draw():
    pass

##############################################################################
###########################Cosas generales####################################
#Funciones generales


def binary_to_decimal( binary): 
    decimal, i= 0, 0
    binary = int(binary)
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal 

def polar_to_xy(flower):
    pass
  
def random_tests():
    for i in current_generation:
        i.flores_visitadas = flowers_generation
        i.distancia_recorrida = randrange(20,70)

    
    flowers_generation[0].polen_other_flowers = [flowers_generation[1], flowers_generation[2]]
    flowers_generation[1].polen_other_flowers = [flowers_generation[1], flowers_generation[2], flowers_generation[3]]
    flowers_generation[2].polen_other_flowers = [flowers_generation[0], flowers_generation[1], flowers_generation[2], flowers_generation[3]]
    flowers_generation[3].polen_other_flowers = [flowers_generation[3]]



##############################################################################
###########################Algoritmo para las abjetas#########################
#Seleccion Abejas

def bee_selection(current_generation):
    total_sum = 0
    for bee in current_generation:
        total_sum += bee.adaptability_function()

    for bee in current_generation:
        bee.normalized_score = bee.selection_score / total_sum
  
    i = 0
    probability_list = []

    for bee in current_generation: 
        probability_list.append((i, i + bee.normalized_score, bee))
        i += bee.normalized_score
  
    # Hacer N randoms en el rango de probabilidad
    selected_bees = []
    num = [0] * bees_quantity

    for i in range(bees_quantity):
        num[i] = randrange(101)/100
        #Buscar la abeja que está dentro de ese rango

    for item in num:
        for prob in probability_list:
            if item <= prob[1]:
                selected_bees.append(prob[2])
                break
   
    return selected_bees

new_gen =[]
#Crossover de abejas
def crossover(bees_to_cross,new_generation_bees):
  if(len(bees_to_cross)==0):
    global new_gen
    new_gen = new_generation_bees 
    return new_generation_bees
  else:
    bee_1 = bees_to_cross[0]
    bee_2 = bees_to_cross[1]
    print("bee1", bee_1.color)
    print("bee2", bee_2.color)
    
    slice_point = randrange(20)#El cromosoma es de 20 bits
    print("slice", slice_point)
    new_bee_1 = cromosoma_to_bee(bee_2.cromosoma[:slice_point] + bee_1.cromosoma[slice_point:])
    new_generation_bees.append(new_bee_1)
    print("new 1", bee_2.cromosoma[:slice_point] + bee_1.cromosoma[slice_point:])
    
    slice_point = randrange(20)
    print("slice2", slice_point)
    
    new_bee_2 = cromosoma_to_bee(bee_1.cromosoma[:slice_point] + bee_2.cromosoma[slice_point:])
    new_generation_bees.append(new_bee_2)
    print("new 2",  bee_1.cromosoma[slice_point:] + bee_2.cromosoma[:slice_point])
    crossover(bees_to_cross[2:], new_generation_bees)
    

#Cromosoma de abejas
def cromosoma_to_bee(cromosoma):
    second_search = binary_to_decimal(cromosoma[:6])
    path = binary_to_decimal(cromosoma[6:8])
    radio = binary_to_decimal(cromosoma[8:11]) 
    angle = binary_to_decimal(cromosoma[11:14]) 
    orientation = binary_to_decimal(cromosoma[14:17])
    color = binary_to_decimal(cromosoma[17:])
    
    print(color, orientation, angle, radio, path, second_search)
    bee= Bee(int(color), int(orientation), int(angle), int(radio), int(path), int(second_search))
    bee.cromosoma = bee.make_cromosoma()

    return bee

def mutation():
    pass

##############################################################################
###########################Algoritmo para las flores##########################

#Cruce de flores
def flower_selection_and_crossover():
    for flower in flowers_generation:
        print(len(flower.polen_other_flowers))
        random_index = randrange(len(flower.polen_other_flowers))
        flower_2 = flower.polen_other_flowers[random_index]
        cut_section = randrange(13)
        new_flower =  cromosoma_to_flower(flower.cromosoma[:cut_section] + flower_2.cromosoma[cut_section:])
  
    new_generation_flowers.append(new_flower)

def cromosoma_to_flower(cromosoma):
    quadrant = binary_to_decimal(cromosoma[:2])
    radio = binary_to_decimal(cromosoma[2:6]) 
    angle = binary_to_decimal(cromosoma[6:10]) 
    color = binary_to_decimal(cromosoma[10:])
    flower= Flower(int(color), int(radio), int(angle), int(quadrant))
    flower.make_flower_cromosoma()

    return flower

def main():
#primera generacion de abejas, totalmente random
    for i in range(bees_quantity):
        color = randrange(8)
        orientation = randrange(8)
        angle = randrange(8)
        radio = randrange(8)
        path = randrange(3)
        second_search = randrange(64)
        bee= Bee(color, orientation, angle, radio,path, second_search)
        bee.cromosoma = bee.make_cromosoma()
        current_generation.append(bee)
        print("BEE #: ", i)
        bee.to_string()

    print("\n")
    #primera generacion de flores
        
    for i in range(flowers_quantity):
        color_flower = randrange(8)
        angle = randrange(16)
        radio = randrange(16)
        quadrant = randrange(4)
        flower = Flower(color_flower, radio, angle, quadrant)
        flower.cromosoma = flower.make_flower_cromosoma()
        flowers_generation.append(flower)
        print("FLOWER #: ", i)
        flower.to_string()

    random_tests()
  
    generation_of_bees = bee_selection(current_generation)
    print("new gen \n")
    for bee in generation_of_bees:
        print(bee.to_string())
    crossover(generation_of_bees, [])
    for bee in new_gen:
        print(bee.to_string())
        
    print("FLOREEEEEEEEES")
    flower_selection_and_crossover()
    
    for flower in new_generation_flowers:
        flower.to_string()
        
    print(len(new_generation_flowers))
    
main()
