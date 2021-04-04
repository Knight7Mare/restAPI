from kafka import KafkaConsumer
import json
import psycopg2

consumer = KafkaConsumer("OmersTopic",bootstrap_servers="kafka:9093",
                                            value_deserializer=lambda m: json.loads(m.decode('utf-8')))


conn = psycopg2.connect(dbname='restfulapiDB', user='postgres', password='omer', host='postgredb')


cur = conn.cursor()
for msg in consumer:
    print (msg.value)
    print (msg.value["method"])
    cur.execute("INSERT INTO cekilenler(method,delay,timestamp) VALUES (%s,%s,%s);", (msg.value["method"],msg.value["delay"],str(msg.value["timestamp"])))
    conn.commit()

conn.close()