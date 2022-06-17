# MLFlowInferenceFromSpark
The project describes various ways of doing MLFlow model inference(batch and streaming) using CDP Spark form factors (CML, CDE and Datahub)

### The goal of this project is to demonstrate Machine Learning Inference capabilities specifically with MLFlow models with Cloudera CDP CML(Cloudera Machine Learning - ML with Spark on K8S), CDE(Cloudera Data Engineering - Spark3 on K8S)--TBD and Datahub(Spark3 on yarn)--TBD


#### CML - Cloudera Machine Learning

##### Step-0:
1) Make sure you have a running CDP environment(AWS or Azure)
2) Create a Workspace in CDP CML (AWS or Azure)
3) Within the CML workspace, create a Project and clone this github project

#### Step-1:
1) Project artifacts explained:
 ````
    0_Setup.py -- Python script for setting up environment variables and create some required directories
    
    1_MLFlow_Tensorflow_Batch_Inference.ipynb -- Jupyter notebook for Spark batch MLFlow UDF based inference
    
    1_SparkStreaming_MLFlow_Model_Inference.ipynb -- Jupyter notebook for Spark Streaming based MLFlow UDF based inference over incoming files in either S3 bucket or ABFS container
    
    gen_files.sh -- Bash script to simulate incoming files for Spark Streaming
    
    requirements.txt -- Python dependencies required to run this project
    
    model - Model directory that hold MLFlow artifacts (The model was prebuilt for inference here)
````

#### Step-2:
1) Create a new session based on Workbench editor
2) Execute the 0_Setup.py script by running all lines
3) Stop the session
4) Create a new session based on Jupyter notebook
5) Open a terminal and execute the command ```` pip install -r requirements.txt````
6) The above command should install all the dependencies you need to run batch inference and streaming inference using Spark Streaming

#### Step-3: MLFlow model inference for batch
1) Open the 1_MLFlow_Tensorflow_Batch_Inference.ipynb notebook from the left panel.The notebook has code that generates input data
2) Execute the notebook and you should see a dataframe printed on to the console with model predictions

#### Step-4: MLFlow model inference with Spark Streaming
1) Open the 1_SparkStreaming_MLFlow_Model_Inference.ipynb notebook from the left panel.
2) Run the notebook and wait for few seconds until the kernel is idle
3) The Spark Streaming app is running and it is waiting for input files to arrive into your object store folder/container
4) Open the terminal and run the gen_files.sh script ````bash gen_files.sh 100````
5) The above command takes one input which is the number of files. You can change the number to suit to your requirements.
6) As the script is running, you can observe the Spark Streaming app from the notebook will start processing those files into the ````$STORAGE/output```` folder of your object store bucket

#### Step-5: Cleanup
1) Stop your running sessions
2) Delete your $STORAGE/tmp, $STORAGE/chkpnt and $STORAGE/output directories


## TBD
MLOps work to run this code in CDE and Datahub
