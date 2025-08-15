# Install 
```bash
mkdir -p $HOME/my_repos/ && \
cd $HOME/my_repos/ && \
git clone https://github.com/rb1hdb/RB_list_subsidiaries.git && \
cd RB_list_subsidiaries && \
python3 -m venv venv && \
source venv/bin/activate && \
pip install --upgrade pip && \
deactivate && \
cd .."  
```

# Usage
```bash
cd $HOME/my_repos/RB_list_subsidiaries
source venv/bin/activate
python list_subsidiaries.py $YOUR_API_KEY <TICKER>
deactivate
```

# wrapper 
- save as `$HOME/my_web_scripts/wrapper_list_subsidiaries`
```bash
#!/bin/bash

source "$HOME/my_repos/RB_list_subsidiaries/venv/bin/activate"
python3 "$HOME/my_repos/RB_list_subsidiaries/RB_list_subsidiaries.py" "$@"
STATUS=$?
deactivate
exit $STATUS
```

## Usage
```bash
wrapper_list_subsidiaries $YOUR_API_KEY <TICKER>
```
