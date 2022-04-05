
class TK:
    def __init__(self,stk, sd):
        self.stk = stk
        self.sd = sd
    def getSTK(self):
        return self.stk
    def getSD(self):
        return self.sd
    
class QLTK:
    listTK = []
    def getTK(self):
        return self.listTK
    def SoLuongTK(self):
        return self.listTK.__len__()
    
    def GuiTien(self,stk):
        Tien = float(input('Nhap so tien muon gui: ')) 
        if self.SoLuongTK() > 0:    
            for i in self.getTK():
                if i.stk == stk  and  Tien >= 0:                            
                    i.sd = i.sd + Tien 
                    print('Ban vua nap:',Tien,'d')
                    print('So du hien tai cua ban: ',i.sd,'d')
                else:
                    print('Khong hop le')
        
    def RutTien(self, Tien,stk):
        if self.SoLuongTK(QLTK) > 0:
            for i in self.getTK(QLTK):
                if i.stk == stk:
                    if Tien >= 0 and Tien < i.sd:           
                        i.sd = i.sd - Tien 
                        print('Ban vua rut: ', Tien, 'd, o stk: ',i.stk)
                        print('So tien hien tai cua ban: ', i.sd,'d')
                    else:
                        print('Khong hop le')
        
                    
    def NhapTK(self):
        stk = input('Nhap so tai khoan: ')
        sd = float(input('Nhap so du: '))
        TaiKhoan = TK(stk,sd)
        self.listTK.append(TaiKhoan)
        return TaiKhoan
    
    
        
class TKTK(QLTK):
    listTKTK = []
    def getlistTKTK(self):
        return self.listTKTK
    
    def NhapTK(self):        
        tk = super().NhapTK(TKTK)
        self.listTKTK.append(tk)
        return tk
        
    def LaiSuat(self):
        return self.sd * 8/100

    def KtrSd(self,stk):    
        for i in self.listTKTK:            
            if stk == i.stk:
                print('TKTK: So tai khoan: ',i.stk,' co so du: ',i.sd,' voi lai suat 8% nam:', i.sd*8/100)
    def RutTien(self, Tien,stk):
        super().RutTien(TKTK,Tien,stk)
        
    
class TKVL(QLTK):
    listTKVL = []
    def getlistTKVL(self):
        return self.listTKVL
    
    def NhapTK(self):        
        tk = super().NhapTK(TKVL)
        self.listTKVL.append(tk)
        return tk 
    
    def KtrSd(self,stk):    
        for i in self.listTKVL:            
            if stk == i.stk:
                print('TKVL: So tai khoan: ',i.stk,' co so du: ',i.sd)
    
    def timkiemTenKH(self,key):
        kh = None
        if self.soluongKH() > 0:
            for i in self.getlistKH():
                if i.tenKH == key:
                    kh = i
        return kh
    
                
    def RutTien(self,Tien,stk):

        super().RutTien(TKVL,Tien,stk)
        