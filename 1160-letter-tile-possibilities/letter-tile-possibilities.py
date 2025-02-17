class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tile_count = Counter(tiles)
        result = set()

        def backtrack(path):
            if path:
                result.add(path)
                
            for tile in tile_count:
                if tile_count[tile] > 0:
                    tile_count[tile] -= 1
                    backtrack(path + tile)  
                    tile_count[tile] += 1  
        backtrack("") 
        return len(result)