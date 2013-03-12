import unittest

from libgravatar import Gravatar


class GravatarTestCase(unittest.TestCase):
    """Test case for the Gravatar class."""

    def setUp(self):
        self.g = Gravatar('myemailaddress@example.com')

    def test_without_params(self):
        """Test a get_image with default parameters."""
        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'
        result = self.g.get_image()
        self.assertEqual(image_url, result)

    def test_image_size(self):
        """Test image size parameter."""
        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346?size=24'
        result = self.g.get_image(size=24)
        self.assertEqual(image_url, result)

    def test_filetype_extension(self):
        """Test filetype_extension parameter."""
        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346.jpg'
        result = self.g.get_image(filetype_extension=True)
        self.assertEqual(image_url, result)

    def test_default(self):
        """Test default parameter."""
        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346?default=monsterid'
        result = self.g.get_image(default='monsterid')
        self.assertEqual(image_url, result)

        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346?default=http%3A%2F%2Fexample.com%2Fimages%2Favatar.jpg'
        result = self.g.get_image(default='http://example.com/images/avatar.jpg')
        self.assertEqual(image_url, result)

        invalid_default_url = 'ftp://example.com/images/avatar.php?key=value'
        self.assertRaises(ValueError, self.g.get_image, default=invalid_default_url)

    def test_forcedefault(self):
        """Test forcedefault parameter."""
        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346?forcedefault=y'
        result = self.g.get_image(force_default=True)
        self.assertEqual(image_url, result)

    def test_use_ssl(self):
        """Test use_ssl parameter."""
        image_url = 'https://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'
        result = self.g.get_image(use_ssl=True)
        self.assertEqual(image_url, result)

    def test_rating(self):
        """Test the rating parameter."""
        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346?rating=g'
        result = self.g.get_image(rating='g')
        self.assertEqual(image_url, result)

        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346?rating=pg'
        result = self.g.get_image(rating='pg')
        self.assertEqual(image_url, result)

        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346?rating=r'
        result = self.g.get_image(rating='r')
        self.assertEqual(image_url, result)

        image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346?rating=x'
        result = self.g.get_image(rating='x')
        self.assertEqual(image_url, result)

        self.assertRaises(ValueError, self.g.get_image, rating='invalid')
