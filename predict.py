""" CS 108   Final Project

This model is the module it contains the Color Predictor module which will display using the view (gui.py) code.


@author: Blessing Amoah (bsa5)
@author: Brad Sinare (bs48)
@date: Fall, 2022
"""


from random import randint


class Predict:
    """ This class contains the predictor colors"""
    
    def __init__(self, color_):
        """ It will reset to a new color"""
        self.color_ = color_
        
        
class Predictor:
    """ This class implements the game model for the predictor. """
    
    def __init__(self, filename):
        """ This will reshuffle the colors from the file
        We got ideas from the game Country guess
        """
        self.score = 0
        self.predictions = []
        with open(filename) as f:
            for col in f:
                self.predictions.append(Predict(col.strip()))
                if len(self.predictions) == 0:
                    print(f'Hey you made an error:{0}', filename)
                self.reset()
                
    def reset(self):
        """ Pick a new color and reset the color file.
        We got ideas from the game Country guess
        """
        self.prediction_ = randint(0, len(self.predictions) - 1)
        self.clue_col = 0
        
        
    def set_predict(self, pre_dict):
        """ Function sets a non-random prediction.
            It is used for tesing purposes.
            Got ideas from the game Country guess
        """
        if pre_dict < 0 or len(self.predictions) <= pre_dict:
            print(f'Sorry prediction {pre_dict}...')
            
        else:
            self.prediction_ = pre_dict
            self.clue_col = 0
            
    def get_ans(self):
        """ Get the answer for the correctly selected color  """
        return self.predictions[self.prediction_].color_
    
    
    def get_clue(self):
        """ Gives clue about the color to predict
        We got idea from the game Country guess 
        """
        color_ = self.predictions[self.prediction_]
        self.clue_col += 1
        if self.clue_col == 1:
            return f'The color starts with {color_.color_[0]}.'
        elif self.clue_col == 2:
            return f'The color has {len(color_.color_)} alphabets.'
        elif self.clue_col == 3:
            return f'The color ends with {color_.color_[-1]}.'
        else:
            return 'clue finished.'
        
        
    def check_ans(self, correct):
        """ Determine if the given answer is correct.
        Got ideas from Country guess
        """
        return correct.lower() == self.predictions[self.prediction_].color_.lower()    
              
                
