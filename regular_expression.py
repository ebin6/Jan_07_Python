import re

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if re.search(pattern, password):
        return "Valid Password"
    else:
        return "Invalid Password"

# Test
password = input("Enter password: ")
print(validate_password(password))