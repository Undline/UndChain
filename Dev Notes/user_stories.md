
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
2. Validator notifies the partner when a utility that they are subscribed to comes up. *pretty sure we are going to send what the partner is looking for rather than the whole file*
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
3. The partner then responds to the jobs they are interested in.
	- What can go wrong here?
		- Validators ignore the partner and don't allow that utility to happen
			- Could happen if the partner takes too long to respond
				- I would say in this case I don't believe the partner should get a response as to why they didn't get the utility since that would put more load on the validators
				- Wonder if this could happen because the partner is too far away and cannot respond quickly. This may be one of the factors we use in creating new domains / networks?
			- Could also happen if they are being censored
				- I would be surprised if this happens a lot considering validators get swapped out, but this would be a case for dropping the perception score of the validator.
4. validators send them connection details to the client so they can initiate communication *unless this is a centralized partner, but that partner wouldn't reach out anyway, they would just wait for connection directly from the client right?*
	- Well... It may make sense for the validator to reach out to the partner that a client is still connecting since they have to keep track of how long the utility is being used along with what block number that utility started on.
	- Guess the wrong information could be sent (like wrong IP or wrong public address)
		- This would be hard to diagnose where the issue is coming from since the information could be bad from the validator or the client has chosen to not to interact. **This is an attack vector that we need to constantly monitor**
5. Once the connection is made the partner confirms with the validator that the utility function has started so that the validator can place it in the payout pool. 
	- Validators could choose not to place it in the pool.
		- Again not sure out of the entire group that would happen
		- Validators do need to send a confirmation that the partner has been added to the payout pool with that utility
6. Partners need to be able to send out a at capacity message in order to tell the validators that they are busy and cannot accept any addition work at this time
	- Why? There will be situations where the partner will not have the resources to take on additional demand from the network.
		- Plus this gives us some realtime statistics of how loaded down the network is. Again leading to possibly creating new networks or shifting traffic to another domain.
7. Partners can also send a sign off message in the event that they need to shutdown. 
	- Why? 
		- In the event of power failures. This wont stop the perception score from dropping, but it will prevent any additional utility requests from coming in and making it worse.
8. Utility complete. As utility completes the partner takes the receipt that the client and they have signed and sends it into the validators. the validators will return the block number that utility was completed on.
	- What could go wrong?
		- Client could refuse to sign and hold the connection open
			- we could create an arbitration mode where the partner could send in the last message from the client to prove the last interaction (using their signature)
			- This can also not be malicious. The client may had a disconnect for any reason causing this to happen. 
			- The key here would be that the partner can send in a partial utility complete with this signature from the client, so they can get some form of payout. 
		- Validators could not recognize the end of transaction 
			- they do have to send a message indicating that the request happened.  If you have that its easy to prove that they acted maliciously. 
			- Could also be due to validators being overloaded. Perhaps this should be on a retry system?