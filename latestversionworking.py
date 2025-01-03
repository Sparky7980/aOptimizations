import pygame
import sys
import os
import subprocess
import shutil
import ctypes

# Initialize Pygame
pygame.init()

def print_ascii_art():
    art = r'''
 
  _____ _                 _     __   __            _____            _   _     _             
 |_   _| |__   __ _ _ __ | | __ \ \ / /__  _   _  |  ___|__  _ __  | | | |___(_)_ __   __ _ 
   | | | '_ \ / _` | '_ \| |/ /  \ V / _ \| | | | | |_ / _ \| '__| | | | / __| | '_ \ / _` |
   | | | | | | (_| | | | |   <    | | (_) | |_| | |  _| (_) | |    | |_| \__ \ | | | | (_| |
   |_| |_| |_|\__,_|_| |_|_|\_\ __|_|\___/ \__,_| |_|  \___/|_|     \___/|___/_|_| |_|\__, |
    / \  _   _  __| (_)_ __    / _ \ _ __ | |_(_)_ __ ___ (_)______ _| |_(_) ___  _ __|___/ 
   / _ \| | | |/ _` | | '_ \  | | | | '_ \| __| | '_ ` _ \| |_  / _` | __| |/ _ \| '_ \/ __|
  / ___ \ |_| | (_| | | | | | | |_| | |_) | |_| | | | | | | |/ / (_| | |_| | (_) | | | \__ \
 /_/   \_\__, |\__,_|_|_| |_|  \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\__|_|\___/|_| |_|___/
         |___/                      |_|                                                     

    '''
    print(art)

print_ascii_art()

# Set up the screen and fonts
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Aydin Optimizations")
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 28)
white = (255, 255, 255)
blue = (0, 0, 255)
blue_hover = (0, 0, 200)
background_color = (30, 30, 30)

# Texts for the pages
main_text = "Thank You For Using Aydin Optimizations"

# Optimizations button names (use the exact dictionary key format)
buttons_home = ["Updates", "Settings", "Start Optimizations", "Exit"]
buttons_updates = ["Back"]
buttons_settings = ["Back"]
buttons_optimizations = [
    "Terminate Chrome", "Disable Visual Effects", "Change DNS", "Clear DNS Cache",
    "Modify Hosts File", "Disable Telemetry", "Disable Windows Defender", "Clean Temp Files", "Update Windows", "Backup Files"
]

# Corresponding keys for settings (this must match the keys used in settings.txt)
optimization_keys = {
    "Terminate Chrome": "terminate_chrome",
    "Disable Visual Effects": "disable_visual_effects",
    "Change DNS": "change_dns",
    "Clear DNS Cache": "clear_dns_cache",
    "Modify Hosts File": "modify_hosts_file",
    "Disable Telemetry": "disable_telemetry",
    "Disable Windows Defender": "disable_windows_defender",
    "Clean Temp Files": "clean_temp_files",
    "Update Windows": "update_windows",
    "Backup Files": "backup_files"
}

# Load settings from a text file or create default settings
def load_settings():
    settings = {}
    if os.path.exists("settings.txt"):
        with open("settings.txt", "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                settings[key] = value == "True"
    else:
        # Default settings
        settings = {key: True for key in optimization_keys.values()}
        save_settings(settings)
    return settings

# Save settings to a text file
def save_settings(settings):
    with open("settings.txt", "w") as file:
        for key, value in settings.items():
            file.write(f"{key}={str(value)}\n")

# Toggle a setting's value
def toggle_setting(setting, settings):
    settings[setting] = not settings[setting]  # Toggle the setting
    save_settings(settings)  # Save the new setting to the file

# Admin check and run command functions
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False

def run_as_admin(command):
    try:
        if sys.platform == "win32":
            subprocess.run(["runas", "/user:Administrator", command], check=True)
        else:
            subprocess.run(["sudo"] + command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        sys.exit(1)

# Optimization functions
def terminate_chrome():
    try:
        subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], check=True)
        print("Terminating chrome.exe")
    except subprocess.CalledProcessError:
        print("Failed to terminate chrome.exe")

def disable_visual_effects():
    try:
        subprocess.run('reg add "HKCU\\Control Panel\\Desktop" /v VisualFXSetting /t REG_DWORD /d 2 /f', shell=True, check=True)
        print("Visual effects disabled")
    except subprocess.CalledProcessError:
        print("Failed to disable visual effects")

def change_dns():
    try:
        subprocess.run('netsh interface ip set dns name="Ethernet" static 8.8.8.8', shell=True, check=True)
        subprocess.run('netsh interface ip add dns name="Ethernet" 8.8.4.4 index=2', shell=True, check=True)
        print("DNS changed to Google DNS (8.8.8.8 and 8.8.4.4)")
    except subprocess.CalledProcessError:
        print("Failed to change DNS")

def clear_dns_cache():
    try:
        subprocess.run("ipconfig /flushdns", shell=True, check=True)
        print("DNS cache cleared")
    except subprocess.CalledProcessError:
        print("Failed to clear DNS cache")

def modify_hosts_file():
    try:
        hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
        with open(hosts_path, "a") as file:
            file.write("\n# Your custom entries\n")
        print("Successfully modified hosts file")
    except PermissionError:
        print("Error optimizing host file: Access denied. Ensure the script is running as Administrator.")
    except Exception as e:
        print(f"An error occurred while modifying the hosts file: {e}")

