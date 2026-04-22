a, b, c = map(int, input().split())

if  (a == b and a == c and b == c):
    print("Triângulo equilátero")
elif (a==b or a==c or b==c):
    print('Triângulo isóceles')
else:
    print("Triângulo escaleno")