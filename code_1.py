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
    },
    "key8": 8
}


def print_depth(data):
    # set the step here
    step = 1
    def depth(data, step):
        for key in data:
            # check if the key is a dictionary
            if type(data[key]) == dict:
                print(key + " " + str(step))
                depth(data[key], step+1)
            else:
                print(key + " " + str(step))
    depth(data, step)
print_depth(a)