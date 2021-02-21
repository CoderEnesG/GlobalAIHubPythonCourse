#2. ÖDEV
# Enes GÜNGÖR
# enesgungor.gs@gmail.com



students = []
pointItems = ['homework', 'midterm', 'final']
# Burada not verilecek kategorileri seçiyoruz
points = []

needStudentNum = 5
# Kaç öğrenci arasında sıralama yapacağımız

whileOperator = 0

while(whileOperator < needStudentNum):
    studentName = str(input(f"{whileOperator+1}. Write Student Name: "))
    students.append(studentName)

    point = []
    for i in pointItems:
        point.append(int(input(f"Write {i}: ")))

    totalPoint = 0
    # Toplam puanı alır (Ortalama işleminde kullanmak için)
    for j in point:
        totalPoint += j
    points.append(totalPoint/len(point))
    # Bütün ortalamaları listeye ekler
    whileOperator += 1

info = dict(sorted(zip(points, students)))
info = dict((value, key) for (key, value) in info.items())


for k, v in info.items():
    print(f"{k} :  {v}")

print(f"**** Congratulations !!! : {students[points.index(max(points))]} ")
