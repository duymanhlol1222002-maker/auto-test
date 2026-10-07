# Câu 3a: Lọc các chuỗi từ danh sách hỗn hợp
ds = [1, 'apple', 3.14, 'banana', True]
ket_qua = [x for x in ds if isinstance(x, str)]
print(ket_qua)
