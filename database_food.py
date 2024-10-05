class person:
    def __init__(self,name,age,sex,height,weight,object_gram):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.object_gram = object_gram
class diet:
    def __init__(self,name,user,food,exercise,calorie):
        self.name = name
        self.user = user
        self.food = food
        self.exercise = exercise
        self.calorie = calorie
    
    def add_calorie(self,calorie):
        self.calorie += calorie

    
    
        
print("Let's begin with filling your data,name,age,sex,height,weight,and object_gram.")
you_user = person(input(),input(),input(),input(),input(),input())
you = diet(you_user.name,1,0,0,0) 
print("you begin the diet!")       


apple = diet("りんご",1,0,0,135)


diet.add_calorie(you,apple.calorie)

print(you.calorie)


