*Please note: This is a massive project and everything is still a work in progress, as such we may need to pivot the functionality until the network is fully functional.*

# What is UndChain

UndChain is a PoU (Proof of Utility) blockchain; that can best be thought of as a decentralized cloud service that anyone can participate with. There are three different utilities that can be performed on the network.

1. **Computation** - The thought behind this function would be items that either are too complex for a ordinary machine to complete in a reasonable amount of time (training AI models, 3D rendering or DNA sequencing) or something that requires modifying data that must be shared with a group (think servers).

2. **Storage** - In order to compute you must have access to data to compute on. UndChain has storage built into it's language so you don't have to use another service. This allows for things such as databases and the ability to store large AI models. 

3. **Access** - This is a functionality that will be expanded more in the future, but for now think of this as the ability to have access to specialty equipment in a specific location such as linking two or more users together, surrogates or VPN like services. When fully realized it is meant to replace the IP protocol by enable secure communications that are digital signed from the source.

 When mixing these three utility types this will enable a full cloud experience that can do things such as spin up gaming servers, webpages and virtual computers. What makes this different than the way the internet is ran today is that anyone can participate and earn rewards for providing utility to the network. This reduces the need for missive data centers and spreads out computational resources throughout the network. This will **NOT** eliminate centralized services, in fact there will be ways (via access) in which you can still direct to a centralized service. The goal of the network is to allow both the centralized and the decentralized systems to co-exist and allow the consumer to choose.

# Co-Chains

Co-Chains is how the network expands it's abilities and services. Anyone can own a co-chain, in fact there is a classification of user called chain owners mentioned later. The goal of a co-chain should be to expand the functionality of the network and not to make new coins as such it is up to the chain owner if they wish to create a new token or use the blockchain's native token. The chain owner can still set their fees even with the native chains token just as they can with their own. The difference is you cannot control the emission rate nor the quantity. The goal in doing this is to attempt to reduce the amount of tokens that go in circulation. It also simplifies the usability of the blockchain the less swaps that need to be performed at the action house. 

## Why Co-Chains?

The purpose of utilizing co-chains rather than having layer 2 blockchains are multifaceted

1. It allows for better security since at each block completion a co-chain blends it's hash with a co-chain it's linked to, which reduces the risk of a attack on the network.

