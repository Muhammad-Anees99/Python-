# formated string-1000 separater
n=10_000_000.234556
print(f'{n:,}')
# formated string-sign indicater
print(f'{n:+}')
# formated string-round off
print(f'{n:.2f}')
# we can use multiple formaters as well
m=0.57
print(f'{m:+.2%}')
print(f'{n:E}')
o=22
# padding
print(f'{o:X>25}')
# represents in 8 bit binary
print(f'{o:0>8b}')
# left
print(f'{o:X<25}')
# caret for formated to b in center
print(f'{o:^100}')
# zero padding if number is not 2-digit
r=int(input("Enter your roll number:"))
print(f'Your registration number is 2021-MC-{r:0>2}')
print('1 2 3 4')
print('2 4 6 8')
print('3 6 9 12')
print('4 6 12 16')
print("_________________")
print(f'{1:>4} {2:>4} {3:>4} {4:>4}')
print(f'{2:>4} {4:>4} {6:>4} {8:>4}')
print(f'{3:>4} {6:>4} {9:>4} {12:>4}')
print(f'{4:>4} {6:>4} {12:>4} {16:>4}')