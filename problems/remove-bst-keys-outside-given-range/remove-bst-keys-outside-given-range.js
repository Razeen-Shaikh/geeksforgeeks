/**
 * @param {Node} root
 * @param {number} l
 * @param {number} r
 * @return {Node}
 */

/*
class Node {
    constructor(x){
        this.data=x;
        this.left=null;
        this.right=null;
    }
}
*/

class Solution {
  removekeys(root, l, r) {
    if (!root) return null;

    if (root.data < l) {
      return this.removekeys(root.right, l, r);
    }

    if (root.data > r) {
      return this.removekeys(root.left, l, r);
    }

    root.left = this.removekeys(root.left, l, r);
    root.right = this.removekeys(root.right, l, r);

    return root;
  }
}
