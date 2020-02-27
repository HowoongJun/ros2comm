import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('server_publisher')
        self.publisher_ = self.create_publisher(String, 'server2client', 10)

    def MsgPublish(self, sendMsg):
        msg = String()
        msg.data = sendMsg
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('server_subscriber')
        self.subscriber_Img = self.create_subscription(Image, 'client2server', self.callback_RecvImg, 10)

    def callback_RecvImg(self, msg):
        cvbridge = CvBridge()
        self.cv_image = cvbridge.imgmsg_to_cv2(msg, "bgr8")

    def getImage(self):
        return self.cv_image