
### Client to Validator Example

In this user story we are going to focus on the interaction between the client to validator communication. This should be the same regardless of what utility is being requested.

1. Client sends a utility request message to the validators. 
	-  How does the client know how to send that message out
		-  We have a list of known validators that comes with the codebase. The client can look up the communication specific information for that validator and use that information to communicate with the validator. In this example we are only focused on IP; but this could be any communication medium. The lower the latency the better
			- Maybe the file should contain the alias / ID, medium / type, the routing information, the amount of latency and the reliability
			- Whoa, should I make a data structure that stores all the active or currently in use validators so that we are not having to constantly jump between the TOML file that contains this information? Seems more efficient since it would be in RAM instead of on disk. Put it in a dictionary?
	2. We establish communication with the validator and that validator sends us a confirmation that they received the message and our utility request has now been placed in the job file (provides the block number). Validator also sends a list of validators who are working on this payout cycle
		- What all bad could happen?
			- Could not get a connection to one or all of the validators that we send this message to
				- What would we do in that scenario?
					- try a resend; maybe set the limit to 4 attempts
					- a fail safe could be the scream cast where you would try every medium and / or address in order to precure a solid connection. This would be a plain text message since you don't know the entity your reaching. which is Dangerous; need to think on this more
					- timeout could be set to 6 seconds since utility functions should take no more than 4 seconds before the job file is filled for that block
						- what if we have a cutoff timer based on block time that just throws a request into the next block's job file if we hit a threshold value. Probably should be however long it takes for validators to agree on a job file
				- how do we know that all the validators will place our utility in the same block number?
					- prior to sending the message the validators have to have consensus on that job number
					- have two job files active at once. One for the current block and another for the next block. If your request comes in too late it jumps to the next block.
	3. The client takes that list of validators and if they have yet to send the request, will feed that request to them as well
		- Does this need to happen? The request should propagate to all validators anyway
			- Maybe if you have three validators confirming they received your request then you don't need to???
	4. The validator then collects a list of partners who are willing to provide utility for what was requested. *In events where a validator has to prove they have the resources, this is done here*
		- Should probably send the perception score with each user they could connect with; that way it's up to the client's risk level on who they connect with.
		- What about cases where the partner is a centralized source? Perhaps we should also send the preferred connection method of the partner? This could be an advantage for validators since they wont need to wait for a validator to respond and prove they have the ability to provide the utility. It's also faster since the validator already knows what to send to the client.
			- Should the client store this information?
				- I don't think so, reason being is cases where a partner may need to jump to another IP address or perhaps they are performing some load balancing.
	1. Once the validator has a list of partners that are willing to work they send that to the client
		- Should this be incremental as the partners come in or all at once?
			- I would rather send it in incrementally since that would kick off the utility much faster
		- Should there be a threshold on how many partners are willing to provide utility?
			- yeah I think so, it would be crazy to provide a client with a list of partners that is practically infinite.
		- Should the client set the threshold?
	2. I think in normal circumstances we would close communication to the validators at this time however, it should pick up again once the utility between the client and the partner is complete. I am going to continue for the sake of this example so that I cover all the bases of client to validator interactions
	3. Client then sends the validator a receipt of the transaction between the client and the partner with the signatures of both parties (this is done for each partner the client worked with). Validator then confirms the utility is complete and provide the client the block number that the utility completed on. *I don't see a case where a utility is completed on the same block that it was initiated on. Only means I can think of that happening is when a client and partner already have established communication with one another and just need to update the ledger.*
		- What could go wrong here?
			- Client could choose not to send in the message to the validator. In this case if the validator receives it from the partner then the utility is complete. If neither party sends it the utility is subject to cancelation at the next payout period (every four hours) and the only payment is the transaction fee.
			- Validator doesn't send a confirmation or just ignores it.
				- Since we have a validator pool there would have to be coercion across more than 2/3 for this to get ignored.

---

#### Partner to Validator

In this user story I want to explore the interaction going from the partner to the validator and how they (partners) could respond to utility requests. I think I will ignore the use case of a centralized partner to keep this one simple. 

1. Partner sends a ready to provide utility message to the validator pool. This can include storage, computation or access. This is done using the same list that was used previously by the clients.
	- What could go wrong?
		- Validator fails to respond.
			- Same answer that was provided for the client to validator 
		- Partner could be lying about the utility that they can perform.
			- Validators could send challenge requests. Maybe offload this responsibility to the passive validators so active validators don't get overloaded (apart of validator to validator communication)?
		- Should we create a system where the validator notifies the partner when a utility that they are interested in opens up or are we expecting the partner to find it in the job file?
			- I am leaning toward having the validator send it since I think it's just as costly to handle a bunch of job file requests from partners every block. not to mention this would be a good use case for the `when` keyword inside of pseudo
		- Partners periodically send a still active message to notify the validators that they are still awaiting additional utility requests. Do this in cases where the partner is waiting to long for more requests. Need to come up with a good time scale for this
