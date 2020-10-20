class Mh: 
    def makhluk(self): 
        print(" Ini termasuk hewan") 

class Hewan(Mh): 
    def makhluk(self): 
        print(" Hewan kaki Empat") 

class Burung(Mh): 
    def makhluk(self): 
        print("Hewan kaki dua") 
  
 
class M(Hewan, Burung): 
    pass
#M.mro()     
b = M()
b.makhluk()