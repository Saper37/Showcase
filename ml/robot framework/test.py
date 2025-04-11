from robot.running import TestSuite

suite = TestSuite.from_file_system( "" )
data = suite.to_json( )
suite.to_json( "", indent=2 )