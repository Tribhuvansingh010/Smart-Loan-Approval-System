import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x='Loan_Status', y='Income', data=data)
plt.title('Loan Approval by Income')
plt.show()


sns.scatterplot(x='Credit_Score', y='Loan_Status', data=data)
plt.title('Loan Approval by Credit Score')
plt.show()
