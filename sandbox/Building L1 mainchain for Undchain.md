# Intro

In this document I plan to outline what was discussed at the meeting on May 17th.

We discussed and came to the common conclusion that there will be the main L1 chain Undchain which:

1. Works according to BFT principles
2. Has a set of validators - **known** and **unknown**. This common set of validators rotates once per epoch and creates an **active validators set** and a **passive validators set**.

> **Active set** - participate in consensus, create blocks and vote for them

> **Passive validators set** - are idle and monitor the chain progress, help in network stability (against DDoS, etc.), but do not participate in consensus and do not generate blocks

### The main functions of such an L1 blockchain:

1. Clients and partners publish receipts in the blocks of this blockchain
2. Through this blockchain, you can initiate transactions (address-address), call smart contracts, etc.
3. Co-chains can interact with this L1


> ***This blockchain serves as the main point of synchronization and sequencing for the entire system - having a clear sequence of blocks in this blockchain where each block has the correct timestamp, the system can progress consistently - block 0, block 1, block 2, ..., block N***


# Required files to launch


Regardless of the node type (validator or regular node), 2 files are required:

1. Genesis - a common entry point for all

In the genesis, you can specify: initial balances, first validators, known validators, configure tokenomics, etc.

2. Configuration - an individual file for each

In the configuration, you can specify: network interfaces and ports, public/private key, other auxiliary options


![](./assets/Pasted%20image%2020250517180509.png)


# A high-level look at how the system works


In this section we'll look at how the system will work at a high level, and then move on to the necessary details.


### Blocks and Epochs

A block is a collection of transactions. It is created by a validator at a given frequency. Then the sequence is as follows:

1. The creator sends the block to validators for approval
2. Waits for 2/3 of the responses
3. Having received 2/3 of the signatures, aggregates them and uses them as proof of acceptance of the block
4. The rest of the network can receive such a block and proof of its acceptance, get transactions from there and execute them, changing the local state


**Visualization**

![](./assets/Pasted%20image%2020250520031803.png)

![](./assets/Pasted%20image%2020250520032233.png)



State modification

![](./assets/Pasted%20image%2020250520033010.png)


**There can be any types of transactions, recipes from clients & partners, etc. The main thing is that they change the state sequentially**


### Epoches

An epoch is a fairly long period of time - several hours, one day, etc. within which:

1) There is one selected active pool of validators (quorum for this epoch)
2) There is a sequence of block generators

Let's see how the system will change from epoch to epoch:


![](./assets/Pasted%20image%2020250521045145.png)


In simple words, each new epoch we will have a large list of validators in the system. From this list we choose:

1) A random subset for the active validators set
2) A random subset for the block creators sequence



# What happens within one epoch

We start the epoch by selecting 2 sets from the entire available set of validators:

1. Active validators set
2. Sequence of block creators


![](./assets/Pasted%20image%2020250521055745.png)


Next, we divide the entire epoch into equal time periods - slots. Each slot is assigned a block creator

![](./assets/Pasted%20image%2020250521061052.png)

In reality, of course, it is worth making such slots small in time - for example, 1 minute, to avoid a situation of network downtime if the creator of the block is inactive or malicious


![](./assets/Pasted%20image%2020250521061556.png)



Within this timeframe, the block creator can generate blocks. Such blocks must be linked to each other - each subsequent block includes the hash of the previous one

The image below shows the process of generating blocks within epoch 5 (the index is taken as an example)

![](./assets/Pasted%20image%2020250521065125.png)


As you can see, each block creator starts their own sequence when it's their turn. It is worth saying that each subsequent block includes the hash of the previous block in the sequence, BUT ONLY IN ITS OWN


![](./assets/Pasted%20image%2020250521070144.png)


# How to carry out rotation?


Rotation plays an important role because it allows the system to:

1) Change active validators
2) Change the order of block creators

Rotation must be pseudo-random so that third-party observers can recalculate everything in a deterministic way and get the same set of active validators and the sequence of block creators


### The hash of the first block of the epoch as a source of pseudo-randomness


