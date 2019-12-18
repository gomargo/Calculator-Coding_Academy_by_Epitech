#!/usr/bin/env python3
import math

class Calc(object):  
    def add(self, a, b): # addition
        r = a + b
        print("%f + %f = %f" %(a, b, r))

    def substract(self, a, b): # substract
        r = a - b
        print("%f - %f = %f" %(a, b, r))
    
    def multiply(self, a, b): # multiplication
        r = a * b
        print("%f x %f = %f" %(a, b, r))

    def divide(self, a, b): # divide
        r = a / b
        print("%f / %f = %f" %(a, b, r))

    def _sin(self, a): # Sine in radians
        r = math.sin(a)
        print("Sin(%f) = %f" %(a, r)) #convert int to float

    def _cos(self, a): # Cosine in radians
        r = math.cos(a)
        print("Cos(%f) = %f" %(a, r)) #convert int to float

    def _tan(self, a): # Tan in radians
        r = math.tan(a)
        print("Tan(%f) = %f" %(a, r)) #convert int to float
    
    def cosecrad(self, a): # Cosecant in radians
        r = 1/math.sin(a)
        print("Sin(%f) = %f" %(a, r)) #convert int to float
    
    def secrad(self, a): # Secant in radians
        r = 1/math.cos(a)
        print("Sec(%f) = %f" %(a, r)) #convert int to float
    
    def cotrad(self, a): # Cot in radians
        r = 1/math.tan(a)
        print("Cot(%f) = %f" %(a, r)) #convert int to float
    
    def sindeg(self, a): # Sine in degrees
        r = math.sin(math.radians(a))
        print("Sin(%f) in degree = %f" %(a, r)) #convert int to float
    
    def cosdeg(self, a): # Cosine in degrees
        r = math.cos(math.radians(a))
        print("Cos(%f) in degree = %f" %(a, r)) #convert int to float

    def tandeg(self, a): # Tan in Degrees
        r = math.tan(math.radians(a))
        print("Tan(%f) in degree = %f" %(a, r)) #convert int to float

    def cosecdeg(self, a): # Cosecant in Degrees
        r = 1/math.sin(math.radians(a))
        print("Sec(%f) in degree = %f" %(a, r)) #convert int to float
    
    def secdeg(self, a): # Secant in Degrees
        r = 1/math.cos(math.radians(a))
        print("Sec(%f) in degree = %f" %(a, r)) #convert int to float
    
    def cotdeg(self, a): # Cot in Degrees
        r = 1/math.tan(math.radians(a))
        print("Cot(%f) in degree = %f" %(a, r)) #convert int to float
    
    def ln(self, a): # Natural Log
        r = math.log(a)
        print("Log(%f) = %f" %(a, r)) #convert int to float

    def lnten(self, a): # Base 10 log
        r = math.log10(a)
        print("Log10(%f) = %f" %(a, r)) #convert int to float
    
    def lnbasex(self, a, x): # Log Base 'x'
        r = math.log(a,x)
        print("Log base(%f)(%f) = %f" %(x, a, r)) #convert int to float
    
    def sqroot(self, a): # Square Root
        r = math.sqrt(a)
        print("Square Root(%f) = %f" %(a, r)) #convert int to float
    
    def _pi(self): # Pi
        print("Pi = ", math.pi) #convert int to float

    def powerOf(self, a, b): # Power Of
        r = math.pow(a, b)
        print("%f ^ (%f) = %f" % (a, b, r)) #convert int to float