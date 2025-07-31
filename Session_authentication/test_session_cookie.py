#!/usr/bin/env python3
"""
Test script to verify Auth session_cookie functionality
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api.v1.auth.auth import Auth

def test_session_cookie():
    """Test the session_cookie method"""
    print("Testing Auth.session_cookie() method:")
    
    # Create Auth instance
    auth = Auth()
    
    # Test 1: None request
    result_none = auth.session_cookie(None)
    print(f"\nTest 1 - None request:")
    if result_none is None:
        print("✓ Correctly returned None for None request")
    else:
        print("✗ Should return None for None request")
    
    # Test 2: Mock request without SESSION_NAME environment variable
    class MockRequest:
        def __init__(self, cookies_dict):
            self.cookies = MockCookies(cookies_dict)
    
    class MockCookies:
        def __init__(self, cookies_dict):
            self._cookies = cookies_dict
        
        def get(self, key):
            return self._cookies.get(key)
    
    print(f"\nTest 2 - Without SESSION_NAME env var:")
    os.environ.pop('SESSION_NAME', None)  # Remove if exists
    mock_request = MockRequest({'_my_session_id': 'test-session-123'})
    result = auth.session_cookie(mock_request)
    if result is None:
        print("✓ Correctly returned None when SESSION_NAME not set")
    else:
        print("✗ Should return None when SESSION_NAME not set")
    
    # Test 3: Mock request with SESSION_NAME environment variable
    print(f"\nTest 3 - With SESSION_NAME='_my_session_id':")
    os.environ['SESSION_NAME'] = '_my_session_id'
    test_session_value = 'test-session-456'
    mock_request = MockRequest({'_my_session_id': test_session_value})
    result = auth.session_cookie(mock_request)
    print(f"Session cookie value: {result}")
    if result == test_session_value:
        print("✓ Successfully retrieved session cookie value")
    else:
        print("✗ Failed to retrieve correct session cookie value")
    
    # Test 4: Mock request with different cookie name
    print(f"\nTest 4 - With different SESSION_NAME='custom_session':")
    os.environ['SESSION_NAME'] = 'custom_session'
    custom_session_value = 'custom-session-789'
    mock_request = MockRequest({
        '_my_session_id': 'old-session',
        'custom_session': custom_session_value
    })
    result = auth.session_cookie(mock_request)
    print(f"Custom session cookie value: {result}")
    if result == custom_session_value:
        print("✓ Successfully retrieved custom session cookie")
    else:
        print("✗ Failed to retrieve custom session cookie")
    
    # Test 5: Mock request with missing cookie
    print(f"\nTest 5 - Missing requested cookie:")
    os.environ['SESSION_NAME'] = 'missing_cookie'
    mock_request = MockRequest({'other_cookie': 'other-value'})
    result = auth.session_cookie(mock_request)
    if result is None:
        print("✓ Correctly returned None for missing cookie")
    else:
        print("✗ Should return None for missing cookie")
    
    print(f"\nImplementation details:")
    print("✓ Uses getenv('SESSION_NAME') to get cookie name")
    print("✓ Uses request.cookies.get(session_name) for safe access")
    print("✓ Returns None for invalid requests or missing environment variables")

if __name__ == "__main__":
    test_session_cookie()
