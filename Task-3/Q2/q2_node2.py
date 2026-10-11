import rclpy
from rclpy.node import Node
from driverless_msgs.msg import RT2String
from std_msgs.msg import Int8, String

class Node2(Node):
    def __init__(self):
        super().__init__('node_2')
        self.sub = self.create_subscription(RT2String, '/string_topic', self.check_palindrome, 10)
        self.pub = self.create_publisher(Int8, '/palindrome_flag', 10)
        self.feedback_sub = self.create_subscription(String, '/feedback_topic', self.feedback_cb, 10)

    def check_palindrome(self, msg):
        s = msg.data
        flag = 1 if s == s[::-1] else 0
        out_msg = Int8()
        out_msg.data = flag
        self.pub.publish(out_msg)

    def feedback_cb(self, msg):
        self.get_logger().info(f'Node 3 conveyed: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Node2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
