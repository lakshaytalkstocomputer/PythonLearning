#Local versus Global part 2

def local():
    #m doesn't belong to the scope defines by the local function
    #SO python will keep looking into the next enclosing scope
    #m is finally found in the global scope
    print(m,"printing from the local scope")

m = 5
print(m, "printing from the global scope")

local()