function runPipeline() {
  const output = document.getElementById("output");

  output.innerHTML = "🔄 Starting Build Pipeline...<br>";

  setTimeout(() => {
    output.innerHTML += "✅ Code fetched from repository<br>";
  }, 1000);

  setTimeout(() => {
    output.innerHTML += "✅ Dependencies installed<br>";
  }, 2000);

  setTimeout(() => {
    output.innerHTML += "✅ Build completed successfully<br>";
  }, 3000);

  setTimeout(() => {
    output.innerHTML += "<br>🎉 <b>Build Status: SUCCESS</b>";
  }, 4000);
}
