# test if the program is working correctly
# usage: bash binary_test.sh
# if the program is working correctly, it will print nothing
# if the program is not working correctly, it will print the difference between the output and the expected output
# if there is no difference, it will print "test passed"

if [ ! -f main.out ]; then
    echo "main.out not found"
    exit 1
fi

# if there is difference, print the difference
# if there is no difference, print "test passed"

# test 1
echo "test 1"
./main.out < input1.txt > output1.txt
diff output1.txt expected_output1.txt
if [ $? -eq 0 ]; then
    echo "test passed"
fi

# test 2
echo "test 2"
./main.out < input2.txt > output2.txt
diff output2.txt expected_output2.txt

if [ $? -eq 0 ]; then
    echo "test passed"
fi
