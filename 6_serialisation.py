from pydantic import BaseModel

# Address model to capture city, state, and pin code
class Address(BaseModel):
    city: str       # City name
    state: str      # State name
    pin: str        # Postal code

# Patient model with a nested Address model
class Patient(BaseModel):
    name: str                       # Patient's name
    gender: str = 'Male'            # Gender with a default value of 'Male'
    age: int                        # Patient's age
    address: Address                # Address must follow the Address model structure

# Dictionary containing address data
address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

# Creating an Address instance using the provided dictionary
address1 = Address(**address_dict)

# Patient dictionary (note: gender is not given, so default 'Male' will be used)
patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

# Creating a Patient instance
patient1 = Patient(**patient_dict)

# Serializing the Patient object to a dictionary
# exclude_unset=True: fields with default values not explicitly set (like gender) will still appear if set via default
temp = patient1.model_dump(exclude_unset=True)

print(temp)             # Display the serialized patient data as a dictionary
print(type(temp))       # Should show <class 'dict'>