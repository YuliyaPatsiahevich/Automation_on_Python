dict_banks={
    'SBER': 3.2,
    'VTB': 2.4,
    'ALFA': 4.92,
    'PRIOR': 3.0}
int_money=int(input ('Money='))
float_SBER=float(3.2)
float_VTB=float(2.4)
float_ALFA=float(4.92)
float_PRIOR=float(3.0)
sum=[int_money*float_SBER/100,
          int_money*float_VTB/100,
          int_money*float_ALFA/100,
          int_money*float_PRIOR/100]
print('Sum=',sum)