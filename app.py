from flask import Flask
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Kaluri Himabindhu"  # Your Full Name
    username = os.getlogin()     # System Username
    
    # IST Time
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
    
    # 'top' Command Output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error fetching top output: {e}"
    
    return f"""
    <h2>Name: {name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {current_time}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

