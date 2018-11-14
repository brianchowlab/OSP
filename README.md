# OSP: An Open-source Plate Reader 
<p align="center">
<img align="center" src="https://github.com/brianchowlab/OSP/blob/master/Software/Graphical%20Files/repoImage.png" width="486" height="245">
</p>

### Introduction
OSP is a low-cost open-source plate reader built out of the Chow Lab at the University of Pennsylvania. The software provided in this repository is required to access the full functionailty of a built OSP device. For information regarding how to build this device and details about how it works, please refer to the ACS: BioChemistry manuscript available at this LINK.

## GETTING STARTED 
### Dependencies
The OSP software is written in Python 2.7 and utilizes the PyQt4 package to create a functional User Interface.   Below is a list of all other Python packages required to successfully use the OSP device: 

* PyQt 4
* Seabreeze
* Numpy
*	Pickle
* Platform
* Xlswriter
*	Matplotlib
*	Numpy
*	Time 
*	Serial
*	Warnings

In addition, the Arduino IDE will have to be installed in order to load the OSP Arduino script (provided int this repository) onto the device's Arduino UNO board. 

**The installation section below will guide you through installing all these dependencies and any programs required!!!**


### Installation (Windows/Mac)
Installation of OSP software dependencies on any Windows/Mac device is accomplished utilizing Anaconda, which should come prepackaged with all requirements except PyQt4, Seabreeze and Pyserial. 

**Step 1.** *Install Anaconda* - Visit the following [LINK](https://www.anaconda.com/download/) to download the Anaconda Software.    
> (**!!CAVEAT!!** Be sure to download the version for Python 2.X and for your specific OS environment (Windows/Mac).

**Step 2.** *Install the PyQt4 package* - Open *Anaconda Prompt* (installed with Anaconda) and type the following line of code:
```sh
$ conda install pyqt=4
```

**Step 3.** *Install the Seabreeze package* - In *Anaconda Prompt* type the following line of code:
```sh
$ conda install -c poehlmann python-seabreeze
```

**Step 4.** *Install the PySerial package* - In *Anaconda Prompt* type the following line of code:
```sh
$ conda install -c anaconda pyserial
```

**Step 5.** *Clone the OSP repository* - In *Anaconda Prompt* type the following line of code:
```sh
$ git clone https://github.com/brianchowlab/OSP.git
```

**Step 6.** *Install Arduino IDE* -  Visit the following [LINK](https://www.arduino.cc/en/Main/Software) to download the latest Arduino IDE. 

**Step 7.** *Upload OSP script onto Arduino UNO* - Using the Arduino IDE open up the OSP Arduino script located in the cloned respository folder *OSP\Software\Arduino Files\OSP_Serial_Communication*.  Make sure the Arduino is connected via USB and click the **UPLOAD** button in the Arduino IDE. 

**Step 8.** ***(ONLY WINDOWS USERS)*** *Setting up Seabreeze Drivers* - Visit the following [LINK](https://github.com/ap--/python-seabreeze/blob/master/misc/windows-driver-files.zip) and download the Windows Seabreeze drivers zip file.  Extract it to a known location.  Then open up *Device Manager* on your Windows machine, find the spectrometer in the list, *right click it* and choose *Update Driver Software*.  A windows will pop up. Navigate to the folder where you extracted the Windows Seabreeze drivers file and select it. 

**Step 9.** *Opening the User Interface* - In order to start utilizing the OSP device, make sure the device is **turned on** and plugged in via USB to a computer.  Open up *Anaconda Prompt* and write the following lines of code:
```sh
$ cd  "OSP\Software\Python Files"
$ python GUI.py
```

### Installation (Raspberry-Pi Image)
The simplest way to install the OSP software on a Raspberry-Pi is by downloading and installing the OSP.img file provided. In order to do this, you will need to have a completely empty 16GB Micro SD Card. If the card is not empty, all of its contents will be deleted in the installation of the OSP.img file. In addition, the first 3 installation steps need to be performed on a computer/laptop with an SD card slot. 

**Step 1.** *Download & Unzip the OSP.img* - Visit the following [LINK](https://www.arduino.cc/en/Main/Software) and download the *OSP.img* file. Once downloaded unzip the file to a known location. 

**Step 2.** *Download & Install the Etcher program* - Visit the following [LINK](https://www.balena.io/etcher/) and download the *Etcher* program for your specific operating system. 

**Step 3.** *Install the OSP.img onto the SD Card* - Insert your empty SD card into the computer. Start up the Etcher software and follow the on screen instructions in order to install the OSP.img onto the card. **This process can take up to 10 minutes**

**Step 4.** *Opening the User Interface* - Once the OSP.img file is installed, insert it into your Raspberry-Pi (which should be connected to the active OSP device, touch-screen/monitor, keyboard & mouse). Turn the Raspberry-Pi on and when it is booted open up the Terminal. To activate the User Interface type the following:
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




