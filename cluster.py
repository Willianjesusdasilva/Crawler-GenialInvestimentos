import pandas as pd
from core import engine
from sklearn.cluster import KMeans
import numpy as np
import os

class Cluster():
    def cluster_data():

        df = pd.read_sql_table("fundos",engine)

        kmeans = KMeans(n_clusters=15, random_state=0)

        X = np.array(df.loc[:, ['TwelveMonths']])

        kmeans.fit(X)

        df['K-classes'] = kmeans.labels_


        html = df.loc[:, ['AssetManagerName','TwelveMonths','K-classes']].sort_values(by=['K-classes']).to_html(classes='table table-striped table-hover')


        text_file = open("index.html", "w")
        text_file.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
        text_file.write(html)
        text_file.close()
        os.startfile('index.html')
