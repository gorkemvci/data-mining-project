import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Veri seti okundu
data = pd.read_csv('ds_salaries.csv')


#Veri seti Dataframe olarak dönüştürüldü
df = pd.DataFrame(data)



#---------------En çok tercih edilen 10 meslek--------------------------

# En çok tekrar eden ilk 10 meslek ve sayısı
top_10_jobs = df['job_title'].value_counts().nlargest(10)


colors = plt.cm.get_cmap('tab10', len(top_10_jobs))

# Çubuk grafiği
plt.figure(figsize=(12, 6))
bars = plt.bar(top_10_jobs.index, top_10_jobs.values, color=colors(np.arange(len(top_10_jobs))))
plt.xlabel('Job Title')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Job Titles and Their Frequencies')
plt.xticks(rotation=45)
plt.tight_layout()

# Çubukların üzerine değerleri yazdırmak için
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', fontsize=8)


plt.show()

#---------------En çok tercih edilen 10 mesleğin ortalama maaşları--------------------------

#En çok tekrar eden 10 meslek
top_10_jobs = df['job_title'].value_counts().nlargest(10).index

# En çok tekrar eden 10 mesleğin ortalama maaşlarını hesaplayalım
avg_salary_by_top_jobs = df[df['job_title'].isin(top_10_jobs)].groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)

colors = plt.cm.get_cmap('tab10', len(avg_salary_by_top_jobs))

# Çubuk grafiği
plt.figure(figsize=(12, 6))
bars = plt.bar(avg_salary_by_top_jobs.index, avg_salary_by_top_jobs, color=colors(np.arange(len(avg_salary_by_top_jobs))))
plt.xlabel('Job Title')
plt.ylabel('Average Salary')
plt.title('Top 10 Most Common Job Titles by Average Salary')
plt.xticks(rotation=45)
plt.tight_layout()

# Değerler
legend_colors = [plt.Rectangle((0,0),1,1, color=colors(i)) for i in range(len(avg_salary_by_top_jobs))]
plt.legend(legend_colors, avg_salary_by_top_jobs.index, loc='upper left')


plt.show()


#---------------Şirketlerin Konumu (En çok tekrar eden Ülkeler)-----------------------------

# En çok tekrar eden ilk 10 ülkeyi ve tekrar sayısı
top_10_countries = df['company_location'].value_counts().nlargest(10)


colors = plt.cm.get_cmap('tab10', len(top_10_countries))

# Çubuk grafiği
plt.figure(figsize=(12, 6))
bars = plt.bar(top_10_countries.index, top_10_countries.values, color=colors(np.arange(len(top_10_countries))))
plt.xlabel('Country')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Company Locations')
plt.xticks(rotation=45)
plt.tight_layout()

# Çubukların üzerine değerlerin eklenmesi
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', fontsize=8)


plt.show()

#---------------Şirketlerin Konumu(En çok tekrar eden Ülkeler) -----------------------------

# En çok tekrar eden ilk 10 ülke ve tekrar sayısı
top_10_emp_countries = df['employee_residence'].value_counts().nlargest(10)


colors = plt.cm.get_cmap('tab10', len(top_10_emp_countries))

# Çubuk grafiği
plt.figure(figsize=(12, 6))
bars = plt.bar(top_10_emp_countries.index, top_10_emp_countries.values, color=colors(np.arange(len(top_10_emp_countries))))
plt.xlabel('Employee Country')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Employee Locations')
plt.xticks(rotation=45)
plt.tight_layout()

# Çubukların üzerine değerlin eklenmesi
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', fontsize=8)


plt.show()



#-----------------------Remote çalışma dağılımı gösteren grafik--------------------

#remote_ratio kolonundaki değerlerin tekrarı
employee_remote_counts = df['remote_ratio'].value_counts()

# Pasta grafiği oluşturalım
plt.figure(figsize=(12, 6))
plt.pie(employee_remote_counts , labels=employee_remote_counts .index, autopct='%1.1f%%', startangle=140)
plt.title('Employee Remote Distribution')
plt.axis('equal')  # Daireyi düzgün bir daire olarak göstermek için

# Grafiği gösterelim
plt.show()




#-----------------------Şirketlerin büyüklük dağılımlarını gösteren--------------------

# company_size kolonundaki değerlerin tekrarı
company_size_counts = df['company_size'].value_counts()

# Pasta grafiği 
plt.figure(figsize=(12, 6))
plt.pie(company_size_counts, labels=company_size_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Company Size Distribution')
plt.axis('equal')  # Daireyi düzgün bir daire olarak göstermek için


plt.show()


#-----------------------Çalışma yıllarının dağılımı gösteren grafik--------------------

# work_year kolonundaki değerlerin tekrarı
work_years = df['work_year'].value_counts()

# Pasta grafiği 
plt.figure(figsize=(12, 6))
plt.pie(work_years, labels=work_years.index, autopct='%1.1f%%', startangle=140)
plt.title('Work Years Distribution')
plt.axis('equal')  # Daireyi düzgün bir daire olarak göstermek için


plt.show()