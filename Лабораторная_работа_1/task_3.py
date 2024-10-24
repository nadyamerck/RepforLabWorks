size_in_bytes = 1.44 * 1024 * 1024
size_of_book = 100 * 50 * 25 * 4
max_count = int(size_in_bytes // size_of_book)

print("Количество книг, помещающихся на дискету:", max_count)