We will use the hash of the first block as a source of pseudo-randomness. Therefore, we need a special function that takes as input the hash of the first block and the total set of available validators, and as output gives:

1) A subset of active validators for a given epoch
2) A sequence of block creators for a given epoch

![](./assets/Pasted%20image%2020250521071820.png)

> **We will do such a recalculation at the beginning of each epoch**


# Intermediate results

So by now you should have some general understanding of the system. Let's look at the big picture - let's imagine that the network is ALREADY WORKING

Let's imagine that to begin with we have a genesis file that specifies the initial list of validators, as well as the physical servers of these validators

> You can think of this as a list of known validators


**Here is a detailed, but still GENERAL diagram of how the system might work**

![](./assets/Intermediate_General.svg)



#### Step 1 - get initial data from genesis


Initially - take the data from genesis. Using special function and **zero_hash** (for example 0x00000000) we can build 2 lists - active validators set and block creators sequence


![](./assets/Pasted%20image%2020250522084702.png)


#### Step 2 - start of blocks generation

During the next 1 hour the network will work like this:

![](./assets/Pasted%20image%2020250522084838.png)


1) Sequence of block creators was set
2) Each block creator has own timeframe to generate blocks
3) Each block creator will send his own blocks to active validators set to confirm block and add to blockchain.
4) To confirm block the block creator should get 2/3 proofs from active validators set
5) The hash of first block in this epoch (violet block) will be used as a seed to calculate the active validators set and block creators sequence for next epoch


#### Step 3 - finish this epoch and move to the next one

Take a look at this segment of picture

![](./assets/Pasted%20image%2020250522113608.png)


This shows how network will move from epoch 0 to epoch 1, so demonstrate the **epoch rotation process**

Here's how the process work (high level):

1) Take the hash of first block on epoch 0 (violet block)
2) Once the time is approximately 14:00 - the active validators set of epoch 0 (blue section - Node1, Node3, Node7, Node8, Node10) start exchanging special proofs to move to next epoch (omit this moment right now, will discuss it in next sections)



### !!! IMPORTANT MOMENT !!!

As you can see we use the hash of first block in epoch 0 to build all we need for epoch 1. Via this block we can also **change the whole validators set**

Take a look at the full list of validators in system

For epoch 0

![](./assets/Pasted%20image%2020250522114857.png)

For epoch 1

![](./assets/Pasted%20image%2020250522114915.png)


As you can see, for epoch 0 we take the initial validators from genesis. But for epoch 1 we can see new validators in system (Node 54, Node 19, Node 82) and lack of old validators (Node 5, Node 9, Node 8)

> THIS IS SUPER IMPORTANT MOMENT WHICH SHOWS YOU HOW WE CAN UPDATE THE LIST OF ALL VALIDATORS


Once again:

![](./assets/Pasted%20image%2020250522115400.png)


1. Green arrow shows that from special transactions in the first block in epoch 0 we'll extract operations to add/delete validators from the registry
2. Red arrow shows that the hash of first block in epoch 0 will be used as a seed to calculate the active validators set and block creators sequence for epoch 1

> This mechanism let us to add/delete new validators - known, unknown, doesn't matter. We can also regulate the perception score and modify it via this mechanism to make the system deterministic.

For example, during the epoch life the validators can ping each other to check if validator is online/offline and do useful work for system.

Then we can collect this votes, add to the first block and this data will be used for next epoch



# Now let's talk about how block approvements works

We remember this general scheme


![](./assets/Pasted%20image%2020250522120503.png)


Let's imagine that we are in epoch 0 and we are the very first block generator. That is, we are discussing this - interval from 13:00 to 13:15 :

![](./assets/Pasted%20image%2020250522120656.png)



### Voting for block in general

![](./assets/Pasted%20image%2020250522141831.png)

