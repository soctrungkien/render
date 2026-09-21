import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()

if __name__ == "__main__":
    # Khởi động web server cho Render nhận diện port
    keep_alive()
    print("Web server started successfully.")

    # Đặt code chạy bot chính của bạn ở đây
    # Ví dụ: import bot_main_file hoặc chạy vòng lặp bất tử
    print("Bot is running...")
    
    # Vòng lặp giữ process không bị tắt
    import time
    while True:
        time.sleep(3600)
