with open("../test_results.txt", "w") as file:
    file.write("Test Passed!")

with open("../test_results.txt", "r") as file:
    print(file.read())
