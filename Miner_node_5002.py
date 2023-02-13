from flask import Flask, jsonify, request
from uuid import uuid4
import Blockchain

# Part 2 - Mining our blockchain

# Create a web app (Flask base)
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain.Blockchain()


# Creating address for the node on Port 5000
node_address = str(uuid4()).replace("-", "")

# Mine a new block
@app.route('/mineblock', methods=['POST'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender = node_address, receiver = 'Node 5002', amount = 10)
    block = blockchain.create_block(proof,previous_hash)
    response = {'message': 'Congradulations, you just mining the block.',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transaction': block['transactions']}
    
    return jsonify(response), 200

# Getting the full blockchain
@app.route('/getchain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

@app.route('/isblockchainvalid', methods=['GET'])
def is_blockchain_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'status': 'valid',
                    'message': 'Blockchain is valid'}
    else: 
        response = {'status': 'invalid',
                'message': 'Sory Blockchain is invalid'},
    
    return jsonify(response), 200

# Add new transaction
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    json = request.get_json()
    transaction_key = ['sender', 'receiver', 'amount']
    if not all (key in json for key in transaction_key):
        return 'Some element of transaction is missing.', 401
    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    response = {'message': f'this transaction will be added to {index} block'},
    return jsonify(response), 201
    
    
# Part 3 - Decentrallization of Blockchain

# Connecting new nodes
@app.route('/connect_node', methods=['POST'])
def connect_node():
    json = request.get_json()
    nodes = json['nodes']
    if nodes is None and type(nodes) == 'list':
        return 'No nodes', 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'All the nodes are connect. The Farcoin blockchain now contains the following nodes',
                'total_nodes': list(blockchain.nodes)}
    return jsonify(response),201

# Replace the chain by ongest one if needed
@app.route('/replacechain', methods=['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'The node has different chain so the chain is replace by longest one.',
                    'new_chain': blockchain.chain}
    else: 
        response = {'message': 'All good. The chain is the longest one.',
                    'actual_chain': blockchain.chain}
    
    return jsonify(response), 200        

# Running the app
app.run(host = '0.0.0.0', port = 5002)