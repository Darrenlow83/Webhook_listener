# Webhook_listener

Dependencies: python 3, ngrok, git

***Install python 3***

If you have some programming backgrounds, you can install python 3 using homebrew, otherwise you can download the installer from https://www.python.org/downloads/

Run `python3 --version` to check your python version

***Install git***

The easiest way is probably to install the Xcode Command Line Tools. Run `git --version` command and if you don’t have it installed, it will prompt you to install it. Alternatively you can download the installer from https://git-scm.com/download/mac

***Install ngrok and setup webhook url***

Sign up an account on ngrok, download the installer from https://ngrok.com/download and install ngrok on your device:

1. Unzip the zip folder and run `./ngrok --version` (in the same directory) to ensure it is properly installed
2. Go to https://dashboard.ngrok.com/auth, copy your authtoken and run the following command:
`./ngrok authtoken [YOUR AUTHTOKEN]`
3. To start a HTTP tunnel, run this next:
`./ngrok http [PORT]`
(Please always use a higher port such as 5000 or above so you won't need sudo privileges, the same port should be used for your webhook listener script later)
4. Update the webhook url in the developer dashboard Settings to the one displayed in your ngrok terminal. e.g.
`https://75d8cfca.ngrok.io/webhook`
(Please use the one with https and add /webhook at the back of the url)
5. You can see the requests logs via the ngrok inspector (Visit http://localhost:4040 in your browser)

***Setup python environment and app***

1. Install pip 
`sudo easy_install pip`

2. Install virtualenv
`pip3 install virtualenv`
Run `pip3 --version` to check if pip3 is installed

3. Go to your workplace folder and clone the webhook project folder from Github
`cd my-workplace`
`git clone https://github.com/Darrenlow83/Webhook_listener.git`

4. Go to the project folder and setup virtualenv 
`cd Webhook_listener/`
`virtualenv venv`

5. In the project folder, run the following command to activate the virtual environment
`source venv/bin/activate`
To deactivate the virtual environment, run:
`deactivate`

6. Run `pip install -r requirements.txt` to install the project dependencies

7. Once dependencies are all installed, run the following command to start the webhook listener
`./app.py -s [YOUR DEV SECRET KEY] -c [CLIENT ID] -p [PORT]`
(Please use the same port you are using for ngrok)
Press `control + c` if you want to terminate the webhook listener service

8. The webhook listner is ready for use now.
