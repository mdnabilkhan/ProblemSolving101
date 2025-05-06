class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        def generate_special_grid(N):
            if N == 0:
                return [[0]]

            size = 2 ** (N - 1)
            prev = generate_special_grid(N - 1)
            new_size = 2 * size
            grid = [[0] * new_size for _ in range(new_size)]

            offset = size * size
            for i in range(size):
                for j in range(size):
                    grid[i][j] = prev[i][j] + 3 * offset        
                    grid[i][j + size] = prev[i][j]               
                    grid[i + size][j + size] = prev[i][j] + offset  
                    grid[i + size][j] = prev[i][j] + 2 * offset     

            return grid
        return generate_special_grid(N)