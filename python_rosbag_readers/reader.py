from rosbag2_py import Player, SequentialReader, SequentialReader, StorageOptions, ConverterOptions
from builtin_interfaces.msg import Time
from rosidl_runtime_py.utilities import get_message
from rclpy.serialization import deserialize_message

reader = SequentialReader()
reader.open(StorageOptions(uri="/home/roboracing/bagfiles/test-ros-bag-2025-09-1417-15-51_300210", storage_id="sqlite3"), ConverterOptions(input_serialization_format="", output_serialization_format=""))

topic_types = reader.get_all_topics_and_types()
type_map = {topic.name: topic.type for topic in topic_types}

while reader.has_next():
    (topic, data, timestamp) = reader.read_next()
    msg_type = get_message(type_map[topic])
    msg = deserialize_message(data, msg_type)
    print(f"[{topic}] @{timestamp}: {msg}")