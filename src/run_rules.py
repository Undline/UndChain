import tomllib
import os
from typing import Dict, Any

from logging import Logger
from logger_util import setup_logger
logger: Logger = setup_logger('RunRules', 'run_rules.log')

class RunRules:
    def __init__(self, config_filename: str) -> None:
        # Construct the path to the run rules file
        root_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Navigate to the root directory
        run_rules_path: str = os.path.join(root_dir, 'Run Rules', config_filename)

        # Load the TOML file
        with open(run_rules_path, 'rb') as f:
            self.config: Dict[str, Any] = tomllib.load(f)

    def get_job_file_structure(self, co_chain_name: str = "base_job_file") -> Dict[str, Any]:
        '''
        Fetch the job file structure for the base job file or a specific co-chain.
        '''

        job_structure: Dict[str, Any] = {
            "fields": self.config[co_chain_name]["fields"],
            "mandatory": self.config[co_chain_name]["mandatory"],
            "job_types": self.config[co_chain_name]["job_types"],
            "token": self.config[co_chain_name]["token"]
        }
        return job_structure

    def get_validator_info(self) -> Dict[str, Any]:
        """
        Fetch the validator information including max and known validators.
        """

        max_validators = self.config["max_validators"]["max"]
        known_validators = self.config["known_validators"]
        return {
            "max_validators": max_validators,
            "known_validators": known_validators
        }

    def get_utilities(self) -> Dict[str, Any]:
        """
        Fetch the list of utilities available on the chain.
        """

        return self.config.get("utilities", {})

    def get_sub_domain_info(self) -> Dict[str, Any]:
        """
        Fetch the sub-domain information including linked co-chains.
        """

        return self.config.get("sub_domains", {})

    def get_governance_rules(self) -> Dict[str, Any]:
        """
        Fetch the governance rules such as voting period and quorum.
        """

        return self.config.get("governance", {})

    def get_tokenomics_rules(self) -> Dict[str, Any]:
        """
        Fetch the tokenomics rules such as token issuance and payout timing.
        """

        return self.config.get("tokenomics", {})

    def get_performance_metrics(self) -> Dict[str, Any]:
        """
        Fetch the performance metrics like max block time and latency thresholds.
        """

        return self.config.get("performance", {})

    def get_subscription_services(self) -> Dict[str, Any]:
        """
        Fetch the subscription services if they are defined.
        """

        return self.config.get("subscription_services", {})

    def validate_job_file(self, job_data: Dict[str, Any], co_chain_name: str = "base_job_file") -> bool:
        """
        Validate a job file against the mandatory fields for a specific co-chain.
        """

        mandatory_fields = self.config[co_chain_name]["mandatory"]
        return all(field in job_data and job_data[field] is not None for field in mandatory_fields)
    
    def get_known_validator_keys(self) -> list[str]:
        '''
        Retrieves a list of all the known validators from the run 
        rules file.
        '''

        known_validators = self.config["known_validators"]
        return [validator["public_key"] for validator in known_validators]
    
    def get_known_validators(self) -> list:
        return self.config["known_validators"]
    
    def get_min_validator_score(self) -> int:
        '''
        Obtain the minimum validator perception score required to join
        the network
        '''

        score = self.config.get("min_validator_score", 0)
        if isinstance(score, int):
            return score
        else:
            logger.warning(f"'min_validator_score' is not an integer. Returning default of 420.")
            return 420
        
    def get_min_partner_score(self) -> int:
        '''
        Obtain the minimum validator perception score required to join
        the network
        '''

        score = self.config.get("min_partner_score", 0)
        if isinstance(score, int):
            return score
        else:
            logger.warning(f"'min_validator_score' is not an integer. Returning default of 420.")
            return 420

# Example Usage
if __name__ == "__main__":
    run_rules = RunRules("UndChain.toml")

    # Print a list of known validators from the run rules file
    known_validators = run_rules.get_known_validators()
    print(f'Known validators: {known_validators}')
    
    # Fetching job file structure for the base job file
    job_file_structure: Dict[str, Any] = run_rules.get_job_file_structure()
    print("Job File Structure:", job_file_structure)

    # Fetching validator information
    validator_info: Dict[str, Any] = run_rules.get_validator_info()
    print("Validator Info:", validator_info)

    # Fetching utilities available on the chain
    utilities: Dict[str, Any] = run_rules.get_utilities()
    print("Utilities:", utilities)

    # Fetching sub-domain information
    sub_domain_info: Dict[str, Any] = run_rules.get_sub_domain_info()
    print("Sub-Domain Info:", sub_domain_info)

    # Fetching governance rules
    governance_rules: Dict[str, Any] = run_rules.get_governance_rules()
    print("Governance Rules:", governance_rules)

    # Fetching tokenomics rules
    tokenomics_rules: Dict[str, Any] = run_rules.get_tokenomics_rules()
    print("Tokenomics Rules:", tokenomics_rules)

    # Fetching performance metrics
    performance_metrics: Dict[str, Any] = run_rules.get_performance_metrics()
    print("Performance Metrics:", performance_metrics)

    # Fetching subscription services
    subscription_services: Dict[str, Any] = run_rules.get_subscription_services()
    print("Subscription Services:", subscription_services)

    # Example job data for validation
    job_data: Dict[str, str] = {
        "user_id": "user123",
        "job_type": "transfer",
        "block_id": "0001",
        "block_time": "2024-08-30T12:34:56Z",
        "job_priority": "high"
    }

    # Test retrieving minimum scores
    min_validator_score = run_rules.get_min_validator_score()
    min_partner_score = run_rules.get_min_partner_score()
    print(f"Minimum Validator Score: {min_validator_score}")
    print(f"Minimum Partner Score: {min_partner_score}")
    
    # Validate the job file
    is_valid: bool = run_rules.validate_job_file(job_data)
    print(f"Is job file valid? {is_valid}")
