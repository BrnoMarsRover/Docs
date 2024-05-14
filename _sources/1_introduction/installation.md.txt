# Installation
Here's a step-by-step guide for installing all necessary software, such as Ubuntu 22.04, ROS2 and Gazebo simulation, for our Brno Mars Rover project.

## Installing Ubuntu 22.04 LTS Dual Boot:
If you don't know how, watch YouTube. For example [here](https://www.youtube.com/watch?v=GXxTxBPKecQ) or [here](https://www.youtube.com/watch?v=G28jfXt9EaI).

1. **Prepare Your System:**
   - Back up your data. If not, it's your own responsibility :).
   - Create a bootable [Ubuntu 22.04 USB](https://ubuntu.com/download/desktop) drive or borrow a bootable USB from us in the lab. Ask us.

2. **Shrink Existing Partition:**
   - Shrink your existing partition to free up space for Ubuntu.

3. **Boot from Ubuntu USB:**
   - Restart your computer and boot from the USB drive.

4. **Install Ubuntu:**
   - Select "Install Ubuntu" from the menu.
   - Choose "Install Ubuntu alongside [existing OS]".
   - Select the partition for Ubuntu installation.
   - Follow prompts to configure settings.
   - Click "Install".

5. **Complete Installation:**
   - Restart your computer.
   - Choose Ubuntu or existing OS from the boot menu


## Installing ROS2 Humble
Follow the steps below to set up ROS2 on your Ubuntu system. Install ros-humble-desktop. It install ROS, RViz, demos, tutorials and other usefull tools. 

## Follow the ROS2 Humble Installation Documentation

Navigate to the ROS2 Humble installation [documentation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html) and carefully follow the instructions provided. This will involve adding ROS2 repositories and installing necessary dependencies using Debian packages.

## Source ROS2 Setup Script

After completing the installation, **it's essential to source the ROS2** setup script in your terminal session. This step allows you to access ROS2 commands and tools from any terminal window.

If you use Bash, add the following line to your `~/.bashrc` or `~/.zshrc` file if you use [zshell](https://ohmyz.sh/):
```bash
source /opt/ros/humble/setup.bash
```

ROS2 will always source when you open new terminal window.

## Verify installation
Run following nodes in two terminals.

Run demo talker (publisher - It publishes data)
```bash
ros2 run demo_nodes_cpp talker
```
Run demo listener (subscriber - It subscribes published data)
```bash
ros2 run demo_nodes_py listener
```

If it does not work. Continue [here](## Source ROS2 Setup Script).


