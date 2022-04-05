
class tk:
    def __init__(self, tenTK, soTK, soDu):
        self.tenTK = tenTK
        self.soTK = soTK
        self.soDu = soDu
    def gettenTK(self):
        return self.tenTK
    def getsoTK(self):
        return self.soTK
    def getsoDu(self):
        return self.soDu
    
    def phiDV(self, dv):
        return dv * 1/100
 
    def napTien(self):
        a = float(input('Nhap so tien muon nap: '))       
        if(a >= 0):           
            phiDV = self.phiDV(a)
            if phiDV > 1000:
                phiDV = phiDV
            else:
                phiDV = 1000
            self.soDu = self.soDu + a - phiDV
            print('Ban vua nap:',a,'d')
            print('phi DV nap tien la: ', phiDV, 'd')
            print('So du hien tai cua ban(da tru phi DV): ',self.soDu,'d')
        else:
            print('Khong hop le')
        return a
    
    def rutTien(self):
        a = float(input('Nhap so tien muon rut: '))
        if a >= 0 and a < self.getsoDu():
            phiDV = self.phiDV(a)
            if phiDV > 1000:
                phiDV = phiDV
            else:
                phiDV = 1000
            self.soDu = self.soDu - a - phiDV
            print('Ban vua rut: ', a, 'd')
            print('Phi DV rut tien la: ', phiDV,'d')
            print('So tien hien tai cua ban(da tru phi DV): ', self.soDu,'d')
        else:
            print('Khong hop le')
        return a
    
    def show(self):
        print('Ten tk:',tk.gettenTK(),'Ma TK:',tk.getsoTK(),'So Du:',tk.getsoDu())

a = 'tung'
b = '1'
c = 50000
tk = tk(a,b,c)

check = True
while check:
    try:
        print('---')
        print('1-nap tien')
        print('2-rut tien')
        print('3-show')
        print('---')
        k = int(input('Nhap k: '))
    except ValueError:
        check = True
    else:
        if k == 1:
            tk.napTien()
            
        if k == 2:
            tk.rutTien()
        if k == 3:
           tk.show() 




    
