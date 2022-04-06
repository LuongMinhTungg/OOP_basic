import string
import random
class KH: 
    def __init__(self, maKH,tenKH,sdt ):
        self.maKH = maKH
        self.tenKH = tenKH
        self.sdt = sdt

class QLKH:
    listKH = []
    def soluongKH(self):
        return self.listKH.__len__()
    
    def ID(self):
        size = 6
        char = string.ascii_uppercase + string.digits
        return ''.join(random.choice(char) for _ in range(size))
    
    def nhapKH(self):
        c = True
        while c:
            maKH = self.ID()
            for i in self.listKH:
                if maKH == i.maKH:
                    c = True
            c = False
        tenKH = input('Nhap ten KH: ')
        sdt = input('Nhap sdt: ')
        kh = KH(maKH, tenKH, sdt)
        self.listKH.append(kh)
    
    def xuatKH(self,list): 
        f = open('DSKH.txt','w+')
        print('{:<18} {:<18} {:<12}'.format('MaKH', 'TenKH', 'sdt'))
        f.write(('{:<18} {:<18} {:<12} \n'.format('MaKH', 'TenKH', 'sdt')))
        for i in list:
            if list.__len__() > 0:
                print('{:<18} {:<18} {:<12}'.format(i.maKH, i.tenKH, i.sdt))
                f.write('{:<18} {:<18} {:<12}'.format(i.maKH, i.tenKH, i.sdt))
        f.close()
            
    def getlistKH(self):
        return self.listKH
    
    
    
    def timkiemTenKH(self,key):
        kh = None
        if self.soluongKH(QLKH) > 0:
            for i in self.getlistKH(QLKH):
                if i.tenKH.upper() == key.upper():
                    kh = i
        else:
            print('chua co kh')
        return kh
        