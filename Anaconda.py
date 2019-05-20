Anaconda


// #Installation

conda create --name tf-lina

// #Now activate the environment, (I'll show my full terminal prompt and output instead of just the commands)

source activate tf-lina

// #Lets install TensorFlow with GPU acceleration and all of the dependencies.

conda install tensorflow

// #Create a Jupyter Notebook Kernel for the TensorFlow Environment

conda install ipykernel

// #Now create the Jupyter kernel
python -m ipykernel install --user --name tf-lina --display-name "TensorFlow-LINCHEN"


// # Install new packages: 
conda install matplotlib
conda install keras


