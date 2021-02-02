# ①配列の末尾から要素を追加、編集、削除
class array_manipulator_last:
    # クラス変数aar1に空の配列代入
    arr1 = []

    # クラス変数arr1に引数の値が代入される
    def __init__(self, input_arr: list):
        self.arr1 = input_arr

    # ①配列の末尾から要素を追加
    def add(self, n: int):
        return self.arr1 + [n]
    
    # ①配列の末尾の要素を編集
    def edit(self, n: int):
        self.arr1[-1] = n
        return self.arr1
    
    # ①配列の末尾から要素を削除
    def delete(self):
        del self.arr1[-1]
        return self.arr1

# ②配列の先頭から要素を追加、編集、削除
class array_manipulator_first:
    arr2 = []    

    def __init__(self, input_arr: list):
        self.arr2 = input_arr

    # ②配列の先頭から要素を追加
    def add(self, n: int):
        return [n] + self.arr2
    
    # ②配列の先頭の要素を編集
    def edit(self, n:int):
        self.arr2[0] = n
        return self.arr2
 
    # ②配列の先頭から要素を削除
    def delete(self):
        del self.arr2[0]
        return self.arr2

# ③配列の「特定の場所」から要素を削除して、「削除した番地はあけたまま」
class array_manipulator_deletion_empty:
    arr3 = []

    def __init__(self, input_arr: list):
          self.arr3 = input_arr

    def delete(self, n: int):
          self.arr3[n] = []
          return self.arr3

# ④配列の「特定の場所」から要素を削除して、「削除した番地を詰める」
class array_manipulator_deletion_nonempty:
    arr4 = []

    def __init__(self, input_arr: list):
        self.arr4 = input_arr
    
    def delete(self, n: int):
        del self.arr4[n]
        return self.arr4

# ⑤配列の順番を逆さまにする(検討中)
class array_manipulator_reverse:
    arr5 = []

    def __init__(self, input_arr: list):
        self.arr5 = input_arr

    def reverse(self):
        arr6 = [self.arr5[-1]] + self.arr5
        del arr6[-1]
        arr7 = arr6 + [arr6[1]]
        del arr7[1]
        return arr7
        
