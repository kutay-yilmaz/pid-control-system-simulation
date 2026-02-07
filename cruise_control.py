import numpy as np
import matplotlib.pyplot as plt
# CRUISE CONTROL PID SIMULATION
def run_cruise_control():
    target_speed = 110.0 # km/h
    kp, ki, kd = 0.8, 0.15, 0.05
    v = 0.0 # initial speed
    dt = 0.1
    history = []
    integral = 0
    prev_err = 0
    time = np.arange(0, 20, dt)
    for t in time:
        err = target_speed - v
        integral += err * dt
        der = (err - prev_err) / dt
        accel = (kp * err) + (ki * integral) + (kd * der)
        v += accel * dt # Physics engine
        history.append(v)
        prev_err = err
    plt.figure(figsize=(10, 4))
    plt.plot(time, history, label='Vehicle Speed')
    plt.axhline(y=target_speed, color='r', linestyle='--', label='Target')
    plt.title('Vehicle Cruise Control (PID)')
    plt.grid(True)
    plt.legend()
    plt.show()
if __name__ == "__main__":
    run_cruise_control()
