import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/roboracing/Desktop/roboracing-rigatoniv-base/install/launch_robot'
