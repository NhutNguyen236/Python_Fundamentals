def doc_tap_tin(duong_dan):
    f = open(duong_dan, 'r')
    noi_dung = f.read()
    f.close()
    return noi_dung


def thong_ke(noi_dung):
    ds_dong = noi_dung.split('\n')
    so_dong = len(ds_dong)
    ds_tu = ' '.join(ds_dong).replace(', ', ' ').replace('. ', ' ').split()
    so_tu = len(ds_tu)
    ds_ky_tu = ''.join(noi_dung)
    so_ky_tu = len(ds_ky_tu)
    return so_dong, so_tu, so_ky_tu


def ghi_de_1_dong(duong_dan, noi_dung):
    f = open(duong_dan, 'w', encoding='utf-8')
    f.write(noi_dung)
    f.close()
    return True


def ghi_tiep_theo_1_dong(duong_dan, noi_dung):
    f = open(duong_dan, 'a', encoding='utf-8')
    f.write(noi_dung)
    f.close()
    return True


def ghi_nhieu_dong(duong_dan, danh_sach_dong):
    f = open(duong_dan, 'w', encoding='utf-8')
    f.writelines(danh_sach_dong)
    f.close()
    return True
