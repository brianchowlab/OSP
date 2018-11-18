# OSP: An Open-source Plate Reader 

## SOFTWARE - GETTING STARTED 
### Dependencies
The OSP software is written in Python 2.7 and utilizes the PyQt4 package to create a functional User Interface.   Below is a list of all other Python packages required to successfully use the OSP device: 

* PyQt 4
* Seabreeze
* Numpy
*	Pickle
* Platform
* Xlswriter
*	Matplotlib
*	Time 
*	Serial
*	Warnings

In addition, the Arduino IDE will have to be installed in order to load the OSP Arduino script (provided int this repository) onto the device's Arduino UNO board. 

**The installation section below will guide you through installing all these dependencies and any programs required**


### Installation (Windows/Mac)
Installation of OSP software dependencies on any Windows/Mac device is accomplished utilizing Anaconda, which should come prepackaged with all requirements except PyQt4, Seabreeze, Pyserial and Git. The following instructions require you to write in command line. If you have never used command line visit the following [LINK (Windows)](https://www.makeuseof.com/tag/a-beginners-guide-to-the-windows-command-line/) or [LINK (Mac)](https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line) for a quick intro.

**Step 1.** *Install Anaconda* - Visit the following [LINK](https://www.anaconda.com/download/) to download the Anaconda Software. Be sure to download the version for Python 2.X and for your specific OS environment (Windows/Mac). When prompted whether to ***add Anaconda to your path*** select yes. 

**Step 2.** *Install Git* - Visit the following [LINK](https://git-scm.com/download) to download the Anaconda Software. Be sure to download the version for your specific OS environment (Windows/Mac).  When prompted whether to ***add Git to your path*** select yes. 

**Step 3.** *Clone the OSP repository* - Open the Terminal on your computer as an administrator. To do this, find the Terminal application, *right-click* it and select *Run as administrator*. To clone the repository onto your system type the following lines of code (Make sure to use the ones specific to your OS):

***WINDOWS***
```sh
cd %USERPROFILE%
git clone https://github.com/brianchowlab/OSP.git
```

***MAC***
```sh
cd ~
git clone https://github.com/brianchowlab/OSP.git
```

**Step 4.** *Run the OSP installation script* - In the open Terminal window type the following and leave the window open:

***WINDOWS***
```sh
.\OSP\Software\install_pc_reqs.sh
```

***MAC***
```sh
./OSP/Software/install_pc_reqs.sh
```

**Step 5.** *Install Arduino IDE* -  Visit the following [LINK](https://www.arduino.cc/en/Main/Software) to download the latest Arduino IDE. 

**Step 6.** *Upload OSP script onto Arduino UNO* - Using the Arduino IDE open up the OSP Arduino script located in the cloned respository folder *OSP\Software\Arduino Files\OSP_Serial_Communication*.  Make sure the Arduino is plugged into the USB-hub of the OSP device and and that the OSP device is connected to your computer via USB.  Click the **UPLOAD** button in the Arduino IDE to compile and upload the code to the Arduino.

**Step 7.** ***(ONLY WINDOWS USERS)*** *Setting up Seabreeze Drivers* - Visit the following [LINK](https://github.com/ap--/python-seabreeze/blob/master/misc/windows-driver-files.zip) and click the download button.  Extract the downloaded .zip file to a known location. Open up *Device Manager* on your Windows machine. Connect your computer to the OSP device via USB. In the  *Device Manager* list of devices make sure that there is now a tab named *Ocean Optics USB Devices*. In that tab should be a device named *Ocean Optics STS (WinUSB). If this device is present you can now move on to step 9.

If for some reason, you cannot find *Ocean Optics USB Devices* in the *Device Manager* you will have to manually set-up the drivers. To do this, in the *Device Manager* find the tab labeled *Other Devices*.  In that tab there should be a deviced named *STS*. *Right-click* on this device name and selected *Update drivers* from the drop-down menu. Next, a window will pop up asking you where the system should look for the drivers. Select the *Browse my computer for the driver software*.  On the next screen click the browse button and direct the system to the *windows-driver-files* folder which you downloaded & extracted at the beginning of this step.

**Step 8.** *Opening the User Interface* - In order to start utilizing the OSP device, make sure the device is **turned on** and plugged in via USB to a computer.  In your open Terminal window type the following:

***WINDOWS***
```sh
activate osp
cd "OSP\Software\Python Files"
python GUI.py
```

***MAC***
```sh
source activate osp
cd "OSP\Software\Python Files"
python GUI.py
```

### Installation (Raspberry-Pi Image)
The simplest way to install the OSP software on a Raspberry-Pi is by downloading and installing the OSP.img file provided. In order to do this, you will need to have a completely empty 16GB Micro SD Card. If the card is not empty, all of its contents will be deleted in the installation of the OSP.img file. In addition, the first 3 installation steps need to be performed on a computer/laptop with an SD card slot. 

**Step 1.** *Download & Unzip the OSP.img* - Visit the following [LINK](https://www.dropbox.com/s/7g2e63knupe5y7j/osp_rasp.img?dl=0) and download the *OSP.img* file. Once downloaded unzip the file to a known location. 

**Step 2.** *Download & Install the Etcher program* - Visit the following [LINK](https://www.balena.io/etcher/) and download the *Etcher* program for your specific operating system. 

**Step 3.** *Install the OSP.img onto the SD Card* - Insert your empty SD card into the computer. Start up the Etcher software and follow the on screen instructions in order to install the OSP.img onto the card. **This process can take up to 10 minutes**

**Step 4.** *Update OSP repository* - Once the OSP.img file is installed, insert it into your Raspberry-Pi (which should be connected to the active OSP device, touch-screen/monitor, keyboard & mouse). Turn the Raspberry-Pi on and when it is booted open up the Terminal. Type the following and close the Terminal when it is finished:
```sh
$ cd OSP
$ git pull origin master
```
**Step 5.** *Running the Usert Interface* - To activate the User Interface make sure the OSP device is turned on and connected to the Raspberry-Pi via USB. Open up the Terminal and type the following:
```sh
$ cd  "OSP\Software\Python Files"
$ sudo python GUI.py
```

### Initial Functionality Testing
Once you have completed the installation process (by following the steps above) it is usefull to check if all the light sources (LEDs) and linear actuators as behaving correctly. These tests can be performed from the Arduino IDE *Serial Monitor*. 

**Step 1.** *Open Arduino Serial Monitor* - Make sure the OSP device is plugged into a computer/Raspberry-Pi and turned on. Open up the Arduino IDE and click on the ***Tools*** tab in the menu bar. From the dropdown menu select ***Serial Monitor***. This will open up the ***Serial Monitor*** in a new window. 

**Step 2.** *Test Linear Actuator Functionality* 
* Type the following into the text box at the top of the Serial Monitor and press the *Send* button: **M1500.001500.00;** 
  * This should extend both linear actuators about half way. 
* Type the following into the text box at the top of the Serial Monitor and press the *Send* button: **M1000.001000.00;** 
  * This should retract both linear actuators all the way. 
  
**Step 3.** *Test LED Functionality* 
* Type the following into the text box at the top of the Serial Monitor and press the *Send* button: **L1;** 
  * This should result in the LED 1 turning on. To turn it off, type the same command in again.   
* Type the following into the text box at the top of the Serial Monitor and press the *Send* button: **L2;** 
  * This should result in the LED 2 turning on. To turn it off, type the same command in again.   
* Type the following into the text box at the top of the Serial Monitor and press the *Send* button: **L3;** 
  * This should result in the LED 3 turning on. To turn it off, type the same command in again.
* Type the following into the text box at the top of the Serial Monitor and press the *Send* button: **L4;** 
  * This should result in the LED 4 turning on. To turn it off, type the same command in again.
* Type the following into the text box at the top of the Serial Monitor and press the *Send* button: **L5;** 
  * This should result in the LED 5 & LED 6 (top) turning on. To turn them off, type the same command in again.
  
### Calibration Guide
The software provided in this repository comes with pre-loaded with calibrated positions for a 24-well plate and a 96-well plate. However, it is recommended that an initial calibration is performed after the OSP device is built to account for any small differences in assembly. 

Before performing any sort of calibration you will need to prepare the calibration lid for the specific plate-type that is to be calibrated. Refer to the *Calibration Lid Assembly* at the end of the *General Assembly Guide* for instructions on how to do this.

The following steps should be followed everytime a calibration is performed:

**Step 1.** *Attach Fiber to Photodiode* - Deattach the fiber from the STS spectrophotometer and screw it into the photodiode mount rigth next to it. 

**Step 2.** *Adjust the Iris* -  As part of the Top Optics assembly there is an iris. Using the guidelines on the rim of the iris, set the iris to a size of 2. 

**Step 3.** *Insert plate into OSP device* - Place the calibration lid onto an empty micro-well plate and insert it into the device. (To move the holder near the door, press the *plate out* button on the GUI). 

**Step 4.** *Initialize calibration* - On the GUI press the *Calibrate* button and when prompted input the size of the micr-well plate (24 or 96). The machine will begin the calibration process and alert you when it is finished. **This process takes around 3 minutes**

