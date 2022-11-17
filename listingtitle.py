class listing:
    def __init__(self, description):
        self.description = description

    def fullitem(self):
        return '{}'.format(self.description) + ", Ghana football kit 2014-2017"

l1 = listing('afsdfgasd')
l2 = listing('zvxczxcvz')

print(l1.fullitem())
print(l2.fullitem())
