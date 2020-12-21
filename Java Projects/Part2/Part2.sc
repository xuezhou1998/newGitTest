abstract class Tree[+T]



case class Node[T](parent: T,left:Tree[T],right:Tree[T]) extends Tree[T]
case class Leaf[T](leaf: T) extends Tree[T]
trait Addable[T]{
  def + (input: T) : T
}

 class A (a: Int) extends Addable [A] {
  val value=a
  override def toString(): String = {
    var catString: String="A("+ this.value.toString+")"

    return catString
  }

  def + (input: A) : A = {
    var sum: Int = input.value
    sum=sum+this.value
    val newinst=new A(sum)
    return newinst
  }

}

 class B(a : Int) extends A (a) {
   override def toString(): String = {
     var catString: String="B("+ this.value.toString+")"

     return catString
   }
}
class C(a:Int)extends B(a){
  override def toString(): String = {
    var catString: String="C("+ this.value.toString+")"

    return catString
  }
}

object Part2{



  def inOrder[T] (tree: Tree[T]): List[T]= tree match {
    case Node ( parent,left, right)=>{
      val parent_list: List[T]=List(parent)
      val left_list: List[T]= inOrder(left)
      val right_list: List[T]= inOrder(right)
      return left_list ::: parent_list ::: right_list
  }
    case Leaf(leaf)=>{
      val l: List[T]=List(leaf)
      return l
    }
  }

  def treeSum[T <: Addable[T]](tree: Tree[T]): T = tree match {
    case Node (parent,left,  right)=>{
  val sum: T =treeSum(left)+parent+treeSum(right)
  return sum
  } case Leaf(leaf)=>{
      val result:T = leaf
  return result
  }
  }
  def treeMap[T,V](func: T=>V, tree: Tree[T]):Tree[V]= tree match {
    case Node(parent,left,right)=>{
      val leftsub: Tree[V]=treeMap(func,left)
      val rightsub: Tree[V]=treeMap(func,right)
      val parentf = func(parent)
      return  Node(parentf,leftsub,rightsub)
    }
    case Leaf(leaf)=>{
      return  Leaf(func(leaf))
    }
  }
  def BTreeMap(func:B=>B,tree:Tree[B]):Tree[B]={
    treeMap[B, B](func, tree)
  }
  def test():Unit = {
    def faa(a:A):A = new A(a.value+10)
    def fab(a:A):B = new B(a.value+20)
    def fba(b:B):A = new A(b.value+30)
    def fbb(b:B):B = new B(b.value+40)
    def fbc(b:B):C = new C(b.value+50)
    def fcb(c:C):B = new B(c.value+60)
    def fcc(c:C):C = new C(c.value+70)
    def fac(a:A):C = new C(a.value+80)
    def fca(c:C):A = new A(c.value+90)

    val myBTree: Tree[B] = Node(new B(4),Node(new B(2),Leaf(new B(1)),Leaf(new B(3))),
      Node(new B(6), Leaf(new B(5)), Leaf(new B(7))))

    val myATree: Tree[A] = myBTree

    println("inOrder = " + inOrder(myATree))
    println("Sum = " + treeSum(myATree))

//    println(BTreeMap(faa,myBTree))//
    /*
   the first parameter is expecting a B=>B but received a A=>A,
   this is not allow since scala does not allow contravariant output
     */
    println(BTreeMap(fab,myBTree))
//    println(BTreeMap(fba,myBTree))//
    /*
    The first parameter is expecting a B=>B but actually received an
    B=>A, which is the supertype of B=>B.this is not allow
    since scala does not allow contravariant output.
    */
    println(BTreeMap(fbb,myBTree))
    println(BTreeMap(fbc,myBTree))
//    println(BTreeMap(fcb,myBTree))//
    /*
    the first parameter is expecting B=>B but received C=>B,
    this is not allowed since scala does not allow covariant input.
     */
//    println(BTreeMap(fcc,myBTree))//
    /*
    the first parameter is expecting B=>B but received C=>C,
    this is not allowed since scala does not allow covariant input.
     */
    println(BTreeMap(fac,myBTree))
//    println(BTreeMap(fca,myBTree))//
    /*
    the first parameter is expecting B=>B but received C=>A,
    this is not allowed since scala does not allow covariant input
    and contravariant output.
     */
    println(treeMap(faa,myATree))
    println(treeMap(fab,myATree))
//    println(treeMap(fba,myATree))
    /*
    the first parameter is expecting A=>A but received B=>A,
    this is not allowed since scala does not allow covariant input.
     */
    //println(treeMap(fbb,myATree))
    /*
    the first parameter is expecting A=>B but received C=>B,
    this is not allowed since scala does not allow covariant input.
     */
    //println(treeMap(fbc,myATree))
    /*
    the first parameter is expecting A=>C but received C=>C,
    this is not allowed since scala does not allow covariant input.
     */
//    println(treeMap(fcb,myATree))
    /*
    the first parameter is expecting A=>B but received C=>B,
    this is not allowed since scala does not allow covariant input.
     */
//    println(treeMap(fcc,myATree))
    /*
    the first parameter is expecting A=>C but received C=>C,
    this is not allowed since scala does not allow covariant input.
     */
    println(treeMap(fac,myATree))
//    println(treeMap(fca,myATree))
    /*
    the first parameter is expecting A=>A but received C=>A,
    this is not allowed since scala does not allow covariant input.
     */
  }
  def main(args: Array[String]): Unit = {
    test()
  }


}


