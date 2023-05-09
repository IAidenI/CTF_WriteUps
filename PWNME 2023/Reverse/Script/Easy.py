# Challenge 2 Reverse
val1 = list('aezx$K+`mcwL<+_3/0S^84B^V8}~8\\TXWmnmFP_@T^RTJ')
val2 = list('1245a0eP2475cr0Fpsg0grs02g0Mg4g02LOLg5gs2g0g7')

flag = ""
# A chaque itération on recupère le caractères de val1, dans a et de val2 dans b
for a, b in zip(val1, val2):
    flag += (chr(ord(a)^ord(b))) # On effectue un XOR entre chaque caractères
print(f"Le flag est : {flag}")