"""
1. verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

kvadrat=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]
def hell(list):
    for i in list:
        if i>0 and (i** 0.5) % 1 ==0:
            print(f'{i} ededi {int(i**0.5)} ededinin kvadratidir')
hell(kvadrat)
"""


"""
 2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
 input:[-1,1,2,2,6,7,7,'say']

girisler=[-1,1,2,2,6,7,7,'say']
def tekrarlanmayan(siyahi):
    print('Tekrarlanmayan elementler :\n')
    for j in siyahi:
        if siyahi.count(j)==1:
            print(j)
tekrarlanmayan(girisler)
"""


"""
3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

ededler = [6, 1, 2,4,6,4,1,9,1]
def tap(edeler):
     hasil = 1
     for j in ededler:
        hasil *= j
     return hasil
print(tap(ededler))
"""




 
"""

#4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın
num=int(input("Bir eded daxil edin: "))
print(list(j for j in range(1,num) if num % j==0))

"""



"""
5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.
mənim listim
mylist=['may','iyun','iyul']
bu şəkildə olacaq
{'may': 3, 'iyun': 4, 'iyul': 4}

months=['may','iyun','iyul']
print(dict((j,len(j)) for j in months))
"""






'''
6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
 verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
istifadə edəbilərsiz).
['rick', 'morty', 'summer', 'jerry', 'beth']

adlar = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

print(list(i.split()[0].lower() for i in adlar))
'''




'''
7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
results=[ 2.5, 3.5, 4.5]


list1 = [16, 32, 333]
list2 = [43, 42, 52]

son = [(list1[i] + list2[i]) / 2 for i in range(len(list1))]
print(son)

'''
