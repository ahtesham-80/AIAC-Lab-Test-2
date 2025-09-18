def parse_soil_moisture_data(csv_text):
    """
    Parse CSV text with soil moisture data and compute averages.
    
    Args:
        csv_text (str): Raw multiline CSV text with format "id,timestamp,soil_moist"
    
    Returns:
        tuple: (dict of {id: average_soil_moist}, overall_average)
    """
    lines = csv_text.strip().split('\n')
    tractor_data = {}  # {id: [soil_moist_values]}
    
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:  # Skip empty lines
            continue
            
        try:
            parts = line.split(',')
            if len(parts) != 3:  # Must have exactly 3 parts
                continue
                
            tractor_id, timestamp, soil_moist_str = parts
            
            # Try to convert soil_moist to float
            try:
                soil_moist = float(soil_moist_str)
            except ValueError:
                # Skip lines with non-numeric soil_moist values
                continue
            
            # Store the soil moisture value for this tractor
            if tractor_id not in tractor_data:
                tractor_data[tractor_id] = []
            tractor_data[tractor_id].append(soil_moist)
            
        except Exception:
            # Skip malformed lines
            continue
    
    # Compute per-tractor averages
    tractor_averages = {}
    all_values = []
    
    for tractor_id, values in tractor_data.items():
        if values:  # Only if we have valid values
            avg = sum(values) / len(values)
            tractor_averages[tractor_id] = round(avg, 2)
            all_values.extend(values)
    
    # Compute overall average
    overall_average = round(sum(all_values) / len(all_values), 2) if all_values else 0.0
    
    return tractor_averages, overall_average


# Example usage and test
if __name__ == "__main__":
    # Test data with your sample input
    test_csv = """tr131,2025-01-01T08:00,32.7
tr132,2025-01-02T09:00,34.2
tr133,2025-01-03T010:00,35.7"""
    
    result = parse_soil_moisture_data(test_csv)
    tractor_averages, overall_average = result
    
    print(f"Per-tractor averages: {tractor_averages}")
    print(f"Overall average: {overall_average}")
    
    # Verify expected output
    expected = {'tr131': 32.7, 'tr132': 34.2, 'tr133': 35.7}
    expected_overall = 34.2
    
    print(f"\nExpected: {expected} and overall_avg={expected_overall}")
    print(f"Actual: {tractor_averages} and overall_avg={overall_average}")
    print(f"Match: {tractor_averages == expected and overall_average == expected_overall}")






