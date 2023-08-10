import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# load data:
data = pd.read_csv('lum_trial_06282023_data.csv', index_col=0)

# clean data to avoid error in heatmap value distribution
data_cleaned = data.dropna(axis=1, how='all').dropna(axis=0, how='all')


data_cleaned.to_csv('data_cleaned.csv', index=False)


# create heatmap:
plt.figure(figsize=(8,2))

sns.heatmap(data_cleaned, cmap='viridis', annot=False, fmt='.2f', cbar_kws={'label': 'Cytokine/Chemokine'})


plt.title('Cytokine/Chemokine MFI Heatmap')
plt.xlabel('Cytokines/Chemokines')
plt.ylabel('Samples')

plt.show()