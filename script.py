from utils import array_manipulator_last
from utils import array_manipulator_first
from utils import array_manipulator_deletion_empty
from utils import array_manipulator_deletion_nonempty
from utils import array_manipulator_reverse
from utils import dict_manipulator_last
        
# ①array_manipulator_lastクラスをインスタンス化、引数に[0, 1, 2]を代入
arr_manip_last = array_manipulator_last([0, 1, 2])

# ①配列の末尾から要素3を追加
result = arr_manip_last.add(3)
print(result)

# ①配列の末尾の要素2を-2に編集
result = arr_manip_last.edit(-2)
print(result)

# ①配列の末尾から要素2を削除
result = arr_manip_last.delete()
print(result)

# ②array_manipulator_firstクラスをインスタンス化、引数に[0, 1, 2]を代入
arr_manip_first = array_manipulator_first([0, 1, 2])

# ②配列の先頭から要素-1を追加
result = arr_manip_first.add(-1)
print(result)

# ②配列の先頭の要素0を100に編集
result = arr_manip_first.edit(100)
print(result)

# ②配列の先頭から要素0を削除
result = arr_manip_first.delete()
print(result)

# ③配列の「特定の場所」から要素を削除して、「削除した番地はあけたまま」
arr_manip_del_emp = array_manipulator_deletion_empty([0, 1, 2])

# ③配列のインデックス番号１を削除、番地はあけたまま
result = arr_manip_del_emp.delete(1)
print(result)

# ④配列の「特定の場所」から要素を削除して、「削除した番地を詰める」
arr_manip_del_noemp = array_manipulator_deletion_nonempty([0, 1, 2])

# ④配列のインデックス番号1を削除、番地を詰める
result = arr_manip_del_noemp.delete(1)
print(result)

# ⑤配列の順番を逆さまにする(検討中)
arr_manip_reverse = array_manipulator_reverse([0, 1, 2, 3])
result = arr_manip_reverse.reverse()
print(result)

# ⑥配列じゃなくて「辞書型」でも同じようなことができるように
dict_manip_last = dict_manipulator_last({"apple": "りんご", "grape": "ぶどう", "banana": "バナナ"})

# 辞書型の末尾に追加
result = dict_manip_last.add("orange", "オレンジ")
print(result)

# 辞書型の末尾の要素編集   
result = dict_manip_last.edit("orange", "みかん")
print(result)


