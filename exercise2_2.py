# Cau 1: 

r = 5
volume = (4/3) * 3.14 * r**3
print("Cau 1:", volume)

# Cau 2: 

cover_price = 24.95
discount_price = cover_price * 0.6
shipping = 3 + 59 * 0.75
total_cost = 60 * discount_price + shipping
print("Cau 2:", total_cost)

# Cau 3: 

start_hour = 6
start_minute = 52

easy_pace = 8*60 + 15
tempo = 7*60 + 12

total_run = easy_pace + 3*tempo + easy_pace

finish_time = start_hour*3600 + start_minute*60 + total_run

hour = finish_time // 3600
minute = (finish_time % 3600) // 60
second = finish_time % 60

print("Cau 3:", hour, ":", minute, ":", second)