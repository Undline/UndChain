
## Phase 1 - Test Net

### Core (in progress)

**Description**: Create the core functions for communications, encryption systems with ability to swap protocols and define the packet structure.

- [ ] Encryption [Encryption Discussion](Encryption_Discussion.md)
	- [ ] Modularity using base class and use a factory to decide which to use.
		- [ ] AES-512
		- [ ] Kyber
		- [ ] Key Generation 
			- [ ] Storage - PEM File
		- [ ] Cold Wallet
		- [ ] Hot Wallet
- [ ] Communication [Communication Discussion](Communication_Discussion.md)
	- [ ] Packet structure
		- [ ] Packet Handler
		- [ ] Packet Generator
	- [ ] Abstract Communication / Communication Factory
		- [ ] IP Communication
			- [ ] TCP - Validators
			- [ ] UDP - Partners and Clients

---

### Validators

**Description**: Define the validator role and establish inter-validator communication protocols, as well as how validators interact with other user types.

- [ ] Discover Validators Protocol
	- [ ] Check Run rules
	- [ ] Identify Validator States
- [ ] Listen for connections
	- [ ] Handle incoming messages
- [ ] Perception Score
	- [ ] Add
	- [ ] Reduce
- [ ] Job File
	- [ ] Add job
	- [ ] Notify Partner
	- [ ] Payout File
- [ ] Test

---

### Owner

Description: Define the run rule's structure created by the chain owner for validators and partners to execute on.

- [ ] Run rule structure
	- [ ] Known Validators
	- [ ] Tokenomics structure - fees / payout period
	- [ ] block generation speed


---

### Partners

Description: Establish rules for partner communication to both validators and clients and run chain owner generated code.

- [ ] Get jobs
	- [ ] Subscribe for jobs by letting validator know we are available
	- [ ] listen using `when`
- [ ] Connect with Client(s)
- [ ] Rules on Storage
	- [ ] Define how storage is handled
		- [ ] plot system
- [ ] Rules on Computation
- [ ] Rules on Access

---

### Clients

Description: Create the client user type and establish protocol for utility request as well as communication to partners.

- [ ] Request jobs
	- [ ] Send job request packet to validator
	- [ ] handle network response
- [ ] Connect with partner
	- [ ] Known partner - TCP
	- [ ] Independent Partner - UDP
		- [ ] packet numbering

---

### Stress Test

Description: Stress the system on a local network and add tests that make each user type malicious to see if they get caught.

- [ ] Intra-network setup
	- [ ] Identify private IPs as well as their roles
- [ ] Need to create metrics for system performance
	- [ ] CPU
	- [ ] Storage
	- [ ] Network throughput

---

### Public Test

Description: Set the validators live on the global network, creating a filter for specific users to interact. Create logs for real time debugging.

- [ ] Bare metal or using a provider for Validator?
	- [ ] What hardware is needed?
- [ ] Set max accounts to 10k
- [ ] Need a reporting location (network / storage location)
	- [ ] logs
	- [ ] performance metrics
	- [ ] storage time
- [ ] Security audit
	- [ ] Encrypted data is encrypted
	- [ ] Signatures can only come from the key holder
	- [ ] double spend attack



---

### Co-Chains

Description: Implement the pages and Auction house co-chains and test those on the test net to see how content is being sent on chain.

- [ ] Auction House
	- [ ] Define bidding
	- [ ] Define quick swap
	- [ ] Define Digital Asset Creation
- [ ] Pages
	- [ ] Define how a page is made
	- [ ] Define how a page is shared by partners
		- [ ] Sharded
		- [ ] data acquisition (external data)
			- [ ] SQeeL
			- [ ] File / CSV in a set location
	- [ ] Rating system
	- [ ] Define AdCoin
		- [ ] Set token supply to 444 trillion
		- [ ] Make system that allows other chains to use this token. Protocol

---

### Interface

