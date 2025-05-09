# What is UndChain?

UndChain is a **Layer 1 blockchain** built to power a decentralized cloud platform that is **permissionless, trustless, and service-oriented**.

It is not a fork, not a derivative — it’s a ground-up architecture designed to support:
- Decentralized storage
- Computation
- Access to devices and services
- Economic systems with built-in user protection

UndChain brings together multiple disciplines: networking, cryptography, distributed systems, cloud infrastructure, and economics.

There is **no direct equivalent** to UndChain — it is not simply a Filecoin, Flux, or Ethereum variant. It combines elements of those systems, but in a fully integrated, modular, and unified way.

This makes it both extremely powerful and inherently complex. That’s why we split the project into clear domains.

At the **center** of that system is **UndChain Core** — the protocol layer responsible for all communication, coordination, validation, and shared infrastructure that powers the rest of the network.

---
# Understanding UndChain Core

**Purpose**: This document is being made as a reference guide into how and why certain aspects of the code were written. This is meant to provide insight into why the structure is made the way it is architecturally and how it can interlink together (i.e. big picture)

Each section will be separated based on a theme or task that is meant to be completed. It should also be accompanied with all of the relevant files for that section. 

This document is a part of a much larger system. The goal is to have each piece of the system be its own self contained system and lays the foundation for how our co-chains will operate on the network.

---
# What is UndChain Core?

UndChain itself is a **layer 1** project that is focused on providing decentralized cloud computing that is permissionless. It is a very advanced and novel system that comprises of many systems working together in order to make this happen. One of the greatest difficulties in this system is making it trustless. Nothing compares to UndChain as nothing exists to compare it to, we are in a league of our own which places us at a significant lead over anyone wanting to make a system like this. This project has been split between several disciplines with the UndChain core team being at the center of that system; its the foundation that will drive all systems (which we call co-chains).

UndChain core comprises of all of the fundamental structures on UndChain and defines how the network operates. It defines 

- Structure for all user types (Validators, Clients, Chain Owners and Partners). 
	- This includes how each are meant to contact one another (networking protocols)
- It also defines base protocol elements, this includes things like our asset protection systems (Will, Freeze and Limiter)
- defines our standard asset contact types. 
- How encryption works on chain
- Defines the perception score (reputation system) and establishes the algorithm for loss and gain.
- Defines base messaging system that allows users to communicate with one another on chain
- Defines our scalability protocols and when to create subdomains (mixture of latency and quantity of users)
- Defines consensus types and the receipt system
	- Storage - Takes 4GB chucks of storage and uses those as 'containers' across the network for user to fill with data
	- Computation - Splits tasks among multiple partners who then are issued standard challenges during execution to determine if they are computing data or not
	- Access - Uses witnesses to determine if an event occurred and shows proof of those events
- Maintains metrics on the network
	- Analytics
	- List of Co-chains
- Defines payment systems
	- Subscription models
	- Redemption system
	- Return policy
- Defines core protocols
	- Convergence protocol - meant to keep the size of the blockchain small
	- UnaS - System that maps user names to public keys

---

# Validator.py Operation

This section goes over how a validator is supposed to interact with one another (does not include interactions between other user types). Validators go through stages on initialization in order to sync with the group. Found in `validator.py` we can see that a validator has multiple states:

```Python
class ValidatorState(Enum):

    DISCOVERY = 1
    SYNC = 2
    PENDING = 3
    REDIRECT = 4
    ACTIVE = 5
    ERROR = 6
```

Each state defines a moment in time as the validator is initializing, we start in discovery. This is where we are actively searching for a network or if we are a known validator for the network we want to work for we only reach out to the other known validators. 

- **Discovery** - This happens when the validator first initializes and doesn't end until it finds another validator that is NOT in discovery mode.
- **Sync** - This mode is reserved in the event that a validator has found another validator that is in the active state and has made a request to sync it files with the active validator. 
- **Pending** - This state is reserved when a validator has been picked to serve in the active validator pool and is preparing to go live
- **Redirect** - This happens when the validator is not active (meaning they are not participating in the pool due to the hard limit in number of validators). This was created so that if another user accidently contacts them they can redirect that use to the active validators.
- **Active** - This is reserved for validators who are actively accepting job requests on the network and directing traffic by matching partners and clients.
- **Error** - This state is reserved for any errors that are encountered during this process. Should be set inside every error handler found in the validator. 

