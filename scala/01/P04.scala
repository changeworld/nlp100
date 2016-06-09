/**
 * 04. 元素記号
 * "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
*     val answer = words.split(" ").zip(chars).map{case(word, len) => word.substring(0, len)}.zipWithIndex.map{case(sym, i) => (sym, i + 1)}.toMap
 */
object P04 {
  def main(args: Array[String]): Unit = {
    val words = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    val chars = List(1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2)
    val answer = words.split(" ").zip(chars).map{case(word, len) => word.substring(0, len)}.zipWithIndex.map{case(sym, i) => (sym, i + 1)}.toMap
    println(answer)
  }
}
