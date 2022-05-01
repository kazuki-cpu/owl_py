import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int16 
from std_msgs.msg import Bool

class RobotManager (Node):
	def __init__(self):
		super(). __init__('robot_manager') 
		self.publisher_ = self.create_publisher (Int16, 'pwm_topic' 10) 
		self.subscription = self.create_subscription(
			Bool, 
			'status_topic', 
			self.timer_callback, 
			10)
		self.i = 500
		
	def timer_callback(self, status_msg):
		pwm_msg = Int16() 
		pwm_msg.data = self.i 
		self.publisher_.publish (pwm_msg) 
		self.get_logger().info('Publishing, "%d"' % pwm_msg.data) 
		if status_msg.data == True: 
			if self.i ==2500:
				self.i = 500 
			else:
				self.i += 100 
		else:
			self.i = self.i
			
		self.get_logger ().info('Subscribed, "%s"' % status_msg.data)
		
def main(args=None): 
	try:
		rclpy.init(args=args)
		robot_manag
		rclpy.spin(robot_manager) 
	except KeyboardInterrupt:
		pass 
	finally:
		robot_manager.destroy_node() 
		rclpy.shutdown()
		
if __name__ == '__main__':
    main()
