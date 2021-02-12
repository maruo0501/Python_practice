# ①配列の末尾から要素を追加、編集、削除
class array_manipulator_last:
    arr = []
    # クラス変数arrに引数の値が代入される
    def __init__(self, input_arr: list):
        self.arr = input_arr

    # 末尾に要素追加
    def add(self, n: int):
        self.arr = self.arr + [n]
        return self.arr
    
    # 末尾の要素を編集
    def edit(self, n: int):
        if self.arr != []:
            self.arr[-1] = n
            return self.arr
        else:
            print("配列に要素が存在していません")
    
    # 末尾の要素を削除
    def delete(self):
        if self.arr != []:
            del self.arr[-1]
            return self.arr
        else:
            print("配列に要素が存在していません")

# ②配列の先頭から要素を追加、編集、削除
class array_manipulator_first:
    arr = []    
    def __init__(self, input_arr: list):
        self.arr = input_arr

    # 先頭の要素追加
    def add(self, n: int):
        self.arr = [n] + self.arr
        return self.arr
    
    # 先頭の要素編集
    def edit(self, n:int):
        self.arr[0] = n
        return self.arr
 
    # 先頭の要素削除
    def delete(self):
        del self.arr[0]
        return self.arr

# ③配列の「特定の場所」から要素を削除して、「削除した番地はあけたまま」
class array_manipulator_deletion_empty:
    arr = []
    def __init__(self, input_arr: list):
          self.arr = input_arr

    def delete(self, n: int):
          self.arr[n] = []
          return self.arr

# ④配列の「特定の場所」から要素を削除して、「削除した番地を詰める」
class array_manipulator_deletion_nonempty:
    arr = []
    def __init__(self, input_arr: list):
        self.arr = input_arr
    
    def delete(self, n: int):
        del self.arr[n]
        return self.arr

# ⑤配列の順番を逆さまにする
class array_manipulator_reverse:
    arr1 = []
    def __init__(self, input_arr: list):
        self.arr1 = input_arr

    def reverse(self):
        # 長さ（要素数）取得
        cnt = 0
        for i in self.arr1:
            cnt += 1
        # 空の配列、要素数宣言
        arr2=[0]*cnt
        last_ind=cnt-1
        # ひっくり返した番地 = 要素数 - 最初の要素番号
        for q in range(cnt):
            arr2[q]=self.arr1[last_ind - q]
        return arr2

# ⑥配列じゃなくて「辞書型」でも同じようなことができるように
class dict_manipulator_last:
    dict1 = {}
    dict2 = {} 
    def __init__(self, input_dict: dict):
        self.dict1= input_dict
    
    # 辞書型の末尾に追加
    def add(self, n: str, m: str):
        if n not in self.dict1:
            self.dict1[n] = m
        return self.dict1
   
    # 辞書型の末尾の要素編集    
    def edit(self, n: str, m: str):
        if n in self.dict1:
            self.dict1[n] = m
        return self.dict1
           
    # 辞書型の末尾の要素削除  
    def delete_last(self):
        cnt = 0
        for i in self.dict1:
            cnt += 1
        
        ans = 0
        for i in self.dict1:
            self.dict2[i]=self.dict1[i]
            ans +=1
            if ans == cnt-1:
                break
        return self.dict2
    
    # 辞書型の特定の場所から要素を削除
    def delete(self, n: str):
        if n in self.dict2:
            del self.dict2[n]
        return self.dict2


