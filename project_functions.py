import pm4py
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pickle
import numpy as np
import tqdm
import seaborn as sns


def plot_cdf(data, img_path=None, title='Cumulative Distribution Function (CDF)', xlabel='Data', ylabel='CDF'):
 
    data_sorted = np.sort(data)
    
    cdf = np.arange(1, len(data_sorted) + 1) / len(data_sorted)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(data_sorted, cdf, marker='.', linestyle='-', color='b', label='CDF')
    

    ax.set_title(title, fontsize=16)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    

    points_of_interest = [np.percentile(data_sorted, q) for q in [50]]
    for point in points_of_interest:
        ax.axvline(point, color='r', linestyle='--', linewidth=1)
        ax.text(point, 0.5, f'{point:.2f}', color='r', ha='center', fontsize=12, 
                bbox=dict(facecolor='white', alpha=0.6, edgecolor='red'))
    
    # Aggiungi la legenda
    ax.legend()
    
    # Mostra o salva il plot
    if img_path:
        plt.savefig(img_path, dpi=300, bbox_inches='tight')
    else:
        plt.show()
        
        
        
def plot_value_counts(data, column_name, img_path=None):

    plt.figure(figsize=(12, 8))
    

    value_counts = data[column_name].value_counts()
    sns.barplot(x=value_counts.index, y=value_counts.values, palette="viridis")

    plt.title(f'Value Counts of {column_name}', fontsize=16)
    plt.xlabel(column_name, fontsize=14)
    plt.ylabel('Counts', fontsize=14)
    
    plt.xticks(rotation=45, ha='right', fontsize=12)

    for index, value in enumerate(value_counts.values):
        plt.text(index, value, str(value), ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    
    if img_path:
        plt.savefig(img_path, bbox_inches='tight', dpi=300)
    
    plt.show()