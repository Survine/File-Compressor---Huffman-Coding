# Huffman Coding Compression Tool

This project implements Huffman coding for file compression and decompression. Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies.

## Overview

The primary components of the project include:
- **BinaryTreeNode**: A class to represent nodes in a binary tree.
- **Huffmancode**: A class to handle the compression and decompression of files using Huffman coding.

## Classes

### 1. `BinaryTreeNode`
Represents a node in the Huffman tree.

#### Attributes
- `value`: The character represented by the node.
- `freq`: The frequency of the character.
- `left`: Pointer to the left child node.
- `right`: Pointer to the right child node.

#### Methods
- `__lt__(self, other)`: Compares nodes based on frequency for heap operations.
- `__eq__(self, other)`: Checks for equality based on frequency.

### 2. `Huffmancode`
Handles the compression and decompression of files using Huffman coding.

#### Attributes
- `path`: Path of the file to be compressed.
- `__heap`: Min-heap for building the Huffman tree.
- `__codes`: Dictionary to hold the binary codes for each character.
- `__reverse_codes`: Dictionary to reverse the codes back to characters.

#### Methods
- `__frequency_from_text(text)`: Calculates the frequency of each character in the input text.
- `__build_heap(freq_dict)`: Builds a min-heap from the frequency dictionary.
- `__build_Binary_Tree()`: Constructs the Huffman binary tree using the heap.
- `__build_Tree_Code_Helper(root, curr_bit)`: Recursively assigns binary codes to characters based on their position in the tree.
- `__build_Tree_Code()`: Initiates the code-building process from the binary tree.
- `__build_encoded_text(text)`: Encodes the input text using the generated codes.
- `__Build_Padded_Text(encoded_text)`: Adds padding to the encoded text to make its length a multiple of 8 bits.
- `__Build_Bit_Array(padded_text)`: Converts the padded binary string to an array of bytes for file writing.
- `compression()`: Reads the input file, compresses its content, and writes the compressed data to a binary file.
- `__remove_padding(text)`: Removes padding from the binary string to retrieve the original encoded data.
- `__decode_text(text)`: Decodes the binary string back to the original text using reverse codes.
- `decompression(input_path)`: Reads a binary file, decompresses its content, and writes the result to a text file.

## Usage

1. Clone the repository and navigate to the project directory.
2. Ensure you have a text file to compress.
3. Run the script and provide the path to the text file when prompted:

    ```bash
    python huffman.py
    ```

4. The script will create a compressed `.bin` file and a decompressed `.txt` file.

## Example

To compress a file named `example.txt`, the program will:
- Read the content of `example.txt`.
- Calculate character frequencies and build the Huffman tree.
- Generate binary codes for each character.
- Create a compressed file named `example.bin`.

The decompressed file will be named `example_decompressed.txt`.

## Conclusion

This project demonstrates the implementation of Huffman coding for file compression and decompression. It provides an efficient way to reduce file size without losing any data.
