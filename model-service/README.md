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

    Windows (powershell):

    ```ps
    PS C:\dev\venv> python -m venv WhatBird-model-service
    PS C:\dev\venv> .\WhatBird-model-service\Scripts\activate
    (WhatBird-model-service) PS C:\dev\venv>PS C:\path\to\dir> 
    ```
3. Install dependencies: 

    Mac/Linux
    ```bash
    $ cd path/to/WhatBird/model-service
    $ pip3 install requirements.txt
    ```

    Windows (powershell):
    ```ps
    PS C:\> cd C:\path\to\WhatBird\model-service
    PS C:\WhatBird\model-service> pip3 install -r requirements-windows.txt

    ```

## Running the service locally
```bash
$ uvicorn model-service:app --reload
```

## Testing the service
Download an app like Postman for a nice gui for testing.  If you like the CLI check out `curl`.


