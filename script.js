function convert() {
    fetch("/convert", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            amount: Number(document.getElementById("amount").value),
            to: document.getElementById("currency").value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").innerText =
            "Result: " + data.result;
    });
}
