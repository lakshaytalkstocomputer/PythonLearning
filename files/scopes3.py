# Local , enclosing, and Global

def enclosing_func():
    m = 13

    def local():
        # m doesn't belong to the scope defined bt the local
        # fucntion so pythopn will keep looking into the next
        # enclosing scope. This time m is founds in the enclosing
        # scope
        print(m, "printing from the local scope")

    # calliung the fdunction local
    local()


m = 5
print(m, "printing from the global scope")

enclosing_func()
