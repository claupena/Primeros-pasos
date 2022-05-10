from ctypes.wintypes import PINT


num = 10
num2 = 25
print(num + num2)
print(num - num2)
print(num / num2)
print(num // num2)
print(num ** num2)
print(num * num2)
print(num % num2)


#ejercicio
peso_payaso = 112 
ctd_payaso = 87

ctd_muneca = 54
peso_muneca = 75

Procedimiento = ((ctd_payaso * peso_payaso) + (ctd_muneca*peso_muneca))

print("Total es: ",  Procedimiento)