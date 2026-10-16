'''
sudent: mohamed islem ben hadj hassine
mail: mohamedislem.benhadjhassine@etudian-isi-utm.tn
'''
def element_product(a,b):
    if len(a) != len(b):
        raise ValueError("arrays must have the same length")
    c= [a[i]*b[i] for i in range (len(a))]
    return c

try :
    n=int(input("type the length of the arrays :"))

    print(f"enter {n} integer for array a:")
    array_a=[]
    for i in range (n):
        val = int(input(f"{n-i-1} left, element number {i+1} :"))
        array_a.append(val)

    print(f"enter {n} integer for array b:")
    array_b=[]
    for i in range (n):
        val = int(input(f"{n-i-1} left, element number {i+1} :"))
        array_b.append(val)
    
    result = element_product(array_a,array_b)

    print("---result---")
    print("array a :",array_a)
    print("array b :",array_b)
    print("the product array c :",result) 

except ValueError as e:
    print("enter valid integers :",e)
