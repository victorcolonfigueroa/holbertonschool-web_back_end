#!/usr/bin/env python3
"""
Test script to verify AUTH_TYPE environment variable switching
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_auth_switching():
    """Test authentication switching based on AUTH_TYPE"""
    
    # Test cases for different AUTH_TYPE values
    test_cases = [
        ("auth", "Auth"),
        ("basic_auth", "BasicAuth"), 
        ("session_auth", "SessionAuth"),
        (None, None),  # Default case
        ("invalid", None)  # Invalid case
    ]
    
    for auth_type, expected_class in test_cases:
        print(f"\nTesting AUTH_TYPE = '{auth_type}':")
        
        # Set environment variable
        if auth_type is not None:
            os.environ["AUTH_TYPE"] = auth_type
        else:
            os.environ.pop("AUTH_TYPE", None)
        
        try:
            # Import and check the auth instance
            from api.v1.app import auth
            
            if expected_class is None:
                if auth is None:
                    print(f"✓ Correctly set auth to None for AUTH_TYPE = '{auth_type}'")
                else:
                    print(f"✗ Expected auth to be None, but got {type(auth).__name__}")
            else:
                if auth is not None and type(auth).__name__ == expected_class:
                    print(f"✓ Correctly created {expected_class} instance")
                else:
                    actual_class = type(auth).__name__ if auth else "None"
                    print(f"✗ Expected {expected_class}, but got {actual_class}")
                    
        except Exception as e:
            print(f"✗ Error importing or checking auth: {e}")
        
        # Clean up imports to allow re-import
        modules_to_remove = [key for key in sys.modules.keys() if key.startswith('api.v1.app')]
        for module in modules_to_remove:
            del sys.modules[module]

if __name__ == "__main__":
    test_auth_switching()
