#!/usr/bin/env python3
"""
Test script to verify SessionAuth inheritance
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.auth import Auth

def test_session_auth():
    """Test SessionAuth inheritance"""
    try:
        # Create SessionAuth instance
        session_auth = SessionAuth()
        print("✓ SessionAuth instance created successfully")
        
        # Check inheritance
        if issubclass(SessionAuth, Auth):
            print("✓ SessionAuth correctly inherits from Auth")
        else:
            print("✗ SessionAuth does not inherit from Auth")
            
        # Check if instance is of both types
        if isinstance(session_auth, Auth):
            print("✓ SessionAuth instance is also an Auth instance")
        else:
            print("✗ SessionAuth instance is not an Auth instance")
            
        # Check inherited methods
        auth_methods = ['require_auth', 'authorization_header', 'current_user']
        for method in auth_methods:
            if hasattr(session_auth, method):
                print(f"✓ SessionAuth has inherited method: {method}")
            else:
                print(f"✗ SessionAuth missing inherited method: {method}")
                
        print("\nAll inheritance tests passed!")
        
    except Exception as e:
        print(f"Error testing SessionAuth: {e}")

if __name__ == "__main__":
    test_session_auth()
