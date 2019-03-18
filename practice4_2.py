import kivy
kivy.require('1.7.0')

from kivy.app import App
from kivy.uix.button import Label

class practice4_2App(App): 
	def build(self):
		return Label()

if __name__=="__main__":
	practice4_2App().run()