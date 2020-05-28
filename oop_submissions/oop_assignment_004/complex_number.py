import math
class ComplexNumber:
    def __init__(self, real_part=0, imaginary_part=0):
        self._real_part=real_part
        self._imaginary_part=imaginary_part
        if type(real_part)==str and type(imaginary_part)!=str:
            raise ValueError("Invalid value for real part")
        #else:
         #   self._real_part=real_part
            
        if type(real_part)!=str and type(imaginary_part)==str:
            raise ValueError("Invalid value for imaginary part")
        #else:
         #   self._imaginary_part=imaginary_part
            
        if type(real_part)==str and type(imaginary_part)==str:
            raise ValueError("Invalid value for real and imaginary part")
        #else:
         #   self._real_part=real_part
          #  self._imagiinary_part=imaginary_part
        
    @property
    def real_part(self):
        return self._real_part
    @property
    def imaginary_part(self):
        return self._imaginary_part
    def __str__(self):
        return (f'{self.real_part}{self.imaginary_part:+}{"i"}')
    
    def conjugate(self):
        return ComplexNumber(self._real_part, -self._imaginary_part)
    
    def __add__(self, other):
        return ComplexNumber(self._real_part+other._real_part,self._imaginary_part+other._imaginary_part)
        
    def __sub__(self, other):
        return ComplexNumber(self._real_part-other._real_part, self._imaginary_part-other._imaginary_part)
        
    def __mul__(self, other):
        real_part=(self.real_part * other.real_part) - (self.imaginary_part*other.imaginary_part)
        img_part=(self.real_part * other.imaginary_part) + (other.real_part*self.imaginary_part)
        return (real_part, img_part)
        
    def __truediv__(self, other):
        sr, si, oor, oi=self._real_part, self._imaginary_part, other._real_part, other._imaginary_part
        r= float(oor**2+oi**2)
        return ComplexNumber((sr*oor+si*oi)/r, (si*oor-sr*oi)/r)
        
    def __abs__(self):
        return round(math.sqrt(self._real_part**2+self._imaginary_part**2),3)
        
    def __eq__(self, other):
        return (self._real_part==other._real_part) and (self._imaginary_part==other._imaginary_part)