1. Block creator sends his block to active validators set
2. Each validator sign the block id + hash - to prevent forks
3. Validator sends back the signature as a proof like "I am validator, I accept the block candidate and it's ok"
4. Block creator (Node3 here) collects 2/3 signatures and get a proof that block is confirmed
5. To send next block, block creator should include these 2/3 signatures as a proof that previous block was accepted. Only when block creators share his first block (with index 0) there is no such proof - it's should be obvious. 


#### Important moment

Let's take a look interaction for pair - block creator (Node3) and validator(Node1). Here you can see that the first block do not need 2/3 proof but the second one need it

![](./assets/Pasted%20image%2020250522141905.png)


### Edge case - which explains why we should also send the proof that the previous block was confirmed

Let's imagine the situation: let's say we have 3 validators [Node1, Node2, Node3] and Node1 was offline during voting for block 0, block 1 and block 2 so these blocks have proofs of confirmation like [signa2, signa3] (what is still 2/3 so enough to finalize block)

Then, during voting for block 3, Node1 is online again, but locally Node1 don't have any knowledge about previous blocks by block creator.

Therefore, when block creator sends block 3 and 2/3 proofs for block 2 - Node1 which has zero knowledge about blocks 0,1,2 - can still vote immediately for block 3. It's O(1) complexity thanks to 2/3 signatures which proofs that:

> "Bro, the blocks sequence block0, block1, block2 is sequence and valid and confirmed by majority (2/3), so please, vote for this block (block 3)"

### Leader rotation in general

Let's now look at the moment of block creator rotation. The most important part here is that each subsequent block creator must include in their title

![](./assets/Pasted%20image%2020250522135325.png)

![](./assets/Pasted%20image%2020250522141654.png)

We need to somehow connect 2 such sequences of blocks from different creators in order to get a complete blockchain.

That is why we come to such a term as **ALRP - Aggregated Leader Rotation Proof**

> **ALRP** is a proof that contains 2/3 of the signatures that the network has finished confirming blocks for the previous leader at height X and hash Y


This proof must be included in the first block. In our illustration, the first validator was Node3, and the second was Node5

Therefore, Node5 must include ALRP for Node3 in its first block

This is what it will look like:

![](./assets/Pasted%20image%2020250522153835.png)

1. Once the time is 13:15 (so Node3 should stop block generation and Node5 should start) - Node5 sends message to active validators set and propose to sign ALRP
2. Once Node5 get 2/3 signatures - add it with ALRP to his first block header
3. Node5 continue to generate next blocks



### Edge case: what if previous leader was offline, malicious or for some reason created no blocks

Situation looks like this. Remember our sequence:

![](./assets/Pasted%20image%2020250522144029.png)


Node3, Node5, Node6 - now imagine that Node5 is AFK (offline, malicious, etc.)


This is what happens next:

![](./assets/Pasted%20image%2020250522154303.png)


1. Node6 needs to get the ALRP for all the previous block creators untill the leader which created at least one block
2. In our case Node5 didn't created blocks, so Node6 needs to include to his first block ALRPs for Node5 and Node3
3. Since Node6 see that Node3 created at least one block - then it's ok and it's possible to generate next blocks - block 1, block 2 ....
4. This helps us to make possible to have a clear understanding about blocks sequence


# Epoch rotation


Now that we know about the process of block finalization, about the process of rotation of the block creator - we can move on to the final points. We will talk about the epoch rotation

We'll focus on this part because we only need to take a look a rotation from epoch 0 to epoch 1 - the following rotation will works absolutely the same way:

![](./assets/Pasted%20image%2020250522150409.png)


### Step 1 - take the first block from epoch 0

Here you can see that at the beginning of epoch 0 we will get the first block (violet block)

![](./assets/Pasted%20image%2020250522150610.png)


That's why approximately on 13:00 we'll know the hash of this block and based on this hash & block - we can calculate the active validators set and block creators sequence FOR NEXT EPOCH (WITH INDEX = 1)

This process is shown below with red and green arrows

![](./assets/Pasted%20image%2020250522151047.png)


> Why it's important moment - because it shows that we can calculate the active validators set and block creators sequence for **NEXT EPOCH (epoch index = 1)** before **THIS EPOCH (epoch index = 0)** will be finished


