from utils import array_manipulator_last
from utils import array_manipulator_first
from utils import array_manipulator_deletion_empty
from utils import array_manipulator_deletion_nonempty
from utils import array_manipulator_reverse
from utils import dict_manipulator_last
        
# ①配列の末尾から要素を追加、編集、削除
print("\n① 配列の末尾から要素を追加、編集、削除")
arr_manip_last = array_manipulator_last([0,1,2])

# 末尾に要素追加
result = arr_manip_last.add(3)
print("末尾に要素追加: " + str(result))

# 末尾の要素編集
result = arr_manip_last.edit(100)
print("末尾の要素編集: " + str(result))

# 末尾の要素削除
result = arr_manip_last.delete()
print("末尾の要素削除: " + str(result))

# ②配列の先頭から要素を追加、編集、削除
print("\n② 配列の先頭から要素を追加、編集、削除")
arr_manip_first = array_manipulator_first([0, 1, 2])

# 先頭の要素追加
result = arr_manip_first.add(-1)
print("先頭に要素追加: " + str(result))

# 先頭の要素編集
result = arr_manip_first.edit(100)
print("先頭の要素編集: " + str(result))

# 先頭の要素削除
result = arr_manip_first.delete()
print("先頭の要素削除: " + str(result))

# ③配列の「特定の場所」から要素を削除して、「削除した番地はあけたまま」
print("\n③ 配列の「特定の場所」から要素を削除して、「削除した番地はあけたまま」")
arr_manip_del_emp = array_manipulator_deletion_empty([0, 1, 2])
# インデックス番号1を削除、番地はあけたまま
result = arr_manip_del_emp.delete(1)
print(result)

# ④配列の「特定の場所」から要素を削除して、「削除した番地を詰める」
print("\n④ 配列の「特定の場所」から要素を削除して、「削除した番地を詰める」")
arr_manip_del_noemp = array_manipulator_deletion_nonempty([0, 1, 2])
# インデックス番号1を削除、番地は詰める
result = arr_manip_del_noemp.delete(1)
print(result)

# ⑤配列の順番を逆さまにする
print("\n⑤ 配列の順番を逆さまにする")
arr_manip_reverse = array_manipulator_reverse([55, 22, 34, 100])
result = arr_manip_reverse.reverse()
print(result)

# ⑥配列じゃなくて「辞書型」でも同じようなことができるように
print("\n⑥ 配列じゃなくて「辞書型」でも同じようなことができるように")
dict_manip_last = dict_manipulator_last({"apple": "りんご", "grape": "ぶどう", "banana": "バナナ"})

# 辞書型の末尾に追加
result = dict_manip_last.add("orange", "オレンジ")
print("末尾に要素追加: \n" + str(result))

# 辞書型の末尾の要素編集   
result = dict_manip_last.edit("orange", "みかん")
print("\n末尾の要素編集: \n" + str(result))

# 辞書型の末尾の要素削除  
result = dict_manip_last.delete_last()
print("\n末尾の要素削除: \n" + str(result))

# 辞書型の特定の場所から要素を削除
result = dict_manip_last.delete("grape")
print("\n特定の場所から要素削除: \n" + str(result))

