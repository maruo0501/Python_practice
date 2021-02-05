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
    arr1 = []    

    def __init__(self, input_arr: list):
        self.arr1 = input_arr

    # ②配列の先頭から要素を追加
    def add(self, n: int):
        return [n] + self.arr1
    
    # ②配列の先頭の要素を編集
    def edit(self, n:int):
        self.arr1[0] = n
        return self.arr1
 
    # ②配列の先頭から要素を削除
    def delete(self):
        del self.arr1[0]
        return self.arr1

# ③配列の「特定の場所」から要素を削除して、「削除した番地はあけたまま」
class array_manipulator_deletion_empty:
    arr1 = []

    def __init__(self, input_arr: list):
          self.arr1 = input_arr

    def delete(self, n: int):
          self.arr1[n] = []
          return self.arr1

# ④配列の「特定の場所」から要素を削除して、「削除した番地を詰める」
class array_manipulator_deletion_nonempty:
    arr1 = []

    def __init__(self, input_arr: list):
        self.arr1 = input_arr
    
    def delete(self, n: int):
        del self.arr1[n]
        return self.arr1

# ⑤配列の順番を逆さまにする(検討中)
class array_manipulator_reverse:
    arr1 = []
    def __init__(self, input_arr: list):
        self.arr1 = input_arr

    def reverse(self):
        # 長さ（要素数）取得
        cnt = 0
        for i in self.arr1:
            cnt += 1
        # 空の配列
        arr2=[0]*cnt
        last_ind=cnt-1
        # ひっくり返した番地 = 要素数 - 最初の要素番号
        for q in range(cnt):
            arr2[q]=self.arr1[last_ind - q]
        return arr2

# ⑥配列じゃなくて「辞書型」でも同じようなことができるように
class dict_manipulator_last:
    dict1 = {}
    def __init__(self, input_dict: dict):
        self.dict1 = input_dict
    
    # 辞書型の末尾に追加
    def add(self, n: str, m: str):
        if n not in self.dict1:
            self.dict1[n] = m
        return self.dict1
   
    # 辞書型の末尾の要素編集    
    def edit(self, n: str, m: str):
        if n in self.dict1:
            self.dict1[n] = n
        return self.dict1
           

