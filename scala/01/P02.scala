/**
 * 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
 * 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
 */
object P02 {
  def main(args: Array[String]): Unit = {
    println(("パトカー" zip "タクシー").map{case(c1, c2) => String.valueOf(Array(c1, c2))}.mkString)
  }
}
