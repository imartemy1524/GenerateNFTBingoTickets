# Generate Bingo NFT tickets 

## How to install dependencies
- On windows: 
    
    Install *python* (for example from [here](https://www.python.org/downloads/release/python-3113/))
    Run command `python -m pip install -r requirements.txt` (from current folder)
- On linux/Mac
     
    `python3 -m pip install -r requirements.txt`
## How to configure  

Edit file [tools.py](tools.py) with some text editor (for example notepad++) and configure all needed variables
 
### For example: 

`OUTPUT_FILENAME = "output/ticket_{}.png"` - output filepath. 

If you want to change it to another directory:

`OUTPUT_FILENAME = "output_prem/ticket_{}.png"`


## How to run
- On windows:

    `python main.py`

- On linux/Mac:

   `python3 main.py` 