def patient_data_insert(name, age):
    print(name)
    print(age)
    print(f"Inserted Name is {name} and age is {age}")

patient_data_insert('Bhavik', 21)

# Here in upper example you can see that we have created a function with two parameters and then called it and passed the value of those parameters but age should be integer and we have passed a string value to that but it is not giving any error so it is the speciality of Python but when we are writing the production grade code then it creates Problem.

# we can use if & else here but as you know this is not good for large code


def patient_data_insert_2(name:str, age:int):
    if ((type(name) == str) & (type(age) == int)):
        if age > 0:
            print(name)
            print(age)
            print(f"Inserted Name is {name} and age is {age}")

        else:
            raise ValueError("There is error in value somewhere")

patient_data_insert_2('Priya', 12)