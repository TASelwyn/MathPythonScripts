"""
Statics Practice Question Solver

Created by: Thomas Selwyn
Last Updated: 1-Oct-2021
Version: 0.1.0 (WORK IN PROGRESS)
"""

import math

# import numpy as np

cartesian_vectors = []
positions = {}


# Display Menu Function
def display_menu():
    print("AV)Add Vector                AP)Add Position")
    print("PV)Print Vectors             PP)Print Position")
    print("CV)Calculate Result Vector   CP)Calculate Position    CU)Calculate Unit Vector ")
    print("MF)Multiply U.V by Force     PEQ)Print Equil Statements")
    print("R)Reset Data                  RP)Remove Position      Q)Quit")


def calcMagnitudes() -> tuple[float, int, int, int]:
    i_total = 0
    j_total = 0
    k_total = 0
    for i in range(0, len(cartesian_vectors)):
        i_total += float(cartesian_vectors[i]["i"])
        j_total += float(cartesian_vectors[i]["j"])
        k_total += float(cartesian_vectors[i]["k"])

    magnitude = math.sqrt(i_total ** 2 + j_total ** 2 + k_total ** 2)
    return magnitude, i_total, j_total, k_total


def calcDirectionalCosines() -> tuple[float, float, float]:
    magnitudes = calcMagnitudes()
    x_angle = math.acos(magnitudes[1] / magnitudes[0]) * 180 / math.pi
    y_angle = math.acos(magnitudes[2] / magnitudes[0]) * 180 / math.pi
    z_angle = math.acos(magnitudes[3] / magnitudes[0]) * 180 / math.pi

    return x_angle, y_angle, z_angle


def calcDistanceVector(position: str) -> dict[str, dict[str, float]]:
    i = positions[position[1]]['x'] - positions[position[0]]['x']
    j = positions[position[1]]['y'] - positions[position[0]]['y']
    k = positions[position[1]]['z'] - positions[position[0]]['z']
    name = str("r%s%s" % (position[0], position[1]))
    calculated_lambda_vector = {name: {"i": i, "j": j, "k": k}}

    return calculated_lambda_vector


def calcUnitVector(position: str) -> dict[str, dict[str, float]]:
    distance_vector = calcDistanceVector(position)["r" + position]

    x = distance_vector['i']
    y = distance_vector['j']
    z = distance_vector['k']

    magnitude = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    i = x / magnitude
    j = y / magnitude
    k = z / magnitude

    name = str("u" + position)
    calculated_unit_vector = {name: {"i": i, "j": j, "k": k}}

    return calculated_unit_vector


def roundToSigFigs(number: float, sigfigs: int) -> float:
    if number == 0:
        return 0.0  # Nice math domain error otherwise :(
    else:
        return round(number, sigfigs - int(math.floor(math.log10(abs(number)))) - 1)


