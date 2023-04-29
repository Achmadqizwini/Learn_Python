from numbers import Number

print("1. divide your number by 10")
print("2. write and write a file")
print("3. add your number")

try:
    do = int(input("\ninput program you want to run: "))
    if do == 1:
        while (True):
            result = 0
            try:
                input_data = int(input("input a number: "))
            except:
                print("input data must be integer")
                continue
            try:
                result = 10 / input_data
                print(result)
                loop = input("want to try again? (y/n) ")
                if loop == "n" or loop == "N" or loop == "No" or loop == "NO":
                    break
            except:
                print("a number cannot be divided by 0, input another number")

            print("program end")
    elif do == 2:
        while (True):
            try:
                with open("data_test.txt", mode="r") as file:
                    print(file.read())
                    break
            except:
                with open("data_test.txt", mode="w", encoding="utf-8") as file:
                    file.write("file baru")
    elif do == 3:
        while (True):
            nums = input("input 2 number separated by space: \n")
            data_nums = nums.split()
            if len(data_nums) != 2:
                print("you have to input 2 number")
                continue
            # if not isinstance(data_nums[0], Number) or not isinstance(data_nums[1], Number):
            #     raise "input must be integer"
            else:
                print("hasil = ", int(data_nums[0]) + int(data_nums[1]))
                break

except Exception as error:
    print("input must be integer")
    print(error)

print("program ended")
