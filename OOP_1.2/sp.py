class SP:
    def __init__(self, maSP, tenSP, thuongHieu, loaiSP, gia):
        self.maSP = maSP
        self.tenSP = tenSP
        self.thuongHieu = thuongHieu
        self.loaiSP = loaiSP
        self.gia = gia

        
class QLSP:
    listSP = []  
    
    def soluongSP(self):
        return self.listSP.__len__()
    
    def ID(self):
        maxID = 1
        if self.soluongSP() > 0:
            maxID = self.listSP[0].maSP
            for i in self.listSP:
                if(maxID < i.maSP):
                    maxID = i.maSP
            maxID = maxID + 1
        return maxID
        
    def nhapSP(self):
        maSp = self.ID()
        tenSP = input('Nhap ten SP: ')
        thuongHieu = input('Nhap ten thuong hieu: ')        
        c = True
        while c:    
            loaiSP = input('Nhap loai sp: ')                  
            if loaiSP.upper() == 'do dien'.upper() or loaiSP.upper() == 'do gia dung'.upper() :
                c = False            
        gia = float(input('gia: '))       
        if(gia > 0):
            s = SP(maSp, tenSP, thuongHieu, loaiSP, gia)
            self.listSP.append(s)
        else:
            print('Gia tien khong dc am')
    def getlistSP(self):
        return self.listSP
    
    def xuatSP(self,list):
        f = open('DSSP.txt','w+')
        print('{:<8} {:<18} {:<18} {:<12}{:<8}'.format('MaSP', 'TenSP', 'Thuong Hieu', 'LoaiSP', 'Gia'))
        f.write('{:<8} {:<18} {:<18} {:<12}{:<8} \n'.format('MaSP', 'TenSP', 'Thuong Hieu', 'LoaiSP', 'Gia'))
        if list.__len__() > 0:
            for i in list:
                print('{:<8} {:<18} {:<18} {:<12}{:<8} \n'.format(i.maSP, i.tenSP, i.thuongHieu, i.loaiSP, i.gia))
                f.write('{:<8} {:<18} {:<18} {:<12}{:<8}'.format(i.maSP, i.tenSP, i.thuongHieu, i.loaiSP, i.gia))
        else:
            print('chua co sp nao')      
                    
        f.close()
        
    def timkiemSP(self,key):
        sp = None
        if self.soluongSP(QLSP) > 0:
            for i in self.getlistSP(QLSP):
                if key == i.tenSP:
                    sp = i
        else:
            print('chua co sp')
        return sp
        
        
 
        
    
    