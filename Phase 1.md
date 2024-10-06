
## Phase 1 - Test Net

### Core (in progress)

**Description**: Create the core functions for communications, encryption systems with ability to swap protocols and define the packet structure.

- [ ] Encryption [[Encryption Discussion]]
	- [ ] Modularity using base class and use a factory to decide which to use.
		- [ ] AES-512
		- [ ] Kyber
- [ ] Communication
	- [ ] Packet structure
	- [ ] IP Communication

---
\
### Validators

**Description**: Define the validator role and establish inter-validator communication protocols, as well as how validators interact with other user types.

- [ ] Discover Validators
	- [ ] Check Run rules

---

### Owner

Description: Define the run rule's structure created by the chain owner for validators and partners to execute on.

- [ ] Run rule structure
	- [ ] TOML structure


---

### Partners

Description: Establish rules for partner communication to both validators and clients and run chain owner generated code.

- [ ] Get jobs
	- [ ] Decide if we pool or subscribe for jobs

---

### Clients

Description: Create the client user type and establish protocol for utility request as well as communication to partners.

- [ ] Request jobs
	- [ ] Base UI (non-M3L)

---

### Stress Test

Description: Stress the system on a local network and add tests that make each user type malicious to see if they get caught.

- [ ] Intra-network setup
	- [ ] Identify private IPs as well as their roles

---

### Test

Description: Set the validators live on the global network, creating a filter for specific users to interact. Create logs for real time debugging.

- [ ] Bare metal or using a provider for Validator?
	- [ ] What hardware is needed?
- [ ] Set max accounts to 10k


---

### Co-Chains

Description: Implement the pages and Auction house co-chains and test those on the test net to see how content is being sent on chain.

- [ ] Auction House
	- [ ] Define bidding
	- [ ] Define quick swap
	- [ ] Define Digital Asset Creation
- [ ] Pages
	- [ ] Define how a page is made
	- [ ] Define AdCoin

---

### Interface

Description: Implement the graphical user interface to allow standard users the ability to interact with the chain using M3L and GSS.

- [ ] M3L Structure
- [ ] GSS Structure

---

### Public

Description: Allow more users to access the test net to stress test the system and see how much storage is needed for receipts.

- [ ] Release account limit to 100k
- [ ] Log bottlenecks and issues / errors
	- [ ] Do we start implementing the Code ledger protocol?