import pandas as pd

class Payment():
    def  sorting(df):
        # Прочитали основной файл
        df = pd.read_csv('var5.csv')
        # Отфильтровали по признаку 'Место оплаты' со значением 'Минск'
        filtered_df = df[df['Место оплаты'].str.startswith('Минск')]
        print(filtered_df)
        # Создали отдельный файл из отфильтрованного значения
        filtered_df.to_csv('output.csv', index=False, encoding='utf-8')