2. It expands Pseudo (UndChain's Pythonic programing language), by allowing others to import functions from other chains. You can choose to private a function or set fees on it. Remember you own it...

3. It provides a sense of ownership for your work and allows you to monetize on it so you can continue to make it better and help you with your personal goals. The goal of UndChain is digital ownership. 

4. I think it's better than saying layer two; you're a creator on this network not a leach and you should be recognized for it. Even the main chain is a co-chain. *Note: I will do some verbiage changes in here that I believe are more accurate and beneficial to the industry.*

## Examples of Co-Chains

I wanted to provide some examples of co-chains to help provide a better idea of what a co-chain could look like.

- **Main Chain** - This co-chain is responsible for creating the messaging protocols that go between various user types. It sets up two tokens, one for validators and the other for partners. Compiler for the Pseudo programing language, it creates an alias system that allows users to have user names that could be used for easier transactions (user names begin with an @). It sets the rules to create chain rules, which includes several options such as developer compensation, tokenomics and preferred validators. It maintains the block time for the chain and it stores the link that go across multiple networks. There will be more details on all this later since the main chain's code is here. There is also a protocol for digital asset assignment meaning that one or more users can own a digital asset and make fees off of it's use (think Music where you have the writer and the music as two separate but required pieces to create the DA); there should also be a way to make groups that can be used as a user.  Create a emergency message system that the chain owner can use to contact all users of that chain. Perception score which helps identify bad actors on the network. Convergence which helps with the blockchain getting too large. Licenses framework to show how to write licenses for the chain (allows users to see what they can and cannot do on chain). Subscriptions, this system allows users to pay using a subscription model that expires on a defined date; this will make budgeting easier for users. Open transaction, this keeps a digital asset transaction with the same end user open in the event something like a tip is to be given. *Does the main chain need to keep a list of the known validators of other chains?*

- **Mimic** - This is our AI chain, in here we create very specific models that are great at a particular task then link that up to a hypervisor that directs the incoming request to the correct model. *The reason for many small models rather than one monolithic model is so it's easier to change and can run on various hardware*

- **Pages** - This is our Web 4 system that delivers something similar to webpages, but instead of HTML and CSS you have **M3L** and **GSS**. The advantages of those markups is they allow a single component to be updated rather than an entire document so it's less load on the network. The goal is to also get rid of cookies so you're not helping companies track your habits online. This also introduces AdCoin which is used for pulling up different pages; you can trade for it or earn it by interacting with ads. This also sets up UnaS (UndChain naming service) which will be responsible for resolving names from addresses, much like how DNS works today. There is also a protocol called Adult_Swim which is a verification system to know if a particular user is above a set age. There will also be a content rating system to help both classify content as well as promote it.

- **Will** - This chain serves as an emergency backup system in the event that either you loose your keys or you pass away. The idea is that you set a threshold of time to transpire where you have no network activity. If this occurs a smart contract (per your instructions) executes and transmits your digital assets to the wallet(s) of your choosing. We will also be creating a 'compromised' button so that if you notice your account is hacked you can hit this button and it will freeze your account (you won't be able to make transactions). You may also set withdraw limits that can go off at a set interval of your choosing (either total daily or per transaction). A Will takes up to seven days in order to take effect, but if a freeze is hit during that time the Will is ignored and the previous one is used (or the assets are locked) *I am debating on this being on the main chain, I think this could be a core feature.*

- **Live** - This is our decentralized audio / video streaming system; this will be our first attempt at making a system who's goal is to have low latency system that is designed to be interactive between the provider and the participant (think live chat and a streamer). 

- **Code Ledger** - This is a software repository system that is specifically built for Pseudo since we need a means of tracking changes to the code from a specific user and pay them out accordingly based on what the chain rules state. Haven't spoke on this, but the idea is that you can earn tokens by contributing code to project and depending on the impact you get rewarded. There is also a bounty system for new developments. Once of the features I am looking to implement is a in-line messaging system as an example, you're working in a team and have a question about a function I want the ability for you to post your question / comment in code that can later be answered by someone else. In doing this we should be able to answer any future questions from new developers.

- **SQeeL** - This is UndChain's SQL system for creating and maintaining decentralized databases on chain. This will have the ability to either be a public database or it can be private with a shared key. One example for a public database would be a video content library where you need to store not only the video, but tags such as upload dates, gene, duration and previews. An example for a private database would be a manufacturing item database where you store the item ICN, cost, warehouse location and quantity.

- **Messaging** - I don't have a great name for this just yet and I'm not sure if this protocol should be moved to the main chain since I would like to create an emergency messaging system, but as the name suggests this is a decentralized messaging protocol, this will not only have the ability to perform direct messaging, but also the ability to create groups. This could be used as a basis for a social network or a forum. 

- **Player 2** - This blockchain is focused on helping developers launch decentralized serves that allow their players to connect live based gaming content. This will be fairly difficult to implement as latency will become the most important metric. Another goal of this is to create something called world engine which has the goal of creating a fully simulated world system, so that actions in one area create ripple effects throughout the globe / map. This should also include our Meta space who's goal is to create a open ruleset for how objects and actions happen in the Meta_Space (character sizing / physics)

As you can see there are a ton of chain ideas and I am sure more that will need to be developed to make this a full ecosystem. I may not be able to develop everything listed here, but my intention is to do as many as I can that are diverse as possible, so I can adjust the protocol based on the needs of these chains. I have personally found that when you use a product, you pick up on things that you would ordinarily miss. When developing co-chains always try to think of the value not just another asset class. 
## Co-chain code

While I believe that the best policy is to have open source code. I will be making the chain so that you can run closed source code, at this time I am not sure on how to do it since there is an inherent risk of a security vulnerability if it's being shared publicly. More thought will have to be put into this at a later time, I just put this here so I wouldn't forget.

# User Types

In UndChain there are four different user types; this is done to create a separation of powers so that no one entity could jeopardize the chain. 

1. **Chain Owner** - It's probably best to think of Chain Owners as developers. This group is responsible for creating the functionality of the chain as well as setting the tokenomics (fees). When a chain is developed and active the chain owner will receive a digital asset indicating the ownership of that chain. This allows the chain to be transferred to another owner(s). Chain owners may select who they are partnered with, at this time I believe the limit will be two. Chain owners are also able to select preferred validators (I'd say in most cases it would be themselves) and how many validators they will have on the network, with the minimum being three. *yep, I already know what you're worried about, it gets addressed later.* 

2. **Validators** - Think of Validators as routers and are responsible for taking a user request and connecting them with an appropriate resource. This is mainly meant to link clients and partners together. They are also responsible for keeping up with utility payout and they validate the traffic going between users. They also maintain the **users file** which is a repository of usernames with the public keys that are associated with it. 
 
3. **Partners** - This classification of users can be best thought of as the miners for this blockchain, however instead of hashing random numbers they focus on the three utility types. They work closely with validators to receive jobs from the jobs file and then either work directly or through a proxy with the client in order to complete that utility. Once it's completed, they sign a receipt with the client indicating the job was completed successfully. 

4. **Clients** - The client on UndChain are what would normally be known as users who utilize the resources on the chain. These are normal people who interact with the services for entertainment or business. The clients however is not simply a by product, but a apart of how the chain secures itself since the client must sign a receipt at the end of a transaction. 

# Block Generation

Blocks will be generated using block time rather than size, I have a concern that the size of the chain may expand too fast, due to this so items such as job files, work files and payout lists once completed will be stored by the partners. There is also a process called **The Convergence** that consolidates the chain; this is explained more later when we discuss encryption standards. Each block is generated in three stages and each of those stages have three steps each. *It's important to note that I considered each stage to be hashed and sent to a co-chain, I have decided not to do that since I think that it's overkill.* 

The timing will have to be experimental in the beginning, we **MUST** have blocks that are long enough to allow a sufficient number of job requests to occur while maintain a network that is responsive to the client. I think we should target 44 seconds per block. Please note that while the block may not complete in 44 seconds the job request should propagate quickly so that a confirmed transaction may occur. 

### Stage 1 - Initialize 

1. **Request** - In this first step we have a client requesting service for a utility, going to the validators. The validators then place this in a job file, so that the utility can be performed by a partner.

2. **Link** - In the second step a partner(s) contacts the validator(s) stating that they have resources to perform the requested utility. *Please note this may seem repetitive considering the next stage. This is here to show that we don't just hold the job until the stage is complete.*

3. **Sync Jobs** - In this step we sync this blocks job file with the other validators on this chain. 

### Stage 2 - Link

1. **Search** - In this step the work that was posted previously in the job file is either waiting on a partner to respond *or* the Validator knows the partner, and contacts them.

2. **Partner(s) Found** - Once a sufficient number of partners respond we then initiate the connection swap. The means of communication depends on both the chain and the user, at this time I think it's wise to go through a proxy in order to avoid the possibility of a DDoS attack.

3. **Connection Established** - In this step we add the connection as well as the block number we connected on (needed for payout later), to the **work file**. Validator listens for hashes from other co-chains it's connected to. 


### Stage 3 - Utility Complete

It's important to note that utility does **NOT** have to be completed when a block ends, in fact it rarely will. Utility completion either completes when the partner or the client end transmission, or when a payout period has been reached (every 4 hours on the main chain).

1. **Receipt** - Either the client or partner show the receipt of the utility, this could be as simple as a signature from both entities or some transactional information in plain text, but a signature from both **MUST** exist for it to be valid. It's best if both partner and client submit the receipt to the validators since either party could choose not to send it. 

2. **Utility Complete** - The validator marks the utility as complete along with the block it was completed on and appends the receipt of the transaction. *Note: Receipts must be less than 128 characters (size constraints). You could place a link to a file on chain that allows you to make your receipt as large as you want.* 

3. **Payout** - This happens at an interval that is defined by the chain owner (main chain is every 4 hours). If no payout occurs then we append this to the **pay sheet**. Validators then hash the transactions and append that to the block, this hash is also shared with co-chains.  

## Tokenomics

UndChain will have two native tokens associated with it's main chain. At this time I don't have a good name for them so I am calling them UndChain GP and SP. *Although AdCoin is **NOT** apart of the main chain I will discuss it as well since I believe pages will play a major role in this network*

### UndChain GP

GP will act somewhat like Bitcoin in regards to halving, GP is provided to validators. We will start with a initial token amount of 4,444,444 which will be distributed in development, advertisement and air drops. While I understand this may upset some, it's important to note that the idea is to use this to both promote and reward developments. I will discuss later how these will be distributed. The chain will start with an emission of 4444 tokens per day. Every four years we will experience a 'flooring' which is the same as a halving except we don't use decimals. This will continue until we reach one token per day which that will continue forever. While this does create an infinite supply I believe this is important to help keep validators interested in maintaining the network without charging high fees. Below is a table that shows the proposed floorings:

|Flooring| Year | Token Per Day| 
|--- | ---- | -----------------|
| 1 | 1 | 4444 |
| 2 | 4 | 2222 |
| 3 | 8 |1111|
| 4 |12|555|
| 5 |16|277|
| 6 |20|138|
| 7 |24|69|
| 8 |28|34|
| 9 |32|17|
| 10 |36|8|
| 11|40|4|
| 12 |44|2|
|13|48+|1|

tokens_per_day = 4444 // 2 ** flooring_number
### UndChain SP

SP is the reward system given to partners.  It's emission schedule is voted on by the active partners on chain. Activity will be defined a bit later, but my initial thoughts are that at least one successful transaction per week and a perception score above 444. During this vote you may either double the daily emission or halve the daily emission. I am concerned that partners will always want the emission to go down while users will want it to go up so I need to think of a way to counterbalance these effects. Maybe set the auto fee to do the same?  The initial daily emission of tokens is 4444 per day and the vote to either floor or double the supply happens every four years (a week before GP), so that the event happens at the same time as GP.

One of the reasons why I wanted the flooring to come to a vote is so that I can test decentralized voting systems that have conditionals that need to be met that have a large impact on the system. If this works well, it could be rolled out as a way to vote for new features / improvements on the main chain. 

### Ad Coin

Again Ad Coin really shouldn't be on here since it's apart of the pages chain. Ad Coin has an initial supply of 4 trillion tokens, the reason for this is because accessing content on a site should be cheep and I envision that it should only cost a couple Ad Coin. All Ad Coin will be created at the start of the chain and will be shared across a couple eco systems as well as air dropped so that users can use the chain immediately. Not sure if it's going to be given when you create an account or if it's part of the onboarding process (so you can learn how to earn tokens rather than purchase and use them). 

At a later time I will generate 444,444,444,444 more tokens. The idea is to test out a token generator system that takes the new tokens minted and splits them (based on percentage) to the token holders. So let's say there were 100 tokens and @Bob had 90 and @Sally had 10, if a token generator event occurs where we minted 10 more tokens, @Bob would then have 99 tokens and @Sally would have 11.

### Token Guidelines

All tokens on the chain will be divisible up to 12 decimal places, we will use the standard way to identify low values as the metric system (mili, micro, nano, pico), for example in order to send a transaction on chain @Jerry requests 100p of GP to provide the service. I think that is a lot easier than having a long decimal number and I'm not going to make up a weird name for sub-dividing tokens.

Again, please refrain from making a bunch of tokens on chain. If you are connected to the main chain you have access to GP and SP by default. This is done by creating a token share across chains. This share is dependent on how many transactions take place on the chain. So, if `MainChain` chain does 10 transactions and `Pages` does 100 (and we assume a daily amount of 4444) then `MainChain` would get 444.4 tokens to distribute to it's validators and `Pages` would get 3,999.6.

### Fees

Fees should reflect UndChain's core ideals of digital ownership, meaning that not only do you own your digital assets, but you also own your labor. Because of this partners are free to set any fee they wish on the service provided (independent of the chain owner). The chain owner can only set a percentage of the fee you collect so if you choose to collect no fee then the chain owner would not receive anything from you as a partner. With that there is an auto-fee system that I believe most people will use since it takes in chain usage and value of the token.

There could be a time when the auto-fee will be adjusted down via a vote, I only see this happening in cases where the value of the token far exceeds the value of the service. In these cases a vote will take place, but keep note that the fee reduction will be placed on a timer (since I wouldn't think clients would never vote for the fee to go higher). 

## Network Fundamentals


### Consensus and Rotation

UndChain operates on a 2/3 majority consensus mechanism, the reason behind this is that since a chain owner is able to set up to 44% of the available slots with **known validators** (which guarantees them a spot), they have to get buy in from another 23% of unknown validators. This consensus system also works in regulating unknown validators since they must have buy in from at least 11% of the known validators. There is a potential problem with this however, the chain owner could simply create more validators that are not listed and have them run on the network. 

Due to this potential vulnerability, a rotation schedule for validators will be implemented that forces **active validators** to swap out with **passive validators** which should reduce the risk. 

Between the rotation schedule and the 2/3 consensus mechanism I believe this will enforce the network to move forward. This also allows up to 32% of the validators to act in a deceptive way. There is a mechanism for validators and partners who operate in a deceptive manner which is called the perception score. If malice is detected your perception score is dropped. 

### Perception Score

The idea behind the perception score is so that a validator or client can judge the merits of a user without having to do blockchain analysis on that user. This system **MUST** be closely monitored and can **NEVER** be used as a means of preventing transactions from occurring. This isn't a social credit score, but more of a reliability rating of that particular user. All users can experience a reduction in their perception score, but validators and partners are the most affected since it can prevent them from providing service on the network. Much like the ledger, the score is maintained by the validators (meaning they request the score to be updated), but is stored by the partners. 

#### Perception Score Loss

Validators can loose their perception score if

1. They provide false records of transactional events
2. They do not maintain up to date user / job / work / payout files
3. They fail to perform a transaction on a particular user(s)
4. Drop connection without notice
5. Being blocked from a large number of clients

Partners can lower their perception score if

1. Failure to maintain saved files
2. Falsify a transaction with a client
3. Are too slow for the task they promised they could do
4. Drop connection without notice
5. Blocked from several clients - *Not sure about this one*

#### Perception Score Gain

It's important to stress that this is **NOT** a social credit score, but like a credit score you can rebuild it. Since I am sure there will be instances where this happens by accident (especially with disconnects). 

Validators can gain perception score by

1. Being a passive validator
2. Participating on the test net
3. Recovering from a outage 7x (that means the resource has been used 7 times with no problems)
4. Having a higher number of connections than your peers

Partners can gain perception tokens by

1. Participating in the test net
2. Getting un-blocked
3. Recovering from a outage 7x (that means the resource has been used 7 times with no problems)

I am concerned about using the block feature as a means of determining a perception score as I am sure it will be used in a poor manner however, clients only hurt themselves when they block other users since that prevents them from using their services. Also, we should consider placing a mechanism that disregards the block if it's noted that client has a abnormally large blocked list. 

### Scaling and Security

UndChain should move very quickly since we use so few validators in order to issue work on the chain, however there is a problem with network delay due to physical size so the use of parallel networks is to be used. The idea is that a parallel network operates in the same manner as each other with the exception being their user base. The user declares which network they wish to be apart of and with that they are provided a list of the validators that are responsible in that region to interact with. This doesn't mean that you are stuck on that network permanently though. You can initiate a transfer at anytime and your assets will travel with you. Again the reason for the parallel networks is to increase QoS by making content more local to that specific space, this includes the ledger. Much like how tokens are dispersed across co-chains they are also dispersed the same way with networks. Token allotment is decided by network 1 and is based on activity. 

##### How do you create a new network? You don't :) 

I still haven't decided just how I am going to do this, but I believe it will most likely be a mixture of algorithmic as well as chain owner responsibility. Perhaps I could leave it to a vote?

#### Convergence

I believe that this blockchain is going to get large fast even with some of the space constraints that I am already planning on implementing. So what I am planning on implementing is a by product of the fact that we have decentralized storage on chain. What I am planning is that at least every flooring we implement The Convergence which is a process where we store all of the blockchains information on file and effectively restart the blockchain using the hash of the old chain as a genesis block. This would effectively lower the barrier in regards to how much RAM a validator needs since they can offload it onto the partners to store. The convergence will also occur when when have a crypto swap.

### Security

There is a concern with quantum computing on the rise that traditional cryptographic algorithms may become obsolete. If history tells us anything is that it's a matter of when a cryptographic algorithm will be cracked rather than if. Because of that potential danger, UndChain can modulate and / or change it's cryptographic algorithm. *This is why we have usernames rather than just use public keys* Initially we will use standard AES encryption since that is industry standard and seems like it should work for quite a while longer. When we are close to that algorithm being compromised we will initiate a crypto swap. This will notify users to generate a new public / private key pair using a more secure cryptographic algorithm. The user then responds with the public key to the new protocol and signs it with the current private key so we know it comes from them. The Validators then update the users file to reflect the new public key and on the day of go live we use those signatures instead. If a user fails to update their keys then during the next transaction we initiate a forced key migration (which sounds worse than what it is, basically we send a emergency message back saying to update the key). If that fails, then we allow the account to continue, but notify them that the account is high risk and can be compromised at anytime. UndChain should NEVER force a user to update their keys, but should warn them of the danger of not doing so. *Important to note, once we reach zero day (meaning the attack is live) we do not allow the user to change the key since we don't know if it's them. Instead they can use the freeze feature and hopefully it will go to a updated account. Or they can loose their digital assets if and when someone cracks their account.*

- Interesting thought would be to allow users to update their key at anytime, but I am not sure why anyone would do this. The validator has to mark the active public key anyway so it wouldn't matter if they did update their keys. 
	- Could lead to an attack if users are constantly updating their keys. Maybe charge for out of sequence key update?



---

# Technical Documentation

Might be wondering why it took this long to get to the technical details; UndChain is very abstract right now and I don't have every technical detail flushed out. 

UndChain uses Python for now; I choose Python due to the ease of development however, it is slow and we will pay a price for that. Ideally everything we need just comes with the language. I think the only imports we will use is `hashlib`, `sockets` and `time`. 

The plan is to separate each user type in classes that inherit from user. Each type should have it's own messaging system that I am planning on making a state machine to handle different packets. We will start with Validators since they are the first entity that performs any action on chain. 

## Main

This is going to be basic for now, just a command line that asks what user type are you. Should also detect if you have a key on the system, if not create one.

## Validator Class 

- Need to create an Enum that has the different states a validator can be in
	- **Discovery**
	- **Time Sync**
	- **Ready**
	- **Busy**
	- **Low Trust** - Not sure about this one, we should have it, but I think this should be in addition to the other states.


