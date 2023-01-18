# Why?
This is a toy project for IITM PALS TechSpeaks Session 2023 on ChatGPT.
This is mainly for demonstration purposes since ChatGPT is down due to heavy traffic.

# How to use
Copy and paste these commands after substituting your api key!

``` bash
git clone https://github.com/bakageddy/chatgpt.git
cd chatgpt
python3 -m pip install virtualenv
virtualenv .
export API_KEY=<your-api-key>
source ./bin/activate
python3 -m pip install openai
python3 chatgpt/main.py
```
