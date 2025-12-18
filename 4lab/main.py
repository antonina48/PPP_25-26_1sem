from abc import ABC, abstractmethod
class TimeInterval(ABC):
    def get_seconds(self) -> float:
        pass

    def to_human_readable(self) -> str:
        total_seconds = self.get_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = total_seconds % 60
        sec_formatted = f"{int(seconds)}" if seconds.is_integer() else f"{seconds:.2f}"
        return f"{hours} h {minutes} min {sec_formatted} s"

class HMSInterval(TimeInterval):
    def init(self, time_str):
        parts = time_str.split(':')
        self.hours, self.minutes, self.seconds = int(parts[0]), int(parts[1]), float(parts[2])
    def get_seconds(self): return self.hours * 3600 + self.minutes * 60 + self.seconds

class MSInterval(TimeInterval):
    def init(self, val): self.ms = float(val)
    def get_seconds(self): return self.ms / 1000

class MinSecInterval(TimeInterval):
    def init(self, m, s): self.m, self.s = int(m), float(s)
    def get_seconds(self): return self.m * 60 + self.s

class HoursInterval(TimeInterval):
    def init(self, val): self.h = float(val)
    def get_seconds(self): return self.h * 3600
def create_interval(line):
    parts = line.split()
    if not parts: return None
    
    kind = parts[0].lower()
    try:
        if kind == 'hms': return HMSInterval(parts[1])
        if kind == 'ms': return MSInterval(parts[1])
        if kind == 'minsec': return MinSecInterval(parts[1], parts[2])
        if kind == 'hours': return HoursInterval(parts[1])
    except (IndexError, ValueError):
        print(f"Ошибка: Неверный формат данных в строке '{line}'")
    return None

def run_console_app():
    print("=== Система учета временных интервалов ===")
    print("Введите интервалы по одному (например: 'hms 01:30:00' или 'hours 2.5').")
    print("Когда закончите, введите пустую строку или 'done'.\n")

    intervals = []
    while True:
        user_input = input("Добавить интервал: ").strip()
        if user_input.lower() in ['', 'done', 'готово', 'стоп']:
            break
        
        obj = create_interval(user_input)
        if obj:
            intervals.append(obj)
            print(f"Добавлено: {obj.to_human_readable()}")

    if not intervals:
        print("Список интервалов пуст. Выход.")
        return
    print("\nДоступные команды: sum, avg, max, min")
    while True:
        cmd = input("\nВведите команду (или 'exit' для выхода): ").strip().lower()
        
        if cmd == 'exit':
            break
            
        seconds_list = [i.get_seconds() for i in intervals]
        
        if cmd == 'sum':
            res = sum(seconds_list)
            label = "Сумма"
        elif cmd == 'avg':
            res = sum(seconds_list) / len(seconds_list)
            label = "Среднее"
        elif cmd == 'max':
            res = max(seconds_list)
            label = "Максимум"
        elif cmd == 'min':
            res = min(seconds_list)
            label = "Минимум"
        else:
            print("Неизвестная команда!")
            continue
        res_obj = HoursInterval(res / 3600) 
        print(f"--- Результат ---")
        print(f"{label}: {res_obj.to_human_readable()}")
        print(f"В секундах: {res:.2f} s")
        print(f"Формат чч:мм:сс: {int(res//3600):02}:{int((res%3600)//60):02}:{int(res%60):02}")

if name == "main":
    run_console_app()
