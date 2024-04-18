'''
try:
    num=10
    deno=0
    
    result=num/deno
    print(result)
except:
    print("Error: Denominator cannot be o.")
print("---------------------")   
try:
    even_numbers=[2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index out of Bound")
print("---------------------")    
try:
    num=int(input("enter a number:"))
    assert num % 2==0
except:
    print("not an even number")
else:
    reciprocal=1/num
    print(reciprocal)
'''
file_path="hari.txt"
try:
    with open(file_path,"r")as file:
        content=file.read()
        print(content)
except Exception as e:
    print(f"An error occured:{e}")
finally:
    print("closing the file")
        