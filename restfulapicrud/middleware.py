import logging
import time
import random
from kafka import KafkaProducer
import json



logger = logging.getLogger(__name__)

class RequestLogger1:
    def __init__(self, get_response):
        self.producer = KafkaProducer(bootstrap_servers=['kafka:9093'],value_serializer=lambda m: json.dumps(m).encode('utf-8'))
        
        self.get_response = get_response
        logging.basicConfig(level=logging.INFO, filename='requests.log',filemode="w")
    
    def __call__(self, request):
        rd = random.randint(1,3000)/1000
        timep = time.time()
        time.sleep(rd)

        response = self.get_response(request)
        logging.info(request.method+ ',' + str(rd) + ',' + str(int(timep)))
        log = {"method":request.method,"delay":str(rd),"timestamp":int(timep)}
        self.producer.send('OmersTopic', log)
        print(request.method)


        return response
        

    