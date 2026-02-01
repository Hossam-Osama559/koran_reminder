# koran_reminder

A  Python application to send a WhatsApp message for each "premier league match".  


## Features
sending a whatsapp message every day at 12pm with the premier league matches of this day 

at each match time sending a whatsapp message 





## Prerequisites
- Python 3.8+ (recommended)
- pip
- free twilo sandbox with your whatsapp number 

## Quick start (local)
1. Clone the repository:
   git clone https://github.com/Hossam-Osama559/koran_reminder.git
   cd koran_reminder

2. Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux


3. Install dependencies:
   pip install -r requirements.txt


4. Add configuration (see below) and run the script:
   python main.py

## Configuration
this project expects a configuration via the .env file at the root of the project dir 
containing the filed of the twilo sandbox and your phone number 
see .env.template for more details 


## limitations:
this program will run only on linux machines because it uses the timerfd syscalls of linux 






