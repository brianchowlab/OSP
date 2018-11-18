# OSP: An Open-source Plate Reader 

## RASBPERRY PI IMAGE - LINK BELOW 

[DISK IMAGE FILE (Updated Nov. 18, 2018)](https://www.dropbox.com/s/7g2e63knupe5y7j/osp_rasp.img?dl=0)

## Instructions for referrence:

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
## SOFTWARE - Before Running a Protocol

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

**Step 3.** *Insert plate into OSP device* - Place the calibration lid onto an empty micro-well plate and insert it into the device, such that well A1 is in the top left corner of the plate holder. (To move the plate holder near the door, press the *plate out* button on the GUI). 

**Step 4.** *Initialize calibration* - On the GUI press the *Calibrate* button and when prompted input the size of the micro-well plate (24 or 96). The machine will begin the calibration process and alert you when it is finished. **This process takes around 3 minutes**

### Loading a Plate

The orientation in which you load the plate is important not only for the calibration process but also for any sort of measurement performed on the OSP device. Please refer to the below picture to ensure you are loading the plate correctly.  The plate should be held firmly in place with attached springs. 
<p align="center">
<img align="center" src="https://github.com/brianchowlab/OSP/blob/master/Software/Graphical%20Files/plate_loading_alignment.png"  width="486" height="400">
</p>

