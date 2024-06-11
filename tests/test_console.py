import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Set up the console"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up resources"""
        del self.console

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(f.getvalue().strip())

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertTrue(f.getvalue().strip())

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_count(self):
        """Test count method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            self.assertEqual(f.getvalue().strip(), "0")

    def test_instance_show(self):
        """Test show method with instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show(123)")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_instance_destroy(self):
        """Test destroy method with instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.destroy(123)")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_instance_update(self):
        """Test update method with instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.update(123)")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_instance_update_dict(self):
        """Test update method with dictionary representation"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.update(123, {'name': 'John'})")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
