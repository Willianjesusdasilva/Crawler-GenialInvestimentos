import requests
import re
import json
from core import data_fundos,engine,metadata
from bs4 import BeautifulSoup
from core_reset import truncate_db
from cluster import *

metadata.create_all()
truncate_db()

page = requests.get('https://www.genialinvestimentos.com.br/investimentos/fundos/lista-completa/')

soup = BeautifulSoup(page.content,'html.parser')

list_script = soup.find_all('script')

pattern_array = re.compile("var arrayFundosLista=\[(.*?)\]")


for i in list_script:

    if pattern_array.findall(str(i)) == []:
        pass
    else:
        string_json = str(i).replace('<script>','').replace('</script>','').replace('var arrayFundosLista=','').replace('[','').replace(']','').replace('},{','}<cut-here>{')
        break


cut_string_json = string_json.split('<cut-here>')

for cut in cut_string_json:

	json_data = json.loads(cut)

	conn = engine.connect()

	conn.execute(data_fundos.insert(), json_data)


cluster = Cluster.cluster_data()