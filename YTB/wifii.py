import subprocess

def check_wifi_password():
    try:
        output = subprocess.check_output("netsh wlan show profile name='Thien Nhan' key=clear", shell=True)
        output = output.decode('utf-8')
        
        if "Key Content" in output:
            start_index = output.index("Key Content") + len("Key Content") + 2
            end_index = output.index("\r", start_index)
            password = output[start_index:end_index]
            
            print("Your Wi-Fi password is:", password)
        else:
            print("Wi-Fi password not found.")
    except subprocess.CalledProcessError:
        print("Error occurred while checking Wi-Fi password.")

# Gọi hàm để kiểm tra mật khẩu Wi-Fi
check_wifi_password()
