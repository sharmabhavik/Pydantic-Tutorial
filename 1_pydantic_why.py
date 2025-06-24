# Importing necessary types and validators from pydantic and typing
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Defining the Patient schema using Pydantic's BaseModel
class Patient(BaseModel):

    # Optional field: Not required in input; defaults to None if not provided
    weight: Optional[float] = None

    # Default value for height is set to 150
    height: float = 150

    bmi: float

    # A list of allergy descriptions, all expected to be strings
    allergies: List[str]

    graduated: bool

    # Dictionary where both keys and values must be strings
    contact: Dict[str, str]

    # Email validation (e.g., "example@gmail.com" is valid; "examplegmail.com" is invalid)
    email: EmailStr

    # URL validation (e.g., "http://linkedin.com/..." is valid; "linkedin.com/..." is invalid)
    linkedin: Optional[AnyUrl] = None

    # Custom field validations
    age: int = Field(gt=0, lt=120)                      # Age must be between 1 and 119
    address: str = Field(max_length=50)                 # Address must not exceed 50 characters
    symptoms: List[str] = Field(max_items=5)            # Maximum of 5 symptoms allowed

    # Let's learn the Annotation meaning and its uses : It is used to add description, field, title, defaults, datatype everything at one place only
    name: Annotated[str, Field(default=None, title='Name', examples=['Himesh','Kartik'], description='This is the name field where you have to enter your Name')]

# Sample input dictionary in JSON format
Patient_info = {
    'name': 'Bhavik',
    'age': 22,
    # 'weight': 51.3,
    # 'height': ,  # This will default to 150 if not provided
    'bmi': 31,
    'allergies': ['steel noise'],
    'graduated': True,
    'contact': {'gmail': 'turuturu@gmail.com', 'phone': '3012092'},
    'email': 'bhavik12@gmail.com',
    'address': 'bhihdj dhuihduwd njuhduhwi',
    'symptoms': ['itching', 'headache', 'handache', 'stomachache', 'hamstring']  # Exceeding this will raise validation error
}

# Creating an instance of the Patient model using unpacked dictionary
patient1 = Patient(**Patient_info)

# Function to handle patient data insertion (example usage)
def insert_patient_data(patient: Patient):
    print(f"The name is {patient.name}, age is {patient.age}, weight is {patient.weight}, and height is {patient.height}")

# Calling the function with created patient object
insert_patient_data(patient1)