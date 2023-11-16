from profiledeco import profile_deco


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


add(1, 2)
add(4, 5)
sub(4, 5)
sub(3, 5)
sub(4, 3)

add.print_stat()
sub.print_stat()