```Python
def __init__(self, public_key: bytearray, rules_file: str) -> None:

        logger.info("Initializing Validator")

        self.state = ValidatorState.DISCOVERY

        self.public_key: bytearray = public_key

        self.run_rules = RunRules(rules_file)

        logger.info(f"Rules for {rules_file} have been loaded")

        self.run = False

        self.is_known_validator: bool = self.check_if_known_validator()

        self.comm: AbstractCommunication

  

        self.packet_generator = PacketGenerator("2024.09.30.1") # Get the version from the run rules file

        self.packet_handler = PacketHandler(self.packet_generator)
```

In the above code we see that 
- we are setting our current state into Discovery (states can be pinged from other validators so they know at what stage the validator is at), 
- we then pull our public key in as this can be shared with others upon request, 
- then we load the run rules file which can be thought of as a configuration file. At this stage the reason its needed is you need the routing information for the known validators. 
- We then set run to false as this is used later inside of the listener and stop methods. Code is async so we need to know when to stop or if it's running.
- Then we check to see if we are a known validator this was used as a conditional to diverge the path between known and unknown validator, but what I found was they both use the same methods (they both reach out to known validators and attempt to get added to the active validator list). I decided to leave this in as there may be a reason I need it in the future, if not we need to delete it. 
- We then call the abstract communication class which was designed this way to allow various mediums of communication. The most common method will be TCP/IP, but the goal is to expand the network to operate outside the traditional internet so a more general approach was needed here. 
- Then we move to the packet generator which is responsible for forming the packets that are meant to be sent and received on the network (currently only focused on validators). These packets form a small header at the beginning so they can be quickly identified as to what type of message this is. The variable passed in is the version number of the communication protocol being used. All versions on UndChain follow a `YYYY.MM.DD.x` format where Y = Year, M = month, D = day and x is any subversion that may exist 9in the event that a co-chain need to have a hot patch for a security flaw). This should be pulled from the run rules file and not statically assigned as I have done. 
	- Reasoning behind version is that if we have to expand our communication protocol a receiver can look at the version and tell if they can interpret what is being sent. If not then they send a message back to the sender with a version that they are using and depending on who is older request an update to the new an updated version. 
	- *This is not implemented yet as it doesn't even pull the version from the run rules file.* 
- Lastly we have the packet handler which is used in our async functions later to handle any packets coming through the listener. Specifically it decodes what those packets are and takes actions based upon the packet type. 

```Python
    async def start_listener(self) -> None:

        '''

        This method is responsible for setting up and running

        the listener portion of the validator until it's terminated.

        '''

  

        logger.info("Starting validator listener...")

  

        # Start the listener in the background

        try:

            self.comm: AbstractCommunication = CommunicationFactory.create_communication("TCP")

        except ValueError as e:

            logger.error(f'Fatal error. Unknown communication type: {e}')

            self.state = ValidatorState.ERROR

            raise ValueError(e)

        # Need to grab our real IP info later

        asyncio.create_task(self.comm.start_listener("127.0.0.1", 4446))

  

        while self.run:

            message: bytes = await self.comm.receive_message() # Get the message

            await self.handle_message(message)
```

The start listener section is built so that validators can active listen for TCP connections coming in (for now its only other validators, but when the system is operational is will be any user type). This was made async so that we would only execute in the event that we receive a packet in and ideally would scale across multiple cores as at this time this is not optimized to handle a large number of requests (last test I ran clocked in at 10k). If you notice we are manually calling start listener on localhost, but in the actual system we would want to run on *this computers IP*, so that its discoverable to external machines. *I believe 0.0.0.0, should do this...*

