# 以下の①〜⑥を、組み込み関数を使わずに自前で関数として実装する
list = [1, 2, 3]
    
# ①配列の末尾から要素を追加、編集、削除
def list_add(n):
    print(list + [n])

user_add = input("配列の末尾に要素を追加してください：")
list_add(int(user_add))

def list_edit(n):
    list[-1] = [n]
    print(list)
    
user_edit = input("配列の末尾を編集してください：")
list_add(int(user_edit))

def list_delete():
    del list[-1]
    print(list)

print("配列の末尾を削除してよろしいですか？")
user_delete = input("削除する場合はyを押してください：")
if user_delete == "y":
    list_delete()

# ②配列の先頭から要素を追加、編集、削除
# ③配列の「特定の場所」から要素を削除して、「削除した番地はあけたまま」
# ④配列の「特定の場所」から要素を削除して、「削除した番地を詰める」
# ⑤配列の順番を逆さまにする
# ⑥配列じゃなくて「辞書型」でも同じようなことができるように