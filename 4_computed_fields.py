from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

# Define a Patient model to hold personal and medical info with automatic validations
class Patient(BaseModel):
    name: str                               # Full name of the patient
    email: EmailStr                         # Validated email (e.g., abc@xyz.com)
    age: int                                # Age in years
    weight: float                           # Weight in kilograms
    height: float                           # Height in meters
    married: bool                           # Marital status (True/False)
    allergies: List[str]                    # List of known allergies
    contact_details: Dict[str, str]         # Dictionary for phone, emergency contact etc.

    # Computed field to dynamically calculate BMI from weight and height
    @computed_field
    @property
    def bmi(self) -> float:
        # BMI = weight (kg) / height^2 (m²), rounded to 2 decimal places
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

# Function to process patient data
def update_patient_data(patient: Patient):
    print(patient.age)                      # Print patient's age
    print(patient.name)                     # Print patient's name
