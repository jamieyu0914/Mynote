var SourceText = document.getElementById("oriContent");
SourceText.onkeyup = function () {
  //來源文字
  var text = document.getElementById("oriContent").value;
  //轉換
  var html = new showdown.Converter().makeHtml(text);
  //寫進指定位置
  document.getElementById("result").innerHTML = html;
};
