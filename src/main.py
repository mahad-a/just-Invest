import pandas

def justInvest():
    print("justInvest System\n", "-"*50, "\nOperations available on the system:")
    print(" 1. View account balance\n",
           "2. View investment portfolio\n",
           "3. Modify investment portfolio\n",
           "4. View Finanical Advisor contact info\n",
           "5. View Finanical Planner contact info\n",
           "6. View money market instruments\n",
           "7. View private consumer instruments\n",
          )

def load_sample_users(filename):
    sample_df = pandas.read_csv(filename, sep=",", header=None)
    sample_df.columns = ["Name", "Role"]
    return sample_df
    

justInvest()
df = load_sample_users('docs/sample.txt')
print(df.head)