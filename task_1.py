str = '1h 45m,360s,25m,30m 120s,2h 60s' 

lst = str.split(',')

total_minutes = 0

for times in lst:
    time = times.split(' ')
    for i in time: 
            if 'h' in i:
                total_minutes += int((i.replace('h', '')))*60
            elif 'm' in i:
               total_minutes += int(i.replace('m', ''))
            elif 's' in i:
                seconds = int(i.replace('s', ''))
                if seconds % 60 != 0:
                    print(f"Ошибка: количество секунд {seconds} не кратно 60")
                total_minutes += seconds // 60
       
print(f"Общее количество минут: {int(total_minutes)}")
