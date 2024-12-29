import secrets

# Generate a 256-bit key (32 bytes)
key = secrets.token_hex(64) # token_hex is more secure than random.randint

print("Generated Secret Key:", key)
