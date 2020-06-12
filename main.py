
def Bubble_Sort(list):
    numbers = list
    length = len(numbers)
    for i in range(length -1, 0, -1):
        for j in range(0,i):
            if(numbers[j] > numbers[j+1]):
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers

numbers=[]
print("Sort of a list with Bubble sort")
x = int(input("How many numbers do you want insert?"))
for i in range(x):
    numbers.append(int(input(f"ingrese elemento, {i+1}: ")))

numbers_sort = Bubble_Sort(numbers)
print("Tu arreglo ordenado es: ")
print(numbers_sort)
