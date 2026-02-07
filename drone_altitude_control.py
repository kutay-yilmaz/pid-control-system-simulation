import numpy as np
import matplotlib.pyplot as plt
# DRONE ALTITUDE HOLD SIMULATION
def run_drone_sim():
    target_alt = 5.0 # meters
    kp, ki, kd = 10.0, 2.0, 5.0
    alt = 0.0 # start at ground
    dt = 0.05
    history = []
    integral = 0
    prev_err = 0
    time = np.arange(0, 5, dt)
    for t in time:
        err = target_alt - alt
        integral += err * dt
        der = (err - prev_err) / dt
        thrust = (kp * err) + (ki * integral) + (kd * der)
        alt += (thrust - 9.81) * dt**2 # Thrust vs Gravity
        history.append(alt)
        prev_err = err
    plt.figure(figsize=(10, 4))
    plt.plot(time, history, color='green', label='Drone Altitude')
    plt.axhline(y=target_alt, color='black', linestyle='--', label='Target Alt')
    plt.title('Drone Altitude Stability (PID)')
    plt.grid(True)
    plt.legend()
    plt.show()
if __name__ == "__main__":
    run_drone_sim()
