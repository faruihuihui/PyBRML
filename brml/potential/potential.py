"Basic Class: potential"
if __name__ == '__main__':
    print 'PotentialClass is running by itself'
else:
    print 'PotentialClass is imported as module'
	
class potential: 
	def __init__(self, variables = [], table = []): 
		self.variables = variables 
		self.table = table 
	def __mul__(self, other):
                newpot = potential(None, None)
		newpot.variables = self.variables
		newpot.table = self.table * other.table
		return newpot
