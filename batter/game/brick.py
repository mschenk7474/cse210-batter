from game.actor import Actor
from game.point import Point
from game import constants
import random

class Brick():
   def __init__(self):
      super().__init__()
      self.bricks = []
      self.constants = constants
   
   def set_brick(self):
      """
      Creates the bricks with all the actor qualties included.
      """
      #Makes what bricks appear random
      brick_y = random.randint(0, 50)
      brick_x = random.randint(0, 100)
      x =[]
      y = []
      for i in range(10, constants.MAX_X, 50):
         x.append(i)
      for i in range(10, constants.MAX_Y_HALF, brick_y):
         y.append(i)
      for i in range(len(y)):
         for j in range(len(x)):
            brick = Actor()
            brick.set_image(constants.IMAGE_BRICK)
            brick.set_height(constants.BRICK_HEIGHT)
            brick.set_width(constants.BRICK_WIDTH)
            position = Point(x[j],y[i])
            brick.set_position(position)
            self.bricks.append(brick)

   def get_bricks(self):
      """
      Returns the brick list.
      """
      return self.bricks