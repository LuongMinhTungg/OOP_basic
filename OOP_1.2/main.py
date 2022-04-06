from banHang import banHang
from sp import QLSP
from kh import QLKH
import datetime
check = True
QLSP = QLSP()
QLKH = QLKH()
BH = banHang()
while check:
    try:
        print('---')
        print('1 - nhap san pham')
        print('2 - hien thi ds sp')
        print('3 - nhap khach hang')
        print('4 - xuat thong tin kh')
        print('5 - mua san pham')
        print('6 - xem hoa don')
        print('7 - danh san pham da ban')
        print('---')
        key = int(input('Nhap tuy chon: '))
    except ValueError:
        check = True
    else:
        if key == 1:       
            QLSP.nhapSP()
        if key == 2:
            QLSP.xuatSP(QLSP.getlistSP())
        if key == 3: 
            QLKH.nhapKH()
        if key == 4: 
            QLKH.xuatKH(QLKH.getlistKH())
        if key == 5:
            kh = input('Nhap ma KH: ')
            sp = input('Nhap ten sp muon mua hang: ')
            BH.banHang(kh,sp)
        if key == 6: 
            kh = input('Nhap ten kh muon xem hoa don: ')
            BH.baocaoMuaHang(kh)
        if key == 7:
            BH.sapXep()
            BH.daBan()
        if key == 100:
            check = False
    
        


