#!/usr/bin/env python3
"""
Test script to verify SessionAuth create_session functionality
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api.v1.auth.session_auth import SessionAuth

def test_create_session():
    """Test the create_session method"""
    print("Testing SessionAuth.create_session() method:")
    
    # Create SessionAuth instance
    session_auth = SessionAuth()
    
    # Test 1: Valid user_id
    user_id = "test-user-123"
    session_id = session_auth.create_session(user_id)
    print(f"\nTest 1 - Valid user_id '{user_id}':")
    if session_id is not None:
        print(f"✓ Session ID created: {session_id}")
        if session_auth.user_id_by_session_id.get(session_id) == user_id:
            print("✓ Session ID correctly mapped to user_id")
        else:
            print("✗ Session ID not correctly mapped to user_id")
    else:
        print("✗ Failed to create session ID")
    
    # Test 2: None user_id
    session_id_none = session_auth.create_session(None)
    print(f"\nTest 2 - None user_id:")
    if session_id_none is None:
        print("✓ Correctly returned None for None user_id")
    else:
        print("✗ Should return None for None user_id")
    
    # Test 3: Non-string user_id
    session_id_int = session_auth.create_session(123)
    print(f"\nTest 3 - Non-string user_id (123):")
    if session_id_int is None:
        print("✓ Correctly returned None for non-string user_id")
    else:
        print("✗ Should return None for non-string user_id")
    
    # Test 4: Multiple sessions for same user
    user_id2 = "same-user"
    session_id1 = session_auth.create_session(user_id2)
    session_id2 = session_auth.create_session(user_id2)
    print(f"\nTest 4 - Multiple sessions for same user '{user_id2}':")
    if session_id1 != session_id2:
        print("✓ Different session IDs created for same user")
        if (session_auth.user_id_by_session_id.get(session_id1) == user_id2 and 
            session_auth.user_id_by_session_id.get(session_id2) == user_id2):
            print("✓ Both session IDs correctly mapped to same user_id")
        else:
            print("✗ Session IDs not correctly mapped")
    else:
        print("✗ Same session ID returned for multiple calls")
    
    # Test 5: Check class attribute
    print(f"\nTest 5 - Class attribute user_id_by_session_id:")
    if hasattr(SessionAuth, 'user_id_by_session_id'):
        print("✓ Class has user_id_by_session_id attribute")
        print(f"Current sessions: {len(session_auth.user_id_by_session_id)} entries")
        for sid, uid in session_auth.user_id_by_session_id.items():
            print(f"  {sid[:8]}... → {uid}")
    else:
        print("✗ Class missing user_id_by_session_id attribute")

if __name__ == "__main__":
    test_create_session()
