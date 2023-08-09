# code qui génère les images
import numpy as np
import matplotlib.pyplot as plt


nl = 1080  # nombre de lignes, nombre de colonnes
nc = 1920


# Points_gravité = [] # Liste des points de gravité


class Tige:
    def __init__(self, base):
        self.base = base

    def élongation_mobile(self, PtGravi):  # Calcule l'élongation du mobile
        long_a_vide = 50
        x1, y1 = self.base
        x2, y2 = PtGravi.coord
        # distance entre le point de gravité et la base de la tige
        d = np.sqrt((x1-x2)**2+(y1-y2)**2)
        # to be continued

    def coord_mobile(self, PtGravi):  # calcul des coordonnées du mobile
        l = 50  # longeur à vide du mobile
        x1, y1 = self.base
        x2, y2 = PtGravi.coord
        dx = x2 - x1
        dy = y2 - y1
        # Calcule l'angle de rotation du mobile
        if dx == 0:
            if dy > 0:
                Γ = np.pi/2
            if dy < 0:
                delta0 = np.pi
                Γ = np.pi/2 + delta0
        if dx > 0:
            # angle dans le triangle formé par la base et le ptgravi
            a = np.arctan(dy/dx)
            delta0 = np.pi/2 - a  # caclul de l'angle a ajouter pour s'aligner avec le ptgravi
            Γ = np.pi/2 - delta0  # angle sur le cercle de rayon l centré sur la base
        if dx < 0:
            a = np.arctan(dy/dx)
            delta0 = np.pi/2 + a
            Γ = np.pi/2 + delta0
        xm = l*np.cos(Γ)
        ym = l*np.sin(Γ)
        return (x1+xm, y1+ym)

    def afficher(self):  # Affiche la tige
        xmob, ymob = self.coord_mobile(gravi)
        plt.plot([self.base[0], xmob], [self.base[1], ymob], 'r', linewidth=3)


class PtGravité:  # Classe des points de gravité
    def __init__(self, coord, gravi):
        self.coord = coord
        self.gravi = gravi

    def afficher(self):
        plt.scatter(self.coord[0], self.coord[1], c='w', s=5)

    def tracer_trajectoire(self):
        pass


for i in range(20):
    Image = np.zeros((nl, nc, 3), dtype='uint8')
    fig, ax = plt.subplots()
    Image = ax.imshow(Image, extent=[0, 1920, 0, 1080])
    gravi = PtGravité((i*100, 540), 1)
    gravi.afficher()
    for j in range(20):
        tige = Tige([j*100, 100])
        tige.afficher()
    plt.savefig('dossier_video/'+str(i)+'.png', dpi=100)
    # plt.show()
