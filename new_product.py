import time


while True:
    time.sleep(1.0)
    new_product = ""
    file = open('new_product.txt', 'r')
    for x, line in enumerate(file):
        if x == 0:
            new_product = str(line)
        if x == 1:
            info = int(line)
        if x == 2:
            product_info = line
    file.close()
    if len(new_product) != 10:
        if len(new_product) == 5:
            file = open(f'{info}.txt', 'r')
            product_info = file.readline()
            file.close()
            file = open('new_product.txt', 'w')
            file.write(product_info)
            file.close()
            time.sleep(2)
        continue
    elif len(new_product) == 10:
        file = open(f'{info}.txt', 'w')
        file.write(product_info)
        file.close()
        print("Product Added")
        file = open('new_product.txt', 'w')
        file.close()


