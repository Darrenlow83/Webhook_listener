# Webhook_listener

Dependency: python 3, ngrok, git

***Install python 3***
If you have programming background, just install python 3 using homebrew. Otherwise you can download the python 3 installer from https://www.python.org/downloads/
Run `python3 --version` to check your python version

***Install git***
The easiest is probably to install the Xcode Command Line Tools. Run `git --version` command and if you don’t have it installed, it will prompt you to install it. Alternatively you can download the git installer from https://git-scm.com/download/mac

***Install ngrok and setup webhook url***
Sign up an account on ngrok, download the installer from https://ngrok.com/download and install ngrok on your device:
1. Unzip the zip folder and run `./ngrok --version` (in the same directory) to ensure it is properly installed
2. Go to https://dashboard.ngrok.com/auth, copy your authtoken and run the following command:
`./ngrok authtoken [YOUR AUTHTOKEN]`
3. To start a HTTP tunnel, run this next:
`./ngrok http [PORT]`
*You should use the same port later for your webhook listener script
4. Update the webhook url in the developer dashboard Settings to the one displayed in your ngrok terminal. e.g.
`https://75d8cfca.ngrok.io`
*Please use the one with https
5. You can see the requests logs via the ngrok inspector (Visit http://localhost:4040 in your browser)

***Setup python environment and app***

1. Install pip 
`sudo easy_install pip`

2. Install virtualenv
`pip3 install virtualenv`
Run `pip3 --version` to check if pip3 is installed

3. Go to your workplace folder and clone the webhook project folder from Github
`cd my-project`
`git clone https://github.com/Darrenlow83/Webhook_listener.git`

4. Go to the project folder and setup virtualenv 
`cd Webhook_listener/`
`virtualenv venv`

5. In the project folder, run the following command to activate the virtual environment
`source venv/bin/activate`
To deactivate the virtual environment, run:
`deactivate`

6. Once virtual environment is up, run the following command to start the webhook listener
`./app.py -s [YOUR DEV SECRET KEY] -c [CLIENT ID] -p [PORT]`
*Press `control + c` to terminate the webhook listener service

7. The webhook listner is ready for use now.
