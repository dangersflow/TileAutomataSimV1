import tkinter as tk

class Tile:
    state_type = None
    tile_num = 0     
        
    def __init__(self, type):
      self.state_type = type
            
class SeedTile(Tile):
    
    def __init__(self, st):
        self.tile_num = 0
        self.state_type = st
        
class NumberedTile(Tile):
      state_number = None
      
      def __init__(self, type, num):
        self.state_type = type
        self.state_number = num

       

class Assembly:
    
    def __init__(self, q_num):
       self.num_tiles = 0
       self.tiles = []
       self.quit_num = q_num
       self.add_seed_tile()

    def add_seed_tile(self):
        self.seed_tile = SeedTile("S")
        self.tiles.append(self.seed_tile)
        self.num_tiles = 1
        print("Seed Added")
        
    def add_back_state(self):
        back_tile = NumberedTile("B", 0)
        self.tiles.append(back_tile)
        self.num_tiles += 1
        print("Back Added")
        self.walk_back()
            

    def walk_back(self):
        for i in range(len(self.tiles)-1, 0, -1):
            
            if(i == 0):
               print("Seed Back")
               
            elif(i == 1 and not len(self.tiles) > 2): 
               print("Ind 1: ", i, "Type: ", self.tiles[i].state_type, " Num: ", self.tiles[i].state_number)         
            if(i >= 2):
                if(self.tiles[i].state_number == self.tiles[i - 1].state_number): 
                    self.tiles[i - 1].state_number += 1
                    print("Changed: ", i, "Type: ", self.tiles[i].state_type, " Num: ", self.tiles[i].state_number)
        display_assembly(self)            
        self.walk_forward()            

    def walk_forward(self):
        for i in range(0, len(self.tiles)):
            if(i == 0):
                continue
            if(i == len(self.tiles)-1):
                self.tiles[i].state_type = "F"
            if(i < len(self.tiles) - 1):
               self.tiles[i+1].state_number = self.tiles[i].state_number 
               self.tiles[i].state_type = "F"
            elif(i == 1 and len(self.tiles) <= 2): 
               print("Ind 1: ", i, "Type: ", self.tiles[i].state_type, " Num: ", self.tiles[i].state_number)
               self.tiles[i].state_type = "F"
              
            
                   
                 
def display_assembly(assembly):
        print("Display:")
        for i in range(len(assembly.tiles)):
            if i == 0:
                print("Index:", i, "Found:", assembly.tiles[i].state_type)
            else:
                print("Index:", i, "Found:", assembly.tiles[i].state_type, "Num:", assembly.tiles[i].state_number)         

def main():
    a = Assembly(5)
    a.add_back_state()
    a.add_back_state()
    a.add_back_state()
    a.add_back_state()
   
    
    print(len(a.tiles))
    display_assembly(a)        

main()    