'''
Write a python program to input °C (Celsius)
temperature and convert to °F (Fahrenheit)
temperature.
Step by step:
1/ Input °C temperature (validate to get valid value)
2/ Calculate °F temperature via formula:
°F = ( °C × 1.8 ) + 32
3/ Display °F temperature
'''
do_c = int(input("Nhiệt độ (oC):"))
do_f = (do_c * 1.8) + 32
print(f"Độ F={do_f}")