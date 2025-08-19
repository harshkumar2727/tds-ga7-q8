"""
Patient Satisfaction Quarterly Analysis - 2024

Author: 23ds3000170@ds.study.iitm.ac.in

This module provides end-to-end analysis of quarterly patient satisfaction scores, supporting targeted recommendations
to improve service quality and wait times.

Generated with LLM/AI assistance for healthcare performance analytics.
LLM Reference: https://chatgpt.com/codex/tasks
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_patient_satisfaction():
    """Prepares the quarterly patient satisfaction DataFrame."""
    data = {
        'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
        'Satisfaction_Score': [1.57, 6.19, 7.47, 3.39]
    }
    df = pd.DataFrame(data)
    avg_score = df['Satisfaction_Score'].mean()
    df['Industry_Benchmark'] = 4.5
    df['Company_Average'] = avg_score
    return df

def create_satisfaction_visualization():
    """Creates a line chart for patient satisfaction analysis."""
    df = analyze_patient_satisfaction()
    sns.set(style="whitegrid")
    plt.figure(figsize=(9,6))
    # Plot quarterly scores
    plt.plot(df['Quarter'], df['Satisfaction_Score'], marker='o', label='Patient Satisfaction Score', color='dodgerblue', linewidth=2)
    # Industry Benchmark
    plt.axhline(y=4.5, color='red', linestyle='--', label='Industry Benchmark (4.5)')
    # Company Average
    plt.axhline(y=4.66, color='green', linestyle='-.', label='Company Average (4.66)')
    plt.title('2024 Quarterly Patient Satisfaction Scores', fontsize=16, fontweight='bold')
    plt.xlabel('Quarter', fontsize=12)
    plt.ylabel('Satisfaction Score', fontsize=12)
    plt.ylim(0, 8)
    plt.legend()
    plt.tight_layout()
    plt.savefig('patient_satisfaction_2024.png', dpi=300)
    plt.close()

if __name__ == "__main__":
    print("🏥 Patient Satisfaction Analysis")
    print("=" * 40)
    print(f"📧 Analysis by: 23ds3000170@ds.study.iitm.ac.in")
    df = analyze_patient_satisfaction()
    # Save CSV
    df[['Quarter', 'Satisfaction_Score']].to_csv('quarterly_patient_satisfaction_2024.csv', index=False)
    print("\n📊 Quarterly Scores:")
    print(df.to_string(index=False))
    # Key Statistics
    avg_score = df['Satisfaction_Score'].mean()
    min_qtr = df.loc[df['Satisfaction_Score'].idxmin(), 'Quarter']
    max_qtr = df.loc[df['Satisfaction_Score'].idxmax(), 'Quarter']
    print("\nSUMMARY STATISTICS")
    print("-" * 20)
    print(f"Annual Average: {avg_score:.2f}")
    print(f"Industry Benchmark: 4.5")
    print(f"Best Quarter: {max_qtr}")
    print(f"Worst Quarter: {min_qtr}")
    # Save Visualization
    create_satisfaction_visualization()
    print("\n✅ Data saved as 'quarterly_patient_satisfaction_2024.csv'")
    print("✅ Chart saved as 'patient_satisfaction_2024.png'")
