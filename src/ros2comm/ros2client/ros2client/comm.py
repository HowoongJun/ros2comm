import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('client_publisher')
        self.publisher_ = self.create_publisher(String, 'win2server', 10)
        self.publisher_Img = self.create_publisher(Image, 'win2server', 10)


    def MsgPublish(self, sendMsg):
        msg = String()
        msg.data = sendMsg
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

    def MsgPublishImage(self, sendMsg):
        self.publisher_Img.publish(sendMsg)

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('client_subscriber')
        self.subscription = self.create_subscription(String, 'server2win', self.listener_callback, 10)
        

    def listener_callback(self, msg):
        self.get_logger().info('Subscribing: "%s"' % msg.data)
