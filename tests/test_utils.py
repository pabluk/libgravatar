import unittest

from libgravatar import sanitize_email, md5_hash, default_url_is_valid


class SanitizeEmailTestCase(unittest.TestCase):
    """Test case for sanitize_email function."""

    def test_valid_email(self):
        """Test a valid email address."""
        email = sanitize_email('myemailaddress@example.com')
        self.assertEqual(email, 'myemailaddress@example.com')

    def test_denormalized_email(self):
        """Test a denormalized email address."""
        email = sanitize_email(' MyEmailAddress@example.com ')
        self.assertEqual(email, 'myemailaddress@example.com')


class MD5HashTestCase(unittest.TestCase):
    """Test case for md5_hash function."""

    def test_md5_hash_from_email(self):
        """Test a md5 hash from an email address."""
        generated_hash = md5_hash('myemailaddress@example.com')
        self.assertEqual(generated_hash, '0bc83cb571cd1c50ba6f3e8a78ef1346')

    def test_md5_hash_with_empty_string(self):
        """Test a md5 hash for an empty string."""
        generated_hash = md5_hash('')
        self.assertEqual(generated_hash, 'd41d8cd98f00b204e9800998ecf8427e')


class DefaultURLTestCase(unittest.TestCase):
    """Test case for default url conditions."""

    def test_a_valid_url(self):
        """Test a valid URL."""
        url = 'http://example.com/images/avatar.jpg'
        self.assertTrue(default_url_is_valid(url))

        url = 'https://example.com/images/avatar.jpg'
        self.assertTrue(default_url_is_valid(url))

        url = 'http://example.com/images/avatar.png'
        self.assertTrue(default_url_is_valid(url))

        url = 'http://example.com/images/avatar.jpeg'
        self.assertTrue(default_url_is_valid(url))

        url = 'http://example.com/images/avatar.gif'
        self.assertTrue(default_url_is_valid(url))

    def test_invalid_protocol(self):
        """Test an URL with an invalid protocol."""
        url = 'ftp://example.com/images/avatar.jpg'
        self.assertFalse(default_url_is_valid(url))

    def test_invalid_extension(self):
        """Test an URL with an invalid extension file."""
        url = 'http://example.com/images/avatar.php'
        self.assertFalse(default_url_is_valid(url))

    def test_invalid_with_query(self):
        """Test an URL with an invalid query."""
        url = 'http://example.com/images/avatar.jpg?key=value'
        self.assertFalse(default_url_is_valid(url))
