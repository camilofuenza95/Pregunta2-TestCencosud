from ElevatorModel import Door, Elevator, FloorButton, MovementButton

# Elevators creation
A1 = Elevator(0,False,None)
A2 = Elevator(0,False,None)
A3 = Elevator(0,False,None)

# List of elevators
elevators = [A1,A2,A3]

# Doors creation for each elevator
doorA1 = Door(False)
doorA2 = Door(False)
doorA3 = Door(False)

# Buttons set for first elevator(A1)
btn1A1 = FloorButton(False,1)
btn2A1 = FloorButton(False,2)
btn3A1 = FloorButton(False,3)
btn4A1 = FloorButton(False,4)
btn5A1 = FloorButton(False,5)
btn6A1 = FloorButton(False,6)
btn7A1 = FloorButton(False,7)
btn8A1 = FloorButton(False,8)
btn9A1 = FloorButton(False,9)
btn10A1 = FloorButton(False,10)

# Buttons set for second elevator(A2)
btn1A2 = FloorButton(False,1)
btn2A2 = FloorButton(False,2)
btn3A2 = FloorButton(False,3)
btn4A2 = FloorButton(False,4)
btn5A2 = FloorButton(False,5)
btn6A2 = FloorButton(False,6)
btn7A2 = FloorButton(False,7)
btn8A2 = FloorButton(False,8)
btn9A2 = FloorButton(False,9)
btn10A2 = FloorButton(False,10)

# Buttons set for third elevator(A3)
btn1A3 = FloorButton(False,1)
btn2A3 = FloorButton(False,2)
btn3A3 = FloorButton(False,3)
btn4A3 = FloorButton(False,4)
btn5A3 = FloorButton(False,5)
btn6A3 = FloorButton(False,6)
btn7A3 = FloorButton(False,7)
btn8A3 = FloorButton(False,8)
btn9A3 = FloorButton(False,9)
btn10A3 = FloorButton(False,10)

# Movement buttons for each floor.
btn1Up = MovementButton(False,1, 'Up')

btn2Up = MovementButton(False,2, 'Up')
btn2Down = MovementButton(False,2, 'Down')

btn3Up = MovementButton(False,3, 'Up')
btn3Down = MovementButton(False,3, 'Down')

btn4Up = MovementButton(False,4, 'Up')
btn4Down = MovementButton(False,4, 'Down')

btn5Up = MovementButton(False,5, 'Up')
btn5Down = MovementButton(False,5, 'Down')

btn6Up = MovementButton(False,6, 'Up')
btn6Down = MovementButton(False,6, 'Down')

btn7Up = MovementButton(False,7, 'Up')
btn7Down = MovementButton(False,7, 'Down')

btn8Up = MovementButton(False,8, 'Up')
btn8Down = MovementButton(False,8, 'Down')

btn9Up = MovementButton(False,9, 'Up')
btn9Down = MovementButton(False,9, 'Down')

btn10Down = MovementButton(False,10, 'Down')
