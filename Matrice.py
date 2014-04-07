class Matrice:
    
    def __init__(this,matrice):
        this.matrice = []
        this.altezza = 0
        this.larghezza = 0
        this.setMatrice(matrice)
        
    def setMatrice(this, matrice):       
        this.altezza = len(matrice)
        this.larghezza = len(matrice[0])
        for i in matrice:
            if len(i) != this.larghezza:
                this.altezza = 0
                this.larghezza = 0
                raise Exception("numero colonne eterogeneo")
        this.matrice = matrice
        this.altezza = len(matrice)
        this.larghezza = len(matrice[0])

    def __add__(this, matrice):
        #se l'argomento è 0 (capita calcolando il determinante di una matrice di matrici)
        #allora:
        if matrice == 0:
            return this
        if this.larghezza != matrice.larghezza or this.altezza != matrice.altezza:
            raise Exception("ops le matrici non sono compatibili: \n"+ str(this) + str(matrice))
        retMat = []
        for i in range(0, this.altezza):
            tmp = []
            for j in range(0, this.larghezza):
                tmp.append(this.matrice[i][j] + matrice.matrice[i][j])
            retMat.append(tmp)
        return Matrice(retMat)
    
    def __mul__(this, matrice):
        retMat = []
        #se l'argomento non è una matrice (quindi in teoria un numero)
        #eseguo cella a cella la moltiplicazione.
        if not isinstance(matrice, Matrice):
            for i in range(0, this.altezza):
                tmp = []
                for j in range(0, this.larghezza):
                    tmp.append(this.matrice[i][j]*matrice)
                retMat.append(tmp)
        else:
            if this.larghezza != matrice.altezza:
                raise Exception("ops le matrici non sono compatibili")
            for i in range(0, this.altezza):
                tmp = []
                for j in range(0, matrice.larghezza):
                    temp = 0
                    for k in range(0, this.larghezza):
                        temp = temp + this.matrice[i][k]*matrice.matrice[k][j]
                    tmp.append(temp)
                retMat.append(tmp)
        return Matrice(retMat)
    
    def __str__(this):
        tmp = ""
        for i in range(0, this.altezza):
            for j in range(0, this.larghezza):
                tmp = tmp + str(this.matrice[i][j]) + "\t"
            tmp = tmp + "\n"
        return tmp

    def complementa(this, riga, colonna):
        ret = []
        for i in range(0, this.larghezza):
            if i != riga:
                temp = []
                for j in range(0, this.altezza):
                    if j != colonna:
                        temp.append(this.matrice[i][j])
                ret.append(temp)
        return Matrice(ret)
    @property
    def determinante(this):
        if this.altezza != this.larghezza:
            raise Exception("ops, la matrice non è quadrata")
        if this.altezza == 1:
            return this.matrice[0][0]
        else:
            det = 0
            for i in range(0, this.larghezza):
                #attenzione: sarebbe -1^i+j, ma gli indici partono da 0 e j è zero.
                det = this.matrice[0][i] * this.complementa(0,i).determinante * pow(-1, i) + det
            return det
    @property
    def trasposta(this):
        ret = []
        for j in range(0,this.larghezza):
            tmp = []
            for i in range(0, this.altezza):
                tmp.append(this.matrice[i][j])
            ret.append(tmp)
        return Matrice(ret)

    def __getitem__(this, k):
        return this.matrice[k[0]][k[1]]
    
m1 = Matrice([[1,2],[3,4]])
m2 = Matrice([[Matrice([[1,0,0]]), Matrice([[0,1,0]]), Matrice([[0,0,1]])],[1,3,2],[3,4,4]])
print(m2.determinante)
#m = m1 + m2
