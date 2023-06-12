with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

# Compile the Solidity

compiled_sol = compile_standard()
