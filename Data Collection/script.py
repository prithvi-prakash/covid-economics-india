import cli
import subprocess
from IPython.display import clear_output
import datetime
since = datetime.date(2019, 1, 1)
delta = datetime.timedelta(days=1)
stop_date = datetime.date(2022, 8, 31)


cities = ["Mumbai", "Delhi", "Kolkata", "Chennai", "Bangalore", "Hyderabad"]

def updateStatus(start, end):
    f = open("./data/status.txt", "w")
    f.write(f"Collected for {start}, {end}")
    f.close()


while since <= stop_date:
    clear_output(wait=True)
    until = since + delta
    start = f"{since.strftime('%Y-%m-%d')}"
    end = f"{until.strftime('%Y-%m-%d')}"
    print(f"--since {start} --until {end}")
    for city in cities:
        command = f'python cli.py --since {start} --until {end} --limit 10 --near {city} -o ./data/{city}/{start}.csv --csv'
        subprocess.run(command, shell=True)
    updateStatus(start, end)
    since += delta
