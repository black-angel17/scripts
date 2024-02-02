import hashlib
import base64

def md5_hash(input_string):

    md5_hash_object = hashlib.md5()
    md5_hash_object.update(input_string.encode('utf-8'))
    md5_hash_hex = md5_hash_object.hexdigest()
    return md5_hash_hex


def base64_encode(input_string):
    # Convert the string to bytes
    input_bytes = input_string.encode('utf-8')
    # Encode the bytes using Base64
    encoded_bytes = base64.b64encode(input_bytes)
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string




# Example usage:
input_string = "pepper"
result = md5_hash(input_string)
result1 = f"carlos:{result}"

encoded_result = base64_encode(result1)
print(f"Input: {input_string}")
print(f"Base64 Encoded: {encoded_result}")



# Example string with non-ASCII characters
original_string = "Hello, 你好, مرحبا"

# Encode the string using UTF-8
encoded_bytes = original_string.encode('utf-8')

# Display the original string and the encoded bytes
print(f"Original String: {original_string}")
print(f"UTF-8 Encoded Bytes: {encoded_bytes}")
