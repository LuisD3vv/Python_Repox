import Birthday_mesagges as bdm
from datetime import date

hoy = date.today()
next_birday = date(2026, 5, 5)

days_away = next_birday - hoy

if hoy == next_birday:
	print(bdm.actual_message)
else:
	print(f"My next birthday is {days_away.days} days away!")

# con .days nos muestra solo los días sin el timedelta
