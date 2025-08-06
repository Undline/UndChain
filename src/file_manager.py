'''
FileManager

This class handles all high-level interactions between users and the Modulr
storage network. It abstracts the low-level details of sector allocation,
replication, and file tracking. It supports mutable and immutable file types,
fast and slow storage options, and integration with global user namespaces
(e.g., @Chris/my_file.txt).

Responsibilities:
- Handle file creation, reading, updating, and deletion
- Track file metadata, including mutability, storage type, and replication count
- Resolve human-readable paths to physical sectors and offsets
- Support replication strategies and auto-deletion settings
- Coordinate with allocation tables, history tracking, and validation services
'''

from typing import Dict, Optional, List

class FileManager:
    def __init__(self):
        self.user_index: Dict[str, Dict] = {}  # Maps @user to file metadata
        self.sector_map: Dict[str, Dict] = {}  # Internal representation: sector_id -> data
        self.allocation_table: Dict[str, Dict] = {}  # file_id -> sector/offset/length/etc.

    def create_file(self, user: str, file_name: str, content: str, *,
                    mutable: bool = True,
                    storage_type: str = "slow",
                    replication: int = 1,
                    ttl: Optional[int] = None) -> str:
        '''
        Stores a new file on the network and updates metadata tables.

        Args:
            user: The @username string.
            file_name: Human-readable file name.
            content: File content.
            mutable: Whether the file can be edited/deleted.
            storage_type: "fast" (SSD) or "slow" (HDD).
            replication: Number of redundant copies.
            ttl: Optional time-to-live in seconds.
        '''

        # Placeholder logic – sector selection + offset would be smart allocation
        file_id = f"{user}/{file_name}"
        sector_id = "sector_dummy"
        offset = 0
        length = len(content)

        # Index file
        self.user_index.setdefault(user, {})[file_name] = {
            "file_id": file_id,
            "mutable": mutable,
            "storage_type": storage_type,
            "replication": replication,
            "ttl": ttl,
            "created": True  # simulate created flag
        }

        self.allocation_table[file_id] = {
            "sector_id": sector_id,
            "offset": offset,
            "length": length,
            "replicas": [sector_id] * replication
        }

        self.sector_map.setdefault(sector_id, {})[file_id] = content
        return file_id

    def read_file(self, file_id: str) -> Optional[str]:
        '''
        Retrieves the file content from its mapped location.
        '''

        location = self.allocation_table.get(file_id)
        if not location:
            return None
        return self.sector_map.get(location["sector_id"], {}).get(file_id)

    def update_file(self, user: str, file_name: str, new_content: str) -> bool:
        '''
        Updates a mutable file with new content.
        '''

        file_id = f"{user}/{file_name}"
        meta = self.user_index.get(user, {}).get(file_name)
        if not meta or not meta["mutable"]:
            return False
        loc = self.allocation_table.get(file_id)
        if not loc:
            return False
        loc["length"] = len(new_content)
        self.sector_map[loc["sector_id"]][file_id] = new_content
        return True

    def delete_file(self, user: str, file_name: str) -> bool:
        '''
        Deletes a mutable file if allowed.
        '''

        file_id = f"{user}/{file_name}"
        meta = self.user_index.get(user, {}).get(file_name)
        if not meta or not meta["mutable"]:
            return False
        loc = self.allocation_table.get(file_id)
        if loc:
            self.sector_map[loc["sector_id"]].pop(file_id, None)
            self.allocation_table.pop(file_id, None)
        self.user_index[user].pop(file_name, None)
        return True

    def resolve_allocation(self, file_id: str) -> Optional[Dict]:
        '''
        Resolves file_id into its physical location and replication info.
        '''

        return self.allocation_table.get(file_id)

    def list_files(self, user: str) -> List[str]:
        '''
        Returns a list of files belonging to a user.
        '''
        
        return list(self.user_index.get(user, {}).keys())

if __name__ == "__main__":
    fm = FileManager()

    # User @Chris stores a file
    file_id = fm.create_file("@Chris", "my_file.txt", "Hello from Modulr!",
                             mutable=True, storage_type="fast", replication=2)
    print(f"\nCreated File ID: {file_id}")

    # Reading the file
    content = fm.read_file(file_id)
    print(f"Read Content: {content}")

    # Updating the file
    updated = fm.update_file("@Chris", "my_file.txt", "Updated content for testing.")
    print(f"Updated Successfully: {updated}")
    print(f"Updated Content: {fm.read_file(file_id)}")

    # Resolving allocation (where it's stored)
    allocation = fm.resolve_allocation(file_id)
    print(f"Allocation Info: {allocation}")

    # Deleting the file
    deleted = fm.delete_file("@Chris", "my_file.txt")
    print(f"Deleted: {deleted}")
    print(f"Remaining Files: {fm.list_files('@Chris')}")
