from sqlalchemy import create_engine, insert, select, MetaData, Table, Column, String, Integer, Float, Boolean
# constans
ENGINE = create_engine('sqlite:///stock_price_db.sqlite')
METADATA = MetaData()


class Sqlite:
    # constructor
    def __init__(self, engine=ENGINE, metadata=METADATA, set50_table=None):
        # create the engine and metadata attributes
        self.engine = engine
        self.metadata = metadata
        self.set50_table = Table('set50_index', metadata,
                                 Column('date_', String(255), unique=False),
                                 Column('high', Integer()),
                                 Column('low', Float()),
                                 Column('open', Float()),
                                 Column('close', Float()),
                                 Column('volume', Integer()),
                                 Column('adj_close', Float())
                                 )

    def create_set50(self):
        # use the metadata to create the table
        result = self.metadata.create_all(self.engine)
        return result

    def insert_set50(self, set50_list):
        # build insert statement: stmt
        stmt = insert(self.set50_table)
        # use values_list to insert data: insert_res
        result = self.engine.execute(stmt, set50_list)
        return result

    def select_set50(self):
        get_set50 = Table('set50_index', self.metadata,
                          autoload=True, autoload_with=self.engine)
        # select statement for set50 table: stmt
        stmt = select([get_set50])
        # execute the statement on connection and fetch 10 records: result
        result = self.engine.execute(stmt).fetchmany(size=10)
        return result
