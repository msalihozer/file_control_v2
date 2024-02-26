# file_control_v2
 File Control and Transfer Utility v2
This Python script enhances the file control and transfer functionality by allowing the user to select a list file, removing duplicate entries, and providing progress bars during file transfer.

Description
The script reads filenames from a selected text file, removes duplicates, and transfers the files from a source directory to a target directory.

Dependencies
Python 3.x
path library
getch library
tkinter library
tqdm library
Installation
Ensure you have Python 3.x installed on your system.
Install the required libraries:
lua
Copy code
pip install path tqdm getch
Usage
Run the script:
Copy code
python file_control_v2.py
Select a text file containing filenames when prompted.
The script will remove duplicate filenames, transfer the files from the source directory to the target directory, and display progress bars for each transfer.
Configuration
Update the KAYNAK variable with the path to your source directory.
Update the HEDEF variable with the path to your target directory.
Important Notes
Ensure that you have appropriate permissions for reading files from the source directory and writing files to the target directory.
Press any key to exit the script after execution.
License
This project is licensed under the MIT License.

Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
