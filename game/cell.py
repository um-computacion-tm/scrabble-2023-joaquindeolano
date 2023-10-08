from board import Board


class Cell(Board):
    
    def returnPointsAndMultiplier(self):
        simple = sum(self.wordPoints)
        if self.condicionCero == True:
            return simple * 2
        
        if self.condicionUno == True:
            return simple * 3
        
        else: 
            return simple
