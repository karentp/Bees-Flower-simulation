from random import randrange
from Bee import Bee
from Flower import Flower
from Scenario import Scenario
from Tree import Tree

#Main settings
w = h = 500
scenario = Scenario()
notes_generation = []

bees_quantity = 20
flowers_quantity = 200
current_generation=[]
field_height = 100
flowers_generation=[]
new_generation_flowers = []

def settings():
    size(w,h)
    
def setup():
    background(255)
    noStroke()
    global scenario
    
    #primera generacion de abejas, totalmente random
    for i in range(bees_quantity):
        color = randrange(8)
        orientation = randrange(8)
        angle = randrange(8)
        radio = randrange(8)
        path = randrange(3)
        #print("path", path)
        second_search = randrange(64)
        bee= Bee(color, orientation, angle, radio,path, second_search)
        bee.cromosoma = bee.make_cromosoma()
        current_generation.append(bee)
        #print("BEE #: ", i)
        #bee.to_string()

    print("\n")
    #primera generacion de flores
        
    for i in range(flowers_quantity):
        color_flower = randrange(8)
        angle = randrange(16)
        #print("angle random", angle)
        radio = randrange(16)
        #print("radio random", radio)
        quadrant = randrange(4)
        flower = Flower(color_flower, radio, angle, quadrant)
        flower.cromosoma = flower.make_flower_cromosoma()
        flowers_generation.append(flower)
        #print("FLOWER #: ", i)
        #flower.to_string()
    
def draw():
    
    main()
    scenario.draw(w,h, flowers_generation)
    print("NOTAS", notes_generation)

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
        notes_generation.append((total_sum)/(bees_quantity))

    for bee in current_generation:
        if(total_sum == 0):
            bee_normalized_score = 0.4
        else:
            bee.normalized_score = bee.selection_score / total_sum
  
    i = 0
    probability_list = []

    for bee in current_generation: 
        probability_list.append((i, i + bee.normalized_score, bee))
        i += bee.normalized_score
  
    # Hacer N randoms en el rango de probabilidad
    selected_bees = []
    #num = [0] * bees_quantity
    
    #print("Probabilistic list", probability_list)
    #num = randrange(101)/100
    #print("NUMBER", num)
    
    
    for i in range(bees_quantity):
        #num[i] = randrange(101)/100
        #Buscar la abeja que está dentro de ese rango
        num = float(randrange(101))/100
        #print("NUMBER", num)
        for prob in probability_list:
            #print("prueba", prob[1])
            if num <= prob[1]:
                #print("prob limite superior", prob[1])
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
    print("CRUCE")
    bee_1 = bees_to_cross[0]
    if len(bees_to_cross) <=1:
        bee_2 = current_generation[3]
    else:
        bee_2 = bees_to_cross[1]
    #print("bee1", bee_1.color)
    #print("bee2", bee_2.color)
    
    slice_point = randrange(20)#El cromosoma es de 20 bits
    #print("slice", slice_point)
    new_bee_1 = cromosoma_to_bee(bee_2.cromosoma[:slice_point] + bee_1.cromosoma[slice_point:])
    new_bee_1.set_parents(bee_1)
    new_bee_1.set_parents(bee_2)
    new_generation_bees.append(new_bee_1)
    #print("new 1", bee_2.cromosoma[:slice_point] + bee_1.cromosoma[slice_point:])
    
    slice_point = randrange(20)
    #print("slice2", slice_point)
    
    new_bee_2 = cromosoma_to_bee(bee_1.cromosoma[:slice_point] + bee_2.cromosoma[slice_point:])
    new_bee_2.set_parents(bee_1)
    new_bee_2.set_parents(bee_2)
    new_generation_bees.append(new_bee_2)
    #print("new 2",  bee_1.cromosoma[slice_point:] + bee_2.cromosoma[:slice_point])
    crossover(bees_to_cross[2:], new_generation_bees)
    

