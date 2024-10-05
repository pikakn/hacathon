class person:
    def __init__(self,user,age,sex,height,weight,object_gram):
        self.user = user
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.object_gram = object_gram
        

class diet:
    def __init__(self,name,usern,food,exercise,calorie):
        self.name = name
        self.usern = usern
        self.food = food
        self.exercise = exercise
        self.calorie = calorie
    
    def add_calorie(self,calorie):
        self.calorie += calorie

    def exerciseGo(self,weight,exercise,duration):
        calorie = exercise*weight*duration*1.05
        self.calorie -= calorie
        return calorie 
    

#消費カロリー(kcal) ＝ メッツ × 体重(kg)×運動時間(分) ×1.05
#運動の消費カロリー
cycling = diet("自転車", 0, 0, 1, 4)
walking = diet("ウォーキング", 0, 0, 1, 3)
running = diet("ランニング", 0, 0, 1, 7)
dance = diet("ダンス", 0, 0, 1, 4)
swimming = diet("水泳", 0, 0, 1, 5)
weak_strength_training = diet("筋トレ(低強度)", 0, 0, 1, 4)
strong_strength_training = diet("筋トレ(高強度)", 0, 0, 1, 8)
yoga = diet("ヨガ", 0, 0, 1, 2.5)
trekking = diet("登山", 0, 0, 1, 5)
weak_sports = diet("スポーツ", 0, 0, 1, 4)
strong_sports = diet("スポーツ(激しめ)", 0, 0, 1, 8)    
    
        
print("Let's begin with filling your data,name,age,sex,height,weight,and object_gram.")
you_user = person(input(),input(),input(),input(),input(),input())
you = diet(you_user.user,1,0,0,0) 
print("you begin the diet!")       


apple = diet("りんご",1,0,0,135)


diet.add_calorie(you,apple.calorie)

diet.exerciseGo(you,you_user.weight,cycling.calorie)

print(you.calorie)

   
    