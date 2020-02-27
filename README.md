# ROS2 Publish/Subscribe

Publish / Subscribe Framework for Robot Operating System 2

## Prerequisite
1. You need to make ros2 workspace
[Link](https://index.ros.org/doc/ros2/Tutorials/Workspace/Creating-A-Workspace/)

2. Make ros2 package
- Move to ros2 workspace src folder
```
cd dev_ws/src
```

- C++
```
ros2 pkg create --build-type ament_cmake --node-name [NODE_NAME] [PKG_NAME]
```
- Python   
```
ros2 pkg create --build-type ament_python --node-name [NODE_NAME] [PKG_NAME]
```

- Move back to ros2 workspcae
```
cd ~/dev_ws
```

- Build package
```
colcon build --packages-select [PKG_NAME]
```

- Run package
```
. install/setup.bash
ros2 run [PKG_NAME] [NODE_NAME]
```

3. Install dependencies
```
sudo apt-get install ros-dashing-cv-bridge
sudo apt-get install ros-dashing-vision-opencv
sudo apt-get install python3-opencv
```

## ros2server
- Waiting for client's message
- When message arrived, server sends ack to the client

- Run 

```
ros2 run ros2comm serverRun
```

## ros2client
- Sends message to the server
- Receives ack from the server

- Run

```
ros2 run ros2comm clientRun
```

## Error List

### 'Package '~' not found' error
- Move to your ros2 workspace

```
cd /root/dev_ws/
. install/setup.bash
```

### 'ros2 command not found' error

```
source /opt/ros/dashing/setup.bash
```
