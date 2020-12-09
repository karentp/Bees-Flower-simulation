from random import randrange
import Bee
import Flower


bees_quantity = 1
flowers_quantity = 1
current_generation = []
field_height = 100
flowers_generation = []

# primera generacion de abejas, totalmente random
for i in range(bees_quantity):

    color = randrange(8)
    orientation = randrange(8)
    angle = randrange(8)
    radio = randrange(8)
    path = randrange(3)
    second_search = randrange(64)
    bee = Bee.Bee(color, orientation, angle, radio, path, second_search)
    bee.cromosoma = bee.make_cromosoma()
    current_generation.append(bee)
    print("\n")
    bee.print_info()

# primera generacion de flores

for i in range(flowers_quantity):
    color_flower = randrange(8)
    angle = randrange(16)
    radio = randrange(16)
    quadrant = randrange(4)
    flower = Flower.Flower(color, radio, angle, quadrant)
    flower.cromosoma = flower.make_flower_cromosoma()
    flowers_generation.append(flower)

# Seleccion


def selection():
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
    for i in range(bees_quantity):
        num = randrange(101)/100
        # Buscar la abeja que está dentro de ese rango
        for prob in probability_list:
            if num <= prob[1]:
                selected_bees.append(prob[2])


# Cruce
new_generation = []


def binary_to_decimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def cromosoma_to_bee(cromosoma):
    """ secondary_search (6) +  path (2) + radio (3) + angle (3) 
    + orientation(3) + color (3)"""

    second_search = binary_to_decimal(cromosoma[:6])
    path = binary_to_decimal(cromosoma[6:8])
    radio = binary_to_decimal(cromosoma[8:11])
    angle = binary_to_decimal(cromosoma[11:14])
    orientation = binary_to_decimal(cromosoma[14:17])
    color = binary_to_decimal(cromosoma[17:])
    bee = Bee.Bee(color, orientation, angle, radio, path, second_search)
    bee.cromosoma(cromosoma)

    return bee


def crossover(bees_to_cross, new_generation):
    if(len(bees_to_cross) == 0):
        return new_generation
    else:
        bee_1 = bees_to_cross[0]
        bee_2 = bees_to_cross[1]
        slice_point = randrange(20)  # El cromosoma es de 20 bits

        new_bee_1 = cromosoma_to_bee(bee_2.cromosoma[:slice_point] 
                                     + bee_1.cromosoma[slice_point:])
        new_generation.append(new_bee_1)

        new_bee_2 = cromosoma_to_bee(
            bee_2.cromosoma[:slice_point] + bee_1.cromosoma[slice_point:])
        new_generation.append(new_bee_2)

        crossover(bees_to_cross[2:], new_generation)


# Cruce de flores

new_flower_gen = []


def flower_crossover():
    for flower in flowers_generation:
        random_index = randrange(len(flower.polen_other_flowers))
        flower_2 = flower.polen_other_flowers[random_index]
        cut_section = randrange(13)
        new_flower = (flower.cromosoma[:cut_section] 
                      + flower_2.cromosoma[cut_section:])

        new_flower_gen.append(new_flower)
