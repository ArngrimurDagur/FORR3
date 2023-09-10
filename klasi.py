class Felag_Tækniskolans():
    numer=0
    def __init__(self,nafn,kennitala,braut,aldur,numer):
        self.nafn=nafn
        self.kennitala=kennitala
        self.braut=braut
        self.aldur=aldur
        self.numer=Felag_Tækniskolans.numer
        Felag_Tækniskolans.numer+=1
    def __str__(self):
        return self.nafn