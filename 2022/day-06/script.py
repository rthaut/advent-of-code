import sys

# read input data from file specified as first command line argument
input_file = open(sys.argv[1], 'r')
input_data = input_file.read().rstrip();

def find_marker(signal, length):
	singal_list = list(signal)
	for i in range(len(singal_list)-length):
		chunk = singal_list[i:i+length]
		if len(set(chunk)) == length:
			return i,chunk
	return -1,''

packet_marker_start,packet_marker = find_marker(input_data, 4)
print("Characters processed before packet marker: " + str(packet_marker_start + len(packet_marker)))

message_marker_start,message_marker = find_marker(input_data, 14)
print("Characters processed before message marker: " + str(message_marker_start + len(message_marker)))
