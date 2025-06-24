# Importing required modules from pydantic and typing
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

# Creating the Patient schema using Pydantic's BaseModel
class Patient(BaseModel):
    # Basic patient information
    name: str                              # Name must be a string
    email: EmailStr                        # Email will be validated using standard email format
    age: int                               # Age must be an integer
    weight: float                          # Weight must be a float
    married: bool                          # Boolean field indicating marital status (True/False)
    
    # Lists and dictionary types
    allergies: List[str]                   # List containing allergy names (all strings)
    contact_details: Dict[str, str]        # Dictionary where both keys and values must be strings

    # Custom validator to check for allowed email domains
    @field_validator('email')              # Validator specifically for the 'email' field
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']  # List of allowed domains only
        domain_name = value.split('@')[-1]         # Extracting domain from email
        print(f"This is Gmail : {value}")
        print(f"This is Domain Name : {domain_name}")

        if domain_name not in valid_domains:       # If domain is not in allowed list, raise error
            raise ValueError('Not a valid domain') # Error message shown if invalid
        return value                                # Return the validated email

    # Custom validator to transform the name to uppercase
    @field_validator('name')                # Validator for 'name' field
    @classmethod
    def transform_name(cls, value):
        return value.upper()                # Converts the name to uppercase before storing

    # Custom validator for age after type coercion is done
    @field_validator('age', mode='after')   # 'mode="after"' means validation runs after value is converted to int
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:                 # Valid age must be between 1 and 99
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')  # Raise error for invalid range


# Function that simulates updating patient data
def update_patient_data(patient: Patient):
    # Printing key patient information
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')


# Sample patient data in dictionary form (similar to JSON input)
patient_info = {
    'name': 'nitish',
    'email': 'abc@icici.com',                # This email domain is allowed
    'age': '30',                             # Pydantic will convert string to integer automatically
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '2353462'}
}

# Creating a Patient object and unpacking the dictionary using **
patient1 = Patient(**patient_info)  # Triggers automatic validation and type coercion

# Calling the function to update and display patient data
update_patient_data(patient1)
