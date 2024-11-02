import heapq
import os

class BinaryTreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq
        


class Huffmancode:
    def __init__(self, path):
        self.path = path
        self.__heap = []
        self.__codes = {}
        self.__reverse_codes = {}
        
        
    def __frequency_from_text(self, text):
        freq_dict = {}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1
        return freq_dict
        
    
    def __build_heap(self, freq_dict):
        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = BinaryTreeNode(key, frequency)
            heapq.heappush(self.__heap, binary_tree_node)
            
    
    def __build_Binary_Tree(self):
        while len(self.__heap) > 1:
            node1 = heapq.heappop(self.__heap)
            node2 = heapq.heappop(self.__heap)
            freq_sum = node1.freq + node2.freq
            newNode = BinaryTreeNode(None, freq_sum)
            newNode.left = node1
            newNode.right = node2
            heapq.heappush(self.__heap, newNode)
        return
    
    
    def __build_Tree_Code_Helper(self, root, curr_bit):
        if root is None:
            return
        
        if root.value is not None:
            self.__codes[root.value] = curr_bit
            self.__reverse_codes[curr_bit] = root.value
            return
        
        self.__build_Tree_Code_Helper(root.left, curr_bit + "0")
        self.__build_Tree_Code_Helper(root.right, curr_bit + "1")
    
    
    def __build_Tree_Code(self):
        root = heapq.heappop(self.__heap)
        self.__build_Tree_Code_Helper(root, "")
    
    
    def __build_encoded_text(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.__codes[char]
        return encoded_text
    
    
    def __Build_Padded_Text(self, encoded_text):
        padding_value = 8 - (len(encoded_text) % 8)
        for i in range(padding_value):
            encoded_text += "0"
        
        padded_info = "{0:08b}".format(padding_value)
        padded_text = padded_info + encoded_text
        return padded_text
     
     
    def __Build_Bit_Array(self, padded_text):
        array = []
        for i in range(0, len(padded_text), 8):
            byte = padded_text[i:i+8]
            array.append(int(byte, 2))
        return array
    
    def compression(self):
        print("Compressing the file...")
        # Access the file and extract the text
        file_name, file_extension = os.path.splitext(self.path)
        output_path = file_name + ".bin"
        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:  
            text = file.read()
            text = text.rstrip()
            
            
            freq_dict = self.__frequency_from_text(text)
            
            # Calculate the frequency of each character and store in freq dictionary
            build_heap = self.__build_heap(freq_dict)
            
            
            # Min Heap for two minimum frequency nodes
            # Construct the Binary Tree from the min heap
            self.__build_Binary_Tree()
            
            
            # Construct code from the binary tree and stored in a dictionary
            self.__build_Tree_Code()
            
            
            # Construct the encoded text from the code dictionary
            encoded_text = self.__build_encoded_text(text)
            
            
            # padding the encoded text
            padded_text = self.__Build_Padded_Text(encoded_text)
            
            
            # Return the encoded text as binary file as an output
            bytes_array = self.__Build_Bit_Array(padded_text)
            final_bytes = bytes(bytes_array)
            output.write(final_bytes)
        print("Compression Done")
        return output_path
    
    
    def __remove_padding(self, text):
        padded_info = text[:8]
        padding_value = int(padded_info, 2)
        text = text[8:]
        text = text[:-1*padding_value]
        return text
    
    
    def __decode_text(self, text):
        current_bits = ""
        decoded_text = ""
        for char in text:
            current_bits += char
            if current_bits in self.__reverse_codes:
                decoded_text += self.__reverse_codes[current_bits]
                current_bits = ""
        return decoded_text
    
    
    def decompression(self, input_path):
        filename, file_extension = os.path.splitext(input_path)
        output_path = filename + "_decompressed" + ".txt"
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)
            text_after_padding_removed = self.__remove_padding(bit_string)
            actual_text = self.__decode_text(text_after_padding_removed)
            output.write(actual_text)



path = input("Enter the file path to compress: ")
h = Huffmancode(path)
compressed_file = h.compression()
h.decompression(compressed_file)