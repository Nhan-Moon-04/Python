i = 3
print(i)
numbers = [1, 2, 3, 4, 5, 6, 7]
names = ["Nhan", "Nguyen", "Thien"]
print(names + numbers)
print(names[0])
print(len(numbers))
print(3 in numbers)
print("4" in numbers)
print("Nhan" in names)


# Câu lệnh điều kiện
print("Học Python thôi")
age = 16
if age < 16:
    print("Bạn chưa đủ 16 tuổi")
else:
    print("Mời bạn xem phim đi")

# Vòng lặp for và while
i = 0
while i < 10:
    print("Chào anh Nhân")
    i = i + 1

web_phim = ["Nhan.com", "NhanNE", "Chao ban nha"]
for web in web_phim:
    print(web)


# Khai báo hàm
def Tinh_Tong(n):
    tong = 0
    i = 0
    while i < n:
        tong = tong + i
        i = i + 1
        print("Tong la: ", tong)

    return tong


print(Tinh_Tong(10))


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "orange", "food", "rice"]
my_function(fruits)


def print_hello(n):
    print("Hello" * n)


print_hello(3)
print_hello(10)
times = 5
print_hello(times)


def draw_sqare():
    print("*" * 15)
    print("*", " " * 11, "*")
    print("*", " " * 11, "*")
    print("*" * 15)


draw_sqare()


# Đệ quy
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
print(tri_recursion(10))

fruit = ["apple", "orange", "food", "rice"]
print(fruit[1])
print(fruit[-1])
print(fruit[:2])
print(fruit[-3:-1])

for i in fruit:
    print(i)

for i in range(len(fruit)):
    print(fruit[i])
