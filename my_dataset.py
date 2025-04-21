import pandas as pd
class Payment():
    def __init__(self):
        pass
    def  sorting(self):
        # Прочитали основной файл
        df = pd.read_csv('var5.csv')
        # Разделение датасета на два датасета по признаку
        filtered1_df = df[df['Место оплаты'] == 'Минск']
        filtered2_df = df[df['Место оплаты'] != 'Минск']
        print(filtered1_df)
        print(filtered2_df)
        # Создали отдельный файл из отфильтрованного значения
        filtered1_df.to_csv('output.csv', index=False, encoding='utf-8')
        filtered2_df.to_csv('output.csv', index=False, encoding='utf-8')



        # Создание полиморфизма унарного оператора для удаления дубликатов
        #  и выведения количества удаленных дубликатов
        num_duplicates = df.duplicated().sum
        df.drop_duplicates()
        print('Количество повторяющихся строк в наборе:',num_duplicates)


        #Создаем функцию main
        def main():
            payment = Payment()
            payment.sorting()

        if __name__=="__main__":
            main()





    












