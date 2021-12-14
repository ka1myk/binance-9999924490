import subprocess

# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/virtualenv/
python_bin = "/home/pi/Downloads/Binance-volatility-trading-bot-main/venv/bin"

# Path to the script that must run under the virtualenv
script_file = "/home/pi/Downloads/Binance-volatility-trading-bot-main/start.py"

subprocess.Popen([python_bin, script_file])