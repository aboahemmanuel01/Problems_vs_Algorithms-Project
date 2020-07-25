## Autocomplete with Tries

A trie is a tree-like data structure that stores a dynamic set of strings. 
Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

In this problem I first created a working trie for storing strings which consisted of two classes as follows:
```
1. A Trie class that contains the root node (empty string)
2. A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
```
Finally, I implemented a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie. 

For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().
