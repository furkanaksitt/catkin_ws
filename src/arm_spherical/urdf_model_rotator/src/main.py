import rospy
from sensor_msgs.msg import JointState
import time
import math

def rotate_joints():
    # ROS node başlat
    rospy.init_node('urdf_model_rotator', anonymous=True)
    
    # ROS sisteminin başlaması için bekle
    time.sleep(0.5)
    
    # Publisher oluştur
    joint_pub = rospy.Publisher('/joint_states', JointState, queue_size=1)
    
    # 30Hz ile çalış - daha sabit bir hız için
    rate = rospy.Rate(30)  
    
    # Joint positions ve limitleri
    joint_positions = [0.0, 0.0, 0.0]
    joint_directions = [1, 1, 1]
    joint_limits = [1.57, 1.57, 2.35]
    
    active_joint = 0
    pause_counter = 0
    
    # Sinusoidal hareket için zaman değişkeni
    t = 0.0
    
    # Hareket modunu belirle (başlangıçta sequential)
    rospy.set_param('/motion_mode', 'sequential')
    
    # İlk pozisyon mesajını gönder
    joint_state = JointState()
    joint_state.header.stamp = rospy.Time.now()
    joint_state.name = ['Base_Revolute', 'Revolute_2', 'Revolute3']
    joint_state.position = joint_positions
    joint_state.velocity = [0.0, 0.0, 0.0]
    joint_state.effort = [0.0, 0.0, 0.0]
    joint_pub.publish(joint_state)
    
    # RViz'in hazır olması için kısa bir süre bekle
    time.sleep(0.5)
    
    rospy.loginfo("Joint state publisher başlatıldı")
    
    while not rospy.is_shutdown():
        # Hareket modunu al
        motion_mode = rospy.get_param('/motion_mode', 'sequential')
        
        if motion_mode == 'sequential':
            # Sequential hareket - Her seferinde bir eklem hareket eder
            if pause_counter > 0:
                pause_counter -= 1
            else:
                # Doğrudan pozisyon değişimi
                joint_positions[active_joint] += joint_directions[active_joint] * 0.05
                
                # Limit kontrolü
                if joint_positions[active_joint] >= joint_limits[active_joint]:
                    joint_positions[active_joint] = joint_limits[active_joint]
                    joint_directions[active_joint] = -1
                    # Bir sonraki ekleme geç
                    active_joint = (active_joint + 1) % 3
                    pause_counter = 5
                
                elif joint_positions[active_joint] <= -joint_limits[active_joint]:
                    joint_positions[active_joint] = -joint_limits[active_joint]
                    joint_directions[active_joint] = 1
                    # Bir sonraki ekleme geç
                    active_joint = (active_joint + 1) % 3
                    pause_counter = 5
        
        elif motion_mode == 'sinusoidal':
            # Sinusoidal hareket - Tüm eklemler sinüs dalgasıyla hareket eder
            joint_positions = [
                math.sin(t) * 1.57,                  # Base_Revolute 
                math.sin(t + math.pi / 2) * 1.57,    # Revolute_2 (90 derece faz farkı)
                math.sin(t + math.pi) * 2.35         # Revolute3 (180 derece faz farkı)
            ]
            # Zaman değişkenini artır (hareket hızını belirler)
            t += 0.05
            
        # JointState mesajı oluştur ve yayınla
        joint_state = JointState()
        joint_state.header.stamp = rospy.Time.now()
        joint_state.name = ['Base_Revolute', 'Revolute_2', 'Revolute3']
        joint_state.position = joint_positions
        joint_state.velocity = [0.0, 0.0, 0.0]
        joint_state.effort = [0.0, 0.0, 0.0]
        
        # Publish
        joint_pub.publish(joint_state)
        
        # Log yazdır
        rospy.loginfo(f"Mode: {motion_mode}, Active Joint: {active_joint}, Positions: {joint_positions}")
        
        # Rate ile bekleme
        rate.sleep()

if __name__ == '__main__':
    try:
        rotate_joints()
    except rospy.ROSInterruptException:
        pass