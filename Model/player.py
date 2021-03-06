import shape
import events
from constants import *

class Player(object):
    def __init__(self, eventManager):
        self.eventManager = eventManager
        self.eventManager.registerListener(self)

        self.name = ""

        self.nextActiveShape = None
        self.activeShape = None
        self.inactiveBlocks = []
        self.board = None
        self.previewBoard = None
        self.holdBoard = None
        self.score = None  # TODO
        self.lineClearDetector = None

    def __str__(self):
        return '<Player %s %s>' % (self.name, id(self))

    def start(self):
        self.activeShape = shape.Shape(self.eventManager,
                                       SHAPETYPES.getRandomShape(),
                                       self.board)
        self.nextActiveShape = shape.Shape(self.eventManager,
                                           SHAPETYPES.getRandomShape(),
                                           self.previewBoard)
        event = events.ShapeAddedEvent(self.activeShape, self.nextActiveShape,
                                       self.board)
        self.eventManager.post(event)

    def shapePlaced(self, oldShape):
        for block in oldShape.blocks:
            self.inactiveBlocks.append(block)
        self.activeShape = self.nextActiveShape
        self.nextActiveShape = shape.Shape(self.eventManager, \
                                       SHAPETYPES.getRandomShape(), \
                                       self.previewBoard)
        event = events.ShapeAddedEvent(self.activeShape, self.nextActiveShape,
                                       self.board)
        self.eventManager.post(event)

        for activeBlock in self.activeShape.blocks:
            for inactiveBlock in self.inactiveBlocks:
                if activeBlock.space == inactiveBlock.space:
                    event = events.GameOverEvent()
                    self.eventManager.post(event)

    def _clearLines(self, rows):
        spacesToClear = [space for row in rows
                         for space in self.board.spaces[row]]
        self.inactiveBlocks = [block for block in self.inactiveBlocks
                                if block.space not in spacesToClear]

    def _shiftLinesDown(self, rows):
        if len(rows) > 0:
            rows.reverse()
            row = rows.pop()
            for i in reversed(range(row + 1)):
                for block in self.inactiveBlocks:
                    if block.space in self.board.spaces[i]:
                        block.move(DIRECTION_DOWN)
            self._shiftLinesDown(rows)


    def _checkLines(self, blocks):
        fullRows = []
        for i in range(len(self.board.spaces)):
            row = self.board.spaces[i]
            if set(row).issubset(set([block.space for block in blocks])):
                fullRows.append(i)

        return fullRows

    def notify(self, event):
        if isinstance(event, events.GameStartedEvent):
            self.board = event.game.board
            self.start()

        elif isinstance(event, events.MiniBoardBuiltEvent):
            if event.boardName == PREVIEW:
                self.previewBoard = event.board
            elif event.boardName == HOLD:
                self.holdBoard = event.board

        elif isinstance(event, events.ShapePlacedEvent):
            self.shapePlaced(event.shape)
            fullRows = self._checkLines(self.inactiveBlocks)
            if fullRows:
                self._clearLines(fullRows)
                self._shiftLinesDown(fullRows)
            event = events.BoardChanged(self.activeShape.blocks,
                                        self.inactiveBlocks)
            self.eventManager.post(event)

        elif isinstance(event, events.ResetEvent):
            self.inactiveBlocks = []
            self.activeShape = shape.Shape(self.eventManager, \
                                           SHAPETYPES.getRandomShape(), \
                                           self.board)
            self.nextActiveShape = shape.Shape(self.eventManager, \
                                           SHAPETYPES.getRandomShape(), \
                                           self.previewBoard)
            event = events.ShapeAddedEvent(self.activeShape,
                                           self.nextActiveShape, self.board)
            self.eventManager.post(event)
            event = events.BoardChanged(self.activeShape.blocks,
                                        self.inactiveBlocks)
            self.eventManager.post(event)

