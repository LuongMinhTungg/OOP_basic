from tk import QLTK,TKTK,TKVL
class KH:
    def __init__(self,tenKH, tk, tongsoTK):
        self.tenKH = tenKH
        self.tk = tk
        self.tongsoTK = tongsoTK
    
class QLKH:
    listKH = []
    QLTK = QLTK()
    TKTK = TKTK()
    TKVL = TKVL()
    def SoluongKH(self):
        return self.listKH.__len__()
    
    def tongsoTK(self,tenKH):
        tongsoTK = 1
        if self.SoluongKH() > 0:
            for i in self.listKH:
                if i.tenKH == tenKH:
                    tongsoTK = tongsoTK + 1
        return tongsoTK
    
    def getlistKH(self):
        return self.listKH
    
    def ThemTK(self):
        count = 0
        check = True
        while check:
            c = True
            TenKH = input('TenKH: ')
            for i in self.getlistKH():
                if TenKH == i.tenKH:
                    count = count+1
            if count >=9:
                print('Ban ko the them tai khoan nua')
                break
            
            while c:
                loaiTK = input('nhap loai tk: ')
                if loaiTK.upper() == 'TKTK':
                    TaiKhoan = TKTK.NhapTK(TKTK)
                    c = False
                if loaiTK.upper() == 'TKVL':
                    TaiKhoan = TKVL.NhapTK(TKVL)
                    c = False
            
            tongsoTK = self.tongsoTK(TenKH)
            
            kh = KH(TenKH, TaiKhoan, tongsoTK)
            self.listKH.append(kh)
            check = False
    '''      
    def KtrSd(self,kh):    
        for i in self.listKH:
            if kh == i.tenKH:
                print('So tai khoan: ',i.tk.stk,' co so du: ',i.tk.sd)
    '''
    
                
    def KtraTKVL(self,tenKH,stk):
        c = False
        for i in self.getlistKH():
            if i.tenKH == tenKH:
                for i in TKVL.getlistTKVL(TKVL):
                    if i.stk == stk:
                        c = True    
                               
        return c      
    def KtraTKTK(self,tenKH,stk):
        c = False 
        for i in self.getlistKH():
            if i.tenKH == tenKH and i.tk.stk == stk:
                for i in TKTK.getlistTKTK(TKTK):                  
                    if i.stk == stk:
                        c = True  
                         
        return c   
     
    def KtraLK(self,tenKH, stk):
        c = False
        for i in self.getlistKH():
               if i.tenKH == tenKH and self.KtraTKVL(tenKH, stk) == True: 
                   for i in TKTK.getlistTKTK(TKTK):
                       if self.KtraTKTK(tenKH,i.stk) == True:
                           c = True
        return c
    
    def TongSODuTKTK(self,tenKH):
        tong = 0
        for i in self.listKH:
            if i.tenKH == tenKH:
                if self.KtraTKTK(tenKH,i.tk.stk) == True:
                    tong = tong + i.tk.sd
        return tong
    
    def LayTK(self,tenKH):
        if self.SoluongKH() > 0:
            print('Ten Khach Hang: ', tenKH)
            if QLTK.SoLuongTK(QLTK) > 0:
                for i in self.listKH:
                    if i.tenKH == tenKH:                    
                        TKTK.KtrSd(TKTK,i.tk.stk)
                        TKVL.KtrSd(TKVL,i.tk.stk)
                        #self.KtrSd(tenKH)
                print('Khach hang co tat ca ',i.tongsoTK,' tk')
                print('Tong So Du trong tat ca tk tiet kiem: ', self.TongSODuTKTK(tenKH))
                                  
    def RutTienTKVL(self,tenKH,Tien,stkvl,stktk):
        TIenChuyen = 0
        for i in self.listKH:
            if i.tenKH == tenKH and i.tk.stk == stkvl:
                if self.KtraLK(tenKH,stkvl) == True:
                    for i in TKTK.getlistTKTK(TKTK):
                        if i.stk == stktk:
                            print('So tien o tk khong du can chuyen them tu tktk')
                            TienChuyen = float(input('Nhap so tien can chuyen: '))
                            i.sd = i.sd - TienChuyen
                    for i in TKVL.getlistTKVL(TKVL):
                        if i.stk == stkvl:
                            i.sd = i.sd + TienChuyen
                            TKVL.RutTien(TKVL,Tien,stkvl)
                else:
                    print('Khong tim thay tk lien ket')
                
    def RutTien(self,tenKH,stk):
        if self.SoluongKH() > 0:
            Tien = float(input('Nhap so tien muon rut: '))
            for i in self.listKH:
                if i.tenKH == tenKH and i.tk.stk == stk:
                    if self.KtraTKTK(tenKH,stk) == True and self.KtraTKVL(tenKH,stk) == False:
                        TKTK.RutTien(TKTK,Tien,stk)                                          
                        break
                    if self.KtraTKTK(tenKH,stk) == False and self.KtraTKVL(tenKH,stk) == True:                   
                        if Tien <= i.tk.sd:
                            TKVL.RutTien(TKVL,Tien,stk)                            
                            break
                        else:
                            print('So tien rut lon hon hien co can phai su dung tktk')
                            stktk = input('Nhap stk tiet kiem lien ket:')
                            print('Chuyen tien tu tktk sang tkvl')
                            self.RutTienTKVL(tenKH,Tien,stk,stktk)                           
                            break          
            
        else:
            print('Chua co tai khoan trong he thong')
                  