def disable_telemetry():
    try:
        subprocess.run("sc stop DiagTrack", shell=True, check=True)
        subprocess.run("sc config DiagTrack start= disabled", shell=True, check=True)
        print("Windows telemetry and tracking services disabled.")
    except subprocess.CalledProcessError:
        print("Failed to disable telemetry services")

def disable_windows_defender():
    try:
        subprocess.run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f', shell=True, check=True)
        print("Windows Defender real-time protection disabled.")
    except subprocess.CalledProcessError:
        print("Failed to disable Windows Defender.")

def clean_temp_files():
    try:
        temp_dirs = [
            os.getenv("TEMP"),
            os.getenv("TMP"),
            "C:\\Windows\\Temp"
        ]
        for temp_dir in temp_dirs:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)
                print(f"Cleaned up temporary files in {temp_dir}")
            else:
                print(f"Temp directory {temp_dir} not found.")
    except Exception as e:
        print(f"Error cleaning temporary files: {e}")

def update_windows():
    try:
        subprocess.run("powershell -Command Start-Process 'ms-settings:windowsupdate' -Verb runAs", shell=True, check=True)
        print("Windows update launched.")
    except subprocess.CalledProcessError:
        print("Failed to launch Windows update.")

def backup_files():
    try:
        backup_path = "D:\\Backup"
        documents_path = os.path.expanduser("~\\Documents")
        if not os.path.exists(backup_path):
            os.makedirs(backup_path)
        shutil.copytree(documents_path, os.path.join(backup_path, "Documents"))
        print("Documents backed up successfully.")
    except Exception as e:
        print(f"Error backing up files: {e}")

# Run all optimizations
def run_all_optimizations(settings):
    if settings.get("terminate_chrome", False):
        terminate_chrome()
    if settings.get("disable_visual_effects", False):
        disable_visual_effects()
    if settings.get("change_dns", False):
        change_dns()
    if settings.get("clear_dns_cache", False):
        clear_dns_cache()
    if settings.get("modify_hosts_file", False):
        modify_hosts_file()
    if settings.get("disable_telemetry", False):
        disable_telemetry()
    if settings.get("disable_windows_defender", False):
        disable_windows_defender()
    if settings.get("clean_temp_files", False):
        clean_temp_files()
    if settings.get("update_windows", False):
        update_windows()
    if settings.get("backup_files", False):
        backup_files()

# Function to draw a button
def draw_button(text, x, y, width, height):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.Rect(x, y, width, height).collidepoint(mouse_x, mouse_y):
        pygame.draw.rect(screen, blue_hover, (x, y, width, height))  # Highlight when hovered
    else:
        pygame.draw.rect(screen, blue, (x, y, width, height))  # Normal button color

    text_surface = button_font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)
    return pygame.Rect(x, y, width, height)

# Main loop
current_page = "home"
running = True
settings = load_settings()  # Load settings at the beginning

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if current_page == "home":
                for button in buttons_home:
                    button_rect = draw_button(button, 300, 250 + buttons_home.index(button) * 70, 200, 50)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        if button == "Updates":
                            current_page = "updates"
                        elif button == "Settings":
                            current_page = "settings"
                        elif button == "Exit":
                            running = False
                        elif button == "Start Optimizations":
                            run_all_optimizations(settings)  # Run all optimizations

            elif current_page == "updates":
                # Place "Back" button in the top-right corner
                button_rect = draw_button("Back", 600, 10, 150, 50)
                if button_rect.collidepoint(mouse_x, mouse_y):
                    current_page = "home"

            elif current_page == "settings":
                # Place "Back" button in the top-right corner
                button_rect = draw_button("Back", 600, 10, 150, 50)
                if button_rect.collidepoint(mouse_x, mouse_y):
                    current_page = "home"

                for optimization in buttons_optimizations:
                    button_rect = draw_button(f"{optimization} [{'ON' if settings[optimization_keys[optimization]] else 'OFF'}]", 
                                              100, 200 + buttons_optimizations.index(optimization) * 60, 600, 50)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        setting_key = optimization_keys[optimization]
                        toggle_setting(setting_key, settings)  # Toggle setting when clicked

    screen.fill(background_color)

    if current_page == "home":
        header_text = font.render(main_text, True, white)
        header_rect = header_text.get_rect(center=(400, 100))
        screen.blit(header_text, header_rect)

        for button in buttons_home:
            button_rect = draw_button(button, 300, 250 + buttons_home.index(button) * 70, 200, 50)

    elif current_page == "updates":
        header_text = font.render("Updates", True, white)
        header_rect = header_text.get_rect(center=(400, 100))
        screen.blit(header_text, header_rect)

    elif current_page == "settings":
        header_text = font.render("Settings", True, white)
        header_rect = header_text.get_rect(center=(400, 100))
        screen.blit(header_text, header_rect)
        for optimization in buttons_optimizations:
            status = "ON" if settings[optimization_keys[optimization]] else "OFF"
            button_rect = draw_button(f"{optimization} [{status}]", 100, 200 + buttons_optimizations.index(optimization) * 60, 600, 50)
            draw_button("Back", 600, 10, 150, 50)

        

    pygame.display.flip()

pygame.quit()
sys.exit()