Description: Implement the graphical user interface to allow standard users the ability to interact with the chain using M3L and GSS. 

M3L should be thought of like the structure / skeleton of the page while GSS is the style / skin of that page.  

- [ ] M3L Structure
	- [ ] Structures - Pulls Data from archive / Database
		- [ ] Background / Wallpaper
			- [ ] Video
			- [ ] Image
		- [ ] Calendar
			- [ ] Date / time / event
		- [ ] Video Library
			- [ ] Player
			- [ ] Collection
			- [ ] Reaction
			- [ ] Thumbnail / Preview
			- [ ] Pagination
			- [ ] Close Captioning
			- [ ] AI reader
				- [ ] Dependent on mimic
			- [ ] Watch share
				- [ ] Allow users to stream other content and share revenue
		- [ ] Table
			- [ ] Spreadsheets
				- [ ] Grid System
				- [ ] Tabs
		- [ ] Chat
			- [ ] Reactions
			- [ ] Bubbles / Chat area
			- [ ] Edit
			- [ ] Forum
				- [ ] Reply
				- [ ] Reaction
				- [ ] Share
		- [ ] Toast / Notifications
			- [ ] Small notification (lower right hand)
			- [ ] Alerts (Call to action)
		- [ ] Map
			- [ ] POI (point of intrest)
			- [ ] Grid (longitude / latatude)
			- [ ] travel paths
			- [ ] zoom
			- [ ] Location (you are here)
		- [ ] Item Grid
			- [ ] Items
			- [ ] On action 
				- [ ] Shopping cart
				- [ ] Quantity
				- [ ] Check
		- [ ] Graphs
			- [ ] Type
				- [ ] Timeline / Gant
				- [ ] Bar
				- [ ] Pie
			- [ ] Legend
			- [ ] Data Source
		- [ ] License / Contract
			- [ ] Type / Classification
			- [ ] Document
			- [ ] Signature
			- [ ] Time Stamp
			- [ ] Approval
		- [ ] Text Area
			- [ ] Code Editor
			- [ ] Rich Text Editor
			- [ ] Plain Text Editor
	- [ ] Display Mode - Changes by input type
		- [ ] Dashboard - Controller
			- [ ] Scrolls horizontally
		- [ ] Site - Keyboard and mouse
			- [ ] Scrolls vertically
			- [ ] Canvas  / work area
		- [ ] Application - Touch
			- [ ] Static
	- [ ] Forms
		- [ ] Name
		- [ ] Contact / Address
		- [ ] Text Field
		- [ ] Submit
	- [ ] Inputs
		- [ ] Keyboard and mouse
		- [ ] Controller 🎮
		- [ ] Touch
	- [ ] Outputs
		- [ ] Screen
			- [ ] Window Size
		- [ ] Audio
			- [ ] Notifications
		- [ ] Haptics
			- [ ] Hints
			- [ ] Feedback
	- [ ] Base UI Elements
		- [ ] Buttons
		- [ ] Drop Down
		- [ ] Radio buttons
		- [ ] Check lists
		- [ ] Canvas
		- [ ] Images
		- [ ] Video
- [ ] GSS Structure
	- [ ] Standard Structure Styling
		- [ ] Video
			- [ ] Loading Screen
			- [ ] Pre-roll
		- [ ] Animations
		- [ ] Colorization
		- [ ] Highlights / Glow / Shadows
- [ ] Rating system
	- [ ] Score
	- [ ] parental rating
	- [ ] content type
	- [ ] comments
- [ ] Age Verification System
	- [ ] Start timer at account creation
	- [ ] Verified granters
- [ ] Tracking System
	- [ ] Feedback metrics on elements that get more attention

---

### Public

Description: Allow more users to access the test net to stress test the system and see how much storage is needed for receipts.

- [ ] Release account limit to 100k
- [ ] Log bottlenecks and issues / errors
	- [ ] Do we start implementing the Code ledger protocol?