1. Validator notifies the partner when a utility that they are subscribed to comes up. *pretty sure we are going to send what the partner is looking for rather than the whole file*
	- What could go wrong?
		- It's possible that a partner could be censored for whatever reason and the validators could be censoring that partner for things other than a low perception score. What solutions could be implemented to mitigate this
			- Partner could send out another request for work. It's possible that it was lost or overlooked (not sure how that's the case). This could spin off a response stating why they are not being utilized by the validators.
				- It's possible that the validators are not receiving demand for the service
			- Partner could also request for the job file (this is something any user type can do). So that they can confirm there are no jobs available
			- If there are jobs available and the partner meets network requirements we could drop the perception score of the offending Validators. The good news is the current unknown validators will be cycled out after a pay period. This isn't the best option for the partner, but I am not sure how to give the partner any additional recourse without giving them too much power.
			- Could always switch your public key then you wont be blocked. validators can't ban all keys and cannot ban usage of the network. *Which makes it stupid to refuse service an account anyway*
			- Is it possible that they could complain to the Chain Owner? Obviously you can send a message, but I'm thinking something more automated. Obviously a user could just post this on social media and show this corruption. More thought needs to be had here
		- Partner doesn't have the correct tools or fails to pass a check on the utility they claim to provide
			- Validators should notify partners when they fail to meet network requirements
		- Partner could have a low perception score which disqualifies them from participating in the network
			- Validators have to send a low perception score message to that partner
			- Unfortunately this is a deterrent and not a solution because you could always jump to another account
2. The partner then responds to the jobs they are interested in.
	- What can go wrong here?
		- Validators ignore the partner and don't allow that utility to happen
			- Could happen if the partner takes too long to respond
				- I would say in this case I don't believe the partner should get a response as to why they didn't get the utility since that would put more load on the validators
				- Wonder if this could happen because the partner is too far away and cannot respond quickly. This may be one of the factors we use in creating new domains / networks?
			- Could also happen if they are being censored
				- I would be surprised if this happens a lot considering validators get swapped out, but this would be a case for dropping the perception score of the validator.
3. validators send them connection details to the client so they can initiate communication *unless this is a centralized partner, but that partner wouldn't reach out anyway, they would just wait for connection directly from the client right?*
	- Well... It may make sense for the validator to reach out to the partner that a client is still connecting since they have to keep track of how long the utility is being used along with what block number that utility started on.
	- Guess the wrong information could be sent (like wrong IP or wrong public address)
		- This would be hard to diagnose where the issue is coming from since the information could be bad from the validator or the client has chosen to not to interact. **This is an attack vector that we need to constantly monitor**
4. Once the connection is made the partner confirms with the validator that the utility function has started so that the validator can place it in the payout pool. 
	- Validators could choose not to place it in the pool.
		- Again not sure out of the entire group that would happen
		- Validators do need to send a confirmation that the partner has been added to the payout pool with that utility
5. Partners need to be able to send out a at capacity message in order to tell the validators that they are busy and cannot accept any addition work at this time
	- Why? There will be situations where the partner will not have the resources to take on additional demand from the network.
		- Plus this gives us some Realtime statistics of how loaded down the network is. Again leading to possibly creating new networks or shifting traffic to another domain.
		- Need to create a cool down so we don't spam this to the validators constantly
1. Partners can also send a sign off message in the event that they need to shutdown. 
	- Why? 
		- In the event of power failures. This wont stop the perception score from dropping, but it will prevent any additional utility requests from coming in and making it worse.
2. Utility complete. As utility completes the partner takes the receipt that the client and they have signed and sends it into the validators. the validators will return the block number that utility was completed on.
	- What could go wrong?
		- Client could refuse to sign and hold the connection open
			- we could create an arbitration mode where the partner could send in the last message from the client to prove the last interaction (using their signature)
			- This can also not be malicious. The client may had a disconnect for any reason causing this to happen. 
			- The key here would be that the partner can send in a partial utility complete with this signature from the client, so they can get some form of payout. 
		- Validators could not recognize the end of transaction 
			- they do have to send a message indicating that the request happened.  If you have that its easy to prove that they acted maliciously. 
			- Could also be due to validators being overloaded. Perhaps this should be on a retry system?

---

#### Validator to Validator Communication

This section will explore how validators will talk among each other and gives some ideas on how consensus can be performed. This will also discuss the roles of active and passive validators as well as known and unknown validators. The advantage of the validators is the small size of active validators this should allow them to be able to come up with a consensus quickly. I don't think there should be more than ten validators per domain, but testing will prove if this is a good idea or not.

**Active Validators** - This is the group of validators that have direct contact with all user types. They maintain the job files, payout file as well as the blockchain. The number of active validators is determined by what the chain owner has set for this co-chain.

**Passive Validators** - This group of validators are ones that are on standby in the event that a validator goes down. They can also be used for offloading some resources. There is no limit to how many passive validators there are. The advantage of being a passive validator is that you can repair your perception score as a passive validator. 

**Known Validators** - This group of validators are ones that are appointed from the chain owners and could be owned by the chain owner. There is a limit to how many known validators you may have in the active validator pool (no more than 44%). 

**Unknown Validators** - This group of validators could be anyone and are swapped out regularly every pay period (every four hours). Unknown validators make up the remaining 56% from the active validator pool.

