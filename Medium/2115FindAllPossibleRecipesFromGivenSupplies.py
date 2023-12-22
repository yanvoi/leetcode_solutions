"""
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The i^th recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.
You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
Return a list of all the recipes that you can create. You may return the answer in any order.
Note that two recipes may contain each other in their ingredients.
 
Example 1:
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Example 3:
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

 
Constraints:

	n == recipes.length == ingredients.length
	1 <= n <= 100
	1 <= ingredients[i].length, supplies.length <= 100
	1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
	recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
	All the values of recipes and supplies combined are unique.
	Each ingredients[i] does not contain any duplicate values.

"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        self.needed_ingredients = {recipy : ingredients[i] for i, recipy in enumerate(recipes)}
        self.can_cook = set(supplies)
        answer = []
        for recipy in recipes:
            # remember already seen recipes to avoid loops
            self.seen = set()
            if self._dfs(recipy): answer.append(recipy)
        return answer

    @cache
    def _dfs(self, recipy: str) -> bool:
        if recipy in self.seen: return False
        if recipy in self.can_cook: return True
        if recipy not in self.needed_ingredients: return False
        self.seen.add(recipy)
        has_all_ingredients = all(self._dfs(ingredient) for ingredient in self.needed_ingredients[recipy])
        if has_all_ingredients: self.can_cook.add(recipy)
        return recipy in self.can_cook
