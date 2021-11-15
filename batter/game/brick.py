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
      # brick_1 = Actor()
      # position = Point(10, 10)
      # width = constants.BRICK_WIDTH
      # height = constants.BRICK_HEIGHT
      # brick_1.set_width(width)
      # brick_1.set_height(height)
      # brick_1.set_position(position)
      # self.bricks.append(brick_1)

      # brick_2 = Actor()
      # position = Point(100, 10)
      # width = constants.BRICK_WIDTH
      # height = constants.BRICK_HEIGHT
      # brick_2.set_width(width)
      # brick_2.set_height(height)
      # brick_2.set_position(position)
      # self.bricks.append(brick_2)

      # brick_3 = Actor()
      # position = Point(200, 10)
      # width = constants.BRICK_WIDTH
      # height = constants.BRICK_HEIGHT
      # brick_3.set_width(width)
      # brick_3.set_height(height)
      # brick_3.set_position(position)
      # self.bricks.append(brick_3)
      #MAX X = 800
      #MAX Y/2 = 300
      brick_y = random.randint(0, 50)
      brick_x = random.randint(0, 100)
      x =[]
      y = []
      for i in range(10, constants.MAX_X, 50): #was 100, MAX_X
         x.append(i)
      for i in range(10, constants.MAX_Y_HALF, brick_y): #was 50
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
            #print(f"The position is :{x[j], y[i]}")

   def get_bricks(self):
      return self.bricks

   # def get_x_y_bricks(self):
   #    for brick in self.bricks:
   #       x = brick._position.get_x()
   #       y = brick._position.get_y()
   #       print(f"{x}, {y}")

   # def set_brick_image(self):
   #    for brick in self.bricks:
   #       brick.set_image(self.constants.IMAGE_BRICK)




