class PRM():
    BLength = 10
    BWidth = 7
    PRM_height = 17
    def formulacalculate(CUlate):
        CUlate.ALL = (CUlate.BLength*CUlate.BWidth*CUlate.PRM_height)/3
        return CUlate.ALL

PRM = PRM()
print("PRM ALL = " + str(PRM.formulacalculate()))