1. Network discovery - When a new validator launches they should reach out to other validators in the known validator list to establish a connection and build up the network. If they are a known validator they wait for unknown validators to reach out in order to build up the validator pool.
	- What could go wrong
		- We could get hung up waiting on unknown validators to join. This will especially be true early in development since not many people will be using this tech. 
			- May have to kick some known validators out so that they become unknown, until the network builds up
		- What if no one responds? Could go on a search for validators by using scream cast
2. Time Consensus - We need to have all validators agreeing on the time known as 'block time'. This is because the goal is to make this chain time dependent instead of block dependent. In the event the network is active (which is should normally be active) we should just inherit what the other active validators say the time is. In cases where the network is being brought online we should have all active validators reach out to each other to first determine the amount of delay between each validator. Then each validator shares the current time they have with the group. Then throw out any extremes and take the average. That will then be the block time.
	- What about cases where clocks get shifted up or down
		- Maybe we should make a time sync message that if all validators agree to reset the time they use this protocol again to set the clock. The catch is, the proposed time cannot be outside a payout period. 
3. Capacity test - Need to come up with a method of determining how may connections a validator can maintain; this can be a form of determine if a validator can be effective in their role; but not a determining factor since it really depends on how they are situated with users. This could be used to determine how much a validator can offload to another validator.
	- I think this test should involve setting a ton of connections between the passive validators and have them perform some simulations of utility requests and job payout so that we can ensure they are storing the correct information. 
4. Job files - Need to come up with a solid time limit as to how long a job file for the current block can be made for; we need to make two job files at a time so that we don't loose any jobs that are coming in from clients. Job files will need to consist of the initiation time and who is involved (you can have a client pool as well as a partner pool). We should incrementally update the job file as they come in with each partner so that they should have a updated listing of the job file at all times. This incremental message should consist of a hash from the validator sending the message so that they can compare their files against one another. If there is a mismatch we would need to come up with a resolution mechanism. I am currently thinking of ordering the users in numerical order then do something like a binary search where we halve the list and send a hash between the validators. If it doesn't match then you have an idea of what may be missing, probably also send the number of jobs. keep halving until you find out what file(s) you are missing. Downside is this will take a while and I kind of think it would make more sense to send the whole job file. Have to do some testing to see which is better, possibly a blend of both? After we have agreeance on the job file from all validators (should be no more than ten) we process that job file for that block. Any jobs coming in during this confluence would be placed in the next job file. Once that occurs we push the job into the payout file which is held until payout occurs (every four hours). *It's called a file, but it is held in RAM until it's been completed then moved off to the partners for storage*
5. Payout file - Similar to the job file, and like a job file if we note that a job comes in at the cutoff period that gets moved into the next payout file. the payout file has similar information to the job file with the added column for utility complete. Actually it may make sense to just store the payout file rather than both the job file and the payout file since you should be able to derive the job file from the payout file... It would be great if I could save storage space like this. So we wouldn't have to evoke the convergence protocol as often.
6. Convergence - Once the network has been congested so much that it's unable to efficiently traverse the block and storage is to high we can force a convergence (also happens if we need to switch hashing algorithms). This should use the same algorithm as the payout file and the job file, but the goal is that we effectively make a new genesis block that starts with all the users who have transacted until the end of the convergence. We would need to set a hard time for the convergence as network activity would need to continue during this event. My thoughts are that we have two block chains at that point, the downside is that you would have to constantly recalculate the new chain since you are continuing transactions on the parent chain. once convergence ends the old chain is saved in deep storage across the network (partners). Could we make it so that we suspend transactions during this time instead?
7. Network status - Validators need to send their status to one another so that they can monitor how the other is doing and seeing if any validator is getting over loaded. This could be sent the same time we are syncing up with job files and payout files????
8. Chain link - This message is sent at the end of the block to each chain that the co-chain is linked to (no more than two). This way it can be tied in with the hash of that chains block. We must make the system in such a way that if a co-chain fails to send their hash that the other chain just keeps going and once that other chain does send a hash then it will hash it with that next block. 
9. Domain link - Similar to chain link but this one can link domains together. This is so users in other geographical locations can have their own 'chain' that operates at a lower latency. *Which is also how we will determine that a new domain is needed*. An abstract scenario for this would be a event where you are running UndChain on Mars. You can't wait 16 minutes (at best) for a transaction to go through or receive service. This would allow tokens to be easily transferred between the two domains just with lower latency. This does require a protocol to transfer tokens from one domain to another if you are traveling between domains. That shouldn't be much of a problem considering information travels faster than us.
10. Network link - Similar to chain and domain, but this protocol operates in a way that is agnostic to UndChain meaning that it has it's own token system and is only connected via these links. The goal with this is so that anyone can make their own UndChain / Web 4 clone and it gets the same security as UndChain. *Provided both parties agree to link together*
	- What could go wrong?
		- have a situation where one network is operating in a way that another network disagrees with and they alienate this chain. This could lead to fractures within the network and cause a split in the system which kills interoperability between the networks.
			- Not sure of a solution for this. Networks deserve to be able to choose who they connect to. Digital ownership works both ways.