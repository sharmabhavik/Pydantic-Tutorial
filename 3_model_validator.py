from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

# Patient model representing structured patient data with validations
class Patient(BaseModel):
    name: str                                # Patient's full name
    email: EmailStr                          # Valid email format (e.g., abc@xyz.com)
    age: int                                 # Patient's age as integer
    weight: float                            # Patient's weight in kg
    married: bool                            # Marital status: True or False
    allergies: List[str]                     # List of allergy strings
    contact_details: Dict[str, str]          # Dictionary with contact info (e.g., phone, emergency)

    # Model-level validator: runs after all fields are parsed & validated
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        # If patient's age is above 60, ensure 'emergency' contact is provided
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

# Function to simulate an update or processing of patient data
def update_patient_data(patient: Patient):
    print(patient.name)                     # Print patient name
    print(patient.age)                      # Print patient age
    print(patient.allergies)                # Print list of allergies
    print(patient.married)                  # Print marital status
    print('updated')                        # Indicate update completion

# Sample patient input (e.g., coming from a form or API)
patient_info = {
    'name': 'nitish',
    'email': 'abc@icici.com',
    'age': '65',                            # String will be coerced to int by Pydantic
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '2353462',
        'emergency': '235236'              # Required if age > 60
    }
}

# Creating a Patient instance with validation and auto-type coercion
patient1 = Patient(**patient_info)

# Process or update patient information
update_patient_data(patient1)
