# Farcoin - A Blockchain-Based Cryptocurrency
Farcoin is a blockchain-based cryptocurrency that is designed to provide fast, secure and decentralized transactions. The project is built on top of a decentralized ledger technology, which ensures that all transactions are immutable and cannot be altered.

## Features
Fast Transactions: Farcoin uses advanced blockchain technology to provide fast transactions with low fees.

Secure: Farcoin uses cryptographic techniques to secure all transactions and protect users' funds.

Decentralized: Farcoin operates on a decentralized network, which means that there is no central authority controlling it.

Mining: Farcoin can be mined using a proof-of-work algorithm, which allows users to contribute to the network and earn rewards.

## Nodes
Farcoin operates on a decentralized network, which is powered by nodes. The project includes three different nodes, node 5001, node 5002 and node 5003, which serve as the backbone of the network. Each node is responsible for verifying transactions and maintaining a copy of the blockchain.

## Getting Started
If you would like to get started with Farcoin, you can download the code from this repository and follow the instructions for setting up your own node. You can also join the existing network by connecting to one of the existing nodes.

## Endpoints

1- baseurl/connect_node: This endpoint allows you to connect nodes by sending a JSON in the body. The JSON is provided in the "json" folder.

2- baseurl/getchain: This endpoint retrieves the current blockchain of the node.

3- baseurl/mineblock: This endpoint is used to mine a new block in the blockchain.

4- baseurl/add_transaction: This endpoint enables you to make transactions by adding them to the blockchain.

5- baseurl/replacechain: This endpoint performs the consensus algorithm to determine the longest chain in the current node and replaces the current chain with the longest one.

5- baseurl/isblockchainvalid: This endpoint checks if the node contains a valid chain. If the chain is valid, it returns a positive response. Otherwise, it returns an error.
