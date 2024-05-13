import subprocess
try:
    # Run the first script
    first_process = subprocess.Popen(["python3", "/home/bagergat/Desktop/Bitirme/speed_check.py"], stderr=subprocess.PIPE)

    # Run the second script
    second_process = subprocess.Popen(["python3", "/home/bagergat/Desktop/Bitirme/graphsperminute.py"], stderr=subprocess.PIPE)

    # Check for errors in the first script
    first_stderr = first_process.communicate()[1]
    if first_stderr:
        print("Error in first script:")
        print(first_stderr.decode())

    # Check for errors in the second script
    second_stderr = second_process.communicate()[1]
    if second_stderr:
        print("Error in second script:")
        print(second_stderr.decode())

except Exception as e:
    print("Error:", e)
