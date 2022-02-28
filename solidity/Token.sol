pragma solidity >=0.4.16 <0.9.0;

contract Token {
    mapping (address => uint) public balances;
    function createToken() public {
        balances[msg.sender] = 1000000;
    }
    function transfer(address _to, uint _amount) public {
        if (balances[msg.sender] < _amount) {
            revert("insufficient funds!");
        }
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;
    }
}
