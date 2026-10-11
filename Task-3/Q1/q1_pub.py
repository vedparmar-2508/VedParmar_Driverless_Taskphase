import rclpy
from rclpy.node import Node
from driverless_msgs.msg import TaskOne

class WheelSpeedPub(Node):
    def __init__(self):
        super().__init__('wheel_speed_pub')
        self.publisher_ = self.create_publisher(TaskOne, '/taskone', 10)
        self.timer = self.create_timer(2.0, self.publish_data)

    def publish_data(self):
        try:
            ang = float(input("Enter angular velocity (angVel): "))
            rad = float(input("Enter radius: "))
            msg = TaskOne()
            msg.ang_vel = ang
            msg.radius = rad
            self.publisher_.publish(msg)
        except ValueError:
            self.get_logger().error("Invalid input. Enter numbers.")

def main():
    rclpy.init()
    node = WheelSpeedPub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
