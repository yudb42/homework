import random
import datetime
ALP = [
"A", "B", "C", "D", "E", "F", "G",
"H", "I", "J", "K", "L", "M", "N", 
"O", "P", "Q", "R", "S", "T", "U", 
"V", "W", "X", "Y", "Z", 
]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
st = datetime.datetime.now()  #開始時間
ans = input("抜けているアルファベットは？")
if ans == r:
    print("正解です")
    et = datetime.datetime.now()  #終了時間
    print(str((et-st).seconds)+"秒かかりました")  #開始～終了の時間を秒数にして出力
else:
    print("違います")