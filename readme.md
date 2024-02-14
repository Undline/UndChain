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

- **Main Chain** - This co-chain is responsible for creating the messaging protocols that go between various user types. It sets up two tokens, one for validators and the other for partners. Compiler for the Pseudo programing language, it creates an alias system that allows users to have user names that could be used for easier transactions (user names begin with an @). It sets the rules to create chain rules, which includes several options such as developer compensation, tokenomics and preferred validators. It also stores the link that go across multiple networks. There will be more details on all this later since the main chain's code is here.

- **Mimic** - This is our AI chain, in here we create very specific models that are great at a particular task then link that up to a hypervisor that directs the incoming request to the correct model. *The reason for many small models rather than one monolithic model is so it's easier to change and can run on various hardware*

- **Pages** - This is our Web 4 system that delivers something similar to webpages, but instead of HTML and CSS you have M3L and GSS. The advantages of those markups is they allow a single component to be updated rather than an entire document so it's less load on the network. The goal is to also get rid of cookies so you're not helping companies track your habits online. This also introduces AdCoin which is used for pulling up different pages; you can trade for it or earn it by interacting with ads.

- **Code Ledger** - This is a software repository that is specifically built for Pseudo since we need a means of tracking changes to the code from a specific user and pay them out accordingly based on what the chain rules state. Haven't spoke on this, but the idea is that you can earn tokens by contributing code to project and depending on the impact you get rewarded. There is also a bounty system for new developments. 

## Co-chain code

While I believe that the best policy is to have open source code. I will be making the chain so that you can run closed source code, at this time I am not sure on how to do it since there is an inherent risk of a security vulnerability if it's being shared publicly. More thought will have to be put into this at a later time, I just put this here so I wouldn't forget.

# User Types

In UndChain there are four different user types; this is done to create a separation of powers so that no one entity could jeopardize the chain. 

1. **Chain Owner** - It's probably best to think of Chain Owners as developers. This group is responsible for creating the functionality of the chain as well as setting the tokenomics (fees). Chain owners also select who they are partnered with, at this time I believe the limit will be two. Chain owners are also able to select preferred validators (I'd say in most cases it would be themselves) and how many validators they will have on the network, with the minimum being four. *yep, I already know what you're worried about, it gets addressed later* 

2. **Validators** - Think of Validators as routers and are responsible for taking a user request and connecting them with an appropriate resource. This is mainly meant to link clients and partners together. They are also responsible for keeping up with utility payout and they validate the traffic going between users. 