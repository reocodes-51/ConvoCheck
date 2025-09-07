async function analyze() {
  const text = document.getElementById("threadInput").value;

  const res = await fetch("/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ 
      thread_text: text, 
      comments: text.split("\n") // one comment per line
    })
  });

  const data = await res.json();

  // Show Gemini-style summary
  document.getElementById("summary").textContent = data.analysis;

  // Update analysis summary
  document.getElementById("Analysis Summary").innerHTML = `
    <p><strong>Total Comments:</strong> ${data.total_comments || data.comments?.length || 'N/A'}</p>
    <p><strong>Sentiment:</strong> ${data.sentiment || 'N/A'}</p>
  `;

  // Show flagged comments
  const flaggedDiv = document.getElementById("flaggedComments");
  flaggedDiv.innerHTML = "";

  data.flagged.forEach((item, index) => {
    const p = document.createElement("p");
    p.textContent = `Comment ${index + 1}: ${item.comment}`;
    p.style.borderLeft = item.toxic ? "4px solid red" : "4px solid green";
    p.style.color = item.toxic ? "red" : "green";
    p.style.fontWeight = item.toxic ? "bold" : "normal";
    flaggedDiv.appendChild(p);
  });
}
