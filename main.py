class MLOps:
    def __init__(self,totalStudents):
        self.totalStudents = totalStudents

    def getTotalStudents(self):
        return self.totalStudents

    def AddStudents(self):
        self.totalStudents = self.totalStudents + 1
    
    def removeStudents(self):
        self.totalStudents -= self.totalStudents - 1

    def getClassName(self):
        return "Machine Learning Operations (CS-B)"

# Mlops_class = MLOps(5)
# Mlops_class.AddStudents()
# Mlops_class.removeStudents()
# print(Mlops_class.getTotalStudents())
# print(Mlops_class.getClassName())
