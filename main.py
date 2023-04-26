import json
import time
from typing import List
import threading
from config import *
from tools import generate_ticket_array, generate_ticket_image, generate_metadata

success_count = 0
# Define function to generate a single ticket
def generate_single_ticket(i: int):
    global success_count
    # Generate random numbers for ticket
    numbers = generate_ticket_array()

    ticket = generate_ticket_image(images, layout, numbers)
    ticket.save(OUTPUT_FILENAME.format(i))
    # save metadata
    metadata = generate_metadata(numbers)
    with open(OUTPUT_FILENAME.format(i).split('.')[0]+".json", 'w') as f:
        json.dump(metadata, f)

    success_count += 1
# If we will encode them one by one it will take a while, so lets create a single Thread for each ticket
print(f"Generating {NUM_TICKETS} tickets...\nIt may take some time, please be patient!")
threads = [threading.Thread(target=generate_single_ticket, args=(i+1, )) for i in range(NUM_TICKETS)]
for i in threads: i.start()
while success_count < NUM_TICKETS:
    finished_count = sum(i.is_alive() for i in threads)
    print(f"Progress: {success_count} / {NUM_TICKETS}")
    time.sleep(0.5)
for i in threads: i.join()

print("Finished generating tickets")

