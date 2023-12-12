# требуемая длительность свободного окна, минуты
FREE_WINDOW_TIME = 30

# время начала рабочего дня
WORK_START = '09:00'

# время окончания рабочего дня
WORK_END = '21:00'

# инициализация списка свободных окон
free = []

# занятое время на приемы, обед, уборку кабинета
BUSY = [
    {
        'start': '10:30',
        'stop': '10:50'
    },
    {
        'start': '18:40',
        'stop': '18:50'
    },
    {
        'start': '14:40',
        'stop': '15:50'
    },
    {
        'start': '16:40',
        'stop': '17:20'
    },
    {
        'start': '20:05',
        'stop': '20:20'
    }
]

# сортировка исходного списка словарей по ключу начала интервала в порядке возрастания значений
sorted_busy = sorted(BUSY, key=lambda x: x['start'])

# свободное время до начала приемов
TIME_BEFORE_APPOINTMENTS = [
    {
        'start': WORK_START,
        'stop': sorted_busy[0]['start']
    },
]

# свободное время по окончании приемов
TIME_AFTER_APPOINTMENTS = [
    {
        'start': sorted_busy[-1]['stop'],
        'stop': WORK_END
    },
]
