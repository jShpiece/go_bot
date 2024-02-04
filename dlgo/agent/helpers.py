import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from gotypes import Point

def is_point_an_eye(board, point, color):
    #Find eyes (current definition is simply a liberty where all adjacent points and at least 3 diagonals are filled with friendly stones)
    if board.get(point) is not None: 
        #An eye is an empty point
        return False
    for neighbor in point.neighbors():
        #Check that all adjacent points are friendly
        if board.is_on_grid(neighbor):
            neighbor_color = board.get(neighbor)
            if neighbor_color != color:
                return False

    #Count friendly corners (we need 3 if in the middle, all if on the edge)
    friendly_corners = 0 
    off_board_corners = 0
    corners = [
        Point(point.row - 1, point.col - 1),
        Point(point.row - 1, point.col + 1),
        Point(point.row + 1, point.col - 1),
        Point(point.row + 1, point.col + 1),
    ]
    for corner in corners:
        if board.is_on_grid(corner):
            corner_color = board.get(corner)
            if corner_color == color:
                friendly_corners += 1
        else:
            off_board_corners += 1

    if off_board_corners > 0:
        #Point is on the edge or corner
        return off_board_corners + friendly_corners == 4
    
    return friendly_corners >= 3 #Point is in the middle