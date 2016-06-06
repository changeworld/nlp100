/**
 * 01. 「パタトクカシーー」
 * 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
 */
object P01 {
  def main(args: Array[String]): Unit = {
    val str = "パタトクカシーー"
    println(String.valueOf(List(str(0), str(2), str(4), str(6)).toArray))
  }
}
