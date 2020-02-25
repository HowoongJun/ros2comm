import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('client_publisher')
        self.publisher_ = self.create_publisher(String, 'server2win', 10)

    def MsgPublish(self, sendMsg):
        msg = String()
        msg.data = sendMsg
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('client_subscriber')
        self.subscriber_Img = self.create_subscription(Image, 'win2server', self.callback_RecvImg, 10)

    def callback_RecvImg(self, msg):
        cvbridge = CvBridge()
        cv_image = cvbridge.imgmsg_to_cv2(msg, "bgr8")
        cv2.imshow("Image Show", cv_image)
        cv2.waitKey(3)
        cv2.imwrite('/root/dev_ws/src/ros2comm/ros2server/RecvImage.png', cv_image)