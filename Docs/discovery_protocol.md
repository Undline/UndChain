
Wanted to write out the goals of the validator discovery protocol so that I can flush out the ideas that I had in my head and then go into writing the code. 

### Purpose

The goal here is to make a protocol that will seek out other validators who have a compatible run rules definition file and sync with them so they can run the network. In this we should be identifying which chain we are referring to as well as which node number (think I am going to use the term node instead of universe). When the discovery protocol completes we should be handing off to the block time negotiation protocol which is where all the validators decide what time it is. 

#### States

I am going to introduce the ideas of validator states here (although it could be argued that the states may need to be apart of the overall initialization routine, perhaps I will move it later). Those states are as follows:

1. **Ready** - This tells the system that we are ready for users to request resources from the chain. 
2. **Discovery** - This tells users that we are in discovery mode (this protocol) and that we are NOT ready to receive requests at this time. The only request we should receive is those from other validators wanting to be apart of the pool.
3. **Time Sync** - This tells users that we are currently syncing the time between the *active* validators and the chain is close to being initialized. 
4. **Busy** - This tells a user that a validator is experiencing a large amount of traffic and cannot process an order that has been sent. The user should contact other validators (this will be used as a scaling metric so that we can dynamically scale the node as it grows; we will need to set a hard limit to which we create a new node)
5. **Low-Trust**  - This tells users that we have less than the recommended amount of *known validators* active on the chain (less than what the chain owner has recommended). This could lead to problems' since your only way of proving out a validators trust worthiness is their perception score. This will matter less as the network grows older, but will be an issue earlier on as we will have several new validators come online with little to no history. Perhaps we could mitigate this later with *experience*?

**NOTE** While we cannot ban a validator (or anyone for that matter). We can choose not to interact with them, this would have to be a decision from everyone as if only one validator chooses to interact then it will go through. *Perception score will drop on any validator seen censoring, so it better be worth it*

**IDEA** - We should implement a warning system prior to deducting from the perception score.

### Overview

There will need to be two different scenarios to establish connection to UndChain. The first and preferred would be with known validators and the other will be scream cast, this is where all available communication vectors the validator has access to will call out for other compatible validators. We will go over the known validators first as this is going to be how the chain initializes itself in the beginning and **won't** result in a low-trust network.

### Known Validator Protocol

- First we look at the known validator list in order to determine who is on the list as well as how to contact them (we will need to have both the public key as well as the means of contact in that list). **IF** you are on that list you are only meant to listen for connections and validate if the other known validators (if any) are active.
- We then wait unit either four minutes has passed or the validator list fills up (this will also means filling the reserve validators). Note: at this time we have NOT decided who is an activate validator and a passive validator we are only creating a list
- We then decide who is on the active validator list using the following parameters
	- Known Validators - This will be filled first, but keep in mind that known validators may only represent 40% of a network. In the beginning that will be 2 out of 5 active slots.
	- Perception Score - This won't be useful during network initialization since no one will have a history on chain and will be set with a perception score of 444, but as the network grows this will be a primary determining factor.
	- History - This is also something that won't help during initiation since no validator will have a history on chain.
	- Time - We look at who shows up first on each list (there should be two since you have two known validators). I wanted to use this metric since we need to focus on latency and we need validators who can respond quickly to one another (otherwise there should probable be another node). We will know this inherently since you need to also download the blockchain.
	- Randomizer - If there is still a tie (not sure how) we perform a randomizer routine where we take the validators who are already on the list and have them select a random number between 1 - 44_444_444 and whichever validator is closest wins.

Potential downfalls with this is if a known validator spins up another validator account that isn't known and tells the unknown when there is a scan for new validators (honestly this is going to happen in the beginning since I don't see this imminently getting attention), so what I decided to do is that during payout we swap out validators from the reserve pool. This should allow for decentralization since you would be lucky to 'control the chain' for a cycle. 

It's important to note that only active validators can earn GP, but along with being in que for running the chain; reserve validators can also increase their perception score. There is a limit to how much you can increase your score and that increase drops off exponentially in order to not allow a validator to simply sit on chain and gain trust by doing nothing, however I feel as though it's important to get something for being on standby. It's also important to note that in times of higher demand the active list could expand as determined by the chain owner.

If a standby validator is sent a request for work they are to send back a list of the active validators. If they are sent a blockchain download request they need to provide both a list of active validators as well as all the chain data.

The validator hand off protocol is to be defined elsewhere. Possibly during the payout routine. 

Note: Validators in waiting can participate in other chains and not loose their spot, if it becomes available and they wish to take it.

Once we have establish the active validator list we then move to the next part of the initialization process which is setting the block time.

### Un-known Validator

I am making this in the event that the network is attacked or if someone wants to spin up their own chain without attaching to the main chain (not sure why you would do that, but best to have this as a feature just in case). The difference between this and the known validator system is that this causes the network to go in low trust mode and at this time I don't see a reason to increase congruence more than 2/3rds, but you could define a higher value if you wish since you are now more trustless. 

This will use a routine called scream cast where we search for validators using any defined means of communication. In the example of IP we would scan each address sending a packet on port 4444 to see if we receive a response. If so we ensure we are operating off the same run rules and 'connect'. In this protocol there wouldn't be a four minute timeout since you don't have validators who are simply listening. 

I could see this being used in cases where known validators go down and new validators don't have a means of finding the ones who are active. I would also like to implement some functionality where you can check the legitimacy of the chain to ensure it isn't forged and someone isn't wasting their time with an 'unofficial' chain. *Maybe I could put a piece of the chain inside the version that user has downloded? Then allow them to change which block they want to lock on to over time. That should make it so an attacker wouldn't know which piece they are looking at* 

