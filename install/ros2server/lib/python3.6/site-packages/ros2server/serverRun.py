import rclpy
import ros2server.comm as comm
import time
import cv2

def main(args=None):
    rclpy.init(args=args)
    print("Server Start !")
    minimal_subscriber = comm.MinimalSubscriber()
    rclpy.spin_once(minimal_subscriber)

    RecvImage = minimal_subscriber.getImage()
    cv2.imshow("Image Show", RecvImage)
    cv2.waitKey(0)
    cv2.imwrite('/root/dev_ws/src/ros2comm/ros2server/RecvImage.png', RecvImage)

    minimal_publisher = comm.MinimalPublisher()
    time.sleep(0.2)
    minimal_publisher.MsgPublish("[Server] Image Received! Thanks")
 
    minimal_subscriber.destroy_node()
    minimal_publisher.destroy_node()
    rclpy.shutdown

if __name__ == '__main__':
    main()
