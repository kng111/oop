import requests
import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Погодное приложение")
        self.root.geometry("1000x250")

        # Метка и поле ввода для города
        self.location_label = tk.Label(root, text="Введите город:")
        self.location_label.pack(pady=5)
        self.location_entry = tk.Entry(root)
        self.location_entry.pack(pady=5)

        # Кнопка для получения погоды
        self.get_weather_button = tk.Button(root, text="Узнать погоду", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        # Метка для отображения погоды
        self.weather_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.weather_label.pack(pady=10)

    def get_weather(self):
        # Получение введенного города
        location = self.location_entry.get()
        if not location:
            messagebox.showerror("Ошибка", "Введите город")
            return

        # API ключ и URL для получения данных о погоде
        api_key = "0e825e64948d357ab43d3cb0f675dc59"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}q={location}&appid={api_key}&units=metric"

        try:
            # Отправка запроса на сервер погоды и получение данных
            response = requests.get(complete_url)
            data = response.json()

            # Проверка наличия данных и обработка полученных данных о погоде
            if data["cod"] == "404":
                messagebox.showerror("Ошибка", "Город не найден")
                return

            weather_desc = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            # Формирование строки с информацией о погоде
            result_text = f"Погода в {location}: {weather_desc}, температура: {temperature}°C, влажность: {humidity}%"
            self.weather_label.config(text=result_text)

        except requests.exceptions.RequestException:
            messagebox.showerror("Ошибка", "Произошла ошибка при получении данных")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
