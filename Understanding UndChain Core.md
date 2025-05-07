# Understanding UndChain Core

**Purpose**: This document is being made as a reference guide into how and why certain aspects of the code were written. This is meant to provide insight into why the structure is made the way it is architecturally and how it can interlink together (i.e. big picture)

Each section will be separated based on a theme or task that is meant to be completed. It should also be accompanied with all of the relevant files for that section. 

This document is a part of a much larger system. The goal is to have each piece of the system be its own self contained system and lays the foundation for how our co-chains will operate on the network.

---

# What is UndChain Core?

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

# Validator Operation

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