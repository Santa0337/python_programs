parsing_data = {'stream_group01': {'stream_group01-EndpointSet-1 - Flow Group 0001': 
                                   {'Tx Frames': '219874', 'Rx Frames': '1978866', 'Loss %': '', 'Frames Delta': '1758992', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '9000.000'}}, 
                'stream_group02': {'stream_group02-EndpointSet-1 - Flow Group 0001': 
                                   {'Tx Frames': '209257', 'Rx Frames': '1255542', 'Loss %': '', 'Frames Delta': '1046285', 'Tx Frame Rate': '1000.000', 'Rx Frame Rate': '6000.000'}}}
for stream_group, flow_group in parsing_data.items():
    for flows, frame_data in flow_group.items():
        tx_rate = float(frame_data['Tx Frame Rate'])
        rx_rate = float(frame_data['Rx Frame Rate'])
        print(f"Transmitted rate is {tx_rate} and Received rate is {rx_rate} on {flows} of {stream_group}")