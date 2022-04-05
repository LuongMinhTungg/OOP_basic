from tkinter import Tk
from kh import QLKH
from tk import TKVL,TKTK,QLTK
KhachHang = QLKH()
TKVL = TKVL()
TKTK = TKTK()
QLTK = QLTK()
check = True
while check:
    try:
        print('---')
        print('1-nhap tai khoan')
        print('2-thong tin khach hang')
        print('3-nap tien')
        print('4-rut tien')
        print('---')
        k = int(input('Nhap k: '))
    except ValueError:
        check = True
    else:
        if k == 1:
            KhachHang.ThemTK()
            
        if k == 2:
            n = input('nhap ten kh: ')
            KhachHang.LayTK(n)
        if k == 3:
            stk = input('Nhap stk muon gui: ')
            QLTK.GuiTien(stk)
        if k == 4:
            TenKH = input('Nhap ten KH: ')
            stk = input('Nhap stk: ')
            KhachHang.RutTien(TenKH,stk)