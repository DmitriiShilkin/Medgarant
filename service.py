from typing import List, Dict

from config import FREE_WINDOW_TIME, free


# переводит время из количества минут в формат часы:минуты
def time_to_str(minutes: int, delta: int) -> str:
    hrs = minutes // 60
    mins = minutes % 60

    if (mins + delta) < 60:
        mins += delta

    elif (mins + delta) >= 60:
        hrs += (mins + delta) // 60
        mins = (mins + delta) % 60

    return f'{hrs:02}:{mins:02}'


# переводит время из формата часы:минуты в количество минут
def time_to_int(time: str) -> int:
    hrs, mins = time.split(':')
    return int(hrs) * 60 + int(mins)


# ищет свободные окна в заданном промежутке времени
def free_window_search(start: str, prev_stop: str) -> List[Dict]:
    start_min = time_to_int(start)
    prev_stop_min = time_to_int(prev_stop)
    delta = start_min - prev_stop_min

    if delta >= FREE_WINDOW_TIME:
        td = FREE_WINDOW_TIME
        start = prev_stop

        while td <= delta:
            stop = time_to_str(prev_stop_min, td)
            free.append({'start': start, 'stop': stop})
            start = stop
            td += FREE_WINDOW_TIME

    return free