### What next

Next we keep working untill the end of epoch - untill 14:00 here

![](./assets/Pasted%20image%2020250522151259.png)


Also, let's imagine a real world scenario that Node5 and Node1 was offline of malicious and created no blocks

![](./assets/Pasted%20image%2020250522154700.png)


So, from this picture it's easy to assump that the first block of epoch will be created by Node3 while epoch will be finished (de-facto) with blocks by Node6


### Moment when active validators set understand that we need to finish epoch

Approximately in the end of epoch 0 - current validators set understand that it's time to finish it. They starts to exchange special data and once majority agree - this proof can be sent to next epoch active validators set.

This will be the signal for epoch 1 that it's time to start new epoch

![](./assets/Pasted%20image%2020250522152444.png)


### Details about proof

The proof which active validators set will try to get in the end of epoch 0 called **AEFP - Aggregated Epoch Finalization Proof**

> **AEFP - Aggregated Epoch Finalization Proof** - is a proof that 2/3 of validators set is agree to finish epoch N on block **X** with hash **Y** to move to epoch N+1


Don't worry if hard - I'll explain.  When it's time to finish epoch (epoch 0 in our example) what should be done?

Remember that we decided to imagine situation like this:

![](./assets/Pasted%20image%2020250522154831.png)

#### Step 1 - active validators set exchange proposition of AEFP

So, imagine that our epoch will finish on Node6


![](./assets/Pasted%20image%2020250522155008.png)

For example, node8 sends proposition to node10. In case node10 is ok with AEFP verification - sign this message and send back the signature

##### Important moment

There may be situations when, say, node8 was offline during voting for node3 and node5 (which created 0 blocks).

In this case:

1) The members of the active validators set (except node Node8) will have information that the last block was block index=4 from Node6

2) Node8 will have information that the last block was, say, index=2 from Node3

In this case, communication from Node8 to Node10 will look like this:

![](./assets/Pasted%20image%2020250522155821.png)


