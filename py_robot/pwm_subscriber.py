import rclpy 
import pigpio
from rclpy.node import Node

from std_msgs.msg import Int16
PWM_PIN = 22 pi = pigpio.pi()

class PwmSubscriber (Node):
	def __init__(self):
		super() .__init__('pwm_subscriber') 
		self. subscription = self.create_subscription(
			Int16, 
			'pwm_topic', 
			self.listener_callback, 
			10)
		self.subscription

	def listener_callback(self, msg):
		self.get_logger().info('Subscribed, "%d" ' % msg.data)
		P_width = msg.data
		pi.set_servo_pulsewidth (PWM_PIN, P_width)
def main(args=None):
	 try:
		rclpy.init(args=args)
		pwm_subscriber = PwmSubscriber()
		rclpy.spin (pwm_subscriber)
	except KeyboardInterrupt:
		Pass
	finally:
		pwm_subscriber.destroy_node() 
		rclpy.shutdown()
		
if -_name__ == '__main__':
    main()

