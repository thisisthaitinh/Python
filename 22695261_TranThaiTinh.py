# import library
from math import ceil
from prettytable import PrettyTable


# thong tin sinh vien
def studentInformation():
    print("Thông tin sinh viên: ")
    print("- MSSV: 22695261")
    print("- Họ và tên: Trần Thái Tính")
    print("- Lớp: KHMT18BTT")


# menu
def menu(arg):
    if arg == 1:
        Cau2()
    elif arg == 2:
        Cau3()
    elif arg == 3:
        Cau4()
    else:
        print("Thoát chương trình thành công!")


# tim uoc so chung lon nhat
def USCLN(a, b):
    result = min(a, b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result


# cau 2
def Cau2():
    a = int(input("\tNhập a: "))
    b = int(input("\tNhập b: "))
    print("Ước số chung lớn nhất của " + str(a) + " và " + str(b) + " là: " + str(USCLN(a, b)))
    print("Bội số chung nhỏ nhất của " + str(a) + " và " + str(b) + " là: " + str(ceil(a * b / USCLN(a, b))))


# kiem tra so nguyen to
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# kiem tra so may man
def is_lucky(num):
    digits = str(num)
    for digit in digits:
        if digit != '6' and digit != '8':
            return False
    return True


# cau 3
def Cau3():
    list_A = []
    list_B = []
    n = int(input("\nNhập số phần tử của List A: "))
    for i in range(0, n):
        x = int(input("\tPhần tử thứ {}: ".format(i + 1)))
        list_A.append(x)
    sum_A = sum(list_A)

    prime_numbers = [num for num in list_A if is_prime(num)]
    sum_primes = sum(prime_numbers)

    lucky_numbers = [num for num in list_A if is_lucky(num)]
    print("Tổng các phần tử trong list A:", sum_A)
    print("Các số nguyên tố trong list A:", *prime_numbers, sep=", ")
    print("Tổng các số nguyên tố trong list A:", sum_primes)
    print("Số may mắn trong list A:", *lucky_numbers, sep=", ")

    m = int(input("\nNhập số phần tử của list B: "))
    for i in range(0, m):
        y = int(input("\tPhần tử thứ {}: ".format(i + 1)))
        list_B.append(y)

    list_C = sorted(list_A + list_B)

    table = PrettyTable()
    table.field_names = ["List A", "List B", "Số nguyên tố trong list A", "Số may mắn trong list A", "List C"]
    table.add_row(["\n".join(str(num) for num in list_A),
                   "\n".join(str(num) for num in list_B),
                   "\n".join(str(num) for num in prime_numbers),
                   "\n".join(str(num) for num in lucky_numbers),
                   "\n".join(str(num) for num in list_C)])

    table.align = "c"  # Set alignment to "middle"

    print("List C:", *list_C, sep=", ")
    print("\nHiển thị danh sách dưới dạng bảng: ")
    print(table)


# cau 4
def Cau4():
    sinhvien = []
    n = int(input("\nNhập số lượng sinh viên: "))
    for i in range(n):
        name = input("\tSinh viên thứ {}: ".format(i + 1))
        result = float(input("\tĐiểm: "))
        sinhvien.append({'name': name, 'result': result})

    print_results(sinhvien)


def print_results(sinhvien):
    highest_result = max(sinhvien, key=lambda x: x['result'])
    lowest_result = min(sinhvien, key=lambda x: x['result'])
    sorted_sinhvien = sorted(sinhvien, key=lambda x: x['result'])

    table = PrettyTable()
    table.field_names = ["Sinh viên", "Điểm"]
    for student in sorted_sinhvien:
        table.add_row([student['name'], student['result']])

    print("Sinh viên có kết quả cao nhất: {} (Điểm: {}).".format(highest_result['name'], highest_result['result']))
    print("Sinh viên có kết quả thấp nhất: {} (Điểm: {}).".format(lowest_result['name'], lowest_result['result']))
    print("\nSắp xếp các sinh viên theo kết quả học tập tăng dần: ")
    print(table)


studentInformation()

print("1. Câu 2 (2.0 điểm).")
print("2. Câu 3 (4.0 điểm).")
print("3. Câu 4 (3.0 điểm).")
choice = int(input("Mời bạn nhập lựa chọn: "))

menu(choice)

# code provided by Tran Thai Tinh.