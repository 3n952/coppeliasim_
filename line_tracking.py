from coppeliasim_zmqremoteapi_client import RemoteAPIClient 
import time

client = RemoteAPIClient()
sim = client.require('sim')
left_joint = sim.getObject('/DynamicLeftJoint')
right_joint = sim.getObject('/DynamicRightJoint')


sim.setStepping(True)

sim.startSimulation()

while True:
        
    time.sleep(0.1)
    #print(f'Simulation time: {t:.2f} [s]')
    sim.setJointTargetVelocity(left_joint, 2)
    sim.setJointTargetVelocity(right_joint, 1)
    sim.step()
    if (t := sim.getSimulationTime()) < 5:
        sim.stopSimulation()
        break
    
