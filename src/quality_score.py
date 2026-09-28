import pandas as pd
import os

def calculate_quality_scores():
    print("Calculating Country Data Quality and Usability Scores...")
    
    processed_path = "data/processed/standardized_ember.csv"
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(processed_path)
    
    # Group by Country/Area to evaluate metrics per country
    countries = []
    
    for area, group in df.groupby('Area'):
        # 1. Recency: What is the latest year reported?
        max_year = group['Year'].max()
        recency_score = 100 if max_year >= 2023 else (80 if max_year >= 2021 else 50)
        
        # 2. Completeness: Percentage of non-null generation values
        completeness = (group['Generation (TWh)'].notnull().mean()) * 100
        
        # 3. Capacity Reporting Rate: Percentage of rows with valid capacity data
        capacity_coverage = (group['Capacity (GW)'].notnull().mean()) * 100
        
        # Composite Usability Score (Weighted average)
        composite_score = round((0.4 * completeness) + (0.4 * recency_score) + (0.2 * capacity_coverage), 2)
        
        countries.append({
            "Country": area,
            "ISO3": group['ISO 3 code'].iloc[0],
            "Latest_Year": max_year,
            "Completeness_Pct": round(completeness, 2),
            "Capacity_Coverage_Pct": round(capacity_coverage, 2),
            "Data_Quality_Score": composite_score
        })
        
    df_rankings = pd.DataFrame(countries)
    df_rankings = df_rankings.sort_values(by="Data_Quality_Score", ascending=False).reset_index(drop=True)
    
    output_file = os.path.join(output_dir, "country_rankings.csv")
    df_rankings.to_csv(output_file, index=False)
    
    print(f"Quality scoring complete! Rankings saved to {output_file}")
    print(df_rankings.head(10))

if __name__ == "__main__":
    calculate_quality_scores()