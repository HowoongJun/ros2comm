# ROS2 Publish/Subscribe

Publish / Subscribe Framework for Robot Operating System 2

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
