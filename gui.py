""" CS 108   Final Project

This model is the view which display the Color Predictor class on GUIzero by allowing the user to predict the
color, the user will be given 3 clues to predict the color. Whenever the user is able to predict the color one
will be added to the scoreboard. We have a timer which will time the seconds the user used to predict the color
correct. 


@author: Blessing Amoah (bsa5)
@author: Brad Sinare (bs48)
@date: Fall, 2022
"""

from guizero import App, Text, TextBox, PushButton, Box, Picture
from predict import Predictor
import time

class ColorPredictor:
    """ GUI color predictor game"""
    
    def __init__(self, app):
        """ Creates the color predictor GUI app. """
        
        # design the application GUI.
        app.title = 'Color Predictor Game'
        app.width = 800
        app.height = 480
        app.font = 'Georgia'
        app.text_size = 20
        
        
        """Gives detail about the predict object using the colors listed in the color.txt.
        Got the color names from englishgrammarhere.com and bciburke.com
        """
        self.predict = Predictor('color.txt')
        
        
        # Layout different colors on the guizero.
        box = Box(app, layout='grid')
        self.welcome = Text(box, text = 'Welcome to Color Predictor! Predict the color.', grid = [0,0])
        self.welcome.text_color = "white"
        
        """Got the picture from vectorstock.com
        """
        box = Box(app, width = 15, height = 10)
        self.c = Picture(app, image='new_color.png')
        
        # Prof Chris gave us the idea to divide it into different Box to have everything working. 
        box = Box(app, layout='grid')
        self.correct = TextBox(box, width=30, grid=[0, 0])
        self._button = PushButton(box, command=self.predicts, text='Predict', grid=[1, 0])
        self.admit_button_ = PushButton(box, command=self.admit_button, text='Call it a day', grid=[2, 0])
        PushButton(box, app.destroy, text='Quit', grid=[3, 0])
        self.directions= Text(app, text = 'Clue: ' + self.predict.get_clue())
        self.directions.text_color = "white"
        
        box = Box(app, width = 15, height = 20)
        self.score = Text(app, text = 'Scoreboard:')
        self.score.text_color = "white"
        
        box = Box(app, width = 5, height = 5)
        self.time_ = Text(app, text = 'Time:')
        self.time_.text_color = "white"
        
    def predicts(self):
        """ Process a user predict - If it's correct move on to a new color.
        Got ideas from the game Country guess
        """
        if self.predict.check_ans(self.correct.value):
            self.predict.reset()
            self.directions.value = f'Nice! Try another color. {self.predict.get_clue()}'
            self.display_score()
        
        else:
            self.directions.value = f'Nope can you try again. {self.predict.get_clue()}'
            
    def admit_button(self):
        """ Process a user admitting request by predicting the answer and reshuffling.
        Got ideas from the game Country guess
        """
        correct = (self.predict.get_ans())
        self.predict.reset()
        clue = self.predict.get_clue()
        self.directions.value = f'The color was {correct}. Predict again. {clue}'
        
    def display_score(self):
        """This displays the score of the number of times the user was able to predict the color
        Got Ideas from api.arcade.academy website.
        Also got some assistance from Prof Chris 
        """
        self.predict.score += 1
        self.score.value = f'Scoreboard: {self.predict.score}'
        
        
        #Got ideas from www.codetoday.co.uk/
        start_time = int(time.time())
        self.time_.value = f'Time: {time.time() - start_time:.02}'
        
        
        
        
app = App()
ColorPredictor(app)
app.display()       