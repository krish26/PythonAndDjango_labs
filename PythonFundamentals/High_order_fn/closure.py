
def outer(n):
    def inner(x):
        if n > 0:
            return x + n
        elif n < 0:
            return x - abs(n)
        else:
            return x
    return inner

add_five = outer(5)
sub_three = outer(-3)
no_change = outer(0)

print(add_five(10))     # 15
print(sub_three(10))    # 7
print(no_change(10))    # 10

   