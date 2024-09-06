from coppeliasim_zmqremoteapi_client import RemoteAPIClient 
import time


def sysCall_actuation(data_left, data_right):
    # put your actuation code here
    v = 4
    dv = 5
    sim.setJointTargetVelocity(left_joint, v)
    sim.setJointTargetVelocity(right_joint, v)

    if data_left != None:
    
        intensity_left = data_left[10]
        intensity_right = data_right[10]
        
    
        if intensity_right > 0.5 and intensity_left < 0.5:
            print('turn left')
            sim.setJointTargetVelocity(right_joint, v+dv)
            
        if intensity_left > 0.5 and intensity_right < 0.5:
            print('turn right')
            sim.setJointTargetVelocity(left_joint, v+dv)

def sysCall_sensing(left_sensor, right_sensor):
    # put your sensing code here
    #result_left, data_left, *_ = sim.handleVisionSensor(left_sensor)
    #result_right, data_right, *_ = sim.handleVisionSensor(right_sensor)
    
    result_left, data_left, *_ = sim.readVisionSensor(left_sensor)
    result_right, data_right, *_ = sim.readVisionSensor(right_sensor)
    
    return data_left, data_right

client = RemoteAPIClient()
sim = client.require('sim')

# initialize

left_joint = sim.getObject('/DynamicLeftJoint')
right_joint = sim.getObject('/DynamicRightJoint')
left_sensor = sim.getObject('/LeftSensor')
right_sensor = sim.getObject('/RightSensor')

sim.setStepping(True)

sim.startSimulation()

while True:
        
    time.sleep(0.1)
    #print(f'Simulation time: {t:.2f} [s]')
    data_left, data_right = sysCall_sensing(left_sensor, right_sensor)
    sysCall_actuation(data_left, data_right)
    sim.step()
    if sim.getSimulationTime() < 50:
        sim.stopSimulation()
        break
    
   

    