import random
import os
import time

class FaceAnimator:
    def __init__(self):
        # Словарь лиц для различных настроений
        self.faces = {
            "neutral": "(o_o)",
            "happy": "(^-^)",
            "sad": "(T-T)",
            "angry": "(>-<)",
            "surprised": "(O_O)",
            "wink": "(^_~)",
            "confused": "(ಠ_ಠ)",
            "bored": "(-_-)",
            "laughing": "(ʘ.ʘ)"
        }

    def clear_screen(self):
        """Очищает экран в зависимости от ОС."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def say(self, emotion=None, text=""):
        """Отображает лицо с облачком текста в зависимости от настроения."""
        # Если настроение не указано, выбираем случайное
        if emotion is None:
            emotion = random.choice(list(self.faces.keys()))
        
        # Получаем лицо для заданного настроения или используем нейтральное по умолчанию
        face = self.faces.get(emotion, self.faces["neutral"])

        # Генерируем облачко для текста
        bubble_width = len(text) + 4  # Учитываем пробелы и границы
        bubble_top = "╔" + "═" * (bubble_width - 2) + "╗"
        bubble_text = f"│ {text} │"
        bubble_bottom = "╚" + "═" * (bubble_width - 2) + "╝"
        
        # Формируем стрелку
        arrow = "    \\"

        # Формируем вывод
        output = f"{bubble_top}\n{bubble_text}\n{bubble_bottom}\n{arrow}\n    {face}"
        return output

    def random_face(self):
        """Возвращает случайное лицо из словаря."""
        return random.choice(list(self.faces.values()))

    def show_face(self, emotion=None):
        """Показывает заданное или случайное лицо в зависимости от настроения."""
        if emotion is None:
            face = self.random_face()
        else:
            face = self.faces.get(emotion, self.faces["neutral"])
        print(face)

    def animate_random_faces(self, duration=5, interval=0.5):
        """Анимирует случайные лица в течение заданного времени."""
        start_time = time.time()
        while time.time() - start_time < duration:
            self.clear_screen()
            face = self.random_face()
            self.show_face(face)
            time.sleep(interval)

    def wink_face(self):
        """Выдает подмигивающее лицо."""
        self.show_face("wink")

# Пример использования
animator = FaceAnimator()

# Отобразить лицо с определенным или случайным настроением и облачко текста
animator.say("angry", "Приветик!")  # Указанное настроение
animator.say("happy", "Ура!")        # Указанное настроение
animator.say(None, "Как дела?")      # Случайное настроение