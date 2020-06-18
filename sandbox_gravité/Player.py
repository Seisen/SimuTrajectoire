
class objet():
    masse=0
    vecX=0
    vecY=0
    x=0
    y=0
    elasticité=0
    friction=0
    largueur=0
    couleur=(0,0,0)
    traine=[]

    def __init__(self):
        self.masse=0
        self.vecX=0
        self.vecY=0
        self.x=0
        self.y=0
        self.elasticité=0
        self.friction=0
        self.largueur=0
        self.traine=[0]#premier attribut est la taille
        self.couleur=(250,250,250)
    def set_taille_traine(self,nmb):
        try:
            int(nmb)
            self.traine[0]=nmb
        except ValueError:
            pass
        
    def set_couleur(self,couleur):
        self.couleur=couleur

    def set_largueur(self,nmb):
        try:
            float(nmb)
            self.largueur=nmb
        except ValueError :            
            pass

    def set_masse(self,nmb):
            try:
                float(nmb)
                self.masse=nmb
            except ValueError :            
                pass

    def set_friction(self,nmb):
        try:
            float(nmb)
            self.friction=nmb
            
        except ValueError:
            pass


    def set_elasticité(self,nmb):
        try:
            float(nmb)
            self.elasticité=nmb
        except ValueError :            
            pass


    def set_Vec(self,x,y):
        
        try:
            float(x)
            float(y)
            self.vecX=x
            self.vecY=y
        except ValueError :            
            pass

    def set_VecX(self,x):
        
        try:
            float(x)
            self.vecX=x
        except ValueError :            
            pass

    def set_VecY(self,y):
        
        try:
            float(y)
            self.vecY=y
        except ValueError :            
            pass

    def set_pos(self,x,y):
            try:
                float(x)
                float(y)
                self.x=x
                self.y=y
            except ValueError :            
                pass

