# rxshowdesktop
Desktop toggle for for Xubuntu.  Can be attached to a custom launcher icon.

### Installation
This application uses `wmctrl` which must be installed for the application to work.  
`sudo apt install wmctrl`

To install locally in editable mode (this has to be manually uninstalled):  
`pip3 install --user -e .`

To install from github:  
`pip3 install --user git+https://github.com/aldencolerain/rxshowdesktop.git#egg=rxshowdesktop`

To uninstall:  
`pip3 uninstall rxshowdesktop`

To test functionality in terminal:  
`rxshowdesktop show ; sleep 1; rxshowdesktop status; sleep 1; rxshowdesktop hide; rxshowdesktop status`

### To create a showcut in Xfce panel:
 * Right click on panel
 * Select *Panel*
 * Select *Panel Preferences* then select the *Items* tab
 * Click the plus button to add new item to panel
 * Select *Launcher*
 * Select *Add* and close dialog
 * Select the new launcher you created and click the edit button that looks like a little paper with an *i*
 * Click the plus button with the little paper behind it to add a new custom item to the launcher
 * Fill in the dialog with:
   * Name: 'Show Desktop'
   * Command: `rxshowdesktop toggle`
   * Icon: Select any icon, or select *Image Files* and select the transparent icon from this package
     (icon locations can be found with `rxshowdesktop locate` command)


### Running tests
To run all tests:  
`nox`

To run a specific test suite:  
`nox -e lint`

To run a specific test module:  
`nox -e test -- -k test_calc` (To see print statements of passing tests use the `-s` flag)
