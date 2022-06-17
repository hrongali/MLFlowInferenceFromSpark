import pandas as pd
import onnx
import onnxruntime
import json
import numpy as np

# For testing only data

features = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]

args = {"0":1.0,"1":1.0,"2":1.0,"3":1.0,"4":1.0,"5":1.0,"6":1.0,"7":1.0,"8":1.0,"9":1.0,"10":1.0,"11":1.0,"12":1.0,"13":1.0,"14":1.0,"15":1.0,"16":1.0,"17":1.0,"18":1.0,"19":1.0,"20":1.0,"21":1.0,"22":1.0,"23":1.0,"24":1.0}

model_path = onnx.load("/home/cdsw/cvsmodel/model.onnx").SerializeToString()

def predictFunc(args):
    #Load data
    filtArgs = {key: [args[key]] for key in features}
    data = pd.DataFrame.from_dict(filtArgs)
    
    #Load model
    #predict = mlflow.pyfunc.spark_udf(spark, "/home/cdsw/cvsmodel")
    #model = mlflow.onnx.load_model("/home/cdsw/cvsmodel")
    so = onnxruntime.SessionOptions()
    so.add_session_config_entry('model.onnx', 'ONNX')
    #session =onnxruntime.InferenceSession('/home/cdsw/cvsmodel/model.onnx',None)
    session =onnxruntime.InferenceSession(model_path,None)

    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name
    #print(input_name)
    #print(output_name)
    args_list=[[*args.values()]]
    #print(args_list)
    data=json.dumps({'domain_tokens' : args_list})
    data=np.array(json.loads(data)['domain_tokens']).astype('float32')
    #print(data)
    result = session.run([output_name], {input_name: data})
    prediction=np.array(result).squeeze()
    #print(np.array(result).squeeze())
    #print(type(prediction))
    #print(np.array(result).squeeze())
    
    return float(prediction)

#print(predictFunc(args))