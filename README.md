# RC-computer-control-system
Computer based (Qt+Python+CAN) control system. Based on ELE340 ComputerControlSystem (https://github.com/ELE340/ComputerControlSystem)

# Features
* See last sent status from CAN-based distance sensors through a network CAN-Socket server (Found in Embedded Linux tools)

# Installing
## Desktop computer (Windows/Linux)
Make sure you have Python 3.9 (might work with newer, but not tested), and Qt. You can install the dependencies using Poetry, or install them manually.

## Raspberry pi 3b+ and/or Raspberry pi 4
Download an apropriate image from: 
https://www.raspberrypi.com/software/
Use Balena etcher, the raspberry os imager or similar software to write the SD-card image to a micro SD card
* Did not get Poetry to work with Raspberry pi OS when trying.
* Some Python modules should be installed with apt on Raspberry Pi
* Not meant to be used on Embedded Linux ...

# Known Issues and Limitations
* Requirements have not been tested on MacOS

# Future Plans
The following are some features that are being considered for the future:
- Offer deb package with requirements for easy installation
- Integrate a larger set of commands
- Create a nice set of graphing alternative 
- Create a larger set of connection alternatives (directly from CAN, serial, load log file from Embedded Linux server)
- Create a larger set of storage alternative (in memory, SQL?)
- Update checkboxes for light status (blink/front/back lights)

# References
1. https://github.com/tranter/raspberry-pi-qt-builds

# Legal Disclaimer
This software is provided "as is" and any expressed or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. in no event shall ICS or its contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.
