
def Comparison_v1():
    print("Введите, последовательно, значения списка 1")
    Act_1 = list(map(str, input().rstrip().split()))

    print("Введите, последовательно, значения списка 2")
    Act_2 = list(map(str, input().rstrip().split()))
    
    Act_3 = []
    Act_4 = []
    
    for el in Act_1:
        if el not in Act_2:
            Act_3.append(el)
            
    for el in Act_2:
        if el not in Act_1:
            Act_4.append(el)
	


    print("Следующие элементы присутствуют в Акте 1 и отсутствуют в Акте 2: ", Act_3)
    print("Следующие элементы присутствуют в Акте 2 и отсутствуют в Акте 1: ", Act_4)
	
Comparison_v1()