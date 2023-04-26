from PIL import Image
# Define ticket size and cell positions
TICKET_WIDTH, TICKET_HEIGHT = 2000, 2000
CELL_WIDTH, CELL_HEIGHT = 140, 140
CELLS_X = [390, 530, 680]
CELLS_Y = [785, 925, 1075]
# Load layout image
layout = Image.open("tickets/classic.jpg")
# Generate NUM_TICKETS tickets and save to output folder
NUM_TICKETS = 200
OUTPUT_FILENAME = "output/ticket_{}.png"

# Load images from folder
NUM_IMAGES = 50
images: 'list[Image.Image]' = [Image.open("images/{}.png".format(i)).resize((CELL_WIDTH, CELL_HEIGHT)) for i in range(1, NUM_IMAGES+1)]
