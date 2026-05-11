import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv(r'Loan_default.csv')

print(df.info())
print(df.groupby('Default').count())

'''
#As age increases the default rate decreases
age_default=df.groupby('Default')['Age'].mean()
plt.plot(age_default.index,age_default.values)
plt.ylabel('Age')
plt.xlabel('Default')
plt.show()

#As income increases default rate decreases
income_default=df.groupby('Default')['Income'].mean()
plt.plot(income_default.index,income_default.values)
plt.xlabel('Default')
plt.ylabel('Income')
plt.show()

#As loan amount increases default rate increases
loanamount_default=df.groupby('Default')['LoanAmount'].mean()
plt.plot(loanamount_default.index,loanamount_default.values)
plt.xlabel('Default')
plt.ylabel('Loan Amount')
plt.show()

#As credit score increases default rate decreases
creditscore_default=df.groupby('Default')['CreditScore'].mean()
plt.plot(creditscore_default.index,creditscore_default.values)
plt.xlabel('Default')
plt.ylabel('Credit Score')
plt.show()

#As interest rate increases default rate increases
interestrate_default=df.groupby('Default')['InterestRate'].mean()
plt.plot(interestrate_default.index,interestrate_default.values)
plt.xlabel('Default')
plt.ylabel('Interest Rate')
plt.show()

#As loan term increases default rate increases
loanterm_default=df.groupby('Default')['LoanTerm'].mean()
plt.plot(loanterm_default.index,loanterm_default.values)
plt.xlabel('Default')
plt.ylabel('Loan Term')
plt.show()

#High school has more number of default and PhD has has the lowest number of interest which tells that the most educated has the less chance of ending in default
sns.barplot(data=df,x='Education',y='Default',palette='Set2')
plt.title('Default VS Education')
plt.show()

#Divorced has more number of default and married has less
sns.barplot(data=df,x='MaritalStatus',y='Default',palette='Set2')
plt.title('Marital VS Sum of Default')
plt.show()

#Who does not have mortgage end in default
sns.barplot(data=df,x='HasMortgage',y='Default',palette='Set2')
plt.title('Has Morgage VS Sum of Default')
plt.show()

#print(df.columns)
#Sum of default is more who do not have dependent
sns.barplot(data=df,x='HasDependents',y='Default',palette='Set2')
plt.title('Has Dependent VS Sum of Default')
plt.show()

#Bussiness load ends in default and home load has lowest
sns.barplot(data=df,x='LoanPurpose',y='Default')
plt.title('Loan Purpose VS Sum of Default')
plt.show()

#Loan amount does not depends on income
loanamount_income=df[['LoanAmount','Income']].corr()
sns.heatmap(loanamount_income,annot=True,cmap='coolwarm')
plt.show()'''