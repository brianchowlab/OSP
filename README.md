# OSP: An Open-source Plate Reader 
<img src="https://dats.seas.upenn.edu/wp-content/uploads/2017/08/cropped-seas-logo-dark.png" width="100" height="35">

### Introduction
OSP is a low-cost open-source plate reader built out of the Chow Lab at the University of Pennsylvania. The software provided in this repository is required to access the full functionailty of a built OSP device. For information regarding how to build this device and details about how it works, please refer to the ACS: BioChemistry manuscript available at this LINK.

## GETTING STARTED 
### Dependencies
The OSP software is written in Python 2.7 and utilizes the PyQt4 package to create a functional User Interface.   Below is a list of all other Python packages required to successfully use the OSP device: 

* PyQt 4
* Seabreeze 
*	Pickle
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
$ conda install -c poehlmann python-seabreeze
```

**Step 5.** *Clone the OSP repository* - In *Anaconda Prompt* type the following line of code:
```sh
$ git clone https://github.com/KokoIsLoko/OSP.git
```

**Step 6.** *Install Arduino IDE* -  Visit the following [LINK](https://www.arduino.cc/en/Main/Software) to download the latest Arduino IDE. 

**Step 7.** *Upload OSP script onto Arduino UNO* - Using the Arduino IDE open up the OSP Arduino script located in the cloned respository folder *OSP\Software\Arduino Files\OSP_Serial_Communication*.  Make sure the Arduino is connected via USB and click the **UPLOAD** button in the Arduino IDE. 

**Step 8.** *Opening the User Interface* - In order to start utilizing the OSP device, open up *Anaconda Prompt* and write the following lines of code:
```sh
$ cd  "OSP\Software\Python Files"
$ python GUI.py
```






