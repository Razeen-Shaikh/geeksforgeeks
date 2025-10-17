/**
 * @param {Node} root
 * @return {void}
 */

/*
class Node
{
    constructor(x){
        this.data=x;
        this.left=null;
        this.right=null;
    }
}
*/

class Solution {
  transformTree(root) {
    let sum = 0;

    function reverseInOrder(node) {
      if (!node) return;

      reverseInOrder(node.right);

      let original = node.data;
      node.data = sum;
      sum += original;

      reverseInOrder(node.left);
    }

    reverseInOrder(root);
  }
}
