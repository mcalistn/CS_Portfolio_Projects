// Nathan McAlister
// 6/5/21
// CSE143
// TA: RanDair Scott Porter
// Assignment #8
//
// This program develops a type of decision tree called a 'Huffman Tree' that is used in conjunction 
// with other java programs to encode and decode text files, allowing for text files to be compressed 
// and subsequently recovered.

// ~*! IMPORTS !~ //
import java.io.*;
import java.util.*;

public class HuffmanTree {

   // ~*! FIELDS !~ //
   HuffmanNode overallRoot;         // overall root node
      
   // ~*! CONSTRUCTOR !*~ //
   // pre:  Passed parameter contains the frequency of each letter in the specified text file.
   // post: Creates a 'Huffman Tree' that will be used to generate a specific code for each character in
   //       the specified text file.
   public HuffmanTree(int[] count) {
      Queue<HuffmanNode> treeQueue = new PriorityQueue<HuffmanNode>();
      int countArrayPosition = 0;
      for(int charCount : count) {
         if(charCount != 0) {
            HuffmanNode newLeafNode = new HuffmanNode(countArrayPosition, charCount);
            treeQueue.add(newLeafNode);
         }
         countArrayPosition++;
      }
      HuffmanNode endOfFile = new HuffmanNode(count.length, 1);
      treeQueue.add(endOfFile);
      int treeSize = treeQueue.size();
      while(treeSize > 1) {
         HuffmanNode removeNodeLeft = treeQueue.remove();
         HuffmanNode removeNodeRight = treeQueue.remove();
         HuffmanNode rootNode = new HuffmanNode(removeNodeLeft.charCount + 
                                                removeNodeRight.charCount,
                                                removeNodeLeft, removeNodeRight);
         treeQueue.add(rootNode);
         treeSize = treeQueue.size();
         overallRoot = rootNode;
      }
   }
   
   // pre:  The passed parameter must be in standard format.
   // post: Re-creates a 'Huffman Tree' from the passed coding file. The decision tree will the be 
   //       used to decode each character from an encoded file.
   public HuffmanTree(Scanner input) {
      HuffmanNode currentRoot = new HuffmanNode();
      overallRoot = currentRoot;
      while(input.hasNextLine()) {
         int n = Integer.parseInt(input.nextLine());
         String code = input.nextLine();
         for(int i = 0; i <= code.length() - 1; i++) {
            if(code.charAt(i) == '0') {
               if(i == code.length() - 1) {
                  HuffmanNode newLeafNode = new HuffmanNode(n, -1);
                  currentRoot.left = newLeafNode;
                  currentRoot = overallRoot;
               } else {
                  if(currentRoot.left == null) {
                     HuffmanNode newBranchNode = new HuffmanNode();
                     currentRoot.left = newBranchNode;
                  }
                  currentRoot = currentRoot.left;
               }
            } else {
               if(i == code.length() - 1) {
                  HuffmanNode newLeafNode = new HuffmanNode(n, -1);
                  currentRoot.right = newLeafNode;
                  currentRoot = overallRoot;
               } else {
                  if(currentRoot.right == null) {
                     HuffmanNode newBranchNode = new HuffmanNode();
                     currentRoot.right = newBranchNode;
                  }
                  currentRoot = currentRoot.right;
               }
            }
         }
      }
   }
   
   // ~*! PUBLIC METHODS !*~
   // pre:  Input file must contain an end-of-file specific character that that only appears once in the
   //       encoded file and does not represent any letter that needs to be transcribed.
   // pre:  Input file must not contain any illegal encoding characters for the 'Huffman Tree'.
   // post: Reads the encoded file and traverses the developed 'Huffman Tree' until a leaf node of 
   //       the 'Huffman Tree' is reached. Writes the character associated with that leaf node's
   //       character value to the specified output file in standard format and traversal order.
   public void decode(BitInputStream input, PrintStream output, int eof) {
      HuffmanNode currentRoot = overallRoot;
      int nextBit = input.readBit();
      int checkEndOfFile = currentRoot.charValue;
      while(checkEndOfFile != eof) {
         while(currentRoot.left != null && currentRoot.right != null) {
            if(nextBit == 0) {
               currentRoot = currentRoot.left;
            } else {
               currentRoot = currentRoot.right;
            } 
            nextBit = input.readBit();
         }
         if(currentRoot.charValue != eof) {
            output.write(currentRoot.charValue);
         }
         checkEndOfFile = currentRoot.charValue;
         currentRoot = overallRoot;
      }
   }
   
   // post: Traverses the 'Huffman Tree' until it reaches an end node of the decision tree. Records 
   //       a specific character code for each end node and writes that code to the specified output
   //       file.
   public void write(PrintStream output) {
      String treeCode = "";
      findNextLeafNode(overallRoot, output, treeCode);
   }

   // ~*! PRIVATE METHODS !*~
   // post: Recursive method that is used to generate the 'Huffman Tree' codes for different 
   //       character values.
   private void findNextLeafNode(HuffmanNode currentRoot, PrintStream output, String treeCode) {
      if(currentRoot != null) {
         if(currentRoot.left == null && currentRoot.right == null) {
            output.println(currentRoot.charValue);
            output.println(treeCode);
         }
         treeCode = treeCode + "0";
         findNextLeafNode(currentRoot.left, output, treeCode);
         treeCode = treeCode.substring(0, treeCode.length() - 1);
         treeCode = treeCode + "1";
         findNextLeafNode(currentRoot.right, output, treeCode);
      }
   }
}