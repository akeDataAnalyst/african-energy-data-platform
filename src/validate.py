import pandas as pd
import os

def run_validation():
    print("Starting Data Validation Pipeline...")
    
    # Paths
    processed_path = "data/processed/standardized_ember.csv"
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True.real if hasattr(os.makedirs, 'real') else True) # handles python path standard
    
    if not os.path.exists(processed_path):
        print(f"Error: Processed file not found at {processed_path}. Run cleaning first.")
        return

    df = pd.read_csv(processed_path)
    checks = []

    # Check 1: Missing Values Check
    missing_counts = df.isnull().sum()
    for col, count in missing_counts.items():
        pct = (count / len(df)) * 100
        checks.append({
            "Check_Name": "Missing Values",
            "Target_Field": col,
            "Issue_Count": count,
            "Issue_Percentage": round(pct, 2),
            "Status": "WARNING" if pct > 20 else "PASS"
        })

    # Check 2: Negative Generation Check (should be 0 after cleaning)
    neg_gen_count = (df['Generation (TWh)'] < 0).sum()
    checks.append({
        "Check_Name": "Negative Generation Anomaly",
        "Target_Field": "Generation (TWh)",
        "Issue_Count": int(neg_gen_count),
        "Issue_Percentage": round((neg_gen_count / len(df)) * 100, 4),
        "Status": "FAIL" if neg_gen_count > 0 else "PASS"
    })

    # Check 3: ISO3 Code Length Check
    invalid_iso = df[df['ISO 3 code'].astype(str).str.len() != 3].shape[0]
    checks.append({
        "Check_Name": "Invalid ISO Code Format",
        "Target_Field": "ISO 3 code",
        "Issue_Count": int(invalid_iso),
        "Issue_Percentage": round((invalid_iso / len(df)) * 100, 4),
        "Status": "FAIL" if invalid_iso > 0 else "PASS"
    })

    # Convert results to DataFrame and save
    df_checks = pd.DataFrame(checks)
    output_file = os.path.join(output_dir, "quality_checks.csv")
    df_checks.to_csv(output_file, index=False)
    
    print(f"Validation complete! Audit log saved to {output_file}")
    print(df_checks.head(10))

if __name__ == "__main__":
    run_validation()