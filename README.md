# RC-computer-control-system
Computer based (Qt+Python+CAN) control system. Based on ELE340 ComputerControlSystem (https://github.com/ELE340/ComputerControlSystem)

# Overview


# Features


# Installing
## Raspberry pi 3b+ and/or Raspberry pi 4
Download an apropriate image from: 
https://www.raspberrypi.com/software/
Use Balena etcher, the raspberry os imager or similar software to write the SD-card image to a micro SD card

If needed: 
```
# Check this part QA!
sudo apt-get update && sudo apt-get upgrade
sudo apt install python3-pip pyqt5chart-dev
pip3 install pyqtgraph==0.12.3
```

Clone this repo and enter it
## In general, make sure to have a new release of Qt 5 and install the python requirements: 
```
pip3 install -r requirements.txt
```

# Known Issues and Limitations
* Requirements have not been tested on MacOS

# Future Plans
The following are some features that are being considered for the future:
- Offer deb package with requirements for easy installation
- Integrate a larger set of commands 

# References

1. https://github.com/tranter/raspberry-pi-qt-builds

# Legal Disclaimer

This software is provided "as is" and any expressed or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. in no event shall ICS or its contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.
