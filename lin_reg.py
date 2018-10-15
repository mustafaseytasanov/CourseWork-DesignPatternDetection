import random
import pylab

# Генерируем 1000 всевдослучайных чисел от -100 до 100
# Тренируем модель до тех пор, пока MSE >= 0.01

w_1 = 0
w_0 = 0 # init
iteration = 0
k=1
array_x=[]
array_y = []
count = 0
amount = 1000

array_model_x = []
array_model_y =[]

def sum_1():
    sum1 = 0
    for i in range(amount):
        sum1 += w_1 * array_x[i] + w_0 - array_y[i]
    return sum1

def sum_2():
    sum2 = 0
    for i in range(amount):
        sum2 += (w_1 * array_x[i] + w_0 - array_y[i])*array_x[i]
    return sum2

def sum_3():
    sum3=0
    for i in range(amount):
        sum3 += (round(w_1, 10) * array_x[i] + round(w_0, 10) - array_y[i])**2
    return sum3

for i in range(amount):
    x = random.randint(-100,100)
    y = 7*x
    array_x.append(x)
    array_y.append(y)

for j in range(1000):
    for i in range(amount):
        iteration += 1
        count += 1
        w_0 = w_0 - k/count*2/amount*sum_1()
        w_1 = w_1 - k/count*2/amount*sum_2()
        array_model_x.append(i)
        array_model_y.append(w_1 * i + w_0)
        summa = 1/amount * sum_3()
        if iteration > 1: # Повышение скорости обучения
            if summa > summa_old:
                count += 10000
            else:
                count /= 2
        summa_old = summa
        
        j+=1
        if summa < 0.01:
            break
    if summa < 0.01:
        break


print("MSE =", summa)
print("Количество итераций: ", iteration)
if w_0>=0:
    print("Модель", w_1, "*x+", w_0)
else:
    print("Модель", w_1, "*x", w_0)

print("Визуализация...")
for i in range(1000):
    pylab.scatter(array_model_x[i], array_model_y[i], 1, "blue")

pylab.show()
