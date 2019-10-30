class Hash:
    def __init__(self):
        self.matriz = [['1','2','3'],['4','5','6'],['7','8','9']]     
                
    def translate_position(self, position):
        if position == 1:
            return 0, 0
        elif position == 2:
            return 0, 1
        elif position == 3:
            return 0, 2
        elif position == 4:
            return 1, 0            
        elif position == 5:
            return 1, 1
        elif position == 6:
            return 1, 2
        elif position == 7:
            return 2, 0
        elif position == 8:
            return 2, 1
        elif position == 9:
            return 2, 2    

    def mark_position(self, position_x, position_y, avatar):        
        self.matriz[position_x][position_y] = avatar

    def draw(self):
        for x in range(0,3):
            for y in range(0,3):
                print(f'[{self.matriz[x][y]:^3}]', end='')

            print()
        
    def verify_option(self, position_x, position_y):
        if self.matriz[position_x][position_y] <= '9' and self.matriz[position_x][position_y] >= '1':
            return True
        else:
            return False