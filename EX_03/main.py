#2次元空間のベクトル
class Vector:
    message = 'クラスメソッドです。'
    #コンストラクタ
    def __init__(self,a,b):
        self.a=a
        self.b=b
    #位置ベクトルを表示するメソッド
    def position(self):
        print("( {} , {} )".format(self.a,self.b))
    #ベクトル和のための特殊メソッド
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)
    #クラスメソッド
    @classmethod
    def classmethod(cls):
        print(cls.message)
    #スタティックメソッド
    @staticmethod
    def staticmethod():
        print("スタティックメソッドです。")

vector1=Vector(3,-4)
vector2=Vector(2,5)
vector3=vector1+vector2
vector1.position()
vector2.position()
vector3.position()
vector1.classmethod()
vector1.staticmethod()