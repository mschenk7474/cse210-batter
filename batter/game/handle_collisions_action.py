from game.actor import Actor
from game.point import Point
from game.action import Action
from game import constants
from game.audio_service import AudioService

class HandleCollisionsAction():
   def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = AudioService()

   def execute(self, cast):
      """Executes the action using the given actors.

      Args:
         cast (dict): The game actors {key: tag, value: list}.
      """
      # marquee = cast["marquee"][0] # there's only one
      # robot = cast["robot"][0] # there's only one
      # artifacts = cast["artifact"]
      # marquee.set_text("")
      # for artifact in artifacts:
      #    if self._physics_service.is_collision(robot, artifact):
      #          description = artifact.get_description()
      #          marquee.set_text(description) 


      # ball_x = ball._position.get_x()
      # ball_y = ball._position.get_y()
      # ball_velocity = ball.get_velocity()
      # if ball_x == 0:
      #    ball_velocity = Point(1, -1)
      #    ball.set_velocity(ball_velocity)
      # elif ball_x == 750:
      #    ball_velocity = Point(-1, -1)
      #    ball.set_velocity(ball_velocity)
      balls = cast["balls"][0]
      paddle = cast["paddle"][0]
      bricks = cast["bricks"]
      balls_x = balls._position.get_x()
      balls_y = balls._position.get_y()
      balls_velocity = balls.get_velocity()
      if self._physics_service.is_collision(balls, paddle):
         self._audio_service.play_sound(constants.SOUND_BOUNCE)
         balls_velocity = Point(-10, -1)
         balls.set_velocity(balls_velocity)
      for brick in bricks:
         if self._physics_service.is_collision(balls, brick):
            balls_velocity = Point(-10, 1)
            balls.set_velocity(balls_velocity)
            self._audio_service.play_sound(constants.SOUND_BOUNCE)
            bricks.remove(brick)
         
         
