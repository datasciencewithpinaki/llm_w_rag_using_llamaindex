import numpy as np
import string
from dataclasses import dataclass

@dataclass
class JsonImage:
    imageid:int
    status:str
    
    def __post_init__(self):
        self.gen_id = JsonImage.generate_number()
        self.gen_str = Utils.generate_alphanum() #+ '==' + self.status
    
    def __str__(self):
        return f"imageid: {self.imageid}\t|\tstatus: {self.status}\t|\tgenid: {self.gen_str}\t{self.gen_id = }"
        
    def generate_number():
        num = 1000001
        yield num+1
        

class Utils:
    
    def generate_alphanum(length:int=10):
        l_mystr = np.random.choice(list(string.ascii_uppercase), 10)
        mystr = ''.join(l_mystr)
        return mystr
    
    
def main():
    image1 = JsonImage(112233, "detected")
    image2 = JsonImage(113322, "not detected")
    image3 = JsonImage(332211, "empty")
    
    images = [image1, image2, image3]
    
    for image in images:
        print(image)
        
main()
    