# Rock-Paper-Scissors

### Installation
Dependencies:
- [python](https://www.python.org/downloads/)
- [virtualenv](https://pypi.org/project/virtualenv)

Set working directory to git repository and run `pip install requirements.txt`

### Data Generation

Run *collect_data.py*, a window with camera feed will pop up. You can capture the images by pressing *Spacebar*.

<ins>Example</ins>
    
    python collect_data.py
    Please select one of the labels:
    Rock(0)
    Paper(1)
    Scissors(2)
    Your input: 1

    Paper selected!
    No. of images do you wish to capture:1
    Hit Space to Capture Image

Your collected data will be stored in the current directory under label name.
