import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty 
from kivy.vector import Vector
from kivy.clock import clock
Clock.schedule_interval(game.update, 1.0/140.0)
class PongGame(Widget): 
	pass
class PongApp(App): 
	def build(self):
		game = PongGame()
		game.serve_ball()
		Clock.schedule_interval(game.update,1.0/140.0)
		return game

class PongBall(Widget): 
	velocity_x = NumericProperty(0) 
	velocity_y = NumericProperty(0)

	velocity = ReferenceListProperty(velocity_x, velocity_y)
	def move(self):
		self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
	ball = ObjectProperty(None)

	def serve_ball(self):
		self.ball.center = self.center
		self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

	def update(self, dt): 
		pass





if __name__ == '__main__':
	PongApp().run()