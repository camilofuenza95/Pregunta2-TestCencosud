from ElevatorModel import Door, Elevator, FloorButton, MovementButton


def callElevator(btnRequested : MovementButton):
    """Call elevator from a specific floor.

    :param btnRequested: Button from where the elevator was called, can have direction Up or Down and a specific floor
    """
    # Cange btnRequested buttonState to True

    # Loop through elevators array, select the one that is closer to button requested floor.

    # Check if elevator is currently moving by elevatorState


    # IF ISN´T MOVING: Return True to start moving the elevator

    # IF buttonRequested  property of btnRequested is True and the floorNumber is minor than elevator currentFloor 

    # Call elevator moveDown function

    # Call validateElevatorFloor function

    # IF validateElevatorFloor = TRUE change direction of the elevator to STOP

    # Cange btnRequested buttonState to False

    # Set elevator movingState as False

    # Call door openDoor() function

    # IF validateElevatorFloor = FALSE call moveElevatorDown and repeat the validation process TRUE


    # IF buttonRequested  property of btnRequested is True and the floorNumber is major than elevator currentFloor 

    # Call elevator moveUp function

    # Call validateElevatorFloor function

    # IF validateElevatorFloor = TRUE change direction of the elevator to STOP

    # Set elevator movingState as False

    # Cange btnRequested buttonState to False

    # Call door openDoor() function

    # IF validateElevatorFloor = FALSE call moveElevatorUp and repeat the validation process TRUE




    # IF IT´S MOVING: check if the direction of the elevator is the same of the button requested direction

    # IF IS THE SAME DIRECTION:

    # Call elevator moveUp or moveDown function dependes un elevator current direction

    # Call validateElevatorFloor function

    # IF validateElevatorFloor = TRUE change direction of the elevator to STOP

    # Set elevator movingState as False

    # Cange btnRequested buttonState to False

    # Call door openDoor() function

    # IF validateElevatorFloor = FALSE call moveElevatorDown and repeat the validation process TRUE

    
    
    # IF ISN´T THE SAME DIRECTION: Return False and check same conditions in the next closer elevator in the list of elevators 

    pass

def selectedFloor(elevator : Elevator, btnSelected: FloorButton, door: Door):
    """Select floor from elevator buttons panel.

    :param elevator: Elevator from which the request was done.
    :param btnSelected: Selected button from buttons panel.
    :param door: Door of the elevator.
    """
    # IF buttonSelected  property of btnSelected is True and the floorNumber is minor than elevator currentFloor 

    # Change the direction of the elevator to DOWN

    # Call elevator moveDown function

    # Call validateElevatorFloor function

    # IF validateElevatorFloor = TRUE change direction of the elevator to STOP

    # Set elevator movingState as False

    # Call door openDoor() function

    # IF validateElevatorFloor = FALSE call moveElevatorDown and repeat the validation process TRUE

    
    #  ELSE

    # Change the direction of the elevator to UP

    # Call elevator moveUp function

    # Call validateElevatorFloor function

    # IF validateElevatorFloor = TRUE change direction of the elevator to STOP

    # Set elevator movingState as False

    # Call door openDoor() function

    # IF validateElevatorFloor = FALSE call moveElevatorUp and repeat until validation process TRUE

    pass

def validateElevatorFloor(elevator:Elevator, btnSelected:FloorButton) -> bool:
    """Validate if the elevator is on the selected floor

    :param elevator: Elevator from which the request was done.
    :param btnSelected: Selected button from buttons panel.
    """
    # IF elevator currentFloor = btnSelected floorNumber RETURN TRUE

    # ELSE RETURN FALSE
    pass