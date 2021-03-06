import random

random.seed()
class StandardShapes:

    # template values
    EMPTY = '.'
    BLOCK = 'O'
    TEMPLATEWIDTH = 5
    TEMPLATEHEIGHT = 5

    # block shapes
    I = 'I'
    J = 'J'
    L = 'L'
    S = 'S'
    T = 'T'
    Z = 'Z'
    O = 'O'

    I_TEMPLATE = [['.....',
                   'OOOO.',
                   '.....',
                   '.....',
                   '.....'],
                 ['..O..',
                  '..O..',
                  '..O..',
                  '..O..',
                  '.....']]
    J_TEMPLATE = [['.....',
                   '.O...',
                   '.OOO.',
                   '.....',
                   '.....'],
                  ['.....',
                   '..OO.',
                   '..O..',
                   '..O..',
                   '.....'],
                  ['.....',
                   '.....',
                   '.OOO.',
                   '...O.',
                   '.....'],
                  ['.....',
                   '..O..',
                   '..O..',
                   '.OO..',
                   '.....']]
    L_TEMPLATE = [['.....',
                   '...O.',
                   '.OOO.',
                   '.....',
                   '.....'],
                  ['.....',
                   '..O..',
                   '..O..',
                   '..OO.',
                   '.....'],
                  ['.....',
                   '.....',
                   '.OOO.',
                   '.O...',
                   '.....'],
                  ['.....',
                   '.OO..',
                   '..O..',
                   '..O..',
                   '.....']]
    S_TEMPLATE = [['.....',
                   '.OO..',
                   'OO...',
                   '.....',
                   '.....'],
                  ['.....',
                   '.O...',
                   '.OO..',
                   '..O..',
                   '.....']]
    T_TEMPLATE = [['.....',
                   '..O..',
                   '.OOO.',
                   '.....',
                   '.....'],
                  ['.....',
                   '..O..',
                   '..OO.',
                   '..O..',
                   '.....'],
                  ['.....',
                   '.....',
                   '.OOO.',
                   '..O..',
                   '.....'],
                  ['.....',
                   '..O..',
                   '.OO..',
                   '..O..',
                   '.....']]
    Z_TEMPLATE = [['.....',
                   'OO...',
                   '.OO..',
                   '.....',
                   '.....'],
                  ['.....',
                   '..O..',
                   '.OO..',
                   '.O...',
                   '.....']]
    O_TEMPLATE = [['.....',
                   '..OO.',
                   '..OO.',
                   '.....',
                   '.....']]

    SHAPES = [I, J, L, O, S, T, Z]
    TEMPLATES = {I: I_TEMPLATE, J: J_TEMPLATE, L: L_TEMPLATE, O: O_TEMPLATE,
                 S: S_TEMPLATE, T: T_TEMPLATE, Z: Z_TEMPLATE}

    #            R    G    B
    GRAY = (100, 100, 100)
    NAVYBLUE = (60, 60, 100)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)

    SHAPECOLORS = {I: ORANGE, J: CYAN, L: RED, O: GRAY, S: YELLOW,
                   T: GREEN, Z: PURPLE}

    def __init__(self):
        self = None

    def getRandomShape(self):
        # all shapes
        return random.choice(StandardShapes.SHAPES)

    def getColor(self, shapeType):
        return StandardShapes.SHAPECOLORS[shapeType]

    def getTemplate(self, shapeType, configuration=None):
        if configuration == None:
            return StandardShapes.TEMPLATES[shapeType]
        else:
            return StandardShapes.TEMPLATES[shapeType][configuration]
