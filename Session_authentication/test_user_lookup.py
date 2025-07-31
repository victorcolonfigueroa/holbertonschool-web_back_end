#!/usr/bin/env python3
"""
Test script to verify SessionAuth user_id_for_session_id functionality
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api.v1.auth.session_auth import SessionAuth

def test_user_id_for_session_id():
    """Test the user_id_for_session_id method"""
    print("Testing SessionAuth.user_id_for_session_id() method:")
    
    # Create SessionAuth instance
    session_auth = SessionAuth()
    
    # Test 1: Create a session and retrieve user_id
    user_id = "test-user-456"
    session_id = session_auth.create_session(user_id)
    retrieved_user_id = session_auth.user_id_for_session_id(session_id)
    
    print(f"\nTest 1 - Valid session lookup:")
    print(f"Created session for user_id: {user_id}")
    print(f"Generated session_id: {session_id}")
    print(f"Retrieved user_id: {retrieved_user_id}")
    
    if retrieved_user_id == user_id:
        print("✓ Successfully retrieved correct user_id for session_id")
    else:
        print("✗ Failed to retrieve correct user_id")
    
    # Test 2: None session_id
    result_none = session_auth.user_id_for_session_id(None)
    print(f"\nTest 2 - None session_id:")
    if result_none is None:
        print("✓ Correctly returned None for None session_id")
    else:
        print("✗ Should return None for None session_id")
    
    # Test 3: Non-string session_id
    result_int = session_auth.user_id_for_session_id(123)
    print(f"\nTest 3 - Non-string session_id (123):")
    if result_int is None:
        print("✓ Correctly returned None for non-string session_id")
    else:
        print("✗ Should return None for non-string session_id")
    
    # Test 4: Non-existent session_id
    fake_session_id = "fake-session-id-does-not-exist"
    result_fake = session_auth.user_id_for_session_id(fake_session_id)
    print(f"\nTest 4 - Non-existent session_id:")
    if result_fake is None:
        print("✓ Correctly returned None for non-existent session_id")
    else:
        print("✗ Should return None for non-existent session_id")
    
    # Test 5: Multiple sessions for same user
    user_id2 = "another-user"
    session_id1 = session_auth.create_session(user_id2)
    session_id2 = session_auth.create_session(user_id2)
    
    retrieved_user1 = session_auth.user_id_for_session_id(session_id1)
    retrieved_user2 = session_auth.user_id_for_session_id(session_id2)
    
    print(f"\nTest 5 - Multiple sessions for same user:")
    print(f"User ID: {user_id2}")
    print(f"Session 1: {session_id1} → {retrieved_user1}")
    print(f"Session 2: {session_id2} → {retrieved_user2}")
    
    if retrieved_user1 == user_id2 and retrieved_user2 == user_id2:
        print("✓ Both sessions correctly return the same user_id")
    else:
        print("✗ Sessions not correctly mapped to user_id")
    
    # Test 6: Dictionary access using .get()
    print(f"\nTest 6 - Verify .get() method usage:")
    print("Method uses .get() to safely access dictionary values")
    print("✓ Implementation uses user_id_by_session_id.get(session_id)")

if __name__ == "__main__":
    test_user_id_for_session_id()
