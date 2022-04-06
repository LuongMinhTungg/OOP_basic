from mailbox import NotEmptyError
from sp import QLSP
from kh import QLKH
import datetime
class HD:
    def __init__(self, tenKH, tenSP, gia, tg):
        self.tenKH = tenKH
        self.tenSP = tenSP
        self.gia = gia
        self.tg = tg
class banHang:
    listHD = []
    QLSP = QLSP()
    QLKH = QLKH()
    list = []
    km = 0
    '''
    def banHang(self,kh,sp):
        s = None
        if QLKH.soluongKH(QLKH) > 0:
            for j in QLKH.getlistKH(QLKH):
                if kh.upper == j.tenKH.upper:       
                    if QLSP.soluongSP(QLSP) > 0:
                        for i in QLSP.getlistSP(QLSP):
                            if i.tenSP == sp:
                                s = i               
                                if s != None:
                                    QLSP.getlistSP(QLSP).remove(s)
                                    self.list.append(s)
                                    self.km = self.km + 1
                                    if self.km <= 5:
                                        tg = datetime.datetime.now()                              
                                        hd = HD(kh,sp,i.gia/2,tg)
                                        self.listHD.append(hd)
                                    else:
                                        tg = datetime.datetime.now()
                                        hd = HD(kh,sp,i.gia,tg)
                                        self.listHD.append(hd)
                            else:
                                print('Khong tim thay san pham')
                    else:
                        print('Kho rong')
                else:
                    print('Khong co khach hang tuong ung')
        else:
            print('chua co khach hang')
    '''
    def khuyenmai(self,tenKH,sp,km):
        km = self.km
        if sp!= None:
            QLSP.getlistSP(QLSP).remove(sp)
            self.list.append(sp)
            self.km = self.km + 1
            if self.km <= 5:
                tg = datetime.datetime.now()                              
                hd = HD(tenKH,sp.tenSP,sp.gia/2,tg)
                self.listHD.append(hd)
            else:
                tg = datetime.datetime.now()
                hd = HD(tenKH,sp.tenSP,sp.gia,tg)
                self.listHD.append(hd)
    def banHang(self,tenKH,tenSP):
        sp = None
        try:
            if QLKH.timkiemTenKH(QLKH,tenKH).tenKH == tenKH.upper():
                if QLSP.timkiemSP(QLSP,tenSP).tenSP == tenSP:
                    sp = QLSP.timkiemSP(QLSP,tenSP)
                    self.khuyenmai(tenKH,sp,self.km)
        except AttributeError:
            print('chua co sp hoac khach hang')
        else:
            print('Mua hang thanh cong')
                
            
                        
    def getlistHD(self):
        return self.listHD
    
    def soluongHD(self):
        return self.listHD.__len__()
    
    def daBan(self):
        if self.soluongHD() > 0:
            print('Danh sach san pham da ban')
            print(' {:<18} {:<18} {:<8} {:<40}'.format('ten kh', 'ten sp', 'Gia', 'thoi gian mua'))
            for i in self.getlistHD():
                print(' {:<18} {:<18} {:<8} {:<40}'.format(i.tenKH, i.tenSP, i.gia, i.tg.strftime("%m/%d/%Y, %H:%M:%S")))
        else:
            print('chua co hoa don')
        
    def sapXep(self):
        self.getlistHD().sort(key = lambda i:(i.tenKH,i.tg), reverse=True)
        
    def baocaoMuaHang(self,kh):
        print(' {:<18} {:<18} {:<8} {:<40}'.format('ten kh', 'ten sp', 'Gia', 'thoi gian mua'))
        for i in self.getlistHD():
            if i.tenKH == kh:               
                print(' {:<18} {:<18} {:<8} {:<40}'.format(i.tenKH, i.tenSP, i.gia, i.tg.strftime("%m/%d/%Y, %H:%M:%S")))
                
            else:
                print('Khong tim thay khach hang tuong ung')
            
                