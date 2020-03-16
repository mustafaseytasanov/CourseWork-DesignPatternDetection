# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:31:51 2020

@author: Mustafa
"""

import numpy as np
#import tflearn
#import random

from sklearn.linear_model import LogisticRegression

f1 = open(r'C:\Users\Mustafa\Desktop\singleton_done.txt', 'r', encoding='utf-8')
array1 = []
#Читаем файл построчно
for line in f1:
    array1.append(line)
f1.close()

f2 = open(r'C:\Users\Mustafa\Desktop\template_method_done.txt', 'r', encoding='utf-8')
array2 = []
for line in f2:
    array2.append(line)
f2.close()

f3 = open(r'C:\Users\Mustafa\Desktop\template_method_done_test.txt', 'r', encoding='utf-8')
array3 = []
for line in f3:
    array3.append(line)
f3.close()


'''
функция, которая чистит код
'''
def clean(array, i):
    if "/*" in array[i]:
        i+=1
        while "*/" not in array[i]:
            i+=1
        i+=1
    if "import" in array[i]:
        i+=1
    if "package" in array[i]:
        i+=1


'''
1. NSF - singleton (100 % works)
'''
def fun_NSF(array, i, amount):
    arr_NSF=[]
    for k in range(amount):
        i+=1
        clean(array, i)
        NSF=0
        while "###" not in array[i]:

            if "static" in array[i]:
                if ';' in array[i]:
                    NSF += 1
            i+= 1
            clean(array,i)
        arr_NSF.append(NSF)
    return arr_NSF

arr_NSF = fun_NSF(array1, 0, 84)

'''
2. NOPC - singleton (100 % works)
'''

def fun_NOPC(array, i, amount):
    arr_NOPC = []
    for k in range(amount):
        i+=1
        clean(array, i)
        NOPC=0
        name=""
        while "###" not in array[i]:
    
            if "class" in array[i]:

                arr = array[i].split()
                if ("class" in arr) and ('{' in arr):
                    a = arr.index("class")
                    name = arr[a+1]
                
                    while "###" not in array[i]:
                        i += 1
                        clean(array, i)
                        if name in array[i]:
                            if "private" in array[i]:
                                if "{" in array[i]:
                                    NOPC += 1
            else:        
                i+=1
                clean(array, i)
        arr_NOPC.append(NOPC)
    return(arr_NOPC)

arr_NOPC = fun_NOPC(array1, 0, 84)
     
'''
3. NOM - singleton, TemplateMethod, adapter, state, strategy
NOM(singleton) 100% works
'''
def fun_NOM(array, i, amount):
    arr_NOM = []
    for k in range(amount):
    
        i+=1
        clean(array, i)
        NOM=0   
        while "###" not in array[i]:

            if ('(' in array[i]) and (')' in array[i]) and ('{' in array[i]) and \
              array[i].find("{", 0) > array[i].find(")", 0):
                if ("byte" in array[i]) and (array[i].find("byte", 0) < array[i].find("(", 0)) \
                 or ("short" in array[i]) and (array[i].find("short", 0) < array[i].find("(", 0)) \
                 or ("int" in array[i]) and (array[i].find("int", 0) < array[i].find("(", 0)) \
                 or ("long" in array[i]) and (array[i].find("long", 0) < array[i].find("(", 0)) \
                 or ("float" in array[i]) and (array[i].find("float", 0) < array[i].find("(", 0)) \
                 or ("double" in array[i]) and (array[i].find("double", 0) < array[i].find("(", 0)) \
                 or ("char" in array[i]) and (array[i].find("char", 0) < array[i].find("(", 0)) \
                 or ("boolean" in array[i]) and (array[i].find("boolean", 0) < array[i].find("(", 0)) \
                 or ("void" in array[i])and (array[i].find("void", 0) < array[i].find("(", 0)) \
                 or ("String" in array[i]) and (array[i].find("String", 0) < array[i].find("(", 0)) and \
                   (array[i][array[i].find("String", 0)-1] != '<') \
                 or ("static" in array[i]) and (array[i].find("static", 0) < array[i].find("(", 0)):
                    NOM+=1
            i+=1
            clean(array, i)
        arr_NOM.append(NOM)
    return arr_NOM

arr_NOM_1 = fun_NOM(array1, 0, 84)

'''
4. NSM - singleton (100% works)
'''
def fun_NSM(array, i, amount):
    arr_NSM = []
    for k in range(amount):
        i+=1
        clean(array, i)
        NSM=0
        while "###" not in array[i]:

            if "static" in array[i]:
                if '(' in array[i]:
                    if ';' not in array[i]:
                        if "=" in array[i]:
                            if array.find('=', 0) > array.find('(', 0):
                                NSM += 1
                        else:
                            NSM += 1
                
            i+= 1
            clean(array, i)
        arr_NSM.append(NSM)
    return arr_NSM

arr_NSM = fun_NSM(array1, 0, 84)


'''
5. NOAM - TemplateMethod, adapter, state, strategy
NOAM (TempalateMethod) 100% works
'''
def fun_NOAM(array, i, amount):
    arr_NOAM = []
    for k in range(amount):
        i+=1
        NOAM = 0
        while "###" not in array[i]:

            if "abstract" in array[i] and '(' in array[i]:
                NOAM += 1
            i+=1
        arr_NOAM.append(NOAM)
    return arr_NOAM
    
arr_NOAM_2 = fun_NOAM(array2, 0, 88)

'''
6. NORM - TemplateMethod, adapter, state, strategy
NORM (TemplateMethod) 100% works
'''
def fun_NORM(array, i, amount):
    arr_NORM = []
    for k in range(amount):
        i+=1
        NORM = 0
        while "###" not in array[i]:

            if "@Override" in array[i]:
                NORM += 1
                
            i += 1
        arr_NORM.append(NORM)
    return arr_NORM
    
arr_NORM_2 = fun_NORM(array2, 0, 88)

'''
3. NOM - singleton, TemplateMethod, adapter, state, strategy
NOM (TemplateMethod) 100% works
'''
def _fun_NOM(array, i, amount):
    arr_NOM = []
    for k in range(amount):
    
        i+=1
        clean(array, i)
        NOM=0   
        while "###" not in array[i]:

            if ('(' in array[i]) and (')' in array[i]) and ('{' in array[i]) and \
              array[i].find("{", 0) > array[i].find(")", 0):
                if ("byte" in array[i]) and (array[i].find("byte", 0) < array[i].find("(", 0)) \
                 or ("short" in array[i]) and (array[i].find("short", 0) < array[i].find("(", 0)) \
                 or ("int" in array[i]) and (array[i].find("int", 0) < array[i].find("(", 0)) \
                 or ("long" in array[i]) and (array[i].find("long", 0) < array[i].find("(", 0)) \
                 or ("float" in array[i]) and (array[i].find("float", 0) < array[i].find("(", 0)) \
                 or ("double" in array[i]) and (array[i].find("double", 0) < array[i].find("(", 0)) \
                 or ("char" in array[i]) and (array[i].find("char", 0) < array[i].find("(", 0)) \
                 or ("boolean" in array[i]) and (array[i].find("boolean", 0) < array[i].find("(", 0)) \
                 or ("void" in array[i]) and (array[i].find("void", 0) < array[i].find("(", 0)) \
                 or ("final" in array[i]) and (array[i].find("final", 0) < array[i].find("(", 0)) \
                 or ("List<Model>" in array[i]) and (array[i].find("List<Model>", 0) < array[i].find("(", 0)) \
                 or ("String" in array[i]) and (array[i].find("String", 0) < array[i].find("(", 0)) and \
                   (array[i][array[i].find("String", 0)-1] == ' ') and \
                   (array[i][array[i].find("String", 0)+6] == ' ') \
                 or ("static" in array[i]) and (array[i].find("static", 0) < array[i].find("(", 0)):
                    NOM+=1
            else:
                
                if "abstract" in array[i] and '(' in array[i]:
                    NOM += 1
                    
            i+=1
            clean(array, i)
        arr_NOM.append(NOM)
    return arr_NOM

arr_NOM_2 = _fun_NOM(array2, 0, 88)

'''
Данные для обучения (детектим каждый шаблон)
'''
def pack():
    
    matrix = []
    train_y = []
    
    for k in range(84):
        matrix.append(np.array([arr_NSF[k], arr_NOPC[k], arr_NOM_1[k], arr_NSM[k], 0, 0]))
        train_y.append(0)
    for k in range(88):
        matrix.append(np.array([0, 0, arr_NOM_2[k], 0, arr_NOAM_2[k], 0]))
        train_y.append(1)
    for k in range(88):
        matrix.append(np.array([0, 0, arr_NOM_2[k], 0, 0, arr_NORM_2[k]]))
        train_y.append(2)

    train_X = np.asarray(matrix)
    train_y = np.asarray(train_y)

    return train_X, train_y


train_X, train_y = pack()

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#clf = LogisticRegression(solver='lbfgs')
clf = LogisticRegression()
clf.fit(train_X, train_y)

'''
Данные для детектирования
'''
    
#Singleton
arr_NSF_1_test = fun_NSF(array1, 2428, 36)
arr_NOPC_1_test = fun_NOPC(array1, 2428, 36)
arr_NOM_1_test = fun_NOM(array1, 2428, 36)
arr_NSM_1_test = fun_NSM(array1, 2428, 36)
arr_NOAM_1_test = fun_NOAM(array1, 2428, 36)
arr_NORM_1_test = fun_NORM(array1, 2428, 36)

#TemplateMethod
arr_NSF_2_test = fun_NSF(array3, 0, 76)
arr_NOPC_2_test = fun_NOPC(array3, 0, 76)
arr_NOM_2_test = _fun_NOM(array3, 0, 76)
arr_NSM_2_test = fun_NSM(array3, 0, 76)
arr_NOAM_2_test = fun_NOAM(array3, 0, 76)
arr_NORM_2_test = fun_NORM(array3, 0, 76)


def unpack():

    matrix_test = []
    test_y = []
    
    for k in range(36):
        matrix_test.append(np.array([arr_NSF_1_test[k], arr_NOPC_1_test[k], arr_NOM_1_test[k], \
                        arr_NSM_1_test[k], arr_NOAM_1_test[k], arr_NORM_1_test[k]]))
        test_y.append(0)
    
    for k in range(76):
        matrix_test.append(np.array([arr_NSF_2_test[k], arr_NOPC_2_test[k], arr_NOM_2_test[k], \
                        arr_NSM_2_test[k], arr_NOAM_2_test[k], arr_NORM_2_test[k]]))
        if k%2 == 0:
            test_y.append(1)
        else:
            test_y.append(2)
    
    
    test_X = np.asarray(matrix_test)
    test_y = np.asarray(test_y)
    
    return test_X, test_y


test_X, test_y = unpack()
#print(clf.predict(test_X) == test_y)
print(clf.predict(test_X))