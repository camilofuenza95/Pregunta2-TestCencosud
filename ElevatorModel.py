class Elevator:
    """
    Elevator object.

    @param currentFloor: Floor where the elevator is
    @param movingState: Is the elevator currently moving?
    @param direction: Moving Up, Down or Stop
    """
    def __init__(self, currentFloor, movingState, direction):
        self.currentFloor = currentFloor
        self.movingState = movingState
        self.direction = direction

    def stopElevator(elevator):
        elevator.direction = None

    def moveElevatorDown(elevator):
        """Move elevator to a minor floor

        :param elevator: Elevator to move down.
        """
        elevator.movingState=True
        elevator.direction = 'Down'
        elevator.currentFloor = elevator.currentFloor-1
        pass

    def moveElevatorUp(elevator):
        """Move elevator to a major floor

        :param elevator: Elevator to move up.
        """
        elevator.movingState=True
        elevator.direction = 'Up'
        elevator.currentFloor = elevator.currentFloor+1

    pass       

    def __str__(self):
        return "Elevator is: ", self.movingState ,', is on: ' , self.currentFloor ,' floor and is moving: ' , self.direction


class Door:

    def __init__(self,open):
        self.open = open
    
    def openDoor(door):
        door.open = True

    def closeDoor(door):
        door.open = False


class FloorButton:

    def __init__(self,buttonState, floorNumber):
        self.buttonState = buttonState
        self.floorNumber = floorNumber

    def pressButton(self, buttonState):
        self.buttonState = not(self.buttonState)


class MovementButton(FloorButton):

    def __init__(self, buttonState, floorNumber, direction):
        super().__init__(buttonState,floorNumber)
        self.direction = direction


        
