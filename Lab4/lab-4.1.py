class structureclass ():
    scope = 5
    height = 10
    def formulacalculate (CUlate):
        CUlate.Measure = 3.14*(CUlate.scope*CUlate.scope)*CUlate.height
        return CUlate.Measure
class structureclass2():
    scope = 7
    height = 13
    def formulacalculate2 (CUlate2):
        CUlate2.Measure = 3.14*(CUlate2.scope*CUlate2.scope)*CUlate.height
        return CUlate2.Measure
CUlate = structureclass()
CUlate2 = structureclass2()

print("answerCUlate is "+ str(CUlate.formulacalculate()))
print("answerCUlate2 is "+ str(CUlate2.formulacalculate2()))

