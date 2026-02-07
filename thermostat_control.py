import numpy as np
import matplotlib.pyplot as plt
# THERMOSTAT TEMPERATURE CONTROL
def run_temp_control():
    target_temp = 24.0 # Celsius
    kp, ki, kd = 1.2, 0.05, 0.1
    temp = 15.0 # Starting room temp
    dt = 1
    history = []
    integral = 0
    prev_err = 0
    time = np.arange(0, 100, dt)
    for t in time:
        err = target_temp - temp
        integral += err * dt
        der = (err - prev_err) / dt
        heat_output = (kp * err) + (ki * integral) + (kd * der)
        temp += heat_output * 0.1 # Room heating up
        temp -= 0.05 # Heat loss to outside
        history.append(temp)
        prev_err = err
    plt.figure(figsize=(10, 4))
    plt.plot(time, history, color='orange', label='Room Temp')
    plt.axhline(y=target_temp, color='blue', linestyle='--', label='Set Point')
    plt.title('Thermostat PID Temperature Control')
    plt.grid(True)
    plt.legend()
    plt.show()
if __name__ == "__main__":
    run_temp_control()
