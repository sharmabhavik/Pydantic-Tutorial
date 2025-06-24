from pydantic import BaseModel

# ✅ Nested model for storing address details
class Address(BaseModel):
    city: str    # City name (e.g., Gurgaon)
    state: str   # State name (e.g., Haryana)
    pin: str     # Postal code (e.g., 122001)

# ✅ Main model representing a patient
class Patient(BaseModel):
    name: str             # Full name of the patient
    gender: str           # Gender (e.g., Male, Female)
    age: int              # Age in years
    address: Address      # Nested Address model

# ✅ Benefits of this structure:
# -----------------------------
# 🔹 Better Organization:
#     Related info like address is grouped in its own model.
# 🔹 Reusability:
#     Address model can be reused across other models (e.g., Doctor, Hospital).
# 🔹 Readability:
#     Clearly separates concerns; improves code readability and API documentation.
# 🔹 Validation:
#     Pydantic auto-validates nested models—no manual parsing needed.

# ✅ Sample address data
address_dict = {
    'city': 'Gurgaon',
    'state': 'Haryana',
    'pin': '122001'
}

# ✅ Create Address instance (will auto-validate fields)
address1 = Address(**address_dict)

# ✅ Sample patient data using nested address
patient_dict = {
    'name': 'Nitish',
    'gender': 'Male',
    'age': 35,
    'address': address1  # Nested model instance
}

# ✅ Create Patient instance (nested validation included)
patient1 = Patient(**patient_dict)

# ✅ Convert Patient model to dict, example: include specific fields
temp = patient1.model_dump(include={'name', 'age'})  # Only include name and age

# ✅ Output the result
print(temp)           # {'name': 'Nitish', 'age': 35}
print(type(temp))     # <class 'dict'>