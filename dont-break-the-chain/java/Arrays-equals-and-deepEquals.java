/*
Equals on arrays
Comparing arrays using the Object.equals method checks only reference equality, which is unlikely to be what is intended.

Code that compares arrays using the Gbject.equals method checks only reference equality. This is unlikely to be what is
intended.

Recommendation
To compare the lengths of the arrays and the corresponding pairs of elements in the arrays, use one of the comparison
methods from java.util.Arrays:
- The method Arrays.equals performs a shallow comparison. That is, array elements are compared using equals.
- The method Arrays. deepEquals performs a deep comparison, which is appropriate for comparisons of nested arrays.

Example
In the following example, the two arrays are first compared using the Dbject.equals method. Because this checks only
reference equality and the two arrays are different objects, Dbject.equals returns false. The two arrays are then
compared using the Arrays. equals method. Because this compares the length and contents of the arrays, Arrays. equals
returns true.
*/

public void arrayExairiple ()
  String[] arrayl = new String[]{”a’, “b”, “C”);
  String[] array2 = new String[]{”a”, “b”, “c”);

  // Reference equality tested: prints ‘false’
  System.out.println(arrayl.equals (array2));

  // Equality of array elements tested: prints ‘true’
  System.cut.println(Arrays.equals(arrayl, array2));
}