#Cromosoma de abejas
def cromosoma_to_bee(cromosoma):
    second_search = binary_to_decimal(cromosoma[:6])
    #print("SLICE SEARCH", cromosoma[:6])
    #print("SLICE PATH", cromosoma[6:8])
    path = binary_to_decimal(cromosoma[6:8])
    radio = binary_to_decimal(cromosoma[8:11]) 
    angle = binary_to_decimal(cromosoma[11:14]) 
    orientation = binary_to_decimal(cromosoma[14:17])
    color = binary_to_decimal(cromosoma[17:])
    
    #print(color, orientation, angle, radio, path, second_search)
    bee= Bee(int(color), int(orientation), int(angle), int(radio), int(path), int(second_search))
    bee.cromosoma = bee.make_cromosoma()

    return bee

def mutation(generation_to_mutate):
    cantidad_cambios = 4
    for i in range(cantidad_cambios):
        print("WENAS", bees_quantity)
        place_for_mutation =(randrange(bees_quantity), randrange(20))
        bee_to_change = generation_to_mutate[place_for_mutation[0]]
        new_cromosoma= bee_to_change.cromosoma
        if(new_cromosoma[place_for_mutation[1]] == "1"): #Flip the bit
            cromosoma_list = list(new_cromosoma)
            cromosoma_list[place_for_mutation[1]] = "0"
            new_cromosoma = "".join(cromosoma_list)

        else:
            #print("NEW CROMOSOMA",new_cromosoma[place_for_mutation[1]])
            #print("NEW CROMOSOMA",new_cromosoma)
            cromosoma_list = list(new_cromosoma)
            cromosoma_list[place_for_mutation[1]] = "1"
            new_cromosoma = "".join(cromosoma_list)
        
        #print("NEW CROMOSOMA", new_cromosoma)
        bee_mutated = cromosoma_to_bee(new_cromosoma) #abeja que mutó 
        #print("Abeja mutada", bee_mutated.cromosoma)
        bee_mutated.set_parents(bee_to_change.parents[0])
        bee_mutated.set_parents(bee_to_change.parents[1])
        new_gen[place_for_mutation[0]] = bee_mutated #reemplazar por la abeja mutada
        
        

##############################################################################
###########################Algoritmo para las flores##########################

#Cruce de flores
def flower_selection_and_crossover():
    for flower in flowers_generation:
        #print("flower1", flower.cromosoma)
        #print(len(flower.polen_other_flowers))
        
        if(len(flower.polen_other_flowers) == 0):
               flower.polen_other_flowers.append(flowers_generation[0])
               
        random_index = randrange(len(flower.polen_other_flowers))
        
        flower_2 = flower.polen_other_flowers[random_index]
        #print("flower2", flower_2.cromosoma)
        cut_section = randrange(13)
        #print("new flower part 1", flower.cromosoma[:cut_section])
        #print("new flower part 2", flower_2.cromosoma[cut_section:])
        new_flower =  cromosoma_to_flower(flower.cromosoma[:cut_section] + flower_2.cromosoma[cut_section+1:])
    
        new_generation_flowers.append(new_flower)


def cromosoma_to_flower(cromosoma):
    quadrant = binary_to_decimal(cromosoma[:2])
    radio = binary_to_decimal(cromosoma[2:6]) 
    angle = binary_to_decimal(cromosoma[6:10]) 
    color = binary_to_decimal(cromosoma[10:])
    flower= Flower(int(color), int(radio), int(angle), int(quadrant))
    flower.make_flower_cromosoma()

    return flower



##########################BÚSQUEDA#####################################

def travers_path(bee,tree):
    recorrido=[]
    #print("TREE 2")
    #tree.print_tree()
    #print("path", bee.path)
    if bee.path == 0: #profundidad
        recorrido = tree.Preorder(tree.root,[])
    
    elif bee.path == 1: #anchura
        recorrido = tree.LevelOrder(tree.root)
    else: #random
        pos = randrange(2)
        if (pos == 0):
            recorrido = tree.LevelOrder(tree.root)
        else:
            recorrido = tree.Preorder(tree.root, [])
    
    #print("RECORRIDO", recorrido)
   
    for flower in recorrido:
        if bee.color == flower.color:
            #polinizar y agregar polen a las flores
            flower.polen_other_flowers = bee.flores_visitadas
            bee.flores_visitadas.append(flower)
        else:
            probability = randrange(101)
            if probability <= bee.second_search:
                #visita la flor que no le gusta por probabilidad
                flower.polen_other_flowers = bee.flores_visitadas
                bee.flores_visitadas.append(flower)
    
    bee.distancia_recorrida = len(recorrido)
    print("DISTANCIA RECO", bee.distancia_recorrida)
    print("FLORES VISIT", len(bee.flores_visitadas))
        


