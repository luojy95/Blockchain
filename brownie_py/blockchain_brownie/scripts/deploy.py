from brownie import accounts, config, SimpleStorage, network

def deploy_simple_storage():
    # account = accounts.load("brownie_test")
    account = get_account()
    print(f"Account: {account}") # Get the account info

    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()

    print(stored_value)
    transaction = simple_storage.store(16, {"from": account})

    transaction.wait(5) # Specify how many blocks need to wait
    updated_stored_value = simple_storage.retrieve()

    print(updated_stored_value) # Check the updated version is correct or not

def get_account():
    if (network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def main():
    deploy_simple_storage()