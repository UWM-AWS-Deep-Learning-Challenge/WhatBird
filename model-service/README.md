# `model-service`
The model service hosts our trained model and responds to requests from the `client-service`. 

## Setup

1. Install python.  I'm running Python 3.8.2.
2. Create a `venv` for the `model-service`. 

    Mac/Linux: 
    
    ```bash
    $ python3 -m venv <VENV_NAME>
    $ source ~/path/to/VENV_NAME/bin/activate
    ```
3. Install dependencies: 

    Mac/Linux
    ```bash
    $ cd path/to/WhatBird/model-service
    $ pip3 install requirements.txt
    ```

## Running the service locally
```bash
$ uvicorn model-service:app --reload
```

## Testing the service
Download an app like Postman for a nice gui for testing.  If you like the CLI check out `curl`.


