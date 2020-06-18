import pygame
import Player
import Physic_engine as mP
import Menu_sandbox
import sys


class Main():

    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    menu=True
    menu_sandbox=Menu_sandbox.menu_sandbox()

    liste_obj=[]
    attracteurs=[]
    joueurs=[]
    
    font = pygame.font.Font('font/Calculator.ttf', 48)
    PlacerObjet = font.render("PLACER L'OBJET ",1,(250,250,250))
    font = pygame.font.Font('font/Calculator.ttf', 100)
    lancer = font.render("SIMULER ",1,(250,250,250))
    font = pygame.font.Font('font/Calculator.ttf', 32)
    masse=font.render("MASSE ",1,(250,250,250))
    taille=font.render("TAILLE",1,(250,250,250))
    traine=font.render("TRAINE",1,(250,250,250))
    font = pygame.font.Font('font/Calculator.ttf', 20)
    Soumit=font.render("SOUMIS AUX CHAMPS",1,(250,250,250))
    Soumet=font.render("SOUMETS UN CHAMP",1,(250,250,250))


    def __init__(self):

        mP.set_gravite(1)
        self.main()

#pour donner l'illusion de se déplacer sur l'écran
    def moveAllH(self):
        for i in range(len(self.liste_obj)):
            self.liste_obj[i].y+=10
            for j in range(1,len(self.liste_obj[i].traine)):
                x,y=self.liste_obj[i].traine[j]
                y+=10
                self.liste_obj[i].traine[j]=(x,y)

    def moveAllB(self):
        for i in range(len(self.liste_obj)):
            self.liste_obj[i].y-=10
            for j in range(1,len(self.liste_obj[i].traine)):
                x,y=self.liste_obj[i].traine[j]
                y-=10
                self.liste_obj[i].traine[j]=(x,y)

    def moveAllG(self):
        for i in range(len(self.liste_obj)):
            self.liste_obj[i].x+=10
            for j in range(1,len(self.liste_obj[i].traine)):
                x,y=self.liste_obj[i].traine[j]
                x+=10
                self.liste_obj[i].traine[j]=(x,y)

    def moveAllD(self):
        for i in range(len(self.liste_obj)):
            self.liste_obj[i].x-=10
            for j in range(1,len(self.liste_obj[i].traine)):
                x,y=self.liste_obj[i].traine[j]
                x-=10
                self.liste_obj[i].traine[j]=(x,y)

    def deleteAll(self):

        while len(self.joueurs)>0:
            self.joueurs.pop(0)

        while len(self.attracteurs)>0:
            self.attracteurs.pop(0)

        while len(self.liste_obj)>0:
            self.liste_obj.pop(0)

    def actualise_texte(self):
    
        font = pygame.font.Font('font/Calculator.ttf', 32)
        self.masse=font.render("MASSE = "+str(self.menu_sandbox.get_masseValue()),1,(250,250,250))
        self.taille=font.render("TAILLE = "+str(self.menu_sandbox.get_tailleValue()),1,(250,250,250))
        self.traine=font.render("TRAINE = "+str(self.menu_sandbox.get_traineValue()),1,(250,250,250))


    def affiche_menu_sandbox(self):
       

        pygame.draw.rect(self.screen, (250,250,250), (550,942,300,5))
        pygame.draw.rect(self.screen, (250,250,250), (950,942,300,5))
        pygame.draw.rect(self.screen, (250,250,250), (1650,942,150,5))

        pygame.draw.rect(self.screen, (250,250,250), (self.menu_sandbox.curseur1,920,3,50))
        pygame.draw.rect(self.screen, (250,250,250), (self.menu_sandbox.curseur2,920,3,50))
        pygame.draw.rect(self.screen, (250,250,250), (self.menu_sandbox.curseur3,920,3,50))


        pygame.draw.rect(self.screen, (250,250,250), (1350,925,50,50))
        pygame.draw.rect(self.screen, (250,250,250), (1500,925,50,50))

        self.screen.blit(self.masse,(630,1000))
        self.screen.blit(self.taille,(1030,1000))
        self.screen.blit(self.Soumit,(1310,1000))
        self.screen.blit(self.Soumet,(1470,1000))
        self.screen.blit(self.traine,(1650,1000))
        


    def main(self):
#______________________________________________________________________________________________________________________
        while self.running:

            self.screen.fill((0,0,0))
            self.clock.tick(60)
            keys = pygame.key.get_pressed()
#____________________________________________________________________________________________________________________
            for event in pygame.event.get():
                

                if event.type == pygame.QUIT:
                    self.running=False
                    pygame.quit()
                if keys[pygame.K_ESCAPE]:
                    self.running=False
                    pygame.quit()
