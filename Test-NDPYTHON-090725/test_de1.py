tests = {
    # Câu 1a: Nhập 2 số thực, in tổng và hiệu
    "Cau1a":  [
        {"input": "", "expected": ["200"]}
    ],

    # Câu 1b: Nhập tên và tuổi, in theo mẫu
    "Cau1b": [
        {"input": "", "expected": ["['100', 'apple', '3.14', 'banana', '200', 'None']"]}
    ],

    # Câu 2a: In bảng bình phương các số nguyên từ 1 đến 10
    "Cau2a":  [
        {"input": "1234567\n", "expected": ["16"]},     # 1+3+5+7=16
        {"input": "8642\n", "expected": ["0"]}
    ],

    # Câu 2b: 
    "Cau2b":[
        {"input": "19374628\n", "expected": ["4"]},     # (1,9) và (4,6) tổng 10
        {"input": "1505050\n", "expected": ["0"]},
        {"input": "555190\n", "expected": ["3"]}          # (5,0),(0,5),(5,0)
    ],
    # Câu 3:
    "Cau3a": [
        {"input": "", "expected": ["Binh - 23 - Hanoi"]}
    ], 

    "Cau3b": [
        {"input": "", "expected": ["45"]}
    ]
}
