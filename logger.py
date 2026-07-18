# DG AI Logger System

from datetime import datetime


def save_log(message):

    time = datetime.now()


    log = f"{time} : {message}\n"


    file = open("dgai_log.txt", "a")

    file.write(log)

    file.close()


    print("Log Saved")



def show_logs():

    try:

        file = open("dgai_log.txt", "r")

        data = file.read()

        file.close()


        print("===== DG AI LOGS =====")

        print(data)


    except:

        print("No logs found")