# User Interface Function
def user_interface():
    choice = 'N'  # Initializing the choice variable
    while choice != 'Q':  # Main loop whole the user is interfacing with the program
        display_menu()
        choice = input("Please enter your choice: ").upper()

        VALID_INPUTS = dict.fromkeys(['AV', 'AP', 'PV', 'PP', 'PEQ', 'CV', 'CP', 'CU', 'MF', 'R', 'RP', 'Q'])
        if choice in VALID_INPUTS:
            valid_command = True
        else:
            valid_command = False

        if valid_command and choice != 'Q':
            if choice == 'AV':
                vectors_to_add = input("How many vectors do you want to add? ")
                for i in range(0, int(vectors_to_add)):
                    i = input("Enter I component of vector " + str(len(cartesian_vectors) + 1) + ": ")
                    j = input("Enter J component of vector " + str(len(cartesian_vectors) + 1) + ": ")
                    k = input("Enter K component of vector " + str(len(cartesian_vectors) + 1) + ": ")

                    current_vector = {"i": i, "j": j, "k": k}
                    cartesian_vectors.append(current_vector)
            elif choice == 'AP':
                positions_to_add = input("How many positions do you want to add? ")
                for i in range(0, int(positions_to_add)):
                    posName = str(input("Enter λ name for position " + str(len(positions) + 1) + ": ")).upper()[
                              :1]  # Limit Position Name to 1 char
                    x = float(input("Enter X component of position " + posName + ": "))
                    y = float(input("Enter Y component of position " + posName + ": "))
                    z = float(input("Enter Z component of position " + posName + ": "))

                    current_position = {posName: {"x": x, "y": y, "z": z}}
                    positions.update(current_position)
            elif choice == 'PV':
                if len(cartesian_vectors) >= 1:
                    for i in range(len(cartesian_vectors)):
                        current_position = cartesian_vectors[i]
                        i_component = roundToSigFigs(float(current_position['i']), 4)
                        j_component = roundToSigFigs(float(current_position['j']), 4)
                        k_component = roundToSigFigs(float(current_position['k']), 4)
                        print("%s    %si    %sj    %sk" % (i, i_component, j_component, k_component))

                else:
                    print("No vectors stored. Add a vector first")
                input()  # Holds the next line until user hits enter
            elif choice == 'PP':
                for key in positions.keys():
                    current_position = positions.get(key)
                    i_component = roundToSigFigs(current_position['x'], 4)
                    j_component = roundToSigFigs(current_position['y'], 4)
                    k_component = roundToSigFigs(current_position['z'], 4)
                    print("%s    %s    %s    %s" % (key, i_component, j_component, k_component))
                input()  # Holds the next line until user hits enter
            elif choice == 'PEQ':
                EquiI = "Ex = 0 = "
                EquiJ = "Ey = 0 = "
                EquiK = "Ez = 0 = "
                for i in range(len(cartesian_vectors)):
                    current_position = cartesian_vectors[i]
                    i_component = roundToSigFigs(float(current_position['i']), 4)
                    j_component = roundToSigFigs(float(current_position['j']), 4)
                    k_component = roundToSigFigs(float(current_position['k']), 4)
                    EquiI += str(i) + "(" + str(i_component) + ")    "
                    EquiJ += str(i) + "(" + str(j_component) + ")    "
                    EquiK += str(i) + "(" + str(k_component) + ")    "
                print(EquiI + "\n")
                print(EquiJ + "\n")
                print(EquiK + "\n")

                input()  # Holds the next line until user hits enter
            elif choice == 'CV':
                if len(cartesian_vectors) >= 1:
                    magnitudes = calcMagnitudes()
                    resMagn = roundToSigFigs(magnitudes[0], 5)
                    i_component = roundToSigFigs(magnitudes[1], 4)
                    j_component = roundToSigFigs(magnitudes[2], 4)
                    k_component = roundToSigFigs(magnitudes[3], 4)
                    print("Fr is %si    %sj    %sk        |Fr| = %s" % (i_component, j_component, k_component, resMagn))
                    directional_cosines = calcDirectionalCosines()
                    x_rnd = roundToSigFigs(directional_cosines[0], 4)
                    y_rnd = roundToSigFigs(directional_cosines[1], 4)
                    z_rnd = roundToSigFigs(directional_cosines[2], 4)
                    print("Directionals are %g° & %g° & %g°" % (x_rnd, y_rnd, z_rnd))
                else:
                    print("No vectors stored. Add a vector first")

                input("Hit any key to continue...")  # Holds the next line until user hits enter
            elif choice == 'CP':
                calculate_pos_vectors_amount = input("How many position vectors do you want to calculate? ")
                for i in range(0, int(calculate_pos_vectors_amount)):
                    inputPosition = str(input("Enter position vector name: ")).upper()[:2]
                    if inputPosition != '':
                        # print("End result is.. %s" % (str(calcDistanceVector(position))))
                        posVector = calcDistanceVector(inputPosition)['r' + inputPosition]
                        i_component = roundToSigFigs(posVector['i'], 4)
                        j_component = roundToSigFigs(posVector['j'], 4)
                        k_component = roundToSigFigs(posVector['k'], 4)
                        posVectorMagnitude = roundToSigFigs(
                            math.sqrt(i_component ** 2 + j_component ** 2 + k_component ** 2), 4)
                        print("r%s is %si    %sj    %sk        |r%s| = %s" % (
                            inputPosition, i_component, j_component, k_component, inputPosition, posVectorMagnitude))
                    else:
                        break  # Exits for loop
                input("Hit any key to continue...")  # Holds the next line until user hits enter
            elif choice == 'CU':
                calculate_unit_vectors_amount = input("How many unit vectors do you want to calculate? ")
                for i in range(0, int(calculate_unit_vectors_amount)):
                    inputPosition = str(input("Enter unit vector name: ")).upper()[:2]
                    if inputPosition != '':
                        # print("End result is...... %s" % (str(calcUnitVector(inputPosition))))
                        unitVector = calcUnitVector(inputPosition)['u' + inputPosition]
                        i_component = roundToSigFigs(unitVector['i'], 4)
                        j_component = roundToSigFigs(unitVector['j'], 4)
                        k_component = roundToSigFigs(unitVector['k'], 4)
                        print("u%s is %si    %sj    %sk" % (inputPosition, i_component, j_component, k_component))
                    else:
                        break  # Exits for loop
                input("Hit any key to continue...")  # Holds the next line until user hits enter
            elif choice == 'MF':
                calculate_unit_vectors_amount = input("How many unit vectors do you want to MULTIPLY? ")
                question = input("Do you want to save these force vectors? (YES/NO) ")[:3].upper()
                for i in range(0, int(calculate_unit_vectors_amount)):
                    inputPosition = str(input("Enter force name: ")).upper()[:2]
                    inputForce = float(input("Enter force: "))
                    if inputPosition != '':
                        unitVector = calcUnitVector(inputPosition)['u' + inputPosition]
                        i_component = roundToSigFigs(inputForce * unitVector['i'], 4)
                        j_component = roundToSigFigs(inputForce * unitVector['j'], 4)
                        k_component = roundToSigFigs(inputForce * unitVector['k'], 4)
                        if question == "YES":
                            cartesian_vectors.append({"i": i_component, "j": j_component, "k": k_component})
                        print("F_%s is %si    %sj    %sk" % (inputPosition, i_component, j_component, k_component))
                    else:
                        break  # Exits for loop
                input("Hit any key to continue...")  # Holds the next line until user hits enter
            elif choice == 'R':
                print("Data reset.")
                cartesian_vectors.clear()
                positions.clear()
            elif choice == 'RP':
                positions.pop(str(input("What position do you want to remove?")).upper())
            else:
                print("No such command")

        print("*" * 80)  # Prints a divider for the program


# Main Function
if __name__ == '__main__':
    user_interface()
