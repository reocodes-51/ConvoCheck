async function analyze() {
  const text = document.getElementById("threadInput").value.trim();
  document.getElementById("summary").textContent =
  "Analyzing discussion...";

  if (!text) {
    alert("Please enter a discussion thread.");
    return;
  }

  document.getElementById("summary").textContent =
    "Analyzing discussion...";

  document.getElementById("analysisSummary").innerHTML = "";

  document.getElementById("flaggedComments").innerHTML = "";

  try {
    const res = await fetch("/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        thread_text: text,
        comments: text
          .split("\n")
          .filter(line => line.trim() !== "")
      })
    });

    const data = await res.json();

    document.getElementById("summary").textContent =
      data.analysis;

    document.getElementById("analysisSummary").innerHTML = `
      <p><strong>Total Comments:</strong> ${data.total_comments}</p>
      <p><strong>Safe Comments:</strong> ${data.safe_comments}</p>
      <p><strong>Toxic Comments:</strong> ${data.toxic_comments}</p>
      <p><strong>Toxicity Score:</strong> ${data.toxicity_percentage}%</p>
      <p><strong>Overall Sentiment:</strong> ${data.sentiment}</p>
      `;

    const flaggedDiv =
      document.getElementById("flaggedComments");

    flaggedDiv.innerHTML = "";

    data.flagged.forEach((item, index) => {
      const p = document.createElement("p");

      p.textContent =
        `Comment ${index + 1}: ${item.comment}`;

      if (item.toxic) {
        p.classList.add("toxic");
      } else {
        p.classList.add("safe");
      }

      flaggedDiv.appendChild(p);
    });

  } catch (error) {

    document.getElementById("summary").textContent =
      "Error analyzing thread.";

    console.error(error);
  }
}