# CS-361-Microservice-Implementation

Hi all, this is my microservice to all the addition of new propduct .txt files and also the pulling the data on the files!

# REQUEST DATA

To reuest data you simply need to change the new_product.txt file to say either pull in the top line the the second line will need to be the six digit product number.

# Example Request

		file = open('new_product.txt', 'w')
        
		file.write(f"pull\n123456")
        
		file.close() 


# RECIEVE DATA

To recieve the data the user will need to open the now changed new_product.txt and their information they requested will now be sitting in there. The user can then take this information and replace the new_product.txt back to an empty file.

# Example Recieve

        time.sleep(2)
        file = open('new_product.txt', 'r')
        data_pulled = file.readline()
        file.close()
        file = open('new_product.txt', 'w')
        file.close()
        print(f'Here is your data: {data_pulled}')

# UML sequence diagram

![image](https://user-images.githubusercontent.com/91296239/199140838-6494bf8a-8819-4d6f-9f41-3dfa07a782fb.png)

