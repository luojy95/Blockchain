# To create new account
`brownie accounts new brownie_test`

# To test
`brownie test`

## To test one specific function
`browine test -k ${FUNCTION_NAME}`

## To debug
`brownie test --pdb`

## To test with print and details
`brownie test -s`

# To add sepolia to brownie
`brownie networks add Ethereum sepolia host="https://sepolia.infura.io/v3/62d874c3a0b84bb980be207564ec91e0" chainid=11155111`

# To deploy
`simple_storage = SimpleStorage.deploy({"from": account})`