import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse): 
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } } 
    response = requests.post(URL, json = myobj, headers=Headers)  
    return response.text  