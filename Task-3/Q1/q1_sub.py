import rclpy
from rclpy.node import Node
from driverless_msgs.msg import TaskOne

class WheelSpeedSub(Node):
    def __init__(self):
        super().__init__('wheel_speed_sub')
        self.subscription = self.create_subscription(TaskOne, '/taskone', self.callback, 10)

    def callback(self, msg):
        speed = msg.ang_vel * msg.radius
        print(f"Calculated Longitudinal Speed: {speed:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = WheelSpeedSub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
