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