#______________________________________________________________________________________________________________________
            if not self.menu:
                #retour au menu
                #pour donner lillusion de se deplacer sur lecran
                if keys[pygame.K_z]:
                    self.moveAllH()
                if keys[pygame.K_q]:
                    self.moveAllG()
                if keys[pygame.K_s]:
                    self.moveAllB()
                if keys[pygame.K_d]:
                    self.moveAllD()

                #revenir au menu
                if keys[pygame.K_SPACE]:
                    self.menu=not self.menu
                    self.deleteAll()
                    pygame.time.wait(200)
                #applique les forces
                
                for j in range(len(self.joueurs)):
                    for i in range (len(self.attracteurs)):
                        if self.joueurs[j]!=self.attracteurs[i]:
                            mP.appliqueForceXY(self.joueurs[j],self.attracteurs[i])
                #dessine les objets

                for i in range(len(self.liste_obj)):
                    pygame.draw.circle(self.screen, self.liste_obj[i].couleur, (int(self.liste_obj[i].x),int(self.liste_obj[i].y)), self.liste_obj[i].largueur)

                #applique et affiche les traines
                mP.test_liste_traine(self.liste_obj)

                for i in range(len(self.liste_obj)):
                    if self.liste_obj[i].traine[0]>0:
                        for j in range(1,len(self.liste_obj[i].traine)-1):
                            pygame.draw.line(self.screen, (250,250,250), self.liste_obj[i].traine[j], self.liste_obj[i].traine[j+1], 2)
                
                for i in range(len(self.liste_obj)):
                    mP.appliqueVec(self.liste_obj[i])
#____________________________________________________________________________________phase de settings
            
            else:#si le bouton placer objet a été cliqué on enleve le menu pour placer l'objet
                if not self.menu_sandbox.boutonClicked:
                    self.actualise_texte()
                    #affiche le cercle de reference
                    pygame.draw.circle(self.screen, self.menu_sandbox.get_couleur(), (1000,500), self.menu_sandbox.get_tailleValue())

                    #affiche les autres objets
                    for i in range(len(self.liste_obj)):
                        pygame.draw.circle(self.screen, self.liste_obj[i].couleur , (int(self.liste_obj[i].x),int(self.liste_obj[i].y)), self.liste_obj[i].largueur)

                    self.affiche_menu_sandbox()

                    checkbox1 = pygame.draw.rect(self.screen, (0,0,0) ,(1353,928,44,44))
                    checkbox2 = pygame.draw.rect(self.screen, (0,0,0) ,(1503,928,44,44))

                    
                    #bouton1
                    ajouter_un_objet=pygame.draw.rect(self.screen, self.menu_sandbox.couleur_bouton, (150,900,300,100))
                    #hover du bouton
                    if ajouter_un_objet.collidepoint(pygame.mouse.get_pos()):
                        self.menu_sandbox.change_couleur(True)
                    else:
                        self.menu_sandbox.change_couleur(False)


                    #bouton2
                    lancer=pygame.draw.rect(self.screen, self.menu_sandbox.couleur_bouton2, (840,50,300,100))
                    #hover du bouTon2
                    if lancer.collidepoint(pygame.mouse.get_pos()):
                        self.menu_sandbox.change_couleur2(True)
                    else:
                        self.menu_sandbox.change_couleur2(False)

                    #barre genre potentiometre jsp
                    if pygame.mouse.get_pressed()==(1 ,0, 0):#si on clique

                        x,y=pygame.mouse.get_pos()

                        # si on clique dans la zone des potentiomaitre donne au curseur la position de la souris
                        if x<self.menu_sandbox.curseur1Max and x>self.menu_sandbox.curseur1Min and y>self.menu_sandbox.yMin and y<self.menu_sandbox.yMax:
                            self.menu_sandbox.set_curseur1Pos(x)
                        if x<self.menu_sandbox.curseur2Max and x>self.menu_sandbox.curseur2Min and y>self.menu_sandbox.yMin and y<self.menu_sandbox.yMax:
                            self.menu_sandbox.set_curseur2Pos(x)
                        if x<self.menu_sandbox.curseur3Max and x>self.menu_sandbox.curseur3Min and y>self.menu_sandbox.yMin and y<self.menu_sandbox.yMax:
                            self.menu_sandbox.set_curseur3Pos(x)

                        #si on clique dans une check box inverse la valeur du booleen correspondant a cette derniere
                        if checkbox1.collidepoint(pygame.mouse.get_pos()):
                            
                            self.menu_sandbox.inverse_checkbox1()
                            pygame.time.wait(200)

                        if checkbox2.collidepoint(pygame.mouse.get_pos()):
                        
                            self.menu_sandbox.inverse_checkbox2()
                            pygame.time.wait(200)
    #______________________________________________________________________si on clique sur placer l'objet on applique les settings
                        if ajouter_un_objet.collidepoint(pygame.mouse.get_pos()):
                            #on créé l'objet
                            self.liste_obj+=[Player.objet()]
                            #l'objet est mit dans les listes correspondantes
                            if self.menu_sandbox.checkbox1:
                                self.joueurs+=[self.liste_obj[len(self.liste_obj)-1]]
                            if self.menu_sandbox.checkbox2:
                                self.attracteurs+=[self.liste_obj[len(self.liste_obj)-1]]

                            #on set l'objet avec les valeurs des potentiometres
                            #set la masse
                            self.liste_obj[len(self.liste_obj)-1].set_masse(self.menu_sandbox.get_masseValue())
                            #set la masse
                            self.liste_obj[len(self.liste_obj)-1].set_largueur(self.menu_sandbox.get_tailleValue())
                            #set la traine
                            self.liste_obj[len(self.liste_obj)-1].set_taille_traine(self.menu_sandbox.get_traineValue())
                            #set la couleur
                            self.liste_obj[len(self.liste_obj)-1].set_couleur(self.menu_sandbox.get_couleur())

                            #on inverse le clicked
                            self.menu_sandbox.inverse_clicked()
                            
                            pygame.time.wait(200)
