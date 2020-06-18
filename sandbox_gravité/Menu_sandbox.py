import pygame
class menu_sandbox():
    curseur1Min=0
    curseur1Max=0
    curseur2Min=0
    curseur2Max=0
    curseur1=0
    curseur2=0
    curseur3=0

    yMax=0
    yMin=0

    boutonClicked=False

    ClickedForPos=False

    checkbox1=False
    checkbox2=False

    couleur_bouton=(80,80,250)
    couleur_bouton2=(250,80,80)
    def __init__(self):

        self.curseur1Min=550
        self.curseur1Max=850
        self.curseur2Min=950
        self.curseur2Max=1250
        self.curseur3Min=1650
        self.curseur3Max=1800

        self.yMax=950
        self.yMin=920

        self.curseur1=self.curseur1Min
        self.curseur2=self.curseur2Min
        self.curseur3=self.curseur3Min

    def set_curseur1Pos(self,nmb):
        try:
            int(nmb)
            self.curseur1=nmb
        except ValueError:
            pass
    def set_curseur2Pos(self,nmb):
        try:
            int(nmb)
            self.curseur2=nmb
        except ValueError:
            pass
    def set_curseur3Pos(self,nmb):
        try:
            int(nmb)
            self.curseur3=nmb
        except ValueError:
            pass
    def change_couleur(self,bool):

        if bool:
            self.couleur_bouton=(150,150,250)
        else:
            self.couleur_bouton=(80,80,250)

    def change_couleur2(self,bool):

        if bool:
            self.couleur_bouton2=(250,150,150)
        else:
            self.couleur_bouton2=(150,80,80)
    #inverse
    def inverse_checkbox1(self):
        self.checkbox1 = not self.checkbox1
    def inverse_checkbox2(self):
        self.checkbox2 = not self.checkbox2
    def inverse_clicked(self):
        self.boutonClicked= not self.boutonClicked
    def inverse_clickedForPos(self):
        self.ClickedForPos= not self.ClickedForPos
    

    def get_masseValue(self):
        val=(self.curseur1-self.curseur1Min)*100/(self.curseur1Max-self.curseur1Min)
        val=int(val)
        return val

    def get_tailleValue(self):
        val=(self.curseur2-self.curseur2Min)*100/(self.curseur2Max-self.curseur2Min)
        val=int(val)
        return val

    def get_traineValue(self):
        val = (self.curseur3-self.curseur3Min)*100/(self.curseur3Max-self.curseur3Min)
        val = ((int(val)*15)//100)*100
        return val

    def get_couleur(self):
        masse = self.get_masseValue()
        masse*=2.5
        couleur=(250-masse,250-masse,250)
        return couleur
