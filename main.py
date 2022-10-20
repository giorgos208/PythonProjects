N = (input("Enter N dimension: "))
x_position = 0
y_position = 0

def isFloat(x):
    length = len(x)
    for i in range(0, length):
        if x[i] == "." or x[i] == ",":
            return True

    return False

def isValid(direction,steps):
    if steps >= int(N):
        return False

    if direction == "u":
        x_new = x_position
        y_new = y_position - steps
    elif direction == "d":
        x_new = x_position
        y_new = y_position + steps
    elif direction == "r":
        x_new = x_position + steps
        y_new = y_position
    elif direction == "l":
        x_new = x_position - steps
        y_new = y_position
    if ((y_new < 0 or x_new < 0) or (y_new >= int(N) or x_new >= int(N))): return False, -1 , -1
    else:
        return True, x_new, y_new


while (isFloat(N)) or int(N) <= 0:
    N = input("Enter a valid N dimension: ")

while (True):
    command = (input("Enter command for robot: "))  # "d15" "d5"
    if command == "": break
    #Direction, Steps, Let's play
    direction = command[0]  # Got the direction of the move
    steps = ""
    for i in range(1, len(command)):
        steps += command[i]

    steps = int(steps)

    return_values = isValid(direction,steps)
    if (return_values[0] == False):
        print("Error move." + "The robot remains at: "+ str(y_position) + ", " + str(x_position))
        continue
    else:
        x_position = return_values[1]
        y_position = return_values[2]
        print("The robot moved to: " + str(y_position) + ", " + str(x_position))