Once a message is received it goes to `handle_message`, which simply takes the message, and sends it to the packet handler for processing. Handle message was placed here because it will later condition the message prior to handing it off to the packet handler, by decrypting the message being sent using the validators private key. *Most communication on UndChain is encrypted, matter a fact the only time it isn't is when a user is requesting the public key from another user.* At the time of writing this functionality has not been built in to aid in debugging. 

```Python
async def stop(self) -> None:

        '''

        This method is responsible for ending the validator loop

        and to communicate to it's peers that it is going offline

        '''

  

        self.run = False

        logger.info(f"shutting down the validator.")

  

        try:

            await self.comm.disconnect() # type: ignore

            logger.info(f'Successfully stopped listening')

        except Exception as e:

            logger.error(f'Failed to stop validator from listening. Inside Validator:stop()')
```

This method is used to inform other validators that it's about to go offline, this is done because Validators that simply go off line with no notification receive a lowed perception score. While they will still encounter a lower perception score, by going offline regardless if they present this or not, it will be less sever. It also gracefully shuts down the listener, which is important for memory management and security. *Note: at this time the code does NOT send a notification to other validators, that needs to be added in*

```Python
def set_state(self, new_state: ValidatorState) -> None:

        '''

        Changes the state of the validator which is used to determine

        this validators readiness on the network.

        '''

  

        logger.info(f"Transitioning to {new_state.name} state.")

        self.state: ValidatorState = new_state
```

Simply sets the state of the validator as it's progressing through it roles (identified in the ENUM above)

```Python
async def handle_message(self, message: bytes) -> None:

        '''

        Send message over to the packet handler for processing.

        '''

  

        logger.info(f"Handling message: {message}")

  

        try:

            response: None | bytes = self.packet_handler.handle_packet(message)

  

            if response:

                await self.comm.send_message(response, bytearray(b'recipient_public_key')) # Need to get teh public key of who we are sending this to

                logger.info("Response sent back to sender")

            else:

                logger.warning("No response sent back for this packet type")

  

        except Exception as e:

            logger.error(f'Failed to process message: {e}')
```

This was referenced earlier, but is responsible for taking in a message coming from the listener and routing it to the appropriate packet handler. If there is no handler, we should return and error stating that we could not process the message.  

```Python
def send_state_update(self, recipient: bytearray) -> None:

        '''

        This method is used for appending the validators state to the

        beginning of a incoming request so that the user knows the heath

        status of this validator

        '''

  

        state_info: LiteralString = f"State: {self.state.name}"

        logger.info(f"Sending state update to {recipient.decode('utf-8')}: {state_info}")

        # Logic to send the state update

        ...
```

When I made this method originally it was when the validator had controlled all packet handling (prior to creating packet handler). Since then I have kept it in as I was thinking that this could be used in the header of each message as a way of consistently providing the state of the validator without a user explicitly asking for it. The method signature would need change as we are no longer sending in a message and we would be returning the state... Probably need to just make this a getter for the state...

```Python
def handle_error(self, error_message: str) -> None:

        '''

        Logic to handle errors and transition to the validator

        into the ERROR state. Validator should communicate this state

        to it's peer (other validators in the pool).

        '''

  

        logger.error(f"Error occurred: {error_message}")

        self.set_state(ValidatorState.ERROR)

        # Implement recovery or notification logic here

        ...
```

This is a place holder for now, but the intent is that if we receive an error we execute this method with the idea it would gracefully handle the error. At minimum, logging the error. ideally by returning a correction for that specific error. We could handle errors on a case by case basis too, so this may not be needed. 

