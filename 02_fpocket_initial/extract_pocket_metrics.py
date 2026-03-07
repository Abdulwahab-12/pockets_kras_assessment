import pandas as pd
import os

def parse_fpocket_info(filepath, state_name):
    pockets = []
    current_pocket = {}
    
    # Check if the file exists in the expected output directory
    if not os.path.exists(filepath):
        print(f"Error: Could not find {filepath}. Please check your paths.")
        return []

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Identify a new pocket block
            if line.startswith("Pocket "):
                if current_pocket:
                    pockets.append(current_pocket)
                pocket_name = line.split(":")[0].strip()
                current_pocket = {'State': state_name, 'Pocket_ID': pocket_name}
                
            # Extract specific metrics
            elif "Druggability Score :" in line:
                current_pocket['Druggability_Score'] = float(line.split(":")[1].strip())
            elif line.startswith("Volume :"):
                current_pocket['Volume'] = float(line.split(":")[1].strip())
            elif "Polarity score:" in line:
                current_pocket['Polarity_Score'] = float(line.split(":")[1].strip())
            elif "Hydrophobicity score:" in line:
                current_pocket['Hydrophobicity_Score'] = float(line.split(":")[1].strip())

        # Append the very last pocket
        if current_pocket:
            pockets.append(current_pocket)

    return pockets

def main():
    # Define file paths based on our Phase 3 project structure
    apo_file = "4OBE_apo_out/4OBE_apo_info.txt"
    holo_file = "4OBE_holo_out/4OBE_holo_info.txt"

    print("Parsing Fpocket results...")
    
    # Parse both files
    apo_data = parse_fpocket_info(apo_file, "Apo")
    holo_data = parse_fpocket_info(holo_file, "Holo")
    
    # Combine into a single pandas DataFrame
    all_pockets = apo_data + holo_data
    if not all_pockets:
        print("No data extracted. Exiting.")
        return

    df = pd.DataFrame(all_pockets)
    
    # Sort by State, then by Druggability Score (highest first)
    df_sorted = df.sort_values(by=['State', 'Druggability_Score'], ascending=[True, False])
    
    # Display the top 3 pockets for each state in the terminal
    print("\n--- Top 3 Pockets per State (Ranked by Druggability) ---")
    print(df_sorted.groupby('State').head(3).to_string(index=False))
    
    # Save the full sorted data to a CSV for the final report
    csv_filename = "pocket_metrics_summary.csv"
    df_sorted.to_csv(csv_filename, index=False)
    print(f"\nSuccess! Full pocket metrics saved to '{csv_filename}'.")
    print("You can use this CSV to create a nice table for your PDF report.")

if __name__ == "__main__":
    main()