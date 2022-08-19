// Nathan McAlister
// 6/5/21
// CSE143
// TA: RanDair Scott Porter
// Assignment #8
//
// The HuffmanNode class is is used to store the information for a branch or leaf node of a 
// 'Huffman Tree', a type of binary tree created by the HuffmanTree class. 

public class HuffmanNode implements Comparable<HuffmanNode> {

   // ~*! FIELDS !~ //
   public int charValue;         // ASCII character value
   public int charCount;         // Number of times the specific character is reference
   public HuffmanNode left;      // Link for left branch of the node
   public HuffmanNode right;     // Link for right branch of the node
   
   // ~*! CONSTRUCTOR !*~ //
   // Constructs an empty node with no character value, no character count, and null links to 
   // other nodes.
   public HuffmanNode() {
      this(-1, -1, null, null);
   }
   
   // Constructs a node with the given data for character value and count, but null links to 
   // other nodes.
   public HuffmanNode(int charValue, int charCount) {
      this(charValue, charCount, null, null);
   }
   
   // Constructs a node with the given data for character count and other node links, but without
   // a specific character value (ie. branch nodes).
   public HuffmanNode(int charCount, HuffmanNode left, HuffmanNode right) {
      this(-1, charCount, left, right);
   }
   
   // Constructs a node with the given data for character value, character count, and other 
   // node links.
   public HuffmanNode(int charValue, int charCount, HuffmanNode left, HuffmanNode right) {
      this.charValue = charValue;
      this.charCount = charCount;
      this.left = left;
      this.right = right;
   }
    
   // ~*! PUBLIC METHODS !*~
   // Compares two node objects by the frequency of the node's character values.
   public int compareTo(HuffmanNode other) {
      return this.charCount - other.charCount;
   }
}