1. Once Node10 receive WRONG proposition - it sends back the more actual info
2. In UPGRADE message Node10 informs Node8 that network progressed more than Node8 thinks
3. Everything in UPGRADE message can be proven - the first part (about last block) is proven by 2/3 of signatures by active set majority. We receive this data during [[#Voting for block in general]]
4. `hashOfFirstBlockByLastCreator` also can be proven - using same principle (see [[#Voting for block in general]])

#### Step 2 - once some of validator have 2/3 signatures - send to next active validators set

Just send the AEFP with 2/3 signatures to next active validators set

![](./assets/Pasted%20image%2020250522160340.png)


#### Step 3 - active validators set of next epoch can start voting for blocks in their epoch

On this step new epoch should start - with new active validators set, new block creators sequence and so on

![](./assets/Pasted%20image%2020250522160450.png)



## So, what the sense of getting AEFP

It's crucial moment because we need AEFP to connect epochs with each other


> **EACH BLOCK CREATOR NEEDS TO INCLUDE AEFP PROOFS TO HIS FIRST BLOCKS TO GET A 100% GUARANTEE OF SECURITY AND CHAIN INTEGRITY**


Let's take a look at the block creators sequence for epoch 1

![](./assets/Pasted%20image%2020250522160945.png)


In this case we de-jure mark with **orange color** the first block but de-facto, remember the cases when nodes can be offline/malicious. In this case it's a rule - **each block creator should include AEFP for previous epoch to own first block**:


![](./assets/Pasted%20image%2020250522161435.png)



# Final words about types of proofs

So, we have mentioned several types of proofs:

#### AFP - Aggregated Finalization Proof

Proof that 2/3 of the active validators set agree with the block **B** created by block creator **C**. This block has index **I** and hash **H**


This is what we get during finalization of blocks

![](./assets/Pasted%20image%2020250522163658.png)


#### ALRP - Aggregated Leader Rotation Proof

Proof that 2/3 of the active validators set agree to finish finalizing blocks creator **C** at index **I** and hash **H** and are ready to move on to finalizing blocks of the next block creator

This is what each next block creator includes to his first block.

> Note: In case you're the first block creator in sequence - you shouldn't include something because there is no other block creators before you


For example in epoch 2, the Node2 shouldn't include any ALRP because it's the first block creator

![](./assets/Pasted%20image%2020250522164317.png)


In epoch 0 (below):

![](./assets/Pasted%20image%2020250522164405.png)


1. Node3 - no ALRP
2. Node6 - should include ALRP for Node5, Node3

**BUT**

If the Node5 created at least one block then:

![](./assets/Pasted%20image%2020250522164606.png)

In this case Node6 can include ALRP for Node5, but no need to include for Node3


#### AEFP - Aggregated Epoch Finalization Proof

Proof that 2/3 of the active validators set agree that it is time to end the epoch on block creator **C**, index of its last block **I** and hash **H**

This is what each block creator includes to their first block

> **Note:** In case it's epoch 0 - no one should include AEFP to header - because it's the first epoch so no previous epoch exists


Take a look:

![](./assets/Pasted%20image%2020250522165256.png)


# Next step - resolve the blocks sequence

In the previous chapters, we looked at the mechanism of block generation, rotation of block creators and changing the epoch.

All this perfectly shows how to keep block generation - from creator to creator and from epoch to epoch.

However, the question remains unclear:

> How can we now have a clear understanding of the block sequence?

In the previous chapters, we got acquainted with different types of proofs - AFP, ALRP, AEFP.

It is on their basis that we will be able to apply special algorithms to resolve the sequence and have a clear idea of ​​the first, second, third and so on blocks.

# Next step - resolve the blocks sequence

To know how to modify the state, we need to have a clear understanding which block is the first, the second, the third and so on.

Because of async, distributed, permissionless nature of L1 blockchain some specific algorithms should be used to use the blocks from block creators and majority proofs and based on this - build the traditional sequence of blocks.

In the previous chapters, we looked at the mechanism of block generation, rotation of block creators and changing the epoch.

All this perfectly shows how to **keep block generation** - from creator to creator and from epoch to epoch.

However, the question remains unclear:

> **How can we now have a clear understanding of the block sequence?**


In the previous chapters, we got acquainted with different types of proofs - AFP, ALRP, AEFP.


It is on their basis that we will be able to apply special algorithms to resolve the sequence and have a clear idea of ​​the first, second, third and so on blocks.

### High level overview

First, we should think of the block processing system as a black box that takes 2 things as input:

1) Block itself
2) Cryptographic proof that the block is indeed should be the next one in sequence.

Only with this pair we can extract the transactions inside the block and safely execute - this will change the local state.

![](./assets/Pasted%20image%2020250528011213.png)

#### Important moment

The whole secret of the block ordering system will lie in this place

![](./assets/Pasted%20image%2020250528012023.png)

At first glance, it may seem that this is a simple AFP (Aggregated Finalization Proof) - just 2/3 of the signatures from the active set of validators approving this block.

**However, this is not always the case - and we will discuss this further.**

# Overview of sequencing scheme in general

Let's recall our general scheme of network workflow

![[Intermediate_General.svg]]

So, since we have both **block creator rotation** and **epoch rotation**, we need to somehow organize the created blocks to simply get a sequence like this:

```
block 0
block 1
block 2
...
block N
```

Now let's pay attention to the right part of the image.

![](./assets/Pasted%20image%2020250528013240.png)


In an ideal world, the sequence of blocks would look like this:

![](./assets/Pasted%20image%2020250528145541.png)

But in reality, it is worth remembering that:

1) Some block creators may be **inactive**
2) The diagram CONDITIONALLY shows 4 blocks created by each creator, but in reality their number depends on the timeframe of the block creator and the block time.

> *For example, if a maximum per one creator is 100 blocks during a time interval (green timeframe in the figure), then there may be situations where someone creates 100 blocks, someone 74, someone 89, and so on.*


For example, here is a situation that could be real

![](./assets/Pasted%20image%2020250528150316.png)

In this situation:

1. In epoch 0, the creator of Node6 was malicious, and in epoch 1, Node4 and Node6 were offline so they did not create a single block
2. In epoch 0, Node5 created only 3 blocks, and Node1 created six blocks.
3. In epoch 1, Node7 created eight blocks, and in epoch 2, Node4 created two blocks.


### The first part of the algorithm - within one epoch

To begin with, we will consider only single epoch. Let's assume (for simplicity) that it is infinite epoch and our only task is to understand how to resolve the sequence of blocks.

So we have this epoch

![](./assets/Pasted%20image%2020250528152710.png)

#### Step 1 - just ask currrently active block creator for AFPs (aggregated finalization proofs)

As long as your local clock shows the timeframe of the current block creator (in our case, it's Node3, so the time is about 13:00-13:15) - you can simply send requests to the network to get a block and AFP for it.

Remember that Node3 (current block creator) generates blocks and sends it to active validators set for finalization.

![](./assets/Pasted%20image%2020250528154108.png)

Remember the AFP structure (pseudocode - Golang):

```go
type AggregatedFinalizationProof struct {

    PrevBlockHash string            `json:"prevBlockHash"`

    BlockID       string            `json:"blockId"`

    BlockHash     string            `json:"blockHash"`

    Proofs        map[string]string `json:"proofs"`

}
```

This is the example of AFP for block `0:Node3:0`

```go
afp0 := AggregatedFinalizationProof{
	PrevBlockHash: "000000000000000000000000000000000000000000000000000000000000",
	BlockID:       "0:Node3:0",
	BlockHash:     "abcd1234efgh5678ijkl9012mnop3456qrst7890uvwx",
	Proofs: map[string]string{
		"validator1": "signature1",
		"validator2": "signature2",
		"validator3": "signature3",
	},
}
```


And AFP for block `0:Node3:1`

```go
afp1 := AggregatedFinalizationProof{
	PrevBlockHash: "abcd1234efgh5678ijkl9012mnop3456qrst7890uvwx",
	BlockID:       "0:Node3:1",
	BlockHash:     "ffff1111aaaa2222bbbb3333cccc4444dddd5555eeee",
	Proofs: map[string]string{
		"validator1": "signature1",
		"validator2": "signature2",
		"validator3": "signature3",
	},
}
```

So, your local system will do the following:

![](./assets/Pasted%20image%2020250528155135.png)

1. Quickly poll the network for new blocks and proof of finality (AFP)
2. Once you receive a block and AFP for the next block, you can perform transactions inside and be 100% sure that the state is finalized
3. Just get the hash of block `0:Node3:0` and compare with hash inside AFP for block `0:Node3:1`

Like this

```go
if hash(Block("0:Node3:0")) == afp1.PrevBlockHash) {

 // execute txs inside block

}
```

#### Step 2 - migrate to the next block creator

Let's say in our core source code, in a separate thread, there is a mechanism that constantly polls active validators about the next block creator.

For example, if we know that Node3 is currently creating blocks. But at the same time, we send requests to active validators to ask if they have switched to Node5

TODO

### The second part of the algorithm - what if the epoch has changed

TODO



# Conclusion


In this large research was showed the process of creating an L1 chain that follows the principles of BFT consensus.

I tried to mention and visualize all the details necessary for understanding and creating a blockchain.

We went from the initial launch of epoch 0 and data in the genesis to the development of the chain up to epoch 2 - to show the rotation of epoches. Further development of the network (to the next epoches) follows the same principles

It was also mentioned:

1) The process of calculating the active validators set and block creators sequence
2) The process of collecting proofs for finalizing a block is demonstrated
3) The process of rotating the block creator and the necessary proofs for this is shown
4) The process of rotating the epoch, the process of collecting proofs and further work of the network in the next epoches is shown

Additionally, this document can be expanded with a section "Assembling the pieces" (like in OffSec manuals) in which to collect all the mentioned sections and simulate the process of network workflow along with visualization.