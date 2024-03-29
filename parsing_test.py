import tomllib
from typing import Dict, Any

class AppConfig:

    _instance: 'AppConfig' = None # type: ignore

    def __new__(cls) -> 'AppConfig':
        """
        Overrides the __new__ method to ensure only one instance of AppConfig is created.
        
        Returns:
            AppConfig: The singleton instance of the AppConfig class.
        """
        if not cls._instance:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self) -> None:
        """
        Loads the configuration data from a TOML file and stores it in the data attribute.
        """
        file_path = 'Validator/preferences.toml'
        with open(file_path, 'rb') as toml_file:
            self.data = tomllib.load(toml_file)

    def get_config(self) -> Dict[str, Any]:
        """
        Retrieves the loaded configuration data.
        
        Returns:
            Dict[str, Any]: The configuration data loaded from the TOML file.
        """
        return self.data

if __name__ == '__main__':
    
    validator_config = AppConfig()
    
    data = validator_config.get_config()

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
