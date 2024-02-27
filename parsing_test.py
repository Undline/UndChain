import tomllib

# Path to your TOML file
file_path = 'Validator/preferences.toml'

# Load and parse the TOML file
with open(file_path, 'rb') as toml_file:
    data = tomllib.load(toml_file)

# Accessing data
validator_name = data['Validator']['name']
validator_public_key = data['Validator']['public_key']

# Iterating through Chains
for chain in data['Chains']:
    print(f"Chain Name: {chain['name']}")
    print(f"Chain ID: {chain['chain_ID']}")
    print(f"Network ID: {chain['network_ID']}")
    
    # If preferred validators are specified
    if 'preferred_validators' in chain:
        for validator in chain['preferred_validators']:
            print(f"  Validator Name: @{validator['name']}")
            print(f"  Validator Public Key: {validator['public_key']}")
            print(f"  Protocol: {validator['protocol']}")
            print(f"  Address: {validator['address']}")
