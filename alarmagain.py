from playsound import playsound
import datetime
import time

# Function to play the selected ringtone
def play_selected_ringtone():
    playsound(ringtones[choice])

# Function to handle the snooze feature
def snooze():
    print("Snoozing for 5 minutes...")
    time.sleep(5 * 60)  # Snooze for 5 minutes
    print("Waking up again...")
    while True:
        now = datetime.datetime.now()
        if aHour == now.hour and aMin == now.minute:
            print("Playing...")
            play_selected_ringtone()
            break
        time.sleep(1)

# Get alarm settings from user
aHour = int(input("Enter Hours: "))
aMin = int(input("Enter Minutes: "))
aAMPM = input("AM/PM: ").strip().upper()

# Adjust hours based on AM/PM
if aAMPM == "PM" and aHour != 12:
    aHour += 12
elif aAMPM == "AM" and aHour == 12:
    aHour = 0

# Provide ringtone options to the user
print("Select a ringtone:")
print("1. Ringtone 1")
print("2. Ringtone 2")
print("3. Ringtone 3")

# Get user choice for ringtone
choice = int(input("Enter the number of your choice: "))

# Map choices to ringtone file paths
ringtones = {
    1: "C:/Users/nkbla/OneDrive/Desktop/Pinnacle Labs/Python/Alarm/alarm1.mp3",
    2: "C:/Users/nkbla/OneDrive/Desktop/Pinnacle Labs/Python/Alarm/alarm2.mp3",
    3: "C:/Users/nkbla/OneDrive/Desktop/Pinnacle Labs/Python/Alarm/alarm3.mp3"
}

# Check if the choice is valid
if choice not in ringtones:
    print("Invalid choice.")
    exit()

# Main alarm loop
while True:
    now = datetime.datetime.now()
    if aHour == now.hour and aMin == now.minute:
        print("Playing...")
        play_selected_ringtone()
        snooze_option = input("Snooze? (yes/no): ").strip().lower()
        if snooze_option == "yes":
            snooze()
        else:
            break
    time.sleep(1)
