class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                # Check if current position is safe
                # cols set tracks which columns have queens
                # diag1 tracks diagonal (row - col is constant)
                # diag2 tracks anti-diagonal (row + col is constant)
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Place queen and recurse
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                count += backtrack(row + 1, cols, diag1, diag2)
                
                # Backtrack - remove queen
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
            
            return count
        
        return backtrack(0, set(), set(), set())