```Python
async def discover_validators(self) -> None:

        '''

        This method is for discovering other validators or listening for

        incoming requests for validators to join the pool.

        '''

  

        logger.info("Discovering validators asynchronously...")

  

        known_validators: list[str] = self.run_rules.get_known_validator_keys()

        tasks = [] # Collect tasks for connecting validators

  

        for validator_key in known_validators:

            if validator_key == self.public_key.decode('utf-8'):

                logger.info(f'You are a known validator {validator_key}, so we are not contacting ourselves')

                continue

  

            logger.info(f'Attempting to connect to validator: {validator_key}')

  

            # Get contact info for this validator

            contact_info: dict[str, str] = self.get_contact_info(validator_key)

            if contact_info:

                try:

                    logger.info(f'Initializing communication with {validator_key} using {contact_info["method"]}')

                    try:

                        comm: AbstractCommunication = CommunicationFactory.create_communication(contact_info["method"])

                    except ValueError as e:

                        logger.error(f'Fatal error. Unknown communication type: {contact_info["method"]}')

                        self.state = ValidatorState.ERROR

                        raise ValueError(e)

                    tasks.append(self.connect_to_validator(comm, validator_key, contact_info))

                except Exception as e:

                    logger.error(f'Failed to connect to validator {validator_key}: {e}')

            else:

                logger.error(f'Failed to retrieve contact info for validator {validator_key}')

  

        # Await all of the gathered tasks

        if tasks:

            await asyncio.gather(*tasks)

        else:

            logger.info("No other validators to connect to...")
```

This is the algorithm that we use to discover other validators on the network. Inside here we request the known validators inside of a list; we then create an empty task list, that is designed to later parallelize sending requests out (speed up the process in the event that you have many known validators). 

We then check to see if we are a known validator so we don't try to contact ourselves. If we are not the validator we are currently looking at we continue on by attempting to contact them using the info contained in the `[route]` section of the run rules file. This is done using the method `get_contact_info`, if we receive that info then we try communicating using that route. *Remember that currently we have only implemented TCP/IP, but UndChain is designed to work across multiple communication types (think Bluetooth or LoRA) so we call the `communicationFactory` to figure out how to do it.* I am not sure if we should set the error for that as a fatal error or just simply proceed to the next validator in the list. 

The last potion of this code takes all the rout information that we have gathered for each validator and places them in a pool to be executed all at asynchronously. 

```Python
async def connect_to_validator(self, comm: AbstractCommunication, validator_key, contact_info):

        try:

            await comm.connect(bytearray(validator_key, 'utf-8'), contact_info) # type: ignore

        except Exception as e:

            logger.error(f'Failed to connect to validator {validator_key}: {e}')
```

This is the helper function used in `discover_validators` mentioned above. The attempts a TCP connection to the end device. 

```Python
def get_contact_info(self, public_key: str) -> dict:

        '''

        Retrieves the contact information for a validator from the run rules

        based on the public key being passed in.

  

        Returns:

            Dictionary with the type of communication and the route

        '''

        known_validators = self.run_rules.get_known_validators()

  

        for validator in known_validators:

            if validator['public_key'] == public_key:

                logger.info(f'Found contact info for public key {public_key}: {validator["contact"]}')

                return validator['contact']

        raise ValueError(f'Validator with public key {public_key} was not found in the rin rules file.')
```

This is another helper method for `discover_validators`, its job is to take a public key and find the contact information (aka route information) for the particular validator so the system knows how to contact them.  

```Python
def check_if_known_validator(self) -> bool:

        '''

        This method is responsible for determining if this validator is

        apart of the known validator class within this co-chain

        '''

        known_validator_keys: list[str] = self.run_rules.get_known_validator_keys()

        public_key_str: str = self.public_key.decode("utf-8")

        is_known: bool = public_key_str in known_validator_keys

        return is_known
```

This helper function simply checks to see if the current profile is a known validator, based on the run rules list (you can also think of this as a configuration file for a co-chain).

```Python
if __name__ == "__main__":

    async def main() -> None:

        public_key = bytearray("validator_pub_key_3", "utf-8")

        run_rules_file: str = "UndChain.toml"

        validator = Validator(public_key, run_rules_file)

  

        try:

            await validator.start_listener()

            await validator.discover_validators()

  

            while validator.run:

                await asyncio.sleep(1)

  

        except ValueError as e:

            logger.error(f'May need to check the run rules file: {run_rules_file} \nThere is a misconfigured communication type')

            return # End program to prevent undefined behavior. TODO: Create a checker to see where in the TOML file we have the misconfiguration.

        finally:

            print("System listening for new connections...")

            await validator.stop()

  

    asyncio.run(main())
```

