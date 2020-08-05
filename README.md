# rxshowdesktop
Example pip package.

### Running tests
To run all tests:  
`nox`

To run a specific test suite:  
`nox -e lint`

To run a specific test module:  
`nox -e test -- -k test_calc` (To see print statements of passing tests use the `-s` flag)

To try out module:  
`rxshowdesktop add 1 2`

To install from github:  
`pip3 install --user git+https://github.com/aldencolerain/rxshowdesktop.git#egg=rxshowdesktop`

To uninstall:  
`pip3 uninstall rxshowdesktop`
