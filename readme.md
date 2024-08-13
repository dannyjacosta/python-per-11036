**To create an environment**
`python -m venv .venv`

**To install Jupyter Notebooks**
`pip install jupyter`

**To save dependencies to a text file**
`pip freeze > packages.txt`

To **Install dependencies from a text file**
`pip install -r .\dependencies.txt`

**To start Jupyter Notebooks**
`jupyter notebook`

**To enable code autocompletion in Jupyter Notebooks**
Jupyter notebooks version 7 and higher doesn't require external extensions to enable code autocompletion.
1. Go to *Settings*
1. Select *Code Completion*
1. Check *Enable autocompletion*
1. On the left pane select *Code Mirror*
1. Check *Auto Closing Brackets*

**To Install Numpy**
`pip install numpy`




**To increase Jupyter Notebook's default rate limit**
- Option 1 - Pass parameter when loading Juypter
`jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000`
*This sets the rate limit to 10,000,000 transactions per second.*
</br>

- Option 2 - Make the change permanent in the jupyeter config file
    - `jupyter notebook --generate-config`
    - Uncoment and modify the generated config to include or update:
    - `c.ServerApp.iopub_data_rate_limit = 10000000`