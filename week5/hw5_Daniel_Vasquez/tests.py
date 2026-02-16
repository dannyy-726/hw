from tuple_and_file_utils import transform_tuple,unique_letters,read_students, grade_summary, write_averages
    

if __name__ == "__main__":
    print("Running tests for HW5:")

    #Task 1 test
    result = transform_tuple((234,324,5,53,75))
    print(f"Task 1 test results: {result}")

    #Task 2 test
    result = unique_letters("apple","weather")
    print(f"Task 2 test results: {result} ")

    #Task 3 test
    test_data = {"Alice":[88,92,100],"Bob":[75,78,80]}
    result = grade_summary(test_data)
    print(f"Task 3 test results: {result} ")

