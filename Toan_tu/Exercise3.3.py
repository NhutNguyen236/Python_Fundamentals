tien = int(input("Nhập số tiền muốn đổi: "))
original_tien = tien

def doi_tien(tien):
    t500 = tien // 500000
    tien = tien - 500000 * t500
    
    t200 = tien // 200000
    tien = tien - 200000 * t200
    
    t100 = tien // 100000
    tien = tien - 100000 * t100
    
    t50 = tien // 50000
    tien = tien - 50000 * t50
    
    print("Số tờ mệnh giá 500000: ", t500)
    print("Số tờ mệnh giá 200000: ", t200)
    print("Số tờ mệnh giá 100000: ", t100)
    print("Số tờ mệnh giá 50000: ", t50)
    print("Số tiền còn dư: {:,}".format(original_tien - (t500*500000 + t200*200000 + t100*100000 + t50*50000)))
doi_tien(tien)