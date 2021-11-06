def solution(ings, menu, sell):
    answer = 0
    
    ing=[]
    ingCost=[]
    foodCost=[]
    dish =[]
    sellCost = []
    benefit = []
    foodName = []
    
    for i in ings :
        ing.append(i.split(' ')[0])
        ingCost.append(int(i.split(' ')[1]))
                
    for food in menu :
        ingredient=food.split(' ')[1]
        dish.append(food.split(' ')[0])
        sellCost.append(food.split(' ')[2])
        result=0        
        for i in range(len(ingredient)):
            for j in range(len(ing)):          
                if ingredient[i]==ing[j]:
                     result += ingCost[j]            
        foodCost.append(result)
        
    for i in range(len(dish)):
        benefit.append(int(sellCost[i])-int(foodCost[i]))
 
    for i in menu:
        foodName.append(i.split(' ')[0])

    for i in sell:
        for j in range(len(foodName)):
            if i.split(' ')[0]==foodName[j]:
                answer += int(i.split(' ')[1])*benefit[j]

                
    return answer