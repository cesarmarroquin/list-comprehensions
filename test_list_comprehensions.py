from list_comprehensions import *

string = "List Comprehensions are the Greatest!"
vowels = ["a", "e","i","o", "u"]
csv_file = "buoy.csv"

def test_remove_vowels():
    assert remove_vowels(string) == \
    "Lst Cmprhnsns r th Grtst!"


def test_daily_water_temps():
    assert daily_water_temps(csv_file) == \
    ['26.5', '26.2', '26.2', '26.2', '26.5', '26.9', '27.0', '26.9', '27.1', '27.0',\
     '26.9', '26.8', '26.9', '27.1','27.1', '27.2', '27.5', '27.7', '27.6', '28.1',\
    '27.5', '27.7', '27.4', '27.4','28.0', '28.7', '28.9', '28.5', '28.1']


def test_string_to_float():
    assert string_to_float(daily_water_temps(csv_file)) == \
    [26.5, 26.2, 26.2, 26.2, 26.5, 26.9, 27.0, 26.9, 27.1, 27.0, 26.9, 26.8, 26.9, 27.1,\
     27.1, 27.2, 27.5, 27.7, 27.6, 28.1, 27.5, 27.7, 27.4, 27.4, 28.0, 28.7, 28.9, 28.5, 28.1]


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(string_to_float(daily_water_temps("buoy.csv"))) == \
    [79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 82, 81, 81, 81, 81, 82, 83, 84, 83, 82]


def test_date_wave_height():
    assert date_wave_height(csv_file) == \
    [('Wave Height', 'Date'), ('1.55', '2015-08-01'), ('1.97', '2015-08-02'), ('1.89', '2015-08-03'), \
    ('1.62', '2015-08-04'), ('1.72', '2015-08-05'), ('4.09', '2015-08-06'), ('3.52', '2015-08-07'),\
     ('2.18', '2015-08-08'), ('2.14', '2015-08-09'), ('2.2', '2015-08-10'), ('1.8', '2015-08-11'), \
     ('1.99', '2015-08-12'), ('1.81', '2015-08-13'), ('1.8', '2015-08-14'), ('1.75', '2015-08-15'),\
      ('1.6', '2015-08-16'), ('1.43', '2015-08-17'), ('1.51', '2015-08-18'), ('1.54', '2015-08-19'), \
      ('1.52', '2015-08-20'), ('1.47', '2015-08-21'), ('1.71', '2015-08-22'), ('2.02', '2015-08-23'),\
       ('0.98', '2015-08-25'), ('0.8', '2015-08-26'), ('0.64', '2015-08-27'), ('0.89', '2015-08-28'),\
        ('1.42', '2015-08-29'), ('1.7', '2015-08-30'), ('1.83', '2015-08-31')]

"""
def test_average_height_per_day():
    assert average_height_per_day() == \


def test_average_homework1():
    assert average_homework1() == \
"""