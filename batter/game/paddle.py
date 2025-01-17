from game.actor import Actor
from game.point import Point
from game import constants

class Paddle():
   def __init__(self):
      super().__init__()
      self._paddle = []
      self._constants = constants
   
   def set_paddle(self):
      """
      Sets the paddle up as an actor.
      """
      paddle = Actor()
      paddle_position = Point(375, 550)
      paddle_image = self._constants.IMAGE_PADDLE
      paddle_width = self._constants.PADDLE_WIDTH
      paddle_height = self._constants.PADDLE_HEIGHT
      paddle.set_position(paddle_position)
      paddle.set_image(paddle_image)
      paddle.set_width(paddle_width)
      paddle.set_height(paddle_height)

      self._paddle.append(paddle)
   
   def get_paddle(self):
      """
      Returns the paddle list.
      """
      return self._paddle