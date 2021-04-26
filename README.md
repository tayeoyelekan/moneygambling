On Windows
step 1. python -m pip install -r requirements.txt

step 2. python -n pytest --driver Chrome --driver-path selenium_driver/chromedriver_win.exe

pytest --driver Chrome --driver-path selenium_driver/chromedriver_win.exe

Please Note the chrome driver in folder "selenium_driver" must be compatible with installed chrome version


###HOW TO RUN TESTS ON DOCKER


#Pre-condition
Ensure that Docker is installed and running on your local machine


#Steps
1. Using your IDE terminal or CLI of your choice, go to the root folder 
2. Run the following command: 'docker build -t regression . (make sure the fullstop is added. Also, 'regression' can be replaced with a phrase of your choice)
3. Once the build finishes...
4. Run the following command: docker run regression 

