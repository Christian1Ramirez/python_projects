def hello():
    print("Hello, how are you!")


def pack(param1,param2,param3):
    return [1,2,3]
    

def eat_lunch(list):
    if len(list) == 0:
        print("My Lunchbox is empty")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")

hello()
print(pack("1","2","3"))
print(pack(1,2,3))
eat_lunch(["cookie"])
eat_lunch(["pie","sandwich","juice","beagle"])
eat_lunch([])