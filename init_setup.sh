echo [$(date)]: "START"
echo [$(date)]: "Creating the virtual environment with python 3.7 Version"
conda create --prefix ./object_detection_env python=3.7 -y
echo [$(date)]: "Successfully Created the virtual environment name is ./object_detection_env"
source activate ./object_detection_env
echo [$(date)]: "Successfully Activated the virtual environment"
echo [$(date)]: "Installing the dev requirements"
pip install -r requirements.txt
echo [$(date)]: "Successfully installed the requirements"
echo [$(date)]: "END"