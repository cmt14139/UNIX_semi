#2次元座標
class Coordinate:
    #コンストラクタ
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #傾きを求めるメソッド
    def slope(self):
        return self.y/self.x
    
data1 = Coordinate(2,3)
data2 = Coordinate(0,6)
try:
    print(data1.slope())
    print(data2.slope())
except ZeroDivisionError as e:
    print(e)
finally:
    print("finish")