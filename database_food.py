class person:
    def __init__(self,user,age,sex,height,weight,object_gram,weight_history):
        self.user = user
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.object_gram = object_gram
        self.weight_history = weight_history
    
        # 体重を更新し、履歴に追加するメソッド
    def update_weight(self, new_weight):
        self.weight = new_weight
        self.weight_history.append(new_weight)  # 体重を履歴に保存
        

class diet:
    def __init__(self,name,usern,food,exercise,calorie):
        self.name = name
        self.usern = usern
        self.food = food
        self.exercise = exercise
        self.calorie = calorie
    
    # 食べ物を食べる関数　calorieに食べ物のcalorieを代入
    def add_calorie(self,calorie):
        self.calorie += calorie

    # 運動をする関数　時間をトラッキングしweightにuserの体重、exerciseに運動のメッツ(calorie)を代入
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


rice = diet("ごはん",0,1,0,336)
bread = diet("食パン1枚",0,1,0,177)
udon = diet("うどん",0,1,0,311)
#副菜
salad = diet("サラダ",0,1,0,81)
misosoup = diet("味噌汁",0,1,0,33)
#主菜
japomlett = diet("卵焼き",0,1,0,142)
natto = diet("納豆",0,1,0,200)
friedfish = diet("焼き魚(鮭)",0,1,0,118)
hamberg = diet("ハンバーグ",0,1,0,437)
#牛乳・乳製品
milk = diet("牛乳200ml",0,1,0,134)
yorgurt = diet("ヨーグルト1パック",0,1,0,62)
#果物
orenge = diet("みかん",0,1,0,34)
apple = diet("りんご",0,1,0,135)    
        

you_user = person(input(),input(),input(),input(),input(),input(),input())
you = diet(you_user.user,1,0,0,0) 
      





diet.add_calorie(you,apple.calorie)

diet.exerciseGo(you,you_user.weight,cycling.calorie)

print(you.calorie)

   
    