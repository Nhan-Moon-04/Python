# -*- coding: utf-8 -*-

arr = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tiep = 'y'
while tiep == 'y':
    plaintext = str(input("Bạn hãy nhập câu muốn mã hoá: ")).upper()
    jump = int(input("Bạn muốn dịch sang mấy ký tự? "))
    t = ''

    for character in plaintext:
        i = 0
        while i < len(arr):
            if character == arr[i]:
               character_code = arr[i + jump - len(arr) * ((i + jump) // len(arr))]
               break
            elif character == ' ':
                character_code = ' '          
            i = i + 1

        t = t + character_code

    print('Câu sau khi được mã hoá là: %s' % t)

    tiep = input('Nhập y để tiếp tục hoặc n để thoát: ')