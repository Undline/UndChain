from logging import Logger
from typing import Any, Dict, List

from logger_util import setup_logger
logger: Logger = setup_logger('Validator', 'validator.log')

class JobFile:
    def __init__(self) -> None:
        # Initialize with an empty list of jobs
        self.jobs: List[Dict[str, Any]] = []

    def add_job(self, job_data: Dict[str, Any]) -> None:
        """
        Adds a new job to the job file. The job data should be a dictionary
        containing all necessary fields for the job.
        """
        logger.info(f'Adding job from user: {job_data["user_id"]}')
        self.jobs.append(job_data)
        self.jobs.sort(key=lambda job: job["user_id"])  # Sort by user_id or any other key

    def get_sorted_jobs(self) -> List[Dict[str, Any]]:
        """
        Returns the list of jobs sorted by user_id.
        """
        return self.jobs

    def to_list(self) -> List[Dict[str, Any]]:
        """
        Converts the job file to a list of dictionaries.
        """
        return self.jobs

    
if __name__ == '__main__':
    # Create a JobFile instance
    job_file = JobFile()

    # Add a first job
    job1: Dict[str, str] = {
        "job_type": "transfer",
        "user_id": "user123",
        "resource": "UGP",
        "block_id": "0001",
        "block_time": "2024-08-30T12:34:56Z",
        "job_priority": "high"
    }
    job_file.add_job(job1)

    # Add a second job
    job2: Dict[str, str] = {
        "job_type": "Status",
        "user_id": "user456",
        "resource": "None",
        "block_id": "0001",
        "block_time": "2024-08-30T12:35:56Z",
        "job_priority": "normal"
    }
    job_file.add_job(job2)

    # Add a third job
    job3: Dict[str, str] = {
        "job_type": "transfer",
        "user_id": "user124",
        "resource": "UGP",
        "block_id": "0001",
        "block_time": "2024-08-30T12:36:56Z",
        "job_priority": "low"
    }
    job_file.add_job(job3)

    # Add a fourth job
    job4: Dict[str, str] = {
        "job_type": "transfer",
        "user_id": "user1",
        "resource": "USP",
        "block_id": "0001",
        "block_time": "2024-08-30T12:46:56Z",
        "job_priority": "low"
    }
    job_file.add_job(job4)

    # Get the sorted list of jobs
    sorted_jobs: List[Dict[str, Any]] = job_file.get_sorted_jobs()
    print("Sorted jobs:", sorted_jobs)
    # Outputs: Sorted jobs: [{'job_type': 'transfer', 'user_id': 'user123', ...}, ...]

    # Convert the job file to a list if needed
    job_list: List[Dict[str, Any]] = job_file.to_list()
    print("Job list:", job_list)