At the end of nearly all Python modules, I add a small test at the end to ensure it works as intended. This scripts job at this time is to simulate finding validators based on the routes contained within the run rules file. If no connections can be made, it terminates the connection (via TCP timeout). If there is no end device you will see an error code like this:

```CMD
[ERROR]  - Failed to connect to validator validator_pub_key_1: [WinError 1225] The remote computer refused the network connection
```

---

# run_rules.py

The `run_rules.py` file is meant to create a well structured system for taking in the run rules file for a specified co-chain and interpreting those rules so that validators (and later partners) can interpret how the chain is to operate / function. This script will need to be extended and there are some methods that are simply not implemented yet, but will need to be. The run rules file can be thought of as the closest UndChain will get to a 'smart contract' as this establishes ideas such as tokenomics and sets preferred validators. This is the entry point for any blockchain project that enters into UndChain. 

```Python
def __init__(self, config_filename: str) -> None:

        # Construct the path to the run rules file

        root_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Navigate to the root directory

        run_rules_path: str = os.path.join(root_dir, 'Run Rules', config_filename)

  

        # Load the TOML file

        with open(run_rules_path, 'rb') as f:

            self.config: Dict[str, Any] = tomllib.load(f)
```

This code defines where to look for the run rules files will exist (currently located a directory above the script itself) and based on which file is selected (co-chain), it loads the rules into a dictionary which is used to parse / extract through the remainder of the code. 

Note: When the UI system (M3) is implemented users should be able to select which co-chains they wish to support. They will at that time be able to make a tier list of which they would like to support so that even when one validator pool is full they are able to support other co-chain validator pools. Users will be able to download addition run rules files as they subscribe to the co-chain. 

**Future addition**: We need to add an error handler here so that in the event a run rules file is requested that doesn't exist the program doesn't crash, while also notifying what called this method what happened so it can handle this error accordingly.

```Python
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
```

This section of code pulls out the job structure fields within the run rules file. It attempts to pull out the values inside fields:

```TOML
[base_job_file]

fields = ["user_id", "job_type", "min_partners", "block_id", "block_time", "job_priority"]

mandatory = ["user_id", "state", "block_id"]

job_types = ["transfer", "auction", "naming_service", "store_req", "dmail"]

token = "UGP"  # The token used for transactions
```

- **Fields** - This defines all of the various fields that can be sent to the validator during a request. For example, a validator could request the current block time which is important during a time sync. 
- **Mandatory** - This defines fields that MUST be provided by a user when responding to any request. In this case, we must always so who we are, what status we are in (Validator state) and what block ID we are currently processing. 
- **Job Types** - This field can be thought of what methods can be called from this chain. For example a user could request the store command in order to store data on the network.
- **Token** - Directs which token is needed to perform this function, this is specific to partners as validators can only accept UGP. If not provided we should always assume USP. 

The methods and fields listed are NOT final and will change as the system evolves, for example there is currently no command for our asset protection protocols at this time. 

I believe that we should have error handling for missing (or empty) fields as that could happen if the file is corrupted someway on the end users computer. Think we should also have a hash that can be used to check against the network to ensure this file wasn't tampered with for security purposes.

```Python
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
```

Get validator info is meant for collecting the list of known validators from the run rules file, as well as what the maximum number of validators can exist on a network. This will give developers some flexibility to define what sort of network they want. The could go with less Validators which means they will reach consensus faster, but it may not have enough bandwidth for high throughput systems. 

Even if a run rules file has more validators that the max 44% that the network allows, the network shall ignore those 'extra' validators and place them in an inactive state with the idea that they can be added if one of the others goes down. We must adhere to having no more that 44% of known validators on a co-chain as that increases concerns with centralization. 

```Python
def get_utilities(self) -> Dict[str, Any]:

        """

        Fetch the list of utilities available on the chain.

        """

  

        return self.config.get("utilities", {})
```

This is one of those methods that I have yet to implement, but could be used. The idea is that we can get a list of utilities that the partners can perform. Each utility should have a fee, what the name of the method is and a description of what that method does.