import subprocess

# Retrieve all Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = data.decode('utf-8').split('\n')

# Extract profile names
profiles = [profile.split(":")[1][1:-1] for profile in data if "All User Profile" in profile]

# Print header
print("{:<20} {:}".format('Wi-Fi Names', 'Passwords'))

# Retrieve and print passwords for each profile
for profile in profiles:
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'])
        data = data.decode('utf-8').split('\n')
        passwords = [passw.split(":")[1][1:-1] for passw in data if "Key Content" in passw]
        print("{:<20} {:}".format(profile, passwords[0]))
    except (IndexError, subprocess.CalledProcessError):
        print("{:<20} {:}".format(profile, ""))