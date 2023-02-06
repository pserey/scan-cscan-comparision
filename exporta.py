import pandas as pd

def export_table(cscan, scan, input_size):
    data = {'CSCAN': [cscan], 'SCAN': [scan], 'INPUT SIZE': [input_size]}
    df = pd.DataFrame(data, columns=['CSCAN', 'SCAN', 'INPUT SIZE'])
    return df

cscan = float(input("Entre com o valor do CSCAN: "))
scan = float(input("Entre com o valor do SCAN: "))
input_size = float(input("Entre com o valor do INPUT SIZE: "))

result = export_table(cscan, scan, input_size)
result.to_csv("tabela.tsv", mode='a',index=False, sep='\t')

print("Tabela salva com sucesso como tabela.csv")