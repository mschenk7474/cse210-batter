from game.actor import Actor
from game.point import Point
from game import constants

class Ball():
   def __init__(self):
      super().__init__()
      self._ball = []
      self._constants = constants
   
   def set_ball(self):
      """
      Creates the ball actor with all the properties to with it.
      """
      ball = Actor()
      ball_position = Point(200, 500)
      ball_image = self._constants.IMAGE_BALL
      ball_width = self._constants.BALL_WIDTH
      ball_height = self._constants.BALL_HEIGHT
      ball_velocity = Point(10, -1)
      ball.set_position(ball_position)
      ball.set_image(ball_image)
      ball.set_width(ball_width)
      ball.set_height(ball_height)
      ball.set_velocity(ball_velocity)
      
      self._ball.append(ball)

   def get_ball(self):
      """
      Returns the ball list to be used by main.
      """
      return self._ball