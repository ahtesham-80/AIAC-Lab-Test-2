class YieldTracker:
    """A class to track float values by unique IDs."""
    
    def __init__(self):
        """Initialize the tracker with an empty dictionary."""
        self._data = {}
    
    def add(self, id, value):
        """Add or update a value for an ID.
        
        Args:
            id: Unique identifier
            value: Float value to store
        """
        self._data[id] = float(value)
    
    def remove(self, id):
        """Remove the value for an ID safely.
        
        Args:
            id: Unique identifier to remove
            
        Returns:
            The removed value if it existed, None otherwise
        """
        return self._data.pop(id, None)
    
    def summary(self):
        """Return summary statistics of all values.
        
        Returns:
            Tuple of (count, average) where average is rounded to 2 decimals
            or None if no values exist
        """
        if not self._data:
            return (0, None)
        
        values = list(self._data.values())
        count = len(values)
        average = round(sum(values) / count, 2)
        
        return (count, average)


# Test with sample input
if __name__ == "__main__":
    tracker = YieldTracker()
    
    # Sample operations
    operations = [
        {'op': 'add', 'id': 'a1', 'value': 22},
        {'op': 'add', 'id': 'b2', 'value': 17},
        {'op': 'remove', 'id': 'a1'},
        {'op': 'add', 'id': 'c3', 'value': 19}
    ]
    
    # Execute operations
    for op in operations:
        if op['op'] == 'add':
            tracker.add(op['id'], op['value'])
        elif op['op'] == 'remove':
            tracker.remove(op['id'])
    
    # Get summary and format output
    count, avg = tracker.summary()
    print(f"count={count}, avg={avg}")







