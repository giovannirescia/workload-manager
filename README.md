# Workload project

This project consists in storing jobs in a database and execute them through time.

## Usage

* Python 2.7

* Conda

* SQLite

* git

## Installation instructions

`git clone git@github.com:giovannirescia/workload-manager.git`

`conda create --name workload python=2.7 ipykernel`

`pip install -r requirements.txt`

### Set up

Run the next commands from inside the project's dir, i.e., workload-manager.

1. Instantiate settings.py.template if you want to customize some paths, otherwise just run `cp settings.py.template settings.py`

2. Create a directory for the database `mkdir data`

3. Run `python scripts/populate.py` to add some Jobs to be executed (these are just test examples)

4. Set the PYTHONPATH so it can find the project's modules: `set PYTHONPATH=$PYTHONPATH:<path_to_the_project>`, eg, if your project is located in `/Users/sarunas/my_projects/workload-manager` then the PYTHONPATH setting will be `set PYTHONPATH=$PYTHONPATH:/Users/sarunas/my_projects/workload-manager`


### Usage

Just run `python scripts/worker.py` to select a queued job from the database and execute it.