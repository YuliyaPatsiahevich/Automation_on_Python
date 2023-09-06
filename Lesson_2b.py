dict_banks={
    'SBER': 3.2,
    'VTB': 2.4,
    'ALFA': 4.92,
    'PRIOR': 3.0}
int_money=int(input ('Money='))
sum=[int_money*dict_banks['SBER']/100,
          int_money*dict_banks['VTB']/100,
          int_money*dict_banks['ALFA']/100,
          int_money*dict_banks['PRIOR']/100]
print('Sum=',sum)