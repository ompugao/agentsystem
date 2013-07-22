AgentSystem
==========

AgentSystem Homeworks

# Homework 3,4
- atlasが上がらない

# Homework 5

## QtAtlas

- atlasのGUIです
- qtpy4が必要です

````
    # terminal 1
    roslaunch atlas_utils atlas_sandia_hands.launch
    # terminal 2
    rosrun atlas_msgs action_server
    # terminal 3
    python scripts/qtatlas.py
````
    
# Homework 6,7

- 顔の方向に腕を向けるプログラムです

````
    # terminal 1
    roslaunch roseus_tutorials usb-camera.launch 
    # terminal 2
    roslaunch roseus_tutorials image-view.launch 
    # terminal 3
    roslaunch roseus_tutorials face-detector-mono.launch 
    # terminal 4
    roseus euslisp/pr2_reach_arm_to_face.l
````
