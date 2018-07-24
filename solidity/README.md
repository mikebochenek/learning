
# Test 1
http://solidity.readthedocs.io/en/v0.4.24/introduction-to-smart-contracts.html

sudo add-apt-repository ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install solc
solc
solc --metadata SimpleStorage.sol



# Test 2
https://dzone.com/articles/ethereum-hello-world-example-using-solc-and-web3

sudo npm install web3
   │  Update available 4.6.1 → 6.2.0    │
   │     Run npm i -g npm to update
sudo npm install abi-decoder  # added 327 packages from 272 contributors and audited 200058 packages in 63.675s
sudo npm install ethereumjs-testrpc  # added 61 packages from 12 contributors in 41.255s
sudo npm install solc  


# Start Local Ethereum Node
./node_modules/.bin/testrpc --gasPrice 20000


# start node
node

# load a few Node.js modules
const fs = require("fs"),
    abiDecoder = require('abi-decoder'),
    Web3 = require('web3'),
    solc = require('solc');

# Compile Smart Contract
const input = fs.readFileSync('contracts/Token.sol');
const output = solc.compile(input.toString(), 1);
const bytecode = output.contracts[':Token'].bytecode;
const abi = JSON.parse(output.contracts[':Token'].interface);

# Connect to Ethereum and Create Contract Object
let provider = new Web3.providers.HttpProvider("http://localhost:8545");
const web3 = new Web3(provider);
let Voting = new web3.eth.Contract(abi);    

# Add ABI to Decoder
abiDecoder.addABI(abi);

# Find (Dummy) Ethereum Accounts
web3.eth.getAccounts().then(accounts => {
  accounts.forEach(account => {
    console.log(account)
  })
});


# Transfer Money between Accounts
var allAccounts;
web3.eth.getAccounts().then(accounts => {
  allAccounts = accounts;
  Voting.deploy({data: bytecode}).send({
    from: accounts[0],
    gas: 1500000,
    gasPrice: '30000000000000'
  }).on('receipt', receipt => {
    Voting.options.address = receipt.contractAddress;
    Voting.methods.transfer(accounts[1], 10).send({from: accounts[0]}).then(transaction => {
      console.log("Transfer lodged. Transaction ID: " + transaction.transactionHash);
      let blockHash = transaction.blockHash
      return web3.eth.getBlock(blockHash, true);
    }).then(block => {
      block.transactions.forEach(transaction => {
        console.log(abiDecoder.decodeMethod(transaction.input));
      });
      allAccounts.forEach(account => {
          Voting.methods.balances(account).call({from: allAccounts[0]}).then(amount => {
            console.log(account + ": " + amount);
          });
      });
    });
  });
});


# Sample Output
  Transaction: 0x9a3acd0c17ef38cddb21f88a059b11edee54a4a4fdd3f1eddbb513f680220141
  Gas usage: 48918
  Block Number: 2
  Block Time: Tue Jul 24 2018 22:26:00 GMT+0200 (CEST)
