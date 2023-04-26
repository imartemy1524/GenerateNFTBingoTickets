import secrets
from typing import List
from PIL import Image
from config import TICKET_WIDTH, TICKET_HEIGHT, CELLS_X, CELLS_Y
import threading
#Threading lock - Pillow is not threadsafe library
lock = threading.Lock()


def generate_ticket_array() -> list[int]:
    arr = []
    for i in range(8):
        numb = secrets.randbelow(50) + 1
        while numb in arr:
            numb = secrets.randbelow(50) + 1
        arr.append(numb)
    return arr

def generate_ticket_image(images: List[Image.Image], layout: Image.Image, numbers: List[int]) -> Image.Image:
    # Create new blank image for ticket
    ticket = Image.new("RGBA", (TICKET_WIDTH, TICKET_HEIGHT), color="white")

    # Paste layout onto ticket
    with lock:
        ticket.paste(layout, (0, 0))


    # Paste images onto cells on ticket
    for i, number in enumerate(numbers):
        if i >= 4: i = i+1
        # Get image for number
        number_image = images[number-1]
        with lock:
            number_image = number_image.copy()
        # Calculate cell position
        cell_x = CELLS_X[i%3]
        cell_y = CELLS_Y[i//3]

        # Paste image onto ticket
        mask = number_image.getchannel("A")

        # Paste image onto ticket with mask
        ticket.paste(number_image, (cell_x, cell_y), mask)


        # ticket.paste(number_image, (cell_x, cell_y))

    return ticket

def generate_metadata(numbers: List[int]):
    metadata = {
        'attributes': [
            {
                'trait_type': 'Numbers',
                'value': ",".join(map(str, numbers)),
            }
        ]
    }

    return metadata

