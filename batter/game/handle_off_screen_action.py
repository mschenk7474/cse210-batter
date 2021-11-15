from game.action import Action
from game.point import Point
from game import constants
from game.actor import Actor
from game.move_actors_action import MoveActorsAction

class HandleOffScreenAction():
   """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
   Stereotype:
        Controller
   """
   def __init__(self):
      super().__init__()
      self.constants = constants
      self.move_actors_action = MoveActorsAction()

   def execute(self, cast):
      """Executes the action using the given actors.

      Args:
         cast (dict): The game actors {key: tag, value: list}.
      """
      ball = cast["balls"][0] #There's only one ball
      ball_x = ball._position.get_x()
      ball_y = ball._position.get_y()
      ball_velocity = ball.get_velocity()
      ball_velocity_x = ball._velocity._x
      ball_velocity_y = ball._velocity._y
      if ball_x == 0:
         ball_velocity_x = ball_velocity_x * -1
         ball_velocity = Point(ball_velocity_x,ball_velocity_y)
         ball.set_velocity(ball_velocity)
      elif ball_x == 750:
         ball_velocity_x = ball_velocity_x * -1
         ball_velocity = Point(ball_velocity_x,ball_velocity_y)
         ball.set_velocity(ball_velocity)
      elif ball_y == 575 or ball_y == 0:
         ball_velocity_y = ball_velocity_y * -1
         ball_velocity = Point(ball_velocity_x,ball_velocity_y)
         ball.set_velocity(ball_velocity)
      
      #Paddle Stuff
      paddle = cast["paddle"][0]
      paddle_x = paddle._position.get_x()
      paddle_y = paddle._position.get_y()
      paddle_dx = paddle._velocity._x
      if paddle_x == 0:
         paddle_x_new = max(paddle_x - paddle_dx, 0)
         paddle_position = Point(paddle_x_new, paddle_y)
         paddle.set_position(paddle_position)
      elif paddle_x == 750:
         paddle_x_new_2 = min(paddle_x - paddle_dx, 735)
         paddle_position = Point(paddle_x_new_2, paddle_y)
         paddle.set_position(paddle_position)

