import numpy as np
#  program to form a matrix and perform some basic matrix operations
rows,cols = map(int,input("Enter rows and columns:").split())
Matrix_array = np.zeros((rows,cols),int)
print(f"Rows:{rows} Colums:{cols}")
for i in range(rows):
    for j in range(cols):
        Matrix_array[i,j] = int(input("Element[{i}][{j}]"))
print(Matrix_array)
print("The Operations the program provides:\n")
print("Addition of a number to all elements (addition)")
print("Subtraction of a number to all elements (Subtraction)")
print("Multiplication of a number to all elements (multiplication)")
print("Division of a number to all elements (division)")
print("Transpose of the matrix (transpose)\n")
option = input("Select The operation:")
match option:
    case "addition":
        num = int(input("Enter the Number To add"))
        Matrix_array = Matrix_array + num
    case "subtraction":
        num = int(input("Enter the Number To subtract"))
        Matrix_array = Matrix_array - num
    case "Mmultiplication":
        num = int(input("Enter the Number To multiply"))
        Matrix_array = Matrix_array * num
    case "division":
        num = int(input("Enter the Number To divide"))
        Matrix_array = Matrix_array / num
    case "transpose":
        Matrix_array = Matrix_array.transpose()
    case _:
        print("Input is not a valid Operation")
print(Matrix_array)

