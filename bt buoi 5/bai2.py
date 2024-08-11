def dem_ky_tu(chuoi):
  dem = {}
  for ky_tu in chuoi:
    if ky_tu in dem:
      dem[ky_tu] += 1
    else:
      dem[ky_tu] = 1
  return dem

chuoi_nhap = input("Nhập chuỗi: ")

ket_qua = dem_ky_tu(chuoi_nhap)
print(ket_qua)
