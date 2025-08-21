import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('DataAnalyst.csv')
def make_size(size):
    if size == '-1':
        return -1
    else:
        x = size.split()
        if len(x) == 4:
            size = x[2]
            return float(size)
        elif len(x) == 2:
            size = x[0]
            size = size.replace('+', '')
            return float(size)
def make_data(data):
    if 'Senior' in data:
        return 'Senior'
    elif 'Junior' in data:
        return 'Junior'
    elif 'Lead' in data:
        return 'Lead'
    else:
        return 'Data Analyst'

df.info()
# (Отфильтровали) что бы использовать команды раз коментите две строчки снизу
df['Size'] = df['Size'].apply(make_size)
df['Job Title'] = df['Job Title'].apply(make_data)
# Первая теория: в связи с обвалом фондовых рынков в 2008 году, компании начали больше всего нуждаться в людях с умениями обычного Data Analyst(а) - ПРАВДА!!!
# (Кол-во вакантий на дата аналиста в компаниях основаных до 2008г. - 1125)
# print(df[df['Founded']< 2008]['Job Title'].value_counts())
# (Кол-во вакансий на  дата аналитика 2007 года - 31)
# print(df[df['Founded']== 2007]['Company Name'].value_counts())
# (Кол-во вакансий на дата аналитика в 2008 году - 80)
# print(df[df['Founded']== 2008]['Company Name'].value_counts()) 
# (Кол-во вакансий на дата аналитика в 2009 году - 17)
# print(df[df['Founded']== 2009]['Company Name'].value_counts())
# (Круговая диаграмма к первой теории)
# s = df[(df['Founded']>=2005)&(df['Founded']<=2010)]['Founded'].value_counts()
# s.plot(kind = 'pie')
# plt.show()

# Вторая теория: Сеньёров в больших компаниях (10000+) ищут чаще чем в маленьких компаниях (меньше 10000) - ВЕРНО!!!
# (Кол-во вакансий больших компаний (10000+) на должность сеньёра - 74 )
# print(df[(df['Size']>= 10000)&(df['Job Title']== 'Senior')])
# (Кол-во вакансий маленьких компаний (меньше 10000) на должность сеньёра - 204 )
# print(df[(df['Size']< 10000)&(df['Job Title']== 'Senior')])
# (Кол-во запросов от больших компаний (10000+) - 472)
# print(df[df['Size']>= 10000])
# (Кол-во запросов от маленьких компаний (меньше 10000) - 1739)
# print(df[df['Size']< 10000])
# (Кол-во больших компаний (10000+) - 267)
# print(df[df['Size']>= 10000]['Company Name'].value_counts())
# (Кол-во маленьких компаний (меньше 10000) - 1210)
# print(df[df['Size']< 10000]['Company Name'].value_counts())
# (Процент запросов на вакансию сеньёра из общего кол-ва у больших компаний (10000+) - 15.7% )
# (Процент запросов на вакансию сеньёра из общего кол-ва у маленькиз компаний (меньше 10000) - 11.7% )
# (Кол-во вакансий в больших компаниях (10000+) на место Junior программитсов)
# print(df[(df['Size']>= 10000)&(df['Job Title']== 'Junior')])
# (Круговая диаграмма с кол-вом вакансий по уровню в крупных компаниях (10000+))
# s = df[df['Size']>= 10000]['Job Title'].value_counts()
# s.plot(kind = 'pie')
# plt.show()
# (Круговая диаграмма с кол-вом вакансий по уровню в маленьких компаниях(меньше 10000))
# s = df[df['Size']< 10000]['Job Title'].value_counts()
# s.plot(kind = 'pie')
# plt.show()
