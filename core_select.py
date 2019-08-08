from sqlalchemy import select
from core import data_fundos

data_select = select([data_fundos])

for row in data_select.execute():
	print(row)