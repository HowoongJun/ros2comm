import rclpy
import ros2client.comm as comm
import time
from cv_bridge import CvBridge
import cv2

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = comm.MinimalSubscriber()
    minimal_publisher = comm.MinimalPublisher()
    cvimg = cv2.imread('/root/dev_ws/src/ros2comm/ros2client/SampleImage.png', cv2.IMREAD_COLOR)
    cvbridge = CvBridge()
    
    time.sleep(0.15)
    minimal_publisher.MsgPublishImage(cvbridge.cv2_to_imgmsg(cvimg, "bgr8"))
    print('Image Sent!')
    rclpy.spin_once(minimal_subscriber)
    minimal_subscriber.destroy_node()
    minimal_publisher.destroy_node()
    rclpy.shutdown
    
if __name__ == '__main__':
    main()
