import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8, String

class Node3(Node):
    def __init__(self):
        super().__init__('node_3')
        self.sub = self.create_subscription(Int8, '/palindrome_flag', self.process_flag, 10)
        self.pub = self.create_publisher(String, '/feedback_topic', 10)

    def process_flag(self, msg):
        reply = String()
        if msg.data == 1:
            reply.data = "Yes"
            print("Output: Yes")
        else:
            reply.data = "No"
            print("Output: No")
        self.pub.publish(reply)

def main(args=None):
    rclpy.init(args=args)
    node = Node3()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
