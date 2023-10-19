def check_year(year):
    can_list = {0: "canh", 1: "Tân", 2: "Nhâm", 3: "Quý", 4: "Giáp", 
           5: "Ất", 6: "Bính", 7: "Đinh", 8: "Mậu", 9: "Kỷ"}
    
    chi_list = {0: "thân", 1: "dậu", 2: "tuất", 3: "hợi", 4: "tý", 
           5: 'sửu', 6: 'dần', 7: 'mão', 8: 'thìn', 9: 'tỵ',
           10: 'ngọ', 11: 'mùi'}
    
    # calculate can 
    can = can_list[year % 10]
    
    #calculate chi
    chi = chi_list[year % 12]
    
    # combine can_chi
    can_chi = can + " " + chi

    return can_chi

year = input("Nhập năm: ")
print(f"Năm {year} âm lịch là năm {check_year(2022)}")