def search_scope(bee, flower_generation):
    if (bee.orientation == "N"):
        inf_angle = 90 - bee.angle
        sup_angle = 90 + bee.angle
    elif (bee.orientation == "O"):
        inf_angle = 90 + bee.angle
        sup_angle = 180 + bee.angle
    elif (bee.orientation == "S"):
        inf_angle = 180 + bee.angle
        sup_angle = 270 + bee.angle
    elif (bee.orientation == "E"):
        inf_angle = 270 + bee.angle
        sup_angle = 90 - bee.angle
    
    if(bee.angle <=45):
        if (bee.orientation == "NE"):
            inf_angle =  bee.angle
            sup_angle = 90 - (45-bee.angle)
        elif (bee.orientation == "NO"):
            inf_angle = 90 + (45-bee.angle)
            sup_angle = 180 - (45-bee.angle)
        elif (bee.orientation == "SO"):
            inf_angle = 180 + (45-bee.angle)
            sup_angle = 270 - bee.angle
        elif (bee.orientation == "SE"):
            inf_angle = 270 + (45-bee.angle)
            sup_angle = 360 - (45-bee.angle)
    if(bee.angle >=45):
        if (bee.orientation == "NE"):
            inf_angle =  45+ bee.angle
            sup_angle = 360 - (bee.angle-45)
        elif (bee.orientation == "NO"):
            inf_angle = bee.angle
            sup_angle = 180 + (bee.angle-45)
        elif (bee.orientation == "SO"):
            inf_angle = 180 - (bee.angle-45)
            sup_angle = 270 - (bee.angle-45)
        elif (bee.orientation == "SE"):
            inf_angle = bee.angle
            sup_angle = 270 - (bee.angle-45)
    
    
    tree = Tree()
    for flower in flower_generation:
        if (flower.radio <= bee.radio):
            #print("RADIO ES MENOR")
            if(bee.orientation == "E" or (bee.orientation =="NE" and bee.angle <=45) or (bee.orientation == "SE" and bee.angle >= 45)):
                #print("casos especiales")
                #print("angulo de flor", flower.angle, " inf angle ", inf_angle, "sup angle ", sup_angle)
                if(flower.angle <= inf_angle and flower.angle >= sup_angle):
                    #print("entra especiales")
                    tree.insert(tree.root,flower)
                    #print("root1") 
            else:
                #print("orientacion")
                #print("angulo de flor", flower.angle, " inf angle ", inf_angle, "sup angle ", sup_angle)
                if(flower.angle >= inf_angle and flower.angle <= sup_angle):
                    #print("ENTRA")
                    tree.insert(tree.root,flower)
                    #print("root")
    #print("SALE")
    tree.print_tree()
    travers_path(bee,tree)

def main():
  
    #Busqueda
    global flowers_generation
    
    for bee in current_generation:
        search_scope(bee, flowers_generation)
        break
  
  
  
    bees_to_cross = bee_selection(current_generation)
    print("Bees to cross\n")
    for bee in bees_to_cross:
        #print(bee.to_string())
        pass
        
    crossover(bees_to_cross, [])
    
    print("New bees generation")
    for bee in new_gen:
        #print(bee.to_string())
        pass
        
    mutation(new_gen)
    
    print("New bees generation MUTATED")
    for bee in new_gen:
        #print(bee.to_string())
        pass
    
        
    print("FLOREEEEEEEEES")
    
    flower_selection_and_crossover()
    
    
    for flower in new_generation_flowers:
        pass
        #flower.to_string()
        
    #print(len(new_generation_flowers))"""
    flowers_generation = new_generation_flowers
