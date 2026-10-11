import rclpy
from rclpy.node import Node
from driverless_msgs.msg import RT2String

class Node1(Node):
    def __init__(self):
        super().__init__('node_1')
        self.publisher_ = self.create_publisher(RT2String, '/string_topic', 10)
        self.timer = self.create_timer(3.0, self.publish_data)

    def publish_data(self):
        user_str = input("Enter a string: ")
        msg = RT2String()
        msg.data = user_str
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
