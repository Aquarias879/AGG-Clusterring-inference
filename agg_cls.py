from influxdb import DataFrameClient
import time
import pickle

model = pickle.load(open("agg.pkl", "rb"))
host = '203.64.131.98'
port = 8086
user = 'sam'
password = '12345678'
protocol='line'
dbname = 'Predicted'

client = DataFrameClient(host, port, user, password, dbname)

soil = client.query('SELECT last("value") FROM "ec_pred" WHERE time > now() - 30m GROUP BY time(1m);')
ec = client.query('SELECT last("value") FROM "ec_pred" WHERE time > now() - 30m GROUP BY time(1m);')


model.fit_predict([soil[:30],ec[:30]])
