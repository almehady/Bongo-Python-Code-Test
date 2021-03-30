class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def dic(self):
        d = {}
        d = {
            "first_name:": self.first_name,
            "last_name:": self.last_name,
            "father:": self.father
        }
        return d


person_a = Person(" User ", " 1 ", None)
person_b = Person(" User1 ", " 2 ", person_a.dic())

a = {
    "key1": 1,
    "key2": {
            "key3": 1,
            "key4": {
                    "key5": 4,
                    "user:": person_b.dic(),
            },
    },
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