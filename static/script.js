async function analyser() {
    let texte = document.getElementById("editor").value;

    let res = await fetch("/analyser", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({texte: texte})
    });

    let data = await res.json();

    let result = `
        <p><b>Corrections :</b> ${data.corrections.join(" ")}</p>
        <p><b>Lemmes :</b> ${data.lemmes.join(" ")}</p>
        <p><b>Sentiment :</b> ${data.sentiment}</p>
    `;

    document.getElementById("result").innerHTML = result;
}

async function lire() {
    let texte = document.getElementById("editor").value;

    let res = await fetch("/tts", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({texte: texte})
    });

    let data = await res.json();

    let audio = new Audio(data.audio);
    audio.play();
}