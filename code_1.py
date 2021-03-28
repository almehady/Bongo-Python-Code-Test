
a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": {
                "key6": {
                    "key7": 1,
                }
            }
        }
    }
}


def print_depth(data):
    d = 1
    def depth(data, d):
        for key in data:
            if type(data[key]) == dict:
                print(key + " " + str(d))
                depth(data[key], d+1)
            else:
                print(key + " " + str(d))
    depth(data, d)
print_depth(a)