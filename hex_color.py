def check(hex_list: dict): #*adapted* from https://www.geeksforgeeks.org/check-if-a-given-string-is-a-valid-hexadecimal-color-code-or-not/
    """
    Checks if a hex code is valid. If a code isn't valid, the key of the hex number will be returned
    `hex_list` is a dictionary of hex colours, suggested use:
    'hover_color' = ...
    'frame_color' = ...
    'root_color' = ...
    'button_color' = ...
    
    """
    for hex in hex_list:
        print(hex_list[hex])
        if hex_list[hex][0] != "#":
            print(1)
            return hex
        if hex_list[hex][0] != "#":
            print(2)
            
            return hex
        if (not(len(hex_list[hex]) == 4 or len(hex_list[hex]) == 7)):
            print(3)
             
            return hex
        for i in range(1, len(hex_list[hex])):
            print(4)
            
            if (not((hex_list[hex][i] >= '0' and hex_list[hex][i] <= '9') or (hex_list[hex][i] >= 'a' and hex_list[hex][i] <= 'f') or (hex_list[hex][i] >= 'A' or hex[i] <= 'F'))): # Dont know what it does.
                return hex
