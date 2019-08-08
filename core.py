from sqlalchemy import (create_engine, MetaData, Column,
						Table, Integer, String, Float , DateTime)


engine = create_engine('sqlite:///data.db', echo=False)

metadata = MetaData(bind=engine)

data_fundos = Table('fundos', metadata,
					Column('id', Integer, primary_key=True),
					Column('FundAdministrationFeeName', String),
					Column('FundPerformanceFeeName', String),
					Column('RiskProfileName', String),
					Column('FundIncomeTaxClassificationName', String),
					Column('AMBIMAClassificationName', String),
					Column('CVMClassificationName', String),
					Column('FinancialInstrumentDrupalURL', String),
					Column('SettlementIsotopeFilterClass', String),
					Column('InitialValueIsotopeFilterClass', String),
					Column('InceptionAverage', Float),
					Column('TimeLimitForFundFinancialTransactionRequest', String),
					Column('FinancialInstrumentFundStatusId', Integer),
					Column('IsQualifiedInvestorOnly', String),
					Column('ClosedToApplicationDescription', String),
					Column('CorporateTaxpayerRegistry', String),
					Column('BenchmarkName', String),
					Column('ShareholderAmount', String),
					Column('AvarageAUMTwelveMonths', Float),
					Column('ShareSettlementRedemptionDescription', String),
					Column('FinancialInstrumentId', Integer),
					Column('Description', String),
					Column('FinancialInstrumentName', String),
					Column('Rating', String),
					Column('IssuanceDate', String),
					Column('FinancialInstrumentTypeName', String),
					Column('ShowProfitabilityDetail', Integer),
					Column('isExclusivo', String),
					Column('Day', Float),
					Column('Year', Float),
					Column('TwelveMonths', Float),
					Column('Inception', Float),
					Column('AssetManagerName', String),
					Column('LogoPath', String),
					Column('FinancialInstrumentFundId', Integer),
					Column('MinimumParticipationAmount', Integer),
					Column('Month', Float),
					Column('isFavorito', String),
					Column('HasOrder', Integer))





