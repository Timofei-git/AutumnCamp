# Напиши функцию count_bits(n), которая считает количество единиц в двоичном представлении числа, используя сдвиги и побитовое И (без str и bin).

def count_bits(n):
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1

    return count

print(count_bits(32))