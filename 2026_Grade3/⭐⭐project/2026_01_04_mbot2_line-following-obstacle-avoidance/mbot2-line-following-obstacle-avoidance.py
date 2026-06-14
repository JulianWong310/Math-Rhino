import cyberpi, mbot2, time, mbuild, event

@event.is_press('a')
def obstacle():
    while True:

        # Obstacle avoidance (high priority)
        if mbuild.ultrasonic2.get(1) < 10:
            mbot2.drive_power(40, 40)
            time.sleep(0.6)

        # Line sensors
        left_black = (
                mbuild.quad_rgb_sensor.is_color("black", "L1") or
                mbuild.quad_rgb_sensor.is_color("black", "L2")
        )
        right_black = (
                mbuild.quad_rgb_sensor.is_color("black", "R1") or
                mbuild.quad_rgb_sensor.is_color("black", "R2")
        )

        # Black line following
        if left_black and right_black:
            mbot2.drive_power(20, -20)
        elif left_black:
            mbot2.drive_power(10, -30)
        elif right_black:
            mbot2.drive_power(30, -10)
        else:
            mbot2.drive_power(10, -10)