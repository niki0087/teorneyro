import matplotlib.pyplot as plt

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
morning_temps = [1, 2, 4, 7, 2, 0, 0]
day_temps = [15, 17, 16, 18, 19, 14, 11]
evening_temps = [6, 7, 4, 8, 7, 5, 3]

fig, axs = plt.subplots(3, 1, figsize=(10, 12))

axs[0].plot(days, morning_temps, marker='o', color='blue', linestyle='-', label='Температура')
axs[0].set_title('Температурные изменения в Муроме на этой неделе утром')
axs[0].set_xlabel('Дни недели')
axs[0].set_ylabel('Температура (°C)')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(days, day_temps, marker='o', color='orange', linestyle='--', label='Температура')
axs[1].set_title('Температурные изменения в Муроме на этой неделе днем')
axs[1].set_xlabel('Дни недели')
axs[1].set_ylabel('Температура (°C)')
axs[1].legend()
axs[1].grid(True)

axs[2].plot(days, evening_temps, marker='o', color='green', linestyle=':', label='Температура')
axs[2].set_title('Температурные изменения в Муроме на этой неделе вечером')
axs[2].set_xlabel('Дни недели')
axs[2].set_ylabel('Температура (°C)')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()

plt.savefig('weather_changes_murom.png')

plt.show()
