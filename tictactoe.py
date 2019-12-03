import learning_model

class tictactoe:
    def __init__(self):
        
        self.grid = [""] * 9

    # Tic Tac Toe Mechanics
    def __str__(self):
        """
        Formats the print to print a grid i.e.
        -  x  -
        -  x  -
        -  x  -

        returns string
        """
        grid = "GRID STATE\n"
        for i in range(0, 9, 3):
            for j in range(i, i+3):
                if self.grid[j] is "":
                    grid = grid + "-  "
                else:
                    grid = grid + self.grid[j] + "  "
            grid = grid + "\n"
        
        return grid

    def get_grid(self):
        """
        returns list with state of the grid
        """
        return self.grid

    def clear_grid(self):
        """
        Clears the grid to all empty strings (like starting state)
        """
        self.grid = [""] * 9
    
    def update_grid(self, index, move):
        """
        Checks to make sure the move is legal, then executes the move and checks if a win case was reached
        
        index: position to place move
        move: x or an o
        
        returns "x" or "o" to indicate which won if a win case was reached, otherwise nothing is returned
        """
        self.grid[index] = move.lower()
        
        win = self.check_win()
        return win

    def one_hot(self, grid=-1):
        """
        One hot encodes current grid state

        grid: list containing state of the grid
        """
        mapp = {"":[1,0,0], "o":[0,1,0], "x":[0,0,1]}
        one_hot_grid = []
        
        if grid == -1:
            grid = self.grid

        for i in range(9):
            one_hot_grid = one_hot_grid + mapp[grid[i]]

        return one_hot_grid

    def check_win(self):
        """
        Checks for win in grid
        
        returns "x" or "o" if win
        returns "" if no win
        """
        checks = [self.check_columns(), 
                  self.check_diags(), 
                  self.check_rows()]
        
        for check in checks:
            if check is not "":
                return check
        
        return ""

    def check_diags(self):
        """
        Checks for win in diagonals
        
        returns "x" or "o" if win
        returns "" if no win
        """
        if self.grid[0] == self.grid[4] and self.grid[0] == self.grid[8] and len(self.grid[0]) > 0:
            return self.grid[0]
        elif self.grid[2] == self.grid[4] and self.grid[2] == self.grid[6] and len(self.grid[2]) > 0:
            return self.grid[2]  
        return ""

    def check_rows(self):
        """
        Checks for win in rows
        
        returns "x" or "o" if win
        returns "" if no win
        """
        # Row
        for i in range(0,9,3):
            # if the entire row is the same
            if len(self.grid[i]) > 0:  
                if self.grid[i] == self.grid[i+1] and self.grid[i] == self.grid[i+2]:
                    return self.grid[i]
        return ""
                    

    def check_columns(self):
        """
        Checks for win in columns
        
        returns "x" or "o" if win
        returns "" if no win
        """
        for i in range(3):
            if len(self.grid[i]) > 0:  
                if self.grid[i] == self.grid[i+3] and self.grid[i] == self.grid[i+6]:
                    return self.grid[i]
        return ""


# if __name__ == "__main__":
    # asdf = tictactoe()
    # asdf.update_grid([1,'x#'])
    # asdf.update_grid([4,'x'])
    # asdf.update_grid([7,'x'])
    # asdf.clear_grid()
    
    # asdf.update_grid([2,'o'])
    # asdf.update_grid([4,'o'])
    # asdf.update_grid([6,'o'])

    # asdf.clear_grid()
    
    # asdf.update_grid([0,'o'])
    # asdf.update_grid([1,'o'])
    # asdf.update_grid([2,'o'])