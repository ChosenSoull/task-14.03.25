import random

class PhysicsExperiment:
    """
    Клас для проведення фізичних експериментів зі статистичним аналізом
    """
    
    def __init__(self, num_measurements=10):
        """
        Ініціалізація параметрів експерименту
        :param num_measurements: кількість вимірювань (за замовчуванням 10)
        """
        self.measurements = [
            round(random.uniform(9.0, 10.0), 2) 
            for _ in range(num_measurements)
        ]
        
    def calculate_stats(self):
        """
        Обчислення повного набору статистичних даних
        """
        return {
            'Середнє': round(sum(self.measurements)/len(self.measurements), 2),
            'Мінімум': min(self.measurements),
            'Максимум': max(self.measurements),
            'Сума': round(sum(self.measurements), 2),
            'Кількість': len(self.measurements)
        }
    
    def show_report(self):
        """
        Форматування звіту з результатами
        """
        stats = self.calculate_stats()
        
        print("Детальний звіт експерименту:")
        print("-" * 30)
        for i, val in enumerate(self.measurements, 1):
            print(f"Вимір #{i}: {val}")
        
        print("\nСтатистичні показники:")
        for key, value in stats.items():
            print(f"→ {key}: {value}")

if __name__ == "__main__":
    experiment = PhysicsExperiment()
    experiment.show_report()