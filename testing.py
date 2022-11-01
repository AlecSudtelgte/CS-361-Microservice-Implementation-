import time

while True:
    print('Here is the demonstration of the micro service!')
    time.sleep(1.0)
    print("Would you like to Pull data or Enter data(PULL/ENTER): ")
    answer = input()
    if answer == "PULL":
        print("Please enter the 6 digit product number: ")
        answer_2 = input()
        file = open('new_product.txt', 'w')
        file.write(f"pull\n{answer_2}")
        file.close()
        print("please wait while your data is pulled...")
        time.sleep(2)
        file = open('new_product.txt', 'r')
        data_pulled = file.readline()
        file.close()
        file = open('new_product.txt', 'w')
        file.close()
        print(f'Here is your data: {data_pulled}')
    elif answer == "ENTER":
        print("Please enter the 6 digit product number: ")
        answer_2 = input()
        print("Please enter the product information(manufacturer/model/price): ")
        answer_3 = input()
        answer_4 = input()
        answer_5 = input()
        data_store = [answer_3, answer_4, answer_5]
        file = open('new_product.txt', 'w')
        file.write(f"enter_new\n{answer_2}\n{data_store}")
        file.close()
        time.sleep(2)
