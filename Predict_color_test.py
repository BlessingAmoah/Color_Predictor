""" CS 108   Final Project

This model is the testing session we will import the Color Predictor module and test if everything works.


@author: Blessing Amoah (bsa5)
@author: Brad Sinare (bs48)
@date: Fall, 2022
"""

from predict import Predictor
# Got the code from country guess

predict = Predictor('color.txt')
predict.set_predict(0)
assert predict.get_ans() == 'Black'
assert predict.get_clue() == 'The color starts with B.'
assert predict.get_clue() == 'The color has 5 alphabets.'
assert predict.get_clue() == 'The color ends with k.'
assert predict.get_clue() == 'clue finished.'
print('all tests pass...')