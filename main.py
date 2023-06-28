import os

def create_registry_entries(name, option_name, icon, command):
    if os.path.exists(f"{name}_create.reg"):
        os.remove(f"{name}_create.reg")

    file = open(f"{name}_create.reg", "a")
    file.write(f"""Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\\*\\shell\\{name}]
@="{option_name}"
"Icon"="{icon}"

[HKEY_CLASSES_ROOT\\*\\shell\\test\\command]
@="{command}"
""")
    file.close()

    

# Call the function to create the registry entries
print("""!! ATTENTION !!
The author of this program is not responsible for your actions! You are responsible for all your actions! If you are still afraid, create a recovery point.

Press ENTER to continue""")
input()

print("Welcome to WinOptionCreator!")
name = input("Enter a name that will be displayed in regedit.exe (HKEY_CLASSES_ROOT/*/shell/{your_name}): ")
option_name = input("Enter a name that will be displayed as an item in the menu (For example: Open with Sublime Text): ")
icon = input("Enter the path to the image (it will be like an icon): ")
command = input("Enter command: ")

create_registry_entries(name, option_name, icon, command)

print(".reg file created successfully!")
os.system(f"{name}_create.reg")
print("Option created successfully! Now you need to restart your PC or end your session")
input("Press ENTER for exit...")
