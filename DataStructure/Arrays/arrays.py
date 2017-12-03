numbers =  [10, 20, 30, 40, 50];
print(numbers);

# random indexing --> O(1) get items if we know the index !!!
print(numbers[0]);

# insert --> O(N)
numbers[1] = 200;
print(numbers[1]);

# Python arrays are not simple arrays
# numbers[1] = 'Python!';

# for i in range(len(numbers)):
#     print(numbers[i]);
# the same
# for num in numbers:
#     print(num);

# semicolon operator
print('semicolon operator ')
print(numbers[0:2]);
print('all items -> numbers[:]');
print(numbers[:]);
print('all items except last two -> numbers[:-2]');
print(numbers[:-2]);
