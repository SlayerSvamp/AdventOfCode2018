PUZZLE_INPUT = 157901
target = str(PUZZLE_INPUT)

search_from = (len(target) + 1) * -1
recipes = '37'
first = 0
second = 1

while target not in recipes[search_from:]:
    recipes += str(int(recipes[first]) + int(recipes[second]))
    first = (first + int(recipes[first]) + 1) % len(recipes)
    second = (second + int(recipes[second]) + 1) % len(recipes)
    
print('Part One:', recipes[PUZZLE_INPUT:PUZZLE_INPUT + 10])
print('Part Two:', recipes.find(target))  # takes about 70 seconds