#__________________________________________________________________________________________________________on lance la simy
                        if lancer.collidepoint(pygame.mouse.get_pos()):
                            self.menu=not self.menu

                            pygame.time.wait(200)
#__________________________________________________________________________________________________________________
                    #met une croix si les check box sont"coché"
                    if self.menu_sandbox.checkbox1:
                        pygame.draw.line(self.screen, (250,250,250),(1353,928) ,(1397, 971),4)
                        pygame.draw.line(self.screen, (250,250,250),(1397,928) , (1353, 971),4)
                    if self.menu_sandbox.checkbox2:
                        pygame.draw.line(self.screen, (250,250,250),(1500,925) ,(1550, 975),4)
                        pygame.draw.line(self.screen, (250,250,250),(1550,925) , (1500, 975),4)

                    self.screen.blit(self.PlacerObjet,(170,925))
                    self.screen.blit(self.lancer,(845,45))

#________________________________________________________________________________________________________________
                else:#phase ou on place l'objet dans la fenetre
                    if not self.menu_sandbox.ClickedForPos:
                        #affiche les autres objets
                        for i in range(len(self.liste_obj)-1):
                            pygame.draw.circle(self.screen, self.liste_obj[i].couleur , (int(self.liste_obj[i].x),int(self.liste_obj[i].y)), self.liste_obj[i].largueur)

                        #on recupere les coo de la souris
                        x,y=pygame.mouse.get_pos()
                        #on affiche le cercle a placer positionné sur la souris
                        pygame.draw.circle(self.screen, self.liste_obj[(len(self.liste_obj)-1)].couleur , (x,y), self.liste_obj[(len(self.liste_obj)-1)].largueur)

                        if pygame.mouse.get_pressed()==(1 ,0, 0):#si on clique
                            self.liste_obj[(len(self.liste_obj)-1)].set_pos(x,y)#on lui donne la position de la ou on a cliqué

                            self.menu_sandbox.inverse_clickedForPos()#on inverse la valeur du bool
                            pygame.time.wait(200)
                    else:#une fois cliqué on à la position reste plus qu'a set le vecteur de l'objet
                         #affiche les autres objets
                        for i in range(len(self.liste_obj)):
                            pygame.draw.circle(self.screen, self.liste_obj[i].couleur , (int(self.liste_obj[i].x),int(self.liste_obj[i].y)), self.liste_obj[i].largueur)

                         #on recupere les coo de la souris
                        x,y=pygame.mouse.get_pos()
                        #on dessine une ligne representant le vecteur
                        pygame.draw.line(self.screen, (250,250,250),(self.liste_obj[(len(self.liste_obj)-1)].x,self.liste_obj[(len(self.liste_obj)-1)].y) ,(x, y),10)
                        if pygame.mouse.get_pressed()==(1 ,0, 0):#si on clique
                            #on set alors le vecteur
                            vecX,vecY = mP.getVecXY(self.liste_obj[(len(self.liste_obj)-1)].x,self.liste_obj[(len(self.liste_obj)-1)].y,x,y)
                            self.liste_obj[(len(self.liste_obj)-1)].set_Vec(vecX,vecY)
                            #on reinverse le clique pour revenir au menu
                            self.menu_sandbox.inverse_clicked()
                            self.menu_sandbox.inverse_clickedForPos()#on inverse la valeur du bool


#_______________________________________________________________________________________________________

            pygame.display.flip()
Main()

