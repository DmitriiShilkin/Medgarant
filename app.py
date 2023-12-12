from config import TIME_BEFORE_APPOINTMENTS, TIME_AFTER_APPOINTMENTS, FREE_WINDOW_TIME, sorted_busy, free
from service import free_window_search


# поиск свободных окон в интервале до начала приемов
free_window_search(TIME_BEFORE_APPOINTMENTS[0]['stop'], TIME_BEFORE_APPOINTMENTS[0]['start'])

prev_stop = sorted_busy[0]['stop']

# поиск свободных окон в интервалах между приемами, обедом и уборками
for d in sorted_busy[1:]:
    free_window_search(d['start'], prev_stop)
    prev_stop = d['stop']

# поиск свободных окон в интервале после окончания приемов
free_window_search(TIME_AFTER_APPOINTMENTS[0]['stop'], TIME_AFTER_APPOINTMENTS[0]['start'])

print()
print('Занятые часы')
for i in sorted_busy:
    print(i)

print()
print(f'Свободные окна по {FREE_WINDOW_TIME} минут')
for j in free:
    print(j)
