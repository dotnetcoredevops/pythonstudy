import sys
import re
import base64

def validate_reference_id(reference_id):
    # Check if the reference ID is exactly 12 characters long and contains only alphanumeric characters
    return len(reference_id) == 12 and re.match("^[a-zA-Z0-9]*$", reference_id)

def encrypt_reference_id(reference_id):
    # Encode the reference ID in base64
    encoded_bytes = base64.b64encode(reference_id.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def main():
    # Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <Reference ID>")
        sys.exit(1)

    reference_id = sys.argv[1]

    # Validate the Reference ID
    if not validate_reference_id(reference_id):
        print("Invalid Reference ID. It must be 12 characters long and contain only alphanumeric characters.")
        sys.exit(1)

    # Encrypt the Reference ID
    encrypted_id = encrypt_reference_id(reference_id)

    # Print the encrypted Reference ID
    print(f"Encrypted Reference ID: {encrypted_id}")

 
main()
