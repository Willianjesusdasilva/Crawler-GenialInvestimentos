from core import engine,metadata
def truncate_db():

    con = engine.connect()
    trans = con.begin()
    for table in metadata.sorted_tables:
        con.execute(table.delete())
    trans.commit()
    print('Cleaned')

