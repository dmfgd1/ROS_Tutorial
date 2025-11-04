import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

# TODO: Q1.3
class TutorialTopic_1_3(Node):
    def __init__(self):
        super().__init__('tutorial_node_q_1_3')
        ### STUDENT CODE HERE

        self.number_publisher = self.create_publisher(
            Int32,
            "/tutorial/counter25",
            10
        )
        ### END STUDENT CODE
        
        # This calls the function timer_callback every 0.01 second
        self.timer = self.create_timer(0.01, self.timer_callback)
        self.counter = 0
    

    def timer_callback(self):
        ### STUDENT CODE HERE
        if(self.counter <= 25):
            msg = Int32()
            msg.data = self.counter
            self.number_publisher.publish(msg)
            self.counter += 1
        else:
            self.timer.cancel()
        ### END STUDENT CODE
        pass

def main(args=None):
    rclpy.init(args=args)
    node = TutorialTopic_1_3()
    rclpy.spin(node)
