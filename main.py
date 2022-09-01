from src.cria_data_frame import CriaDataFrame

file_path = 'file.xlsx'
data_frame = CriaDataFrame()
df = data_frame.cria_data_frame(file_path=file_path)
print(df)