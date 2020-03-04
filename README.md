This is a school project done in Python. We had a day to build a calcultator.

# Calculator-Coding_Academy_by_Epitech
Calculator to be executed in terminal. Done in python

## Prerequisites
You need to have python on your computer. [here to have the right setup](https://www.python.org/downloads/ "Python's Download Page")

## How to
You need first to clone this repo and check if you have the rights in execution on **calc_UI.py** to execute the program into your terminal with the following command:
```python calc_UI.py```

## Structure

### calc.py
Calc.py contains a class **Calc** in which you have 22 methods which correspond to a calculation each time.
It includes calculations like addition, cos, tan or power of.

### calc_UI.py
With this file, we get all the information from the user and we process it using **calc.py** and return it via **calc_UI.py** which contains, obviously, the UI of the program.
We take a number or two and we return a *float*. If the input is not a number, it will return an error and ask the user to redo the operation he wanted using the right values this time.

To exit the program, you just need to enter `0` when you are in the menu.
