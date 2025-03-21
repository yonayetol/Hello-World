# class Solution:
#     def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
class Solution: 
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies) 
        foodStore = {recipes[i]:i for i in range(len(recipes))} 
        reminder = Counter() 
        ans = set() 
        def can_I_make(food_at_I): 
            if recipes[food_at_I] in reminder: return False 
            temp = 0 
            nonlocal ans 
            reminder[recipes[food_at_I]] = temp 
            for ingredient in ingredients[food_at_I]: 
                if ingredient in supplies or ingredient in ans: temp += 1 
                elif ingredient in foodStore and can_I_make(foodStore[ingredient]): temp += 1 
                if temp == len(ingredients[food_at_I]): 
                    ans.add(recipes[food_at_I]) 
                    return True 

            return False 

        for i in range(len(recipes)): 
            if recipes[i] in ans: continue 
            can_I_make(i) 
            
        return list(ans)