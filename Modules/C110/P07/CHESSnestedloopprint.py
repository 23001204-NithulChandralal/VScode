"""
 Write a program that used nested loops to displays a chess board but instead of the colors black and white, display the character B for black and W for white instead.
"""

a = 8 

for b in range(a):
    print(abs(b - 8) , end=' ')
    for c in range(a):
        if (b + c) % 2 == 0:
            d = 'W'
        else:
            d = 'B'
        print ("%2s"% d, end=' ')
    print()

print("   a  b  c  d  e  f  g  h ")