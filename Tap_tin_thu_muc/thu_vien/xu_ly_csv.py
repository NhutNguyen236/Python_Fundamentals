import csv


def doc_tap_tin_csv(duong_dan, bo_dong_dau=False):
    du_lieu = []
    f = open(duong_dan, 'r', encoding='utf-8')
    csv_reader = csv.reader(f)
    if bo_dong_dau:
        next(csv_reader)
    for dong in csv_reader:
        du_lieu.append(dong)
    f.close()
    return du_lieu


def ghi_tap_tin_csv(duong_dan, noi_dung):
    f = open(duong_dan, 'w', encoding='utf-8', newline='')
    for dong in noi_dung:
        csv.writer(f).writerow(dong)
    f.